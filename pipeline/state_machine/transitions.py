"""
Matriz de transições e mapeamento de status.

TRANSITIONS: define quais transições entre estágios são válidas.
STATUS_MAP: mapeia estágios terminais para seus status automáticos.
"""

from typing import Dict, FrozenSet

from pipeline.state_machine.enums import Stage, Status


# Matriz de transições válidas.
# Cada chave é um Stage, e o valor é um frozenset de Stages para os quais
# a transição é permitida. Estados terminais têm frozenset vazio.
TRANSITIONS: Dict[Stage, FrozenSet[Stage]] = {
    Stage.IDLE: frozenset({Stage.SETUP, Stage.FAILED}),
    Stage.SETUP: frozenset({Stage.SEARCH, Stage.FAILED}),
    Stage.SEARCH: frozenset({Stage.SCREENING, Stage.NO_RESULTS, Stage.FAILED}),
    Stage.SCREENING: frozenset({Stage.COMPARATIVE_ANALYSIS, Stage.FAILED}),
    Stage.COMPARATIVE_ANALYSIS: frozenset({Stage.WHITESPACE_ANALYSIS, Stage.FAILED}),
    Stage.WHITESPACE_ANALYSIS: frozenset({Stage.REPORTING, Stage.FAILED}),
    Stage.REPORTING: frozenset({Stage.DONE, Stage.FAILED}),
    Stage.DONE: frozenset(),
    Stage.NO_RESULTS: frozenset(),
    Stage.FAILED: frozenset(),
}


# Mapeamento de estágios terminais para status automáticos.
# Estágios não listados aqui têm status RUNNING por padrão.
STATUS_MAP: Dict[Stage, Status] = {
    Stage.IDLE: Status.IDLE,
    Stage.DONE: Status.COMPLETED,
    Stage.NO_RESULTS: Status.NO_RESULTS,
    Stage.FAILED: Status.ERROR,
}
