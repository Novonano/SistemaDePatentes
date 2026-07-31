"""
Exceções da máquina de estados.
"""


class InvalidTransitionError(Exception):
    """Lançada quando uma transição inválida é tentada."""
    
    def __init__(self, from_stage: str, to_stage: str, valid_targets: list[str]):
        self.from_stage = from_stage
        self.to_stage = to_stage
        self.valid_targets = valid_targets
        
        message = (
            f"Transição inválida: {from_stage} → {to_stage}. "
            f"Transições válidas de {from_stage}: {valid_targets}"
        )
        super().__init__(message)
