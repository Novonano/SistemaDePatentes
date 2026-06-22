"""Testes unitários para run_agent().

Usa MagicMock para o evaluator e um _StubScraper inline para injetar
patentes controladas, sem necessidade de Docker, Ollama ou arquivos de fixture.

Três cenários:
  - caminho feliz: 2 patentes, ambas incluídas, pipeline completa normalmente
  - LLM indisponível: check_connection() retorna False, todas as patentes
    vão para revisão manual sem chamar screen_patent()
  - sem resultados: scraper retorna lista vazia, status = "no_results"
"""

import os
import tempfile
import unittest
from unittest.mock import MagicMock

from models.patent import Patent, PatentEvaluation
from pipeline.features import PipelineFeatures
from pipeline.orchestrator import run_agent
from scraper.base import BaseScraper


class _StubScraper(BaseScraper):
    """Scraper que retorna patentes pré-definidas sem acessar a internet."""

    def __init__(self, patents):
        super().__init__()
        self._patents = patents

    def search(self, query, max_results=10):
        return list(self._patents)

    def get_patent_details(self, patent_url):
        raise NotImplementedError


def _make_evaluator(check_connection=True):
    """Constrói um MagicMock que imita OllamaEvaluator."""
    ev = MagicMock()
    ev.check_connection.return_value = check_connection
    ev.is_degraded.return_value = False
    ev.total_failures = 0
    ev.cache_stats.return_value = {}
    ev.telemetry_stats.return_value = {
        "operations": {
            "screening": {"total_calls": 2, "total_duration_seconds": 0.1},
            "rerank": {"total_duration_seconds": 0.0},
        }
    }

    def _screen(patent, query, **kwargs):
        return PatentEvaluation(
            record_id=patent.record_id,
            patent_id=patent.patent_id,
            screening_decision="include",
            screening_score=8.0,
            summary="Patente relevante.",
            technical_domain="CO2 Cycle Configurations",
        )

    def _evaluate(patent, query, screening=None, **kwargs):
        return PatentEvaluation(
            record_id=patent.record_id,
            patent_id=patent.patent_id,
            screening_decision="include",
            screening_score=8.0,
            relevance_score=8.5,
            summary="Patente relevante.",
            technical_domain="CO2 Cycle Configurations",
        )

    ev.screen_patent.side_effect = _screen
    ev.evaluate_patent.side_effect = _evaluate
    ev.generate_comparative_analysis.return_value = (
        "## Análise Comparativa\nDuas abordagens complementares identificadas."
    )
    ev.generate_whitespace_analysis.return_value = {
        "status": "ok",
        "whitespace_candidates": [],
        "corpus_summary": {"selected_patents": 2},
    }
    return ev


_PATENTS = [
    Patent(
        patent_id="US001",
        title="Thermal Storage Assembly",
        abstract="Packed-bed thermal storage for industrial energy shifting.",
        source="Google Patents",
        assignee="Example Inc.",
    ),
    Patent(
        patent_id="WO002",
        title="Supercritical CO2 Storage System",
        abstract="System for thermal energy storage using supercritical CO2.",
        source="Patentscope",
        assignee="Future LLC.",
    ),
]


class RunAgentUnitTests(unittest.TestCase):

    # ------------------------------------------------------------------ #
    # Caminho feliz                                                        #
    # ------------------------------------------------------------------ #

    
    """
    test_caminho_feliz_pipeline_completa
    
    Simula a execução normal do sistema: dois scrapers retornam uma patente cada, o LLM aprova as duas. Verifica 9 coisas:

    1. state.status == "completed" — o pipeline chegou até o fim sem erros
    2. state.llm_available == True — o evaluator reportou conexão ok
    3. len(state.patents) == 2 — as duas patentes foram encontradas e deduplicadas
    4. coverage_metrics["included"] == 2 — as duas passaram na triagem com decisão "include"
    5. coverage_metrics["manual_review_required"] == 0 — nenhuma foi para fila de revisão humana
    6. "## Análise Comparativa" in state.comparative_analysis — o orchestrator chamou generate_comparative_analysis() e armazenou o resultado
    7. whitespace_analysis["status"] == "ok" — o orchestrator chamou generate_whitespace_analysis() e armazenou o resultado
    8. os.path.exists(output_paths["markdown"]) — o ReportGenerator escreveu o arquivo .md em disco
    9. os.path.exists(output_paths["json"]) — o ReportGenerator escreveu o arquivo .json em disco
    10. os.path.exists(output_paths["whitespace_json"]) — o artefato de whitespace foi salvo em disco

    """

    def test_caminho_feliz_pipeline_completa(self):
        """Duas patentes incluídas → pipeline encerra com status completed."""
        ev = _make_evaluator()
        with tempfile.TemporaryDirectory() as tmpdir:
            state = run_agent(
                query="carbon dioxide thermal storage",
                max_results=5,
                model="stub-model",
                output_dir=tmpdir,
                scrapers=[_StubScraper(_PATENTS)],
                evaluator_factory=lambda **_: ev,
                features=PipelineFeatures(),
            )

            self.assertEqual(state.status, "completed")
            self.assertTrue(state.llm_available)
            self.assertEqual(len(state.patents), 2)
            self.assertEqual(state.coverage_metrics["included"], 2)
            self.assertEqual(state.coverage_metrics["manual_review_required"], 0)
            self.assertIn("## Análise Comparativa", state.comparative_analysis)
            self.assertEqual(state.whitespace_analysis.get("status"), "ok")
            self.assertTrue(os.path.exists(state.output_paths["markdown"]))
            self.assertTrue(os.path.exists(state.output_paths["json"]))
            self.assertTrue(os.path.exists(state.output_paths["whitespace_json"]))

    # ------------------------------------------------------------------ #
    # LLM indisponível                                                    #
    # ------------------------------------------------------------------ #

    """
    ---
    test_llm_indisponivel_patentes_vao_para_revisao_manual

    Simula o cenário onde o Ollama não está acessível: check_connection() retorna False. Verifica 5 coisas:

    1. state.llm_available == False — o estado registrou que o LLM está fora
    2. len(state.patents) == 2 — as patentes foram encontradas normalmente (o scraper não depende do LLM)
    3. ev.screen_patent.assert_not_called() — o orchestrator nunca tentou chamar o modelo; este é o assert mais importante, pois prova que o pipeline não tenta
    usar o LLM quando ele está indisponível
    4. all(e.manual_review_required for e in state.evaluations) — todas as patentes receberam manual_review_required=True automaticamente
    5. coverage_metrics["included"] == 0 e coverage_metrics["screened"] == 0 — nenhuma patente foi triada ou incluída

    """

    def test_llm_indisponivel_patentes_vao_para_revisao_manual(self):
        """check_connection() False → screening pulado, todas com manual_review_required."""
        ev = _make_evaluator(check_connection=False)
        with tempfile.TemporaryDirectory() as tmpdir:
            state = run_agent(
                query="carbon dioxide thermal storage",
                max_results=5,
                model="stub-model",
                output_dir=tmpdir,
                scrapers=[_StubScraper(_PATENTS)],
                evaluator_factory=lambda **_: ev,
                features=PipelineFeatures(),
            )

            self.assertFalse(state.llm_available)
            self.assertEqual(len(state.patents), 2)
            ev.screen_patent.assert_not_called()
            self.assertTrue(all(e.manual_review_required for e in state.evaluations))
            self.assertEqual(state.coverage_metrics["included"], 0)
            self.assertEqual(state.coverage_metrics["screened"], 0)

    # ------------------------------------------------------------------ #
    # Sem resultados                                                       #
    # ------------------------------------------------------------------ #

    
    """
    ---
    test_sem_resultados_status_no_results
    
    Simula o cenário onde nenhuma patente é encontrada: o scraper retorna lista vazia. Verifica 4 coisas:

    1. state.status == "no_results" — o pipeline entrou no caminho de encerramento antecipado
    2. len(state.patents) == 0 — confirmação de que não há patentes no estado
    3. ev.screen_patent.assert_not_called() — o orchestrator não chegou nem à etapa de triagem
    4. "markdown" not in state.output_paths e "json" not in state.output_paths — nenhum relatório foi gerado, pois não há dados para reportar

    """

    def test_sem_resultados_status_no_results(self):
        """Scraper retorna lista vazia → status = 'no_results', sem relatório."""
        ev = _make_evaluator()
        with tempfile.TemporaryDirectory() as tmpdir:
            state = run_agent(
                query="carbon dioxide thermal storage",
                max_results=5,
                model="stub-model",
                output_dir=tmpdir,
                scrapers=[_StubScraper([])],
                evaluator_factory=lambda **_: ev,
                features=PipelineFeatures(),
            )

            self.assertEqual(state.status, "no_results")
            self.assertEqual(len(state.patents), 0)
            ev.screen_patent.assert_not_called()
            self.assertNotIn("markdown", state.output_paths)
            self.assertNotIn("json", state.output_paths)


if __name__ == "__main__":
    unittest.main()
