"""
Estado persistido de uma execução do pipeline.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List

from models.patent import Patent, PatentEvaluation
from pipeline.state_machine import PipelineStateMachine, Stage, Status


@dataclass
class RunState:
    """Resumo persistido de uma execução."""

    query: str
    max_results: int
    model: str
    output_dir: str
    feature_flags: Dict[str, object] = field(default_factory=dict)
    config_snapshot: Dict[str, object] = field(default_factory=dict)
    snapshot_hash: str = ""
    protocol: Dict[str, object] = field(default_factory=dict)
    writing_context: Dict[str, object] = field(default_factory=dict)
    memory_sidecar: Dict[str, object] = field(default_factory=dict)
    memory_journal: List[Dict[str, object]] = field(default_factory=list)
    stage_metrics: List[Dict[str, object]] = field(default_factory=list)
    llm_cache_stats: Dict[str, int] = field(default_factory=dict)
    llm_telemetry: Dict[str, object] = field(default_factory=dict)
    observability_metrics: Dict[str, object] = field(default_factory=dict)
    run_id: str = field(default_factory=lambda: datetime.now().strftime("%Y%m%d_%H%M%S"))
    started_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )
    finished_at: str = ""
    screened_count: int = 0
    llm_available: bool = False
    patents: List[Patent] = field(default_factory=list)
    evaluations: List[PatentEvaluation] = field(default_factory=list)
    patents_by_source: Dict[str, int] = field(default_factory=dict)
    scraper_diagnostics: Dict[str, List[Dict[str, str]]] = field(default_factory=dict)
    coverage_metrics: Dict[str, int] = field(default_factory=dict)
    manual_review_queue: List[Dict[str, object]] = field(default_factory=list)
    prisma_flow: Dict[str, object] = field(default_factory=dict)
    thematic_clusters: Dict[str, object] = field(default_factory=dict)
    whitespace_analysis: Dict[str, object] = field(default_factory=dict)
    scraper_durations: Dict[str, float] = field(default_factory=dict)
    evaluation_duration_seconds: float = 0.0
    rerank_duration_seconds: float = 0.0
    comparative_analysis_duration_seconds: float = 0.0
    total_duration_seconds: float = 0.0
    comparative_analysis: str = ""
    output_paths: Dict[str, str] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)
    
    # Máquina de estados (privada, não serializada diretamente)
    _state_machine: PipelineStateMachine = field(
        default_factory=PipelineStateMachine,
        repr=False,
        compare=False,
    )
    
    @property
    def status(self) -> str:
        """Status derivado da máquina de estados."""
        return self._state_machine.status.value
    
    @status.setter
    def status(self, value: str) -> None:
        """Setter no-op para compatibilidade com código legado."""
        pass
    
    @property
    def current_stage(self) -> str:
        """Estágio atual derivado da máquina de estados."""
        return self._state_machine.stage.value
    
    @current_stage.setter
    def current_stage(self, value: str) -> None:
        """Setter no-op para compatibilidade com código legado."""
        pass
    
    def __post_init__(self):
        """Inicializa máquina de estados."""
        pass
    
    def transition_to(self, stage: Stage) -> None:
        """Transiciona para um novo estágio, validando via máquina de estados.
        
        Args:
            stage: estágio de destino
            
        Raises:
            InvalidTransitionError: se a transição não é válida
        """
        self._state_machine.transition_to(stage)

    def to_dict(self) -> dict:
        """Converte o estado para JSON serializável."""
        return {
            "query": self.query,
            "max_results": self.max_results,
            "model": self.model,
            "output_dir": self.output_dir,
            "feature_flags": self.feature_flags,
            "config_snapshot": self.config_snapshot,
            "snapshot_hash": self.snapshot_hash,
            "protocol": self.protocol,
            "writing_context": self.writing_context,
            "memory_sidecar": self.memory_sidecar,
            "memory_journal": self.memory_journal,
            "stage_metrics": self.stage_metrics,
            "llm_cache_stats": self.llm_cache_stats,
            "llm_telemetry": self.llm_telemetry,
            "observability_metrics": self.observability_metrics,
            "run_id": self.run_id,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "status": self.status,
            "current_stage": self.current_stage,
            "screened_count": self.screened_count,
            "llm_available": self.llm_available,
            "patents": [patent.to_dict() for patent in self.patents],
            "evaluations": [evaluation.to_dict() for evaluation in self.evaluations],
            "patents_by_source": self.patents_by_source,
            "scraper_diagnostics": self.scraper_diagnostics,
            "coverage_metrics": self.coverage_metrics,
            "manual_review_queue": self.manual_review_queue,
            "prisma_flow": self.prisma_flow,
            "thematic_clusters": self.thematic_clusters,
            "whitespace_analysis": self.whitespace_analysis,
            "scraper_durations": self.scraper_durations,
            "evaluation_duration_seconds": self.evaluation_duration_seconds,
            "rerank_duration_seconds": self.rerank_duration_seconds,
            "comparative_analysis_duration_seconds": self.comparative_analysis_duration_seconds,
            "total_duration_seconds": self.total_duration_seconds,
            "comparative_analysis": self.comparative_analysis,
            "output_paths": self.output_paths,
            "errors": self.errors,
            "state_machine": self._state_machine.to_dict(),
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "RunState":
        """Restaura estado a partir de JSON, validando consistência da máquina.
        
        Args:
            data: dicionário com dados do estado
            
        Returns:
            RunState restaurado
            
        Raises:
            ValueError: se o estado persistido é inconsistente
        """
        from models.patent import Patent, PatentEvaluation
        
        state = cls(
            query=data.get("query", ""),
            max_results=data.get("max_results", 0),
            model=data.get("model", ""),
            output_dir=data.get("output_dir", ""),
            feature_flags=data.get("feature_flags", {}),
            config_snapshot=data.get("config_snapshot", {}),
            snapshot_hash=data.get("snapshot_hash", ""),
            protocol=data.get("protocol", {}),
            writing_context=data.get("writing_context", {}),
            memory_sidecar=data.get("memory_sidecar", {}),
            memory_journal=data.get("memory_journal", []),
            stage_metrics=data.get("stage_metrics", []),
            llm_cache_stats=data.get("llm_cache_stats", {}),
            llm_telemetry=data.get("llm_telemetry", {}),
            observability_metrics=data.get("observability_metrics", {}),
            run_id=data.get("run_id", ""),
            started_at=data.get("started_at", ""),
            finished_at=data.get("finished_at", ""),
            screened_count=data.get("screened_count", 0),
            llm_available=data.get("llm_available", False),
            patents=[Patent.from_dict(p) for p in data.get("patents", [])],
            evaluations=[PatentEvaluation.from_dict(e) for e in data.get("evaluations", [])],
            patents_by_source=data.get("patents_by_source", {}),
            scraper_diagnostics=data.get("scraper_diagnostics", {}),
            coverage_metrics=data.get("coverage_metrics", {}),
            manual_review_queue=data.get("manual_review_queue", []),
            prisma_flow=data.get("prisma_flow", {}),
            thematic_clusters=data.get("thematic_clusters", {}),
            whitespace_analysis=data.get("whitespace_analysis", {}),
            scraper_durations=data.get("scraper_durations", {}),
            evaluation_duration_seconds=data.get("evaluation_duration_seconds", 0.0),
            rerank_duration_seconds=data.get("rerank_duration_seconds", 0.0),
            comparative_analysis_duration_seconds=data.get("comparative_analysis_duration_seconds", 0.0),
            total_duration_seconds=data.get("total_duration_seconds", 0.0),
            comparative_analysis=data.get("comparative_analysis", ""),
            output_paths=data.get("output_paths", {}),
            errors=data.get("errors", []),
        )
        
        # Valida consistência com máquina de estados persistida
        persisted_sm = data.get("state_machine", {})
        if persisted_sm:
            persisted_stage = persisted_sm.get("stage", "idle")
            current_stage = state.current_stage
            
            # Verifica se o estágio atual corresponde ao persistido
            if current_stage != persisted_stage:
                raise ValueError(
                    f"Inconsistência de estado: current_stage={current_stage}, "
                    f"state_machine.stage={persisted_stage}"
                )
            
            # Valida que o histórico é consistente
            persisted_history = persisted_sm.get("history", [])
            current_history = state._state_machine.history
            if len(persisted_history) != len(current_history):
                raise ValueError(
                    f"Histórico inconsistente: persistido={len(persisted_history)}, "
                    f"atual={len(current_history)}"
                )
        
        return state
