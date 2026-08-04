"""
Orquestrador orientado a estagios.

A classe ``PipelineOrchestrator`` decompoe o antigo monolito ``run_agent`` em
metodos por estagio (setup, search, screening, comparative, whitespace,
reporting, finalize), mantendo o ``EventBus`` e os observers como atributos da
instancia. O comportamento e identico ao legado; apenas a estrutura muda.

A fachada ``run_agent`` em ``pipeline/orchestrator.py`` instancia esta classe.

A classe nao construi observers internamente.
Ela recebe observers "prontos" de duas formas:
  * ``observers``: lista ja instanciada (substitui completamente o conjunto).
  * ``observers_builder``: callable ``(state, store, memory) -> List[Observer]``
    invocado apos a criacao do contexto interno.
A fachada e o composition root que acopla ``build_default_observers`` ao
contexto; a classe aqui permanece agnostica a fabrica concreta.
"""

from __future__ import annotations

import logging
import os
import time
from datetime import datetime
from typing import Callable, Dict, List

from analysis_utils import (
    COMPARATIVE_ANALYSIS_NO_INPUT,
    has_substantive_comparative_analysis,
)
import config
from evaluator.llm_evaluator import OllamaEvaluator
from models.patent import Patent, PatentEvaluation
from pipeline.observers import (
    ErrorEvent,
    EventBus,
    Observer,
    PipelineEvent,
    ProgressEvent,
    StageEvent,
)
from pipeline.orchestrator import (
    RunStateStore,
    _build_config_snapshot,
    _build_manual_review_queue,
    _build_observability_metrics,
    _build_thematic_clusters,
    _build_writing_context,
    _dedupe_patents,
    _display_patent_id,
    _entity_key,
    _evaluation_map,
    _hash_snapshot,
    _pair_patents_with_evaluations,
    _prisma_stage_artifact,
)
from pipeline.features import PipelineFeatures
from pipeline.memory import MemorySidecar
from pipeline.protocol import build_review_protocol
from pipeline.router import ThemeRouter
from pipeline.state import RunState
from report.generator import ReportGenerator
from scraper.base import BaseScraper
from scraper.epo import EPOScraper
from scraper.google_patents import GooglePatentsScraper
from scraper.patentscope import PatentscopeScraper

logger = logging.getLogger(__name__)


class PipelineOrchestrator:
    """Orquestra os estagios do pipeline com EventBus e observers."""

    def __init__(
        self,
        query: str,
        max_results: int,
        model: str,
        output_dir: str,
        features: PipelineFeatures | None = None,
        scrapers: List[BaseScraper] | None = None,
        evaluator_factory: Callable[..., OllamaEvaluator] | None = None,
        state_sink: Callable | None = None,
        observers: List[Observer] | None = None,
        observers_builder: "Callable[[RunState, RunStateStore, MemorySidecar], List[Observer]] | None" = None,
    ) -> None:
        self.query = query
        self.max_results = max_results
        self.model = model
        self.output_dir = output_dir
        self.features = features or PipelineFeatures()
        self.scrapers_input = scrapers
        self.evaluator_factory = evaluator_factory
        self.state_sink = state_sink

        self.start_time = time.perf_counter()
        config_snapshot = (
            _build_config_snapshot(query, max_results, model, output_dir, self.features)
            if self.features.enable_snapshot
            else {}
        )
        self.state = RunState(
            query=query,
            max_results=max_results,
            model=model,
            output_dir=output_dir,
            feature_flags=self.features.to_dict(),
            config_snapshot=config_snapshot,
            snapshot_hash=_hash_snapshot(config_snapshot) if config_snapshot else "",
            protocol=build_review_protocol(query, max_results, model),
        )
        self.store = RunStateStore(output_dir=output_dir, run_id=self.state.run_id)
        self.memory = MemorySidecar(run_id=self.state.run_id)
        self.router = ThemeRouter()

        if self.state_sink is not None:
            self.state_sink(self.state)

        self.bus = EventBus()
        if observers is not None:
            for _observer in observers:
                self.bus.subscribe(_observer)
        elif observers_builder is not None:
            for _observer in observers_builder(self.state, self.store, self.memory):
                self.bus.subscribe(_observer)
        # Se ambos forem None: barramento vazio (modo "seco", util para testes
        # que injetam seus proprios observers opacos).

        # Atributos preenchidos pelos estagios e compartilhados entre eles.
        self.evaluator: OllamaEvaluator | None = None
        self.scrapers: List[BaseScraper] | None = None
        self.raw_total = 0
        self.dedupe_stats: Dict[str, int] = {
            "records_with_content_identity": 0,
            "records_with_fallback_identity": 0,
            "family_duplicates_removed": 0,
        }
        self.missing_abstract = 0
        self.missing_id = 0
        self.duplicates_removed = 0
        self.screenings: List[PatentEvaluation] = []
        self.llm_screening_failures = 0

    # ------------------------------------------------------------------
    # Emissores de evento (closures viraram metodos)
    # ------------------------------------------------------------------
    def emit_stage(self, stage: str, title: str, level: int = logging.INFO, **fields: object) -> None:
        self.bus.emit(StageEvent(
            kind="stage_transition",
            level=level,
            stage=stage,
            title=title,
            fields=dict(fields),
        ))

    def emit_metric(
        self,
        stage: str,
        start_time: float,
        end_time: float,
        status: str,
        items_processed: int = 0,
        detail: str = "",
    ) -> None:
        self.bus.emit(StageEvent(
            kind="stage_metric",
            level=logging.INFO,
            stage=stage,
            status=status,
            duration_seconds=round(end_time - start_time, 3),
            items_processed=items_processed,
            detail=detail,
        ))

    def emit_progress(self, step: str, current: int = 0, total: int = 0) -> None:
        self.bus.emit(ProgressEvent(
            kind="progress",
            level=logging.INFO,
            step=step,
            current=current,
            total=total,
        ))

    def emit_log(self, level: int, name: str, **fields: object) -> None:
        self.bus.emit(PipelineEvent(
            kind=name,
            level=level,
            fields=dict(fields),
        ))

    def emit_error(self, message: str) -> None:
        self.bus.emit(ErrorEvent(
            kind="run_error",
            level=logging.WARNING,
            error=message,
        ))

    # ------------------------------------------------------------------
    # Orquestracao
    # ------------------------------------------------------------------
    def run(self) -> RunState:
        """Executa os estagios em sequencia, preservando o fluxo legado."""
        self._setup()
        if self._search() is False:
            return self.state
        self._screening()
        self._persist_after_screening()
        self._comparative()
        self._whitespace()
        self._persist_after_whitespace()
        self._reporting()
        self._finalize()
        return self.state

    # ------------------------------------------------------------------
    # Estagios
    # ------------------------------------------------------------------
    def _setup(self) -> None:
        state = self.state
        state.current_stage = "setup"
        self.emit_stage("setup", "Verificando conexão com Ollama", model=state.model)

        setup_start = time.perf_counter()
        if self.evaluator_factory is None:
            evaluator = OllamaEvaluator(model=state.model, cache_dir=self.output_dir)
        else:
            evaluator = self.evaluator_factory(model=state.model, output_dir=self.output_dir)
        self.evaluator = evaluator
        state.llm_available = evaluator.check_connection()
        self.memory.append(
            "setup",
            "llm_check",
            "Verificação de disponibilidade do Ollama concluída.",
            {"llm_available": state.llm_available, "model": state.model},
        )
        self.emit_metric("setup",
            setup_start,
            time.perf_counter(),
            "ok" if state.llm_available else "degraded",
            items_processed=1,
            detail="Verificação do modelo Ollama",
        )
        if not state.llm_available:
            self.emit_log(
                logging.WARNING,
                "llm_unavailable",
                model=state.model,
                recommended_command=f"ollama pull {state.model}",
                fallback_mode="manual_review_only",
            )
        else:
            self.emit_log(
                logging.INFO,
                "llm_available",
                model=state.model,
            )

    def _search(self) -> bool:
        """Executa busca e dedupe. Retorna False se encerrou sem resultados."""
        state = self.state
        query = self.query
        max_results = self.max_results

        state.current_stage = "search"
        self.emit_stage(
            "search",
            "Buscando patentes",
            query=query,
            max_results=max_results,
        )

        search_start = time.perf_counter()
        scrapers = self.scrapers_input or [
            GooglePatentsScraper(),
            PatentscopeScraper(),
            EPOScraper(),
        ]
        self.scrapers = scrapers

        patents: List[Patent] = []
        raw_total = 0
        for scraper in scrapers:
            source_name = scraper.__class__.__name__.replace("Scraper", "")
            self.emit_progress(f"Iniciando scraping no {source_name}")
            scraper_start = time.perf_counter()
            try:
                results = scraper.search(query, max_results=max_results)
                raw_total += len(results)
                state.patents_by_source[source_name] = len(results)
                patents.extend(results)
                state.patents, self.dedupe_stats = _dedupe_patents(patents)
                state.scraper_diagnostics[source_name] = scraper.get_diagnostics()
                self.memory.append(
                    "identification",
                    "scrape_completed",
                    f"{source_name} retornou patentes.",
                    {
                        "source": source_name,
                        "count": len(results),
                        "diagnostics": scraper.get_diagnostics(),
                    },
                )
                self.emit_log(
                    logging.INFO,
                    "scrape_completed",
                    source=source_name,
                    raw_results=len(results),
                    unique_patents=len(state.patents),
                    diagnostics_count=len(scraper.get_diagnostics()),
                )
            except Exception as e:
                message = f"Erro no scraper {source_name}: {e}"
                logger.exception(message)
                self.emit_error(message)
            finally:
                if source_name not in state.scraper_diagnostics:
                    state.scraper_diagnostics[source_name] = scraper.get_diagnostics()
                state.scraper_durations[source_name] = round(
                    time.perf_counter() - scraper_start,
                    3,
                )
                self.store.save(state)

        self.raw_total = raw_total

        self.emit_metric("search",
            search_start,
            time.perf_counter(),
            "ok" if state.patents else "empty",
            items_processed=raw_total,
            detail=f"{len(state.patents)} patentes únicas após dedupe",
        )

        if not state.patents:
            self._finalize_no_results()
            return False

        self.missing_abstract = sum(1 for patent in state.patents if not (patent.abstract or patent.snippet))
        self.missing_id = sum(1 for patent in state.patents if not patent.patent_id)
        self.duplicates_removed = max(raw_total - len(state.patents), 0)

        self.emit_log(
            logging.INFO,
            "search_results_ready",
            patents_found=len(state.patents),
            duplicates_removed=self.duplicates_removed,
            missing_abstract=self.missing_abstract,
            missing_id=self.missing_id,
        )

        for i, patent in enumerate(state.patents, 1):
            self.emit_log(
                logging.INFO,
                "patent_discovered",
                index=i,
                patent_id=_display_patent_id(patent),
                title=patent.title[:80],
                assignee=patent.assignee or "",
                source=patent.source or "",
            )
        return True

    def _finalize_no_results(self) -> None:
        """Encerra a execucao quando nenhum resultado foi encontrado."""
        state = self.state
        evaluator = self.evaluator
        assert evaluator is not None
        dedupe_stats = self.dedupe_stats
        raw_total = self.raw_total
        pipeline_features = self.features

        self.emit_log(
            logging.WARNING,
            "no_results",
            query=self.query,
            max_results=self.max_results,
            recommendation="Tente termos diferentes ou mais genéricos.",
        )
        state.status = "no_results"
        state.finished_at = datetime.now().isoformat(timespec="seconds")
        state.coverage_metrics = {
            "raw_scraped": raw_total,
            "unique_patents": 0,
            "duplicates_removed": raw_total,
            "screened": 0,
            "included": 0,
            "review": 0,
            "excluded": 0,
            "manual_review_required": 0,
            "manual_review_deferred": 0,
            "full_extractions": 0,
            "missing_abstract": 0,
            "missing_id": 0,
            "records_with_content_identity": dedupe_stats.get("records_with_content_identity", 0),
            "records_with_fallback_identity": dedupe_stats.get("records_with_fallback_identity", 0),
            "family_duplicates_removed": dedupe_stats.get("family_duplicates_removed", 0),
            "llm_screening_failures": 0,
            "llm_total_failures": 0,
        }
        state.total_duration_seconds = round(time.perf_counter() - self.start_time, 3)
        state.prisma_flow = (
            _prisma_stage_artifact(state, state.coverage_metrics)
            if pipeline_features.enable_prisma
            else {}
        )
        self.memory.append(
            "synthesis",
            "no_results",
            "Execução encerrada sem patentes encontradas.",
            state.coverage_metrics,
        )
        state.memory_sidecar = self.memory.to_dict()
        state.memory_journal = [entry.to_dict() for entry in self.memory.journal]
        state.llm_cache_stats = evaluator.cache_stats()
        state.llm_telemetry = evaluator.telemetry_stats()
        state.rerank_duration_seconds = round(
            state.llm_telemetry.get("operations", {}).get("rerank", {}).get("total_duration_seconds", 0.0),
            3,
        )
        state.observability_metrics = _build_observability_metrics(state)
        journal_path = self.store.save_artifact(f"memory_journal_{state.run_id}.json", state.memory_journal)
        sidecar_path = self.store.save_artifact(f"memory_sidecar_{state.run_id}.json", state.memory_sidecar)
        state.output_paths = {
            "state": os.path.abspath(self.store.state_path),
            "memory_journal": os.path.abspath(journal_path),
            "memory_sidecar": os.path.abspath(sidecar_path),
        }
        self.emit_metric("finalization",
            self.start_time,
            time.perf_counter(),
            "empty",
            items_processed=0,
            detail="Execução encerrada sem resultados",
        )
        self.emit_log(
            logging.INFO,
            "run_completed",
            status=state.status,
            total_duration_seconds=round(state.total_duration_seconds, 1),
            output_paths=state.output_paths,
        )
        self.store.save(state)

    def _screening(self) -> None:
        state = self.state
        evaluator = self.evaluator
        assert evaluator is not None
        query = self.query
        pipeline_features = self.features
        raw_total = self.raw_total
        dedupe_stats = self.dedupe_stats
        missing_abstract = self.missing_abstract
        missing_id = self.missing_id
        duplicates_removed = self.duplicates_removed

        screenings: List[PatentEvaluation] = []
        llm_screening_failures = 0
        llm_circuit_open_logged = False
        screening_start = time.perf_counter()
        state.current_stage = "screening"
        if state.llm_available:
            self.emit_stage(
                "screening",
                "Triagem e extração estruturada",
                model=state.model,
                include_threshold=config.SCREEN_INCLUDE_THRESHOLD,
                review_threshold=config.SCREEN_REVIEW_THRESHOLD,
            )

            for i, patent in enumerate(state.patents, 1):
                self.emit_progress(
                    f"Triando: {_display_patent_id(patent)} — {patent.title[:40]}...",
                    i,
                    len(state.patents),
                )
                if evaluator.is_degraded():
                    screening = evaluator._llm_failure_evaluation(
                        patent,
                        "Circuit breaker global do LLM ativo; revisão manual necessária.",
                    )
                else:
                    screening = evaluator.screen_patent(
                        patent,
                        query,
                        require_evidence=pipeline_features.require_evidence,
                        enable_thematic_clusters=pipeline_features.enable_thematic_clusters,
                        enable_structural_roles=pipeline_features.enable_structural_roles,
                        enable_screening_rerank=pipeline_features.enable_screening_rerank,
                    )
                    if screening.llm_error:
                        llm_screening_failures += 1
                if evaluator.is_degraded() and not llm_circuit_open_logged:
                    message = (
                        "Circuit breaker global do Ollama acionado após "
                        f"{evaluator.total_failures} falha(s) na execução."
                    )
                    self.emit_error(message)
                    self.memory.append(
                        "policy",
                        "llm_circuit_open",
                        message,
                        {"failures": evaluator.total_failures},
                    )
                    llm_circuit_open_logged = True
                route = self.router.route(patent, screening)
                screening.analysis_route = route.route
                screening.route_reason = route.reason
                screenings.append(screening)
                state.screened_count += 1
                self.memory.append(
                    "screening",
                    "screening_completed",
                    f"{_display_patent_id(patent)} roteada para {route.route}.",
                    {
                        "record_id": patent.record_id,
                        "patent_id": patent.patent_id,
                        "decision": screening.screening_decision,
                        "score": screening.screening_score,
                        "route": route.to_dict(),
                        "llm_error": screening.llm_error,
                    },
                )
                self.memory.set_slot(
                    route.slot,
                    {
                        "record_id": patent.record_id,
                        "patent_id": patent.patent_id,
                        "title": patent.title,
                        "route": route.route,
                        "score": screening.screening_score,
                    },
                )

                self.emit_log(
                    logging.INFO,
                    "screening_result",
                    index=i,
                    patent_id=_display_patent_id(patent),
                    decision=screening.screening_decision,
                    screening_score=screening.screening_score,
                    technical_domain=screening.technical_domain or "N/A",
                    route=screening.analysis_route,
                    llm_error=screening.llm_error or "",
                )

            included = [
                item for item in screenings
                if item.screening_decision == "include"
            ]
            review = [
                item for item in screenings
                if item.screening_decision == "review"
            ]
            excluded = [
                item for item in screenings
                if item.screening_decision == "exclude"
            ]

            review.sort(key=lambda item: item.screening_score, reverse=True)
            review_limit = config.SCREEN_MAX_ITEMS_FOR_REVIEW
            review_to_process = (
                review[:review_limit]
                if pipeline_features.enable_manual_review_queue
                else []
            )
            if not pipeline_features.enable_manual_review_queue:
                self.memory.append(
                    "policy",
                    "manual_review_disabled",
                    "Fila de revisão manual desativada por feature flag.",
                )

            screening_map = _evaluation_map(screenings)
            review_ids = {item.record_id for item in review_to_process}
            included_ids = {item.record_id for item in included}

            eval_start = time.perf_counter()
            evaluations: List[PatentEvaluation] = []
            for patent in state.patents:
                screening = screening_map.get(_entity_key(patent.record_id, patent.patent_id))
                if screening is None:
                    continue

                if screening.record_id in included_ids or screening.record_id in review_ids:
                    if evaluator.is_degraded():
                        detailed = screening
                        detailed.screening_decision = "review"
                        detailed.manual_review_required = True
                        detailed.llm_error = (
                            detailed.llm_error
                            or "Circuit breaker global do LLM ativo antes da extração detalhada."
                        )
                    else:
                        detailed = evaluator.evaluate_patent(
                            patent,
                            query,
                            screening=screening,
                            require_evidence=pipeline_features.require_evidence,
                            enable_thematic_clusters=pipeline_features.enable_thematic_clusters,
                            enable_structural_roles=pipeline_features.enable_structural_roles,
                            enable_screening_rerank=pipeline_features.enable_screening_rerank,
                        )
                    detailed.manual_review_required = screening.screening_decision == "review"
                    if detailed.llm_error:
                        detailed.screening_decision = "review"
                        detailed.manual_review_required = True
                    detailed.analysis_route = screening.analysis_route
                    detailed.route_reason = screening.route_reason
                    evaluations.append(detailed)
                    self.memory.append(
                        "extraction",
                        "detailed_evaluation_completed",
                        f"{_display_patent_id(patent)} recebeu extração detalhada.",
                        {
                            "record_id": patent.record_id,
                            "patent_id": patent.patent_id,
                            "route": detailed.analysis_route,
                            "confidence": detailed.confidence,
                        },
                    )
                else:
                    evaluations.append(screening)
                    self.memory.append(
                        "extraction",
                        "screening_only",
                        f"{_display_patent_id(patent)} permaneceu apenas na triagem.",
                        {
                            "record_id": patent.record_id,
                            "patent_id": patent.patent_id,
                            "route": screening.analysis_route,
                        },
                    )

            state.evaluation_duration_seconds = round(time.perf_counter() - eval_start, 3)
            state.evaluations = evaluations
            state.manual_review_queue, review_deferred_count = _build_manual_review_queue(
                state.patents,
                state.evaluations,
                review_limit if pipeline_features.enable_manual_review_queue else 0,
            )
            state.thematic_clusters = (
                _build_thematic_clusters(state.patents, state.evaluations)
                if pipeline_features.enable_thematic_clusters
                else {"clusters": [], "total_clusters": 0}
            )
            state.coverage_metrics = {
                "raw_scraped": raw_total,
                "unique_patents": len(state.patents),
                "duplicates_removed": duplicates_removed,
                "screened": len(screenings),
                "included": len(included),
                "review": len(review),
                "excluded": len(excluded),
                "manual_review_required": len(state.manual_review_queue),
                "manual_review_deferred": review_deferred_count,
                "full_extractions": len(included) + len(review_to_process),
                "missing_abstract": missing_abstract,
                "missing_id": missing_id,
                "records_with_content_identity": dedupe_stats.get("records_with_content_identity", 0),
                "records_with_fallback_identity": dedupe_stats.get("records_with_fallback_identity", 0),
                "family_duplicates_removed": dedupe_stats.get("family_duplicates_removed", 0),
                "llm_screening_failures": llm_screening_failures,
                "llm_total_failures": evaluator.total_failures,
            }
            self.memory.append(
                "synthesis",
                "coverage_computed",
                "Cobertura e seleção consolidadas após triagem.",
                state.coverage_metrics,
            )

            self.emit_log(
                logging.INFO,
                "screening_completed",
                screened=len(screenings),
                included=len(included),
                review=len(review),
                excluded=len(excluded),
                manual_review_queue=len(state.manual_review_queue),
            )
            self.emit_metric("screening",
                screening_start,
                time.perf_counter(),
                "degraded" if llm_screening_failures or evaluator.is_degraded() else "ok",
                items_processed=len(screenings),
                detail=f"{len(included)} incluídas, {len(state.manual_review_queue)} revisão",
            )
        else:
            self.emit_log(
                logging.WARNING,
                "screening_skipped",
                reason="LLM indisponível",
                patents=len(state.patents),
            )
            review_limit = config.SCREEN_MAX_ITEMS_FOR_REVIEW
            state.evaluations = [
                PatentEvaluation(
                    record_id=patent.record_id,
                    patent_id=patent.patent_id,
                    screening_score=0.0,
                    screening_decision="review",
                    screening_reason="LLM indisponível.",
                    manual_review_required=True,
                    llm_error="LLM indisponível.",
                )
                for patent in state.patents
            ]
            state.manual_review_queue, review_deferred_count = _build_manual_review_queue(
                state.patents,
                state.evaluations,
                review_limit if pipeline_features.enable_manual_review_queue else 0,
            )
            state.coverage_metrics = {
                "raw_scraped": raw_total,
                "unique_patents": len(state.patents),
                "duplicates_removed": duplicates_removed,
                "screened": 0,
                "included": 0,
                "review": len(state.patents),
                "excluded": 0,
                "manual_review_required": len(state.manual_review_queue),
                "manual_review_deferred": review_deferred_count,
                "full_extractions": 0,
                "missing_abstract": missing_abstract,
                "missing_id": missing_id,
                "records_with_content_identity": dedupe_stats.get("records_with_content_identity", 0),
                "records_with_fallback_identity": dedupe_stats.get("records_with_fallback_identity", 0),
                "family_duplicates_removed": dedupe_stats.get("family_duplicates_removed", 0),
                "llm_screening_failures": len(state.patents),
                "llm_total_failures": 0,
            }

            state.thematic_clusters = {"clusters": [], "total_clusters": 0}
            self.memory.append(
                "synthesis",
                "llm_unavailable",
                "Síntese temática desativada porque o LLM não está disponível.",
            )
            self.emit_metric("screening",
                screening_start,
                time.perf_counter(),
                "skipped",
                items_processed=len(state.patents),
                detail="LLM indisponível",
            )

        self.screenings = screenings
        self.llm_screening_failures = llm_screening_failures

    def _persist_after_screening(self) -> None:
        """Persiste prisma/journal/telemetria apos a triagem (legado)."""
        state = self.state
        evaluator = self.evaluator
        assert evaluator is not None
        state.prisma_flow = (
            _prisma_stage_artifact(state, state.coverage_metrics)
            if self.features.enable_prisma
            else {}
        )
        state.memory_sidecar = self.memory.to_dict()
        state.memory_journal = [entry.to_dict() for entry in self.memory.journal]
        state.llm_cache_stats = evaluator.cache_stats()
        state.llm_telemetry = evaluator.telemetry_stats()
        state.rerank_duration_seconds = round(
            state.llm_telemetry.get("operations", {}).get("rerank", {}).get("total_duration_seconds", 0.0),
            3,
        )
        self.store.save(state)

    def _comparative(self) -> None:
        state = self.state
        evaluator = self.evaluator
        assert evaluator is not None
        query = self.query
        pipeline_features = self.features

        state.current_stage = "comparative_analysis"
        synthesis_start = time.perf_counter()
        comparative_status = "disabled_or_skipped"
        comparative_detail = "Síntese comparativa"
        if (
            state.llm_available
            and len(state.patents) > 1
            and pipeline_features.enable_comparative_analysis
            and not evaluator.is_degraded()
        ):
            self.emit_stage(
                "comparative_analysis",
                "Gerando análise comparativa",
                eligible_patents=len(state.evaluations),
            )

            comp_start = time.perf_counter()
            self.emit_progress("Gerando análise comparativa com IA")
            analysis_eval_map = _evaluation_map(state.evaluations)
            analysis_patents = [
                patent for patent in state.patents
                if (
                    _entity_key(patent.record_id, patent.patent_id) in analysis_eval_map
                    and not analysis_eval_map[_entity_key(patent.record_id, patent.patent_id)].llm_error
                )
            ]
            analysis_evaluations = [
                analysis_eval_map[_entity_key(patent.record_id, patent.patent_id)]
                for patent in analysis_patents
                if _entity_key(patent.record_id, patent.patent_id) in analysis_eval_map
            ]
            if len(analysis_patents) > 1 and len(analysis_evaluations) > 1:
                state.comparative_analysis = evaluator.generate_comparative_analysis(
                    analysis_patents,
                    analysis_evaluations,
                    query,
                )
                if state.comparative_analysis == COMPARATIVE_ANALYSIS_NO_INPUT:
                    comparative_status = "skipped"
                    comparative_detail = "Nenhuma patente elegível para síntese comparativa"
                    self.memory.append(
                        "synthesis",
                        "comparative_analysis_skipped",
                        "Síntese comparativa pulada por falta de patentes elegíveis.",
                        {"patents_compared": 0},
                    )
                    self.emit_log(
                        logging.INFO,
                        "comparative_analysis_skipped",
                        reason="Nenhuma patente elegível para síntese comparativa",
                    )
                elif has_substantive_comparative_analysis(state.comparative_analysis):
                    comparative_status = "ok"
                    comparative_detail = "Síntese comparativa gerada"
                    self.memory.append(
                        "synthesis",
                        "comparative_analysis_completed",
                        "Síntese comparativa gerada via Ollama.",
                        {"patents_compared": len(analysis_patents)},
                    )
                else:
                    comparative_status = "degraded"
                    comparative_detail = "Fallback da síntese comparativa"
                    self.emit_error("Falha na geração da análise comparativa via Ollama.")
                    self.memory.append(
                        "synthesis",
                        "comparative_analysis_fallback",
                        "Síntese comparativa caiu em fallback após falha do Ollama.",
                        {"patents_compared": len(analysis_patents)},
                    )
                    self.emit_log(
                        logging.WARNING,
                        "comparative_analysis_fallback",
                        patents_compared=len(analysis_patents),
                    )
            else:
                state.comparative_analysis = COMPARATIVE_ANALYSIS_NO_INPUT
                comparative_status = "skipped"
                comparative_detail = "Nenhuma patente elegível para síntese comparativa"
                self.memory.append(
                    "synthesis",
                    "comparative_analysis_skipped",
                    "Síntese comparativa pulada por falta de patentes elegíveis.",
                    {"patents_compared": 0},
                )
                self.emit_log(
                    logging.INFO,
                    "comparative_analysis_skipped",
                    reason="Nenhuma patente elegível para síntese comparativa",
                )
            state.comparative_analysis_duration_seconds = round(
                time.perf_counter() - comp_start,
                3,
            )
            if comparative_status == "ok":
                self.emit_log(
                    logging.INFO,
                    "comparative_analysis_completed",
                    patents_compared=len(analysis_patents),
                    duration_seconds=state.comparative_analysis_duration_seconds,
                )
        elif not pipeline_features.enable_comparative_analysis:
            state.comparative_analysis = ""
            comparative_status = "disabled"
            comparative_detail = "Feature de síntese comparativa desabilitada"
        elif state.llm_available and evaluator.is_degraded():
            state.comparative_analysis = ""
            comparative_status = "degraded"
            comparative_detail = "Circuit breaker do LLM ativo; síntese comparativa pulada"
        elif not state.llm_available:
            state.comparative_analysis = ""
            comparative_status = "skipped"
            comparative_detail = "LLM indisponível para síntese comparativa"
        else:
            state.comparative_analysis = ""
            comparative_status = "skipped"
            comparative_detail = "Síntese comparativa requer ao menos 2 patentes"
        self.emit_metric("comparative_analysis",
            synthesis_start,
            time.perf_counter(),
            comparative_status,
            items_processed=len(state.evaluations),
            detail=comparative_detail,
        )

    def _whitespace(self) -> None:
        state = self.state
        evaluator = self.evaluator
        assert evaluator is not None
        query = self.query
        pipeline_features = self.features

        state.current_stage = "whitespace_analysis"
        whitespace_start = time.perf_counter()
        whitespace_status = "skipped"
        whitespace_detail = "Whitespace analysis indisponível"
        state.whitespace_analysis = {}
        if not pipeline_features.enable_whitespace_analysis:
            whitespace_status = "disabled"
            whitespace_detail = "Feature de whitespace analysis desabilitada"
        elif len(state.evaluations) > 1 and hasattr(evaluator, "generate_whitespace_analysis"):
            state.whitespace_analysis = evaluator.generate_whitespace_analysis(
                state.patents,
                state.evaluations,
                query,
            )
            if state.whitespace_analysis.get("status") == "ok":
                whitespace_status = "ok"
                whitespace_detail = "Whitespace analysis estruturada gerada"
                self.memory.append(
                    "synthesis",
                    "whitespace_analysis_completed",
                    "Matriz estruturada de whitespace gerada.",
                    {
                        "selected_patents": state.whitespace_analysis.get("corpus_summary", {}).get("selected_patents", 0),
                        "candidates": len(state.whitespace_analysis.get("whitespace_candidates", [])),
                    },
                )
                self.emit_log(
                    logging.INFO,
                    "whitespace_analysis_completed",
                    selected_patents=state.whitespace_analysis.get("corpus_summary", {}).get("selected_patents", 0),
                    candidates=len(state.whitespace_analysis.get("whitespace_candidates", [])),
                )
            else:
                whitespace_detail = "Whitespace analysis sem corpus elegível"
        self.emit_metric("whitespace_analysis",
            whitespace_start,
            time.perf_counter(),
            whitespace_status,
            items_processed=len(state.whitespace_analysis.get("coverage_matrix", [])),
            detail=whitespace_detail,
        )

    def _persist_after_whitespace(self) -> None:
        """Recalcula prisma/telemetria/observabilidade apos a sintese (legado)."""
        state = self.state
        evaluator = self.evaluator
        assert evaluator is not None
        state.prisma_flow = (
            _prisma_stage_artifact(state, state.coverage_metrics)
            if self.features.enable_prisma
            else {}
        )
        state.llm_cache_stats = evaluator.cache_stats()
        state.llm_telemetry = evaluator.telemetry_stats()
        state.rerank_duration_seconds = round(
            state.llm_telemetry.get("operations", {}).get("rerank", {}).get("total_duration_seconds", 0.0),
            3,
        )
        state.observability_metrics = _build_observability_metrics(state)

    def _reporting(self) -> None:
        state = self.state
        query = self.query
        output_dir = self.output_dir

        state.current_stage = "reporting"
        self.emit_stage("reporting", "Gerando relatórios", output_dir=output_dir)

        report_start = time.perf_counter()
        state.writing_context = _build_writing_context(state)
        self.memory.set_slot(
            "writer",
            {
                "top_patents": state.writing_context.get("top_patents", []),
                "route_summary": state.writing_context.get("route_summary", {}),
            },
            overwrite=True,
        )
        self.memory.append(
            "writer",
            "context_prepared",
            "Contexto compartilhado preparado para o writer.",
            {
                "top_patents": len(state.writing_context.get("top_patents", [])),
                "route_summary": state.writing_context.get("route_summary", {}),
            },
        )
        state.memory_sidecar = self.memory.to_dict()
        state.memory_journal = [entry.to_dict() for entry in self.memory.journal]
        reporter = ReportGenerator(output_dir=output_dir)
        md_path, json_path = reporter.generate_report(
            query,
            state.patents,
            state.evaluations,
            state.comparative_analysis,
            run_metadata=state.to_dict(),
        )
        state.output_paths = {
            "markdown": os.path.abspath(md_path),
            "json": os.path.abspath(json_path),
            "state": os.path.abspath(self.store.state_path),
        }
        self.emit_metric("reporting",
            report_start,
            time.perf_counter(),
            "ok",
            items_processed=len(state.evaluations),
            detail="Relatórios Markdown e JSON",
        )

    def _finalize(self) -> None:
        state = self.state
        query = self.query
        pipeline_features = self.features

        state.status = "completed"
        state.finished_at = datetime.now().isoformat(timespec="seconds")
        state.total_duration_seconds = round(time.perf_counter() - self.start_time, 3)
        finalize_start = time.perf_counter()
        self.memory.append(
            "finalization",
            "report_generated",
            "Relatórios finais gerados com sucesso.",
            {"markdown": state.output_paths["markdown"], "json": state.output_paths["json"]},
        )
        state.memory_sidecar = self.memory.to_dict()
        state.memory_journal = [entry.to_dict() for entry in self.memory.journal]
        if pipeline_features.enable_prisma and state.prisma_flow:
            prisma_path = self.store.save_artifact(f"prisma_flow_{state.run_id}.json", state.prisma_flow)
            state.output_paths["prisma"] = os.path.abspath(prisma_path)
        if pipeline_features.enable_snapshot and state.config_snapshot:
            snapshot_path = self.store.save_artifact(f"config_snapshot_{state.run_id}.json", state.config_snapshot)
            state.output_paths["snapshot"] = os.path.abspath(snapshot_path)
        if state.whitespace_analysis:
            whitespace_path = self.store.save_artifact(
                f"whitespace_analysis_{state.run_id}.json",
                state.whitespace_analysis,
            )
            state.output_paths["whitespace_json"] = os.path.abspath(whitespace_path)
        journal_path = self.store.save_artifact(f"memory_journal_{state.run_id}.json", state.memory_journal)
        sidecar_path = self.store.save_artifact(f"memory_sidecar_{state.run_id}.json", state.memory_sidecar)
        state.output_paths["memory_journal"] = os.path.abspath(journal_path)
        state.output_paths["memory_sidecar"] = os.path.abspath(sidecar_path)
        self.emit_metric("finalization",
            finalize_start,
            time.perf_counter(),
            "ok",
            items_processed=len(state.output_paths),
            detail="Persistência de artefatos e estado",
        )
        reporter = ReportGenerator(output_dir=self.output_dir)
        reporter.write_report_files(
            state.output_paths["markdown"],
            state.output_paths["json"],
            query,
            state.patents,
            state.evaluations,
            state.comparative_analysis,
            run_metadata=state.to_dict(),
        )
        self.store.save(state)

        self.emit_log(
            logging.INFO,
            "reports_generated",
            markdown=state.output_paths.get("markdown", ""),
            json=state.output_paths.get("json", ""),
            prisma=state.output_paths.get("prisma", ""),
            snapshot=state.output_paths.get("snapshot", ""),
            whitespace_json=state.output_paths.get("whitespace_json", ""),
            memory_journal=state.output_paths.get("memory_journal", ""),
            memory_sidecar=state.output_paths.get("memory_sidecar", ""),
        )

        summary_fields = {
            "query": query,
            "patents_found": len(state.patents),
            "total_duration_seconds": round(state.total_duration_seconds, 1),
        }
        if state.coverage_metrics:
            summary_fields.update({
                "duplicates_removed": state.coverage_metrics.get("duplicates_removed", 0),
                "screened": state.coverage_metrics.get("screened", 0),
                "included": state.coverage_metrics.get("included", 0),
                "review": state.coverage_metrics.get("review", 0),
            })
        if state.llm_available:
            scored = [
                e for e in state.evaluations
                if e.screening_decision == "include" and not e.llm_error
            ]
            avg_score = (
                sum(e.relevance_score for e in scored) / len(scored)
                if scored
                else 0
            )
            summary_fields["average_relevance_score"] = round(avg_score, 1)

            top_patents = sorted(
                _pair_patents_with_evaluations(state.patents, state.evaluations),
                key=lambda x: x[1].relevance_score,
                reverse=True,
            )[:3]

            if top_patents:
                for i, (patent, evaluation) in enumerate(top_patents, 1):
                    self.emit_log(
                        logging.INFO,
                        "top_patent",
                        rank=i,
                        patent_id=_display_patent_id(patent),
                        relevance_score=evaluation.relevance_score,
                        title=patent.title[:60],
                    )

        self.emit_log(
            logging.INFO,
            "run_summary",
            **summary_fields,
        )

        if state.manual_review_queue:
            patent_map = {
                patent.record_id: patent
                for patent in state.patents
            }
            for item in state.manual_review_queue[:10]:
                record_id = item.get("record_id", "")
                patent = patent_map.get(record_id)
                if patent:
                    self.emit_log(
                        logging.INFO,
                        "manual_review_item",
                        record_id=record_id,
                        patent_id=_display_patent_id(patent),
                        route=item.get("route", "N/A"),
                    )
                else:
                    self.emit_log(
                        logging.INFO,
                        "manual_review_item",
                        record_id=record_id,
                        route=item.get("route", "N/A"),
                    )
            if len(state.manual_review_queue) > 10:
                self.emit_log(
                    logging.INFO,
                    "manual_review_overflow",
                    omitted=len(state.manual_review_queue) - 10,
                )

        if state.thematic_clusters and state.thematic_clusters.get("clusters"):
            for cluster in state.thematic_clusters["clusters"][:5]:
                self.emit_log(
                    logging.INFO,
                    "thematic_cluster_summary",
                    cluster=cluster["cluster"],
                    patents=cluster["count"],
                    average_score=round(cluster["average_score"], 1),
                )

        if state.errors:
            for error in state.errors:
                self.emit_log(
                    logging.WARNING,
                    "run_error",
                    detail=error,
                )

        self.emit_log(
            logging.INFO,
            "run_completed",
            status=state.status,
            total_duration_seconds=round(state.total_duration_seconds, 1),
            output_paths=state.output_paths,
        )