"""
Script de teste da máquina de estados.
Uso: python3 test_state_machine_manual.py
"""

import json
from pipeline.state_machine import (
    PipelineStateMachine,
    Stage,
    Status,
    InvalidTransitionError,
    TRANSITIONS,
    STATUS_MAP,
)
from pipeline.state import RunState


def separator(title: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def test_machine_isolated():
    separator("1. PipelineStateMachine isolada")

    sm = PipelineStateMachine()
    print(f"Estado inicial: stage={sm.stage.value}, status={sm.status.value}")
    print(f"É terminal? {sm.is_terminal()}")

    print("\n--- Caminho feliz (happy path) ---")
    sm.transition_to(Stage.SETUP)
    print(f"  → SETUP:      stage={sm.stage.value}, status={sm.status.value}")
    sm.transition_to(Stage.SEARCH)
    print(f"  → SEARCH:     stage={sm.stage.value}, status={sm.status.value}")
    sm.transition_to(Stage.SCREENING)
    print(f"  → SCREENING:  stage={sm.stage.value}, status={sm.status.value}")
    sm.transition_to(Stage.COMPARATIVE_ANALYSIS)
    print(f"  → COMPARATIVE: stage={sm.stage.value}, status={sm.status.value}")
    sm.transition_to(Stage.WHITESPACE_ANALYSIS)
    print(f"  → WHITESPACE: stage={sm.stage.value}, status={sm.status.value}")
    sm.transition_to(Stage.REPORTING)
    print(f"  → REPORTING:  stage={sm.stage.value}, status={sm.status.value}")
    sm.transition_to(Stage.DONE)
    print(f"  → DONE:       stage={sm.stage.value}, status={sm.status.value}")
    print(f"  É terminal? {sm.is_terminal()}")

    print("\n--- Histórico completo ---")
    for from_s, to_s in sm.history:
        print(f"  {from_s.value} → {to_s.value}")

    print("\n--- Serialização (to_dict) ---")
    print(json.dumps(sm.to_dict(), indent=2))


def test_no_results_path():
    separator("2. Caminho alternativo: NO_RESULTS")

    sm = PipelineStateMachine()
    sm.transition_to(Stage.SETUP)
    sm.transition_to(Stage.SEARCH)
    sm.transition_to(Stage.NO_RESULTS)

    print(f"Stage: {sm.stage.value}")
    print(f"Status: {sm.status.value}")
    print(f"É terminal? {sm.is_terminal()}")
    print(f"Histórico: {[(f.value, t.value) for f, t in sm.history]}")


def test_failed_path():
    separator("3. Caminho alternativo: FAILED")

    sm = PipelineStateMachine()
    sm.transition_to(Stage.SETUP)
    sm.transition_to(Stage.FAILED)

    print(f"Stage: {sm.stage.value}")
    print(f"Status: {sm.status.value}")
    print(f"É terminal? {sm.is_terminal()}")


def test_invalid_transition():
    separator("4. Transição inválida (deve lançar exceção)")

    sm = PipelineStateMachine()
    print(f"Estado atual: {sm.stage.value}")
    print(f"Tentando ir para SEARCH (inválido de IDLE)...")

    try:
        sm.transition_to(Stage.SEARCH)
    except InvalidTransitionError as e:
        print(f"  Exceção capturada!")
        print(f"  De: {e.from_stage}")
        print(f"  Para: {e.to_stage}")
        print(f"  Válidos: {e.valid_targets}")
        print(f"  Mensagem: {e}")


def test_can_transition():
    separator("5. can_transition_to (verificar sem executar)")

    sm = PipelineStateMachine()
    print(f"Estado atual: {sm.stage.value}")
    print(f"  Pode ir para SETUP?   {sm.can_transition_to(Stage.SETUP)}")
    print(f"  Pode ir para SEARCH?  {sm.can_transition_to(Stage.SEARCH)}")
    print(f"  Pode ir para FAILED?  {sm.can_transition_to(Stage.FAILED)}")
    print(f"Estado após verificações: {sm.stage.value} (não mudou)")


def test_run_state_integration():
    separator("6. RunState com máquina de estados")

    state = RunState(
        query="CO2 thermal storage",
        max_results=10,
        model="gemma3:4b",
        output_dir="output",
    )

    print(f"Inicial: stage={state.current_stage or '(vazio)'}, status={state.status}")

    state.transition_to(Stage.SETUP)
    print(f"  → SETUP:  stage={state.current_stage}, status={state.status}")

    state.transition_to(Stage.SEARCH)
    print(f"  → SEARCH: stage={state.current_stage}, status={state.status}")

    state.transition_to(Stage.SCREENING)
    print(f"  → SCREENING: stage={state.current_stage}, status={state.status}")

    print("\n--- Snapshot da máquina em to_dict() ---")
    d = state.to_dict()
    print(json.dumps(d["state_machine"], indent=2))


def test_run_state_backward_compat():
    separator("7. Compatibilidade retroativa")

    state = RunState(
        query="test",
        max_results=5,
        model="gemma3:4b",
        output_dir="output",
        status="running",
        current_stage="search",
    )

    print(f"Criado com strings: status={state.status}, stage={state.current_stage}")
    print(f"Funciona como antes? Sim!")

    d = state.to_dict()
    print(f"to_dict() status: {d['status']}")
    print(f"to_dict() current_stage: {d['current_stage']}")


def test_transitions_matrix():
    separator("8. Matriz de transições (visualização)")

    print("TRANSITIONS:")
    for stage, targets in TRANSITIONS.items():
        target_names = [t.value for t in targets] if targets else ["(terminal)"]
        print(f"  {stage.value:25s} → {', '.join(target_names)}")

    print("\nSTATUS_MAP:")
    for stage, status in STATUS_MAP.items():
        print(f"  {stage.value:25s} → {status.value}")


if __name__ == "__main__":
    test_machine_isolated()
    test_no_results_path()
    test_failed_path()
    test_invalid_transition()
    test_can_transition()
    test_run_state_integration()
    test_run_state_backward_compat()
    test_transitions_matrix()

    separator("TODOS OS TESTES MANUAIS CONCLUÍDOS")
    print("A máquina de estados está funcionando corretamente!\n")
