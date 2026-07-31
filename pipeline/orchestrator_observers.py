"""
Observadores concretos do pipeline.

Cada observer aqui e um wrapper fino sobre um helper existente no modulo
``pipeline.orchestrator``. Nada substitui o comportamento original: apenas
reendereca side-effects por meio de eventos, mantendo compatibilidade total.

Os helpers permanecem definidos em ``orchestrator.py`` e sao injetados nos
observers (via callable ou logger).``run_agent`` instanciara um
``EventBus`` e o conjunto default destes observers.
"""

from __future__ import annotations

import logging
from typing import Any, Callable, Mapping

from logging_utils import log_event

from pipeline.observers import (
    ErrorEvent,
    PatentEvent,
    PipelineEvent,
    ProgressEvent,
    StageEvent,
)
from pipeline.state import RunState


class LoggingObserver:
    """Replica ``log_event(logger, level, event.kind, **fields)``."""

    def __init__(self, logger: logging.Logger) -> None:
        self._logger = logger

    def on_event(self, event: PipelineEvent) -> None:
        fields = dict(event.fields)
        if event.stage:
            fields.setdefault("stage", event.stage)
        if event.run_id:
            fields.setdefault("run_id", event.run_id)
        if isinstance(event, StageEvent):
            if event.title:
                fields.setdefault("title", event.title)
            if event.detail:
                fields.setdefault("detail", event.detail)
            if event.items_processed:
                fields.setdefault("items_processed", event.items_processed)
            if event.status:
                fields.setdefault("status", event.status)
            if event.duration_seconds:
                fields.setdefault("duration_seconds", event.duration_seconds)
        elif isinstance(event, PatentEvent):
            if event.patent_id:
                fields.setdefault("patent_id", event.patent_id)
            if event.title:
                fields.setdefault("title", event.title)
        elif isinstance(event, ErrorEvent):
            if event.error:
                fields.setdefault("error", event.error)

        log_event(self._logger, event.level, event.kind, **fields)


class ProgressObserver:
    """Replica ``print_progress(step, current, total)`` do orchestrator."""

    def __init__(self, print_progress: Callable[..., None]) -> None:
        self._print_progress = print_progress

    def on_event(self, event: PipelineEvent) -> None:
        if isinstance(event, ProgressEvent):
            self._print_progress(event.step, event.current, event.total)


class StageMetricObserver:
    """Anexa a metrica de fim de etapa em ``state.stage_metrics``.

    Reage a ``StageEvent`` cujo ``kind`` denote fim de etapa
    (``stage_metric``/``stage_end``/``<stage>_end``). O log estruturado
    ``stage_metric`` fica a cargo do ``LoggingObserver`` (que loga o ``kind``
    do evento), evitando duplicacao.
    """

    def __init__(self, state: RunState) -> None:
        self._state = state

    @staticmethod
    def _is_metric_event(event: StageEvent) -> bool:
        return (
            event.kind == "stage_metric"
            or event.kind == "stage_end"
            or event.kind.endswith("_end")
        )

    def on_event(self, event: PipelineEvent) -> None:
        if not isinstance(event, StageEvent):
            return
        if not self._is_metric_event(event):
            return
        self._state.stage_metrics.append({
            "stage": event.stage,
            "status": event.status,
            "duration_seconds": round(event.duration_seconds, 3),
            "items_processed": event.items_processed,
            "detail": event.detail,
        })


class MemoryObserver:
    """Replica ``memory.append(stage, event, detail, payload)``.

    A mensagem do journal e derivada de ``title``|``detail``|``kind``; o
    payload combina ``fields`` com ``record``/``extra`` (quando presentes).
    """

    def __init__(self, memory: Any) -> None:
        self._memory = memory

    def on_event(self, event: PipelineEvent) -> None:
        if isinstance(event, StageEvent):
            detail = event.title or event.detail or event.kind
        else:
            detail = (event.fields.get("description")
                      or getattr(event, "title", "")
                      or event.kind)

        payload: Mapping[str, Any] = dict(event.fields)
        if isinstance(event, PatentEvent):
            if event.record:
                payload = {**payload, **event.record}
            if event.extra:
                payload = {**payload, **event.extra}
        self._memory.append(event.stage, event.kind, detail, dict(payload))


class PersistenceObserver:
    """Replica ``store.save(state)`` ao fim de cada etapa."""

    def __init__(self, store: Any, state: RunState) -> None:
        self._store = store
        self._state = state

    def on_event(self, event: PipelineEvent) -> None:
        if isinstance(event, StageEvent) and (
            event.kind.endswith("_end") or event.kind == "stage_end"
        ):
            self._store.save(self._state)


class ErrorObserver:
    """Replica ``state.errors.append(message)`` do bloco de erros."""

    def __init__(self, state: RunState) -> None:
        self._state = state

    def on_event(self, event: PipelineEvent) -> None:
        if isinstance(event, ErrorEvent) and event.error:
            self._state.errors.append(event.error)


def build_default_observers(
    state: RunState,
    store: Any,
    memory: Any,
    logger: logging.Logger,
    print_progress: Callable[..., None],
    *,
    include_memory: bool = True,
    include_persistence: bool = True,
) -> list:
    """Monta o conjunto padrao de observers injetando dependencias legadas.

    ``include_memory``/``include_persistence`` permitem excluir
    ``MemoryObserver``/``PersistenceObserver`` durante a migracao incremental
    quando ``memory.append``/``store.save`` continuam sendo chamados
    explicitamente pelo orquestrador para preservar paridade 1:1.
    """
    observers = [
        LoggingObserver(logger),
        ProgressObserver(print_progress),
        StageMetricObserver(state),
        ErrorObserver(state),
    ]
    if include_memory:
        observers.append(MemoryObserver(memory))
    if include_persistence:
        observers.append(PersistenceObserver(store, state))
    return observers