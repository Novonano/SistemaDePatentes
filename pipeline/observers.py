from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, List, Mapping, Protocol, runtime_checkable

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True, kw_only=True)
class PipelineEvent:
    """Evento base do pipeline emitido pelo orquestrador."""

    kind: str
    level: int
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))
    stage: str = ""
    fields: Mapping[str, Any] = field(default_factory=dict)
    run_id: str = ""


@dataclass(frozen=True, slots=True, kw_only=True)
class StageEvent(PipelineEvent):
    """Transicao de etapa (begin/end) com metrica de duracao."""

    title: str = ""
    detail: str = ""
    items_processed: int = 0
    status: str = "ok"
    duration_seconds: float = 0.0


@dataclass(frozen=True, slots=True, kw_only=True)
class PatentEvent(PipelineEvent):
    """Evento de uma patente individual (descoberta, triagem, extracao)."""

    patent_id: str = ""
    title: str = ""
    record: Mapping[str, Any] = field(default_factory=dict)
    # Alias legado para consumidores que esperavam ``extra``.
    extra: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True, kw_only=True)
class ErrorEvent(PipelineEvent):
    """Falha capturada durante uma etapa."""

    error: str = ""
    exc_info: Any = None


@dataclass(frozen=True, slots=True, kw_only=True)
class ProgressEvent(PipelineEvent):
    """Atualizacao de progresso incremental de uma etapa."""

    step: str = ""
    current: int = 0
    total: int = 0
    percent: float = 0.0


@runtime_checkable
class Observer(Protocol):
    """Contrato estrutural de um observador de eventos do pipeline."""

    def on_event(self, event: PipelineEvent) -> None:
        """Recebe um evento emitido pelo barramento."""
        ...


class EventBus:
    """Barramento sincrono que notifica observers na ordem de inscricao.

    Excecoes lancadas por um observer sao isoladas (logadas em ``logger``) e
    nao interrompem a notificacao dos demais observers, garantindo que um
    side-effect falho nao quebre o fluxo do pipeline.
    """

    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        """Inscreve um observer (idempotente: nao duplica)."""
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        """Remove um observer previamente inscrito (no-op se ausente)."""
        if observer in self._observers:
            self._observers.remove(observer)

    def emit(self, event: PipelineEvent) -> None:
        """Notifica todos os observers, isolando falhas individuais."""
        for observer in list(self._observers):
            try:
                observer.on_event(event)
            except Exception:
                logger.exception(
                    "Observer %r falhou ao processar evento %s",
                    observer,
                    event.kind,
                )

    def __len__(self) -> int:
        return len(self._observers)