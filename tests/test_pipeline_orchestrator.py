"""Testes dedicados do ``PipelineOrchestrator`` (Fase 6).

Cobrem:
  * Inversao de dependencia (Fase 5): barramento vazio quando nem
    ``observers`` nem ``observers_builder`` sao fornecidos.
  * Precedencia de ``observers`` (lista pronta) sobre ``observers_builder``.
  * ``observers_builder`` recebendo o contexto interno (state/store/memory).
  * Snapshot da sequencia de eventos numa execucao congelada.
  * Desacoplamento: sem observers default, ``state.stage_metrics`` fica vazio
    (comprovando que side-effects nao sao acoplados a classe).
"""

from __future__ import annotations

import os
import tempfile
import unittest
from typing import List

from pipeline.features import PipelineFeatures
from pipeline.frozen_benchmark import build_frozen_components
from pipeline.observers import (
    Observer,
    PipelineEvent,
    StageEvent,
)
from pipeline.pipeline_orchestrator import PipelineOrchestrator


class _CapturingObserver:
    def __init__(self) -> None:
        self.events: List[PipelineEvent] = []

    def on_event(self, event: PipelineEvent) -> None:
        self.events.append(event)


def _fixture_path() -> str:
    return os.path.join("benchmarks", "frozen_pipeline_fixture.json")


class ObserverInjectionTests(unittest.TestCase):
    def test_empty_bus_when_no_observers_and_no_builder(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            orch = PipelineOrchestrator(
                query="q",
                max_results=3,
                model="m",
                output_dir=tmpdir,
            )
        self.assertEqual(len(orch.bus), 0)
        self.assertIsInstance(orch.state.run_id, str)
        self.assertIsNotNone(orch.store)
        self.assertIsNotNone(orch.memory)

    def test_observers_list_takes_precedence_over_builder(self):
        builder_called = {"n": 0}

        def _builder(state, store, memory):
            builder_called["n"] += 1
            return []

        sentinel_a = _CapturingObserver()
        sentinel_b = _CapturingObserver()
        with tempfile.TemporaryDirectory() as tmpdir:
            orch = PipelineOrchestrator(
                query="q",
                max_results=3,
                model="m",
                output_dir=tmpdir,
                observers=[sentinel_a, sentinel_b],
                observers_builder=_builder,
            )
        self.assertEqual(builder_called["n"], 0, "builder nao deve ser chamado quando observers=lista")
        self.assertEqual(len(orch.bus), 2)

    def test_observers_builder_receives_internal_context(self):
        seen = {}

        class Marker:
            def on_event(self, event: PipelineEvent) -> None: ...

        def _builder(state, store, memory):
            seen["state"] = state
            seen["store"] = store
            seen["memory"] = memory
            return [Marker()]

        with tempfile.TemporaryDirectory() as tmpdir:
            orch = PipelineOrchestrator(
                query="q",
                max_results=3,
                model="m",
                output_dir=tmpdir,
                observers_builder=_builder,
            )
        self.assertIs(seen["state"], orch.state)
        self.assertIs(seen["store"], orch.store)
        self.assertIs(seen["memory"], orch.memory)
        self.assertEqual(len(orch.bus), 1)


class EventSequenceSnapshotTests(unittest.TestCase):
    def test_frozen_run_emits_expected_event_sequence(self):
        scrapers, evaluator_factory = build_frozen_components(_fixture_path())
        capturer = _CapturingObserver()

        with tempfile.TemporaryDirectory() as tmpdir:
            state = PipelineOrchestrator(
                query="carbon dioxide thermal energy storage",
                max_results=5,
                model="frozen-model",
                output_dir=tmpdir,
                features=PipelineFeatures(),
                scrapers=scrapers,
                evaluator_factory=evaluator_factory,
                observers=[capturer],
            ).run()

        self.assertEqual(state.status, "completed")
        self.assertTrue(capturer.events, "nenhum evento capturado")

        kinds = [e.kind for e in capturer.events]
        self.assertIn("stage_transition", kinds)
        self.assertIn("stage_metric", kinds)
        self.assertIn("run_completed", kinds)

        stage_transitions = [
            (e.stage, e.title)
            for e in capturer.events
            if isinstance(e, StageEvent) and e.kind == "stage_transition"
        ]
        stage_order = [stage for stage, _ in stage_transitions]
        # whitespace_analysis nao emite stage_transition no legado (paridade);
        # apenas stage_metric. Os demais estagios transicionam explicitamente.
        for expected in ("setup", "search", "screening", "comparative_analysis",
                         "reporting"):
            self.assertIn(expected, stage_order, f"estagio {expected} ausente")

        metric_stages = [
            e.stage
            for e in capturer.events
            if isinstance(e, StageEvent) and e.kind == "stage_metric"
        ]
        for expected in ("setup", "search", "screening", "comparative_analysis",
                         "whitespace_analysis", "reporting", "finalization"):
            self.assertIn(expected, metric_stages, f"metrica de {expected} ausente")

        self.assertEqual(capturer.events[-1].kind, "run_completed")

    def test_no_default_observers_means_empty_stage_metrics_and_clean_state(self):
        scrapers, evaluator_factory = build_frozen_components(_fixture_path())
        capturer = _CapturingObserver()

        with tempfile.TemporaryDirectory() as tmpdir:
            state = PipelineOrchestrator(
                query="carbon dioxide thermal energy storage",
                max_results=5,
                model="frozen-model",
                output_dir=tmpdir,
                features=PipelineFeatures(),
                scrapers=scrapers,
                evaluator_factory=evaluator_factory,
                observers=[capturer],
            ).run()

        self.assertEqual(state.stage_metrics, [], "sem StageMetricObserver nao ha metricas")
        self.assertEqual(state.errors, [], "sem ErrorObserver nenhum erro e coletado")
        self.assertTrue(capturer.events)
        self.assertEqual(len(capturer.events), len(set(map(id, capturer.events))))


class ObserverProtocolTests(unittest.TestCase):
    def test_capturing_observer_satisfies_observer_protocol(self):
        self.assertIsInstance(_CapturingObserver(), Observer)


if __name__ == "__main__":
    unittest.main()