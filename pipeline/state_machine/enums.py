"""
Enums de estágio e status do pipeline.

Stage: estágios do pipeline (onde estamos)
Status: status de execução (como está)
"""

from enum import Enum


class Stage(Enum):
    """Estágios do pipeline de patentes."""
    
    # Inicial
    IDLE = "idle"
    
    # Pipeline principal
    SETUP = "setup"
    SEARCH = "search"
    SCREENING = "screening"
    COMPARATIVE_ANALYSIS = "comparative_analysis"
    WHITESPACE_ANALYSIS = "whitespace_analysis"
    REPORTING = "reporting"
    
    # Terminal (sucesso)
    DONE = "done"
    
    # Terminal (sem resultados)
    NO_RESULTS = "no_results"
    
    # Terminal (erro)
    FAILED = "failed"


class Status(Enum):
    """Status de execução do pipeline."""
    
    # Antes de iniciar
    IDLE = "idle"
    
    # Executando
    RUNNING = "running"
    
    # Terminal (sucesso)
    COMPLETED = "completed"
    
    # Terminal (sem resultados)
    NO_RESULTS = "no_results"
    
    # Terminal (erro)
    ERROR = "error"
