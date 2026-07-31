"""
Máquina de estados para o pipeline de patentes.

Controla transições válidas entre estágios do pipeline,
garantindo consistência e prevenindo estados inválidos.
"""

from pipeline.state_machine.enums import Stage, Status
from pipeline.state_machine.exceptions import InvalidTransitionError
from pipeline.state_machine.machine import PipelineStateMachine
from pipeline.state_machine.transitions import STATUS_MAP, TRANSITIONS

__all__ = [
    "Stage",
    "Status",
    "InvalidTransitionError",
    "PipelineStateMachine",
    "TRANSITIONS",
    "STATUS_MAP",
]
