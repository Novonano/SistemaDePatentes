"""
Classe principal da máquina de estados.

PipelineStateMachine encapsula toda a lógica de transição entre estágios,
validando transições contra a matriz TRANSITIONS e derivando status
automaticamente via STATUS_MAP.
"""

from typing import List, Tuple

from pipeline.state_machine.enums import Stage, Status
from pipeline.state_machine.exceptions import InvalidTransitionError
from pipeline.state_machine.transitions import STATUS_MAP, TRANSITIONS


class PipelineStateMachine:
    """Máquina de estados para o pipeline de patentes.
    
    Valida transições entre estágios e mantém o estado atual.
    O status é derivado automaticamente do estágio atual.
    """
    
    def __init__(self) -> None:
        """Inicializa a máquina no estágio IDLE."""
        self._stage = Stage.IDLE
        self._history: List[Tuple[Stage, Stage]] = []
    
    @property
    def stage(self) -> Stage:
        """Retorna o estágio atual."""
        return self._stage
    
    @property
    def status(self) -> Status:
        """Retorna o status derivado do estágio atual.
        
        Usa STATUS_MAP para estágios terminais (IDLE, DONE, NO_RESULTS, FAILED).
        Para todos os outros estágios, retorna Status.RUNNING.
        """
        return STATUS_MAP.get(self._stage, Status.RUNNING)
    
    @property
    def history(self) -> List[Tuple[Stage, Stage]]:
        """Retorna o histórico de transições realizadas.
        
        Cada entrada é uma tupla (from_stage, to_stage).
        O histórico é uma cópia para prevenir modificação externa.
        
        Returns:
            Lista de tuplas representando as transições
        """
        return list(self._history)
    
    def can_transition_to(self, target: Stage) -> bool:
        """Verifica se uma transição é válida sem executá-la.
        
        Args:
            target: estágio de destino
            
        Returns:
            True se a transição é válida, False caso contrário
        """
        valid_targets = TRANSITIONS.get(self._stage, frozenset())
        return target in valid_targets
    
    def transition_to(self, target: Stage) -> None:
        """Executa uma transição de estágio, validando antes.
        
        Args:
            target: estágio de destino
            
        Raises:
            InvalidTransitionError: se a transição não é válida
        """
        if not self.can_transition_to(target):
            valid_targets = list(TRANSITIONS.get(self._stage, frozenset()))
            raise InvalidTransitionError(
                from_stage=self._stage.value,
                to_stage=target.value,
                valid_targets=[s.value for s in valid_targets],
            )
        self._history.append((self._stage, target))
        self._stage = target
    
    def is_terminal(self) -> bool:
        """Verifica se a máquina está em um estado terminal.
        
        Estados terminais: DONE, NO_RESULTS, FAILED
        
        Returns:
            True se está em estado terminal, False caso contrário
        """
        terminal_states = {Stage.DONE, Stage.NO_RESULTS, Stage.FAILED}
        return self._stage in terminal_states
    
    def to_dict(self) -> dict:
        """Serializa o estado atual para um dicionário.
        
        Útil para persistência, debug e integração com sistemas externos.
        
        Returns:
            Dicionário com stage, status, history e is_terminal
        """
        return {
            "stage": self._stage.value,
            "status": self.status.value,
            "history": [(from_stage.value, to_stage.value) 
                       for from_stage, to_stage in self._history],
            "is_terminal": self.is_terminal(),
        }
