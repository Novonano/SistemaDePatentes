"""Testes dos observers concretos (Fase 1) e do EventBus (Fase 0).

Estilo unittest (sem pytest), alinhado a tests/test_frozen_pipeline.py.
"""

from __future__ import annotations

import logging
import unittest
from typing import List

from pipeline.memory import MemorySidecar
from pipeline.observers import (
    ErrorEvent,
    EventBus,
    PatentEvent,
    PipelineEvent,
    ProgressEvent,
    StageEvent,
)
from pipeline.orchestrator_observers import (
    ErrorObserver,
    LoggingObserver,
    MemoryObserver,
    PersistenceObserver,
    ProgressObserver,
    StageMetricObserver,
    build_default_observers,
)
from pipeline.state import RunState


class _ListHandler(logging.Handler):
    def __init__(self) -> None:
        super().__init__(level=logging.DEBUG)
        self.records: List[logging.LogRecord] = []

    def emit(self, record: logging.LogRecord) -> None:
        self.records.append(record)


def _make_state() -> RunState:
    return RunState(query="q", max_results=3, model="m", output_dir="out")


class EventBusTests(unittest.TestCase):
    def test_notifies_in_order_and_isolates_exceptions(self):
        bus = EventBus()
        received: List[str] = []

        class Fine:
            def on_event(self, event: PipelineEvent) -> None:
                received.append(event.kind)

        class Boom:
            def on_event(self, event: PipelineEvent) -> None:
                raise RuntimeError("observer morto")

        fine = Fine()
        bus.subscribe(fine)
        bus.subscribe(Boom())
        another = Fine()
        bus.subscribe(another)
        self.assertEqual(len(bus), 3)

        with self.assertLogs("pipeline.observers", level="ERROR"):
            bus.emit(StageEvent(kind="stage_end", level=logging.INFO, stage="setup"))

        self.assertEqual(received.count("stage_end"), 2)
        self.assertEqual(received[-1], "stage_end")
        bus.unsubscribe(fine)
        self.assertEqual(len(bus), 2)
        bus.unsubscribe(fine)
        self.assertEqual(len(bus), 2)

    def test_subscribe_is_idempotent(self):
        bus = EventBus()

        class O:
            def on_event(self, event: PipelineEvent) -> None: ...

        o = O()
        bus.subscribe(o)
        bus.subscribe(o)
        self.assertEqual(len(bus), 1)


class LoggingObserverTests(unittest.TestCase):
    def test_emits_structured_event_with_fields_and_stage(self):
        handler = _ListHandler()
        logger = logging.getLogger("test_logging_observer")
        logger.handlers = [handler]
        logger.setLevel(logging.DEBUG)
        logger.propagate = False

        obs = LoggingObserver(logger)
        obs.on_event(StageEvent(
            kind="stage_begin",
            level=logging.INFO,
            stage="screening",
            title="Triagem",
            fields={"include_threshold": 0.6},
        ))

        self.assertTrue(handler.records)
        rec = handler.records[0]
        self.assertEqual(rec.event_name, "stage_begin")
        self.assertEqual(rec.event_fields["stage"], "screening")
        self.assertEqual(rec.event_fields["include_threshold"], 0.6)
        self.assertEqual(rec.event_fields["title"], "Triagem")

    def test_patent_event_includes_patent_id_and_title(self):
        handler = _ListHandler()
        logger = logging.getLogger("test_logging_patent")
        logger.handlers = [handler]
        logger.setLevel(logging.DEBUG)
        logger.propagate = False

        LoggingObserver(logger).on_event(PatentEvent(
            kind="patent_discovered",
            level=logging.INFO,
            stage="identification",
            patent_id="US999",
            title="Algo",
        ))

        rec = handler.records[0]
        self.assertEqual(rec.event_fields["patent_id"], "US999")
        self.assertEqual(rec.event_fields["title"], "Algo")


class ProgressObserverTests(unittest.TestCase):
    def test_delegates_to_print_progress_only_for_progress_events(self):
        calls: List[tuple] = []

        def fake_print_progress(step: str, current: int = 0, total: int = 0) -> None:
            calls.append((step, current, total))

        obs = ProgressObserver(print_progress=fake_print_progress)
        obs.on_event(ProgressEvent(
            kind="progress",
            level=logging.DEBUG,
            step="Buscando",
            current=2,
            total=10,
        ))
        obs.on_event(StageEvent(kind="stage_end", level=logging.INFO, stage="x"))

        self.assertEqual(calls, [("Buscando", 2, 10)])


class StageMetricObserverTests(unittest.TestCase):
    def test_records_metric_on_stage_metric_kind(self):
        state = _make_state()
        obs = StageMetricObserver(state)
        obs.on_event(StageEvent(
            kind="stage_metric",
            level=logging.INFO,
            stage="search",
            status="ok",
            duration_seconds=1.234,
            items_processed=12,
            detail="dedupe",
        ))
        self.assertEqual(state.stage_metrics, [{
            "stage": "search",
            "status": "ok",
            "duration_seconds": 1.234,
            "items_processed": 12,
            "detail": "dedupe",
        }])

    def test_records_metric_on_stage_end_kind(self):
        state = _make_state()
        obs = StageMetricObserver(state)
        obs.on_event(StageEvent(
            kind="stage_end", level=logging.INFO, stage="setup", status="ok",
            duration_seconds=0.5,
        ))
        self.assertEqual(len(state.stage_metrics), 1)

    def test_begin_does_not_record_metric(self):
        state = _make_state()
        obs = StageMetricObserver(state)
        obs.on_event(StageEvent(kind="stage_begin", level=logging.INFO, stage="search"))
        self.assertEqual(state.stage_metrics, [])


class MemoryObserverTests(unittest.TestCase):
    def test_appends_journal_entry_with_merged_payload(self):
        memory = MemorySidecar(run_id="rid")
        obs = MemoryObserver(memory)
        ev = PatentEvent(
            kind="screening_completed",
            level=logging.INFO,
            stage="screening",
            patent_id="US123",
            title="Titulo curto",
            record={"record_id": "rec_abc"},
            fields={"decision": "include"},
        )
        obs.on_event(ev)

        self.assertEqual(len(memory.journal), 1)
        entry = memory.journal[0]
        self.assertEqual(entry.stage, "screening")
        self.assertEqual(entry.event, "screening_completed")
        self.assertEqual(entry.detail, "Titulo curto")
        self.assertEqual(entry.payload["decision"], "include")
        self.assertEqual(entry.payload["record_id"], "rec_abc")

    def test_stage_event_uses_title_as_detail(self):
        memory = MemorySidecar(run_id="rid")
        MemoryObserver(memory).on_event(StageEvent(
            kind="stage_end",
            level=logging.INFO,
            stage="setup",
            title="Config OK",
            detail="modelo verificado",
        ))
        self.assertEqual(memory.journal[0].detail, "Config OK")


class PersistenceObserverTests(unittest.TestCase):
    def test_saves_on_stage_end_only(self):
        state = _make_state()
        saved: List[RunState] = []

        class FakeStore:
            def save(self, s: RunState) -> None:
                saved.append(s)

        obs = PersistenceObserver(FakeStore(), state)
        obs.on_event(StageEvent(kind="stage_end", level=logging.INFO, stage="setup"))
        obs.on_event(StageEvent(kind="stage_begin", level=logging.INFO, stage="search"))

        self.assertEqual(saved, [state])


class ErrorObserverTests(unittest.TestCase):
    def test_collects_error_messages(self):
        state = _make_state()
        obs = ErrorObserver(state)
        obs.on_event(ErrorEvent(kind="run_error", level=logging.WARNING, error="boom"))
        obs.on_event(StageEvent(kind="stage_end", level=logging.INFO, stage="x"))
        self.assertEqual(state.errors, ["boom"])

    def test_ignores_empty_error(self):
        state = _make_state()
        ErrorObserver(state).on_event(
            ErrorEvent(kind="run_error", level=logging.WARNING, error=""))
        self.assertEqual(state.errors, [])


class BuildDefaultObserversTests(unittest.TestCase):
    def test_returns_six_distinct_observer_types_by_default(self):
        state = _make_state()

        class FakeStore:
            def save(self, s: RunState) -> None: ...

        observers = build_default_observers(
            state, FakeStore(), MemorySidecar(run_id="rid"),
            logging.getLogger("test_build"),
            lambda *a, **k: None,
        )
        expected = {
            LoggingObserver, ProgressObserver, StageMetricObserver,
            MemoryObserver, PersistenceObserver, ErrorObserver,
        }
        self.assertEqual({type(o) for o in observers}, expected)
        self.assertEqual(len(observers), 6)

    def test_excludes_memory_and_persistence_when_disabled(self):
        state = _make_state()

        class FakeStore:
            def save(self, s: RunState) -> None: ...

        observers = build_default_observers(
            _make_state(), FakeStore(), MemorySidecar(run_id="rid"),
            logging.getLogger("test_build_subset"),
            lambda *a, **k: None,
            include_memory=False,
            include_persistence=False,
        )
        types = {type(o) for o in observers}
        self.assertEqual(types, {
            LoggingObserver, ProgressObserver, StageMetricObserver, ErrorObserver,
        })
        self.assertEqual(len(observers), 4)


if __name__ == "__main__":
    unittest.main()