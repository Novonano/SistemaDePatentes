"""
Testes unitários da máquina de estados - Parte 1: Enums e Exceções.
"""

import unittest
from pipeline.state_machine import (
    STATUS_MAP,
    TRANSITIONS,
    InvalidTransitionError,
    PipelineStateMachine,
    Stage,
    Status,
)
from pipeline.state import RunState


class TestStageEnum(unittest.TestCase):
    """Testes do enum Stage."""
    
    def test_stage_has_all_expected_values(self):
        """Verifica que todos os estágios esperados existem."""
        expected_stages = [
            "idle",
            "setup",
            "search",
            "screening",
            "comparative_analysis",
            "whitespace_analysis",
            "reporting",
            "done",
            "no_results",
            "failed",
        ]
        actual_stages = [stage.value for stage in Stage]
        self.assertEqual(actual_stages, expected_stages)
    
    def test_stage_values_are_strings(self):
        """Verifica que todos os valores são strings."""
        for stage in Stage:
            self.assertIsInstance(stage.value, str)
    
    def test_stage_can_be_accessed_by_name(self):
        """Verifica que pode acessar por nome."""
        self.assertEqual(Stage.IDLE.value, "idle")
        self.assertEqual(Stage.SEARCH.value, "search")
        self.assertEqual(Stage.DONE.value, "done")
    
    def test_stage_can_be_accessed_by_value(self):
        """Verifica que pode acessar por valor."""
        self.assertEqual(Stage("idle"), Stage.IDLE)
        self.assertEqual(Stage("search"), Stage.SEARCH)
    
    def test_stage_invalid_value_raises_error(self):
        """Verifica que valor inválido lança exceção."""
        with self.assertRaises(ValueError):
            Stage("invalid_stage")
    
    def test_stage_is_immutable(self):
        """Verifica que enums são imutáveis."""
        with self.assertRaises(AttributeError):
            Stage.IDLE.value = "changed"


class TestStatusEnum(unittest.TestCase):
    """Testes do enum Status."""
    
    def test_status_has_all_expected_values(self):
        """Verifica que todos os status esperados existem."""
        expected_statuses = [
            "idle",
            "running",
            "completed",
            "no_results",
            "error",
        ]
        actual_statuses = [status.value for status in Status]
        self.assertEqual(actual_statuses, expected_statuses)
    
    def test_status_values_are_strings(self):
        """Verifica que todos os valores são strings."""
        for status in Status:
            self.assertIsInstance(status.value, str)
    
    def test_status_can_be_accessed_by_name(self):
        """Verifica que pode acessar por nome."""
        self.assertEqual(Status.IDLE.value, "idle")
        self.assertEqual(Status.RUNNING.value, "running")
        self.assertEqual(Status.COMPLETED.value, "completed")
    
    def test_status_can_be_accessed_by_value(self):
        """Verifica que pode acessar por valor."""
        self.assertEqual(Status("idle"), Status.IDLE)
        self.assertEqual(Status("running"), Status.RUNNING)
    
    def test_status_invalid_value_raises_error(self):
        """Verifica que valor inválido lança exceção."""
        with self.assertRaises(ValueError):
            Status("invalid_status")


class TestInvalidTransitionError(unittest.TestCase):
    """Testes da exceção InvalidTransitionError."""
    
    def test_error_message_contains_stages(self):
        """Verifica que mensagem contém os estágios."""
        error = InvalidTransitionError(
            from_stage="idle",
            to_stage="search",
            valid_targets=["setup"],
        )
        message = str(error)
        self.assertIn("idle", message)
        self.assertIn("search", message)
        self.assertIn("setup", message)
    
    def test_error_stores_context(self):
        """Verifica que armazena contexto."""
        error = InvalidTransitionError(
            from_stage="idle",
            to_stage="search",
            valid_targets=["setup"],
        )
        self.assertEqual(error.from_stage, "idle")
        self.assertEqual(error.to_stage, "search")
        self.assertEqual(error.valid_targets, ["setup"])
    
    def test_error_is_exception(self):
        """Verifica que é uma exceção."""
        error = InvalidTransitionError("idle", "search", ["setup"])
        self.assertIsInstance(error, Exception)
    
    def test_error_can_be_raised_and_caught(self):
        """Verifica que pode ser lançada e capturada."""
        with self.assertRaises(InvalidTransitionError) as context:
            raise InvalidTransitionError("idle", "search", ["setup"])
        
        self.assertEqual(context.exception.from_stage, "idle")
        self.assertEqual(context.exception.to_stage, "search")


class TestTransitionsMatrix(unittest.TestCase):
    """Testes da matriz de transições TRANSITIONS."""
    
    def test_all_stages_have_transitions_entry(self):
        """Verifica que todos os estágios têm uma entrada na matriz."""
        for stage in Stage:
            self.assertIn(stage, TRANSITIONS, f"Stage {stage} não está na matriz TRANSITIONS")
    
    def test_terminal_states_have_empty_transitions(self):
        """Verifica que estados terminais não têm transições de saída."""
        terminal_states = [Stage.DONE, Stage.NO_RESULTS, Stage.FAILED]
        for stage in terminal_states:
            self.assertEqual(
                TRANSITIONS[stage],
                frozenset(),
                f"Estado terminal {stage} deveria ter frozenset vazio",
            )
    
    def test_failed_is_accessible_from_all_non_terminal_states(self):
        """Verifica que FAILED é acessível de todos os estados não-terminais."""
        terminal_states = {Stage.DONE, Stage.NO_RESULTS, Stage.FAILED}
        for stage in Stage:
            if stage not in terminal_states:
                self.assertIn(
                    Stage.FAILED,
                    TRANSITIONS[stage],
                    f"Stage {stage} deveria poder transicionar para FAILED",
                )
    
    def test_idle_can_transition_to_setup_or_failed(self):
        """Verifica que IDLE pode ir para SETUP ou FAILED."""
        valid_targets = {Stage.SETUP, Stage.FAILED}
        self.assertEqual(TRANSITIONS[Stage.IDLE], frozenset(valid_targets))
    
    def test_search_can_transition_to_screening_or_no_results(self):
        """Verifica que SEARCH pode ir para SCREENING ou NO_RESULTS."""
        valid_targets = {Stage.SCREENING, Stage.NO_RESULTS, Stage.FAILED}
        self.assertEqual(TRANSITIONS[Stage.SEARCH], frozenset(valid_targets))
    
    def test_reporting_can_transition_to_done_or_failed(self):
        """Verifica que REPORTING pode ir para DONE ou FAILED."""
        valid_targets = {Stage.DONE, Stage.FAILED}
        self.assertEqual(TRANSITIONS[Stage.REPORTING], frozenset(valid_targets))
    
    def test_transitions_values_are_frozensets(self):
        """Verifica que todos os valores são frozensets (imutáveis)."""
        for stage, targets in TRANSITIONS.items():
            self.assertIsInstance(
                targets,
                frozenset,
                f"TRANSITIONS[{stage}] deveria ser frozenset",
            )
    
    def test_transitions_targets_are_valid_stages(self):
        """Verifica que todos os alvos são estágios válidos."""
        all_stages = set(Stage)
        for stage, targets in TRANSITIONS.items():
            for target in targets:
                self.assertIn(
                    target,
                    all_stages,
                    f"TRANSITIONS[{stage}] contém {target} que não é um Stage válido",
                )
    
    def test_transitions_matrix_is_complete(self):
        """Verifica que a matriz tem o número esperado de entradas."""
        self.assertEqual(len(TRANSITIONS), len(Stage))


class TestStatusMap(unittest.TestCase):
    """Testes do mapeamento STATUS_MAP."""
    
    def test_status_map_covers_all_terminal_states(self):
        """Verifica que STATUS_MAP cobre todos os estágios terminais."""
        terminal_states = [Stage.IDLE, Stage.DONE, Stage.NO_RESULTS, Stage.FAILED]
        for stage in terminal_states:
            self.assertIn(stage, STATUS_MAP, f"Stage terminal {stage} não está em STATUS_MAP")
    
    def test_status_map_idle_maps_to_idle(self):
        """Verifica que IDLE mapeia para Status.IDLE."""
        self.assertEqual(STATUS_MAP[Stage.IDLE], Status.IDLE)
    
    def test_status_map_done_maps_to_completed(self):
        """Verifica que DONE mapeia para Status.COMPLETED."""
        self.assertEqual(STATUS_MAP[Stage.DONE], Status.COMPLETED)
    
    def test_status_map_no_results_maps_to_no_results(self):
        """Verifica que NO_RESULTS mapeia para Status.NO_RESULTS."""
        self.assertEqual(STATUS_MAP[Stage.NO_RESULTS], Status.NO_RESULTS)
    
    def test_status_map_failed_maps_to_error(self):
        """Verifica que FAILED mapeia para Status.ERROR."""
        self.assertEqual(STATUS_MAP[Stage.FAILED], Status.ERROR)
    
    def test_status_map_values_are_valid_statuses(self):
        """Verifica que todos os valores são Status válidos."""
        all_statuses = set(Status)
        for stage, status in STATUS_MAP.items():
            self.assertIn(
                status,
                all_statuses,
                f"STATUS_MAP[{stage}] contém {status} que não é um Status válido",
            )
    
    def test_non_terminal_stages_are_not_in_status_map(self):
        """Verifica que estágios não-terminais não estão no STATUS_MAP."""
        non_terminal = [
            Stage.SETUP,
            Stage.SEARCH,
            Stage.SCREENING,
            Stage.COMPARATIVE_ANALYSIS,
            Stage.WHITESPACE_ANALYSIS,
            Stage.REPORTING,
        ]
        for stage in non_terminal:
            self.assertNotIn(
                stage,
                STATUS_MAP,
                f"Stage não-terminal {stage} não deveria estar em STATUS_MAP",
            )


class TestPipelineStateMachine(unittest.TestCase):
    """Testes da classe PipelineStateMachine."""
    
    def test_initial_state_is_idle(self):
        """Verifica que o estado inicial é IDLE."""
        sm = PipelineStateMachine()
        self.assertEqual(sm.stage, Stage.IDLE)
    
    def test_initial_status_is_idle(self):
        """Verifica que o status inicial é IDLE."""
        sm = PipelineStateMachine()
        self.assertEqual(sm.status, Status.IDLE)
    
    def test_can_transition_to_returns_true_for_valid_transition(self):
        """Verifica que can_transition_to retorna True para transições válidas."""
        sm = PipelineStateMachine()
        self.assertTrue(sm.can_transition_to(Stage.SETUP))
    
    def test_can_transition_to_returns_false_for_invalid_transition(self):
        """Verifica que can_transition_to retorna False para transições inválidas."""
        sm = PipelineStateMachine()
        self.assertFalse(sm.can_transition_to(Stage.SEARCH))
    
    def test_valid_transition_changes_stage(self):
        """Verifica que transição válida muda o estágio."""
        sm = PipelineStateMachine()
        sm.transition_to(Stage.SETUP)
        self.assertEqual(sm.stage, Stage.SETUP)
    
    def test_invalid_transition_raises_error(self):
        """Verifica que transição inválida lança InvalidTransitionError."""
        sm = PipelineStateMachine()
        with self.assertRaises(InvalidTransitionError):
            sm.transition_to(Stage.SEARCH)
    
    def test_intermediate_stages_have_running_status(self):
        """Verifica que estágios intermediários têm status RUNNING."""
        intermediate_stages = [
            Stage.SETUP,
            Stage.SEARCH,
            Stage.SCREENING,
            Stage.COMPARATIVE_ANALYSIS,
            Stage.WHITESPACE_ANALYSIS,
            Stage.REPORTING,
        ]
        for stage in intermediate_stages:
            sm = PipelineStateMachine()
            # Navega até o estágio
            if stage == Stage.SETUP:
                sm.transition_to(Stage.SETUP)
            elif stage == Stage.SEARCH:
                sm.transition_to(Stage.SETUP)
                sm.transition_to(Stage.SEARCH)
            elif stage == Stage.SCREENING:
                sm.transition_to(Stage.SETUP)
                sm.transition_to(Stage.SEARCH)
                sm.transition_to(Stage.SCREENING)
            elif stage == Stage.COMPARATIVE_ANALYSIS:
                sm.transition_to(Stage.SETUP)
                sm.transition_to(Stage.SEARCH)
                sm.transition_to(Stage.SCREENING)
                sm.transition_to(Stage.COMPARATIVE_ANALYSIS)
            elif stage == Stage.WHITESPACE_ANALYSIS:
                sm.transition_to(Stage.SETUP)
                sm.transition_to(Stage.SEARCH)
                sm.transition_to(Stage.SCREENING)
                sm.transition_to(Stage.COMPARATIVE_ANALYSIS)
                sm.transition_to(Stage.WHITESPACE_ANALYSIS)
            elif stage == Stage.REPORTING:
                sm.transition_to(Stage.SETUP)
                sm.transition_to(Stage.SEARCH)
                sm.transition_to(Stage.SCREENING)
                sm.transition_to(Stage.COMPARATIVE_ANALYSIS)
                sm.transition_to(Stage.WHITESPACE_ANALYSIS)
                sm.transition_to(Stage.REPORTING)
            # Verifica status
            self.assertEqual(sm.status, Status.RUNNING, 
                           f"Stage {stage} deveria ter status RUNNING")
    
    def test_done_stage_has_completed_status(self):
        """Verifica que DONE tem status COMPLETED."""
        sm = PipelineStateMachine()
        sm.transition_to(Stage.SETUP)
        sm.transition_to(Stage.SEARCH)
        sm.transition_to(Stage.SCREENING)
        sm.transition_to(Stage.COMPARATIVE_ANALYSIS)
        sm.transition_to(Stage.WHITESPACE_ANALYSIS)
        sm.transition_to(Stage.REPORTING)
        sm.transition_to(Stage.DONE)
        self.assertEqual(sm.status, Status.COMPLETED)
    
    def test_no_results_stage_has_no_results_status(self):
        """Verifica que NO_RESULTS tem status NO_RESULTS."""
        sm = PipelineStateMachine()
        sm.transition_to(Stage.SETUP)
        sm.transition_to(Stage.SEARCH)
        sm.transition_to(Stage.NO_RESULTS)
        self.assertEqual(sm.status, Status.NO_RESULTS)
    
    def test_failed_stage_has_error_status(self):
        """Verifica que FAILED tem status ERROR."""
        sm = PipelineStateMachine()
        sm.transition_to(Stage.FAILED)
        self.assertEqual(sm.status, Status.ERROR)
    
    def test_is_terminal_returns_true_for_terminal_states(self):
        """Verifica que is_terminal retorna True para estados terminais."""
        terminal_states = [Stage.DONE, Stage.NO_RESULTS, Stage.FAILED]
        for stage in terminal_states:
            sm = PipelineStateMachine()
            if stage == Stage.DONE:
                sm.transition_to(Stage.SETUP)
                sm.transition_to(Stage.SEARCH)
                sm.transition_to(Stage.SCREENING)
                sm.transition_to(Stage.COMPARATIVE_ANALYSIS)
                sm.transition_to(Stage.WHITESPACE_ANALYSIS)
                sm.transition_to(Stage.REPORTING)
                sm.transition_to(Stage.DONE)
            elif stage == Stage.NO_RESULTS:
                sm.transition_to(Stage.SETUP)
                sm.transition_to(Stage.SEARCH)
                sm.transition_to(Stage.NO_RESULTS)
            elif stage == Stage.FAILED:
                sm.transition_to(Stage.FAILED)
            
            self.assertTrue(sm.is_terminal(), 
                          f"Stage {stage} deveria ser terminal")
    
    def test_is_terminal_returns_false_for_non_terminal_states(self):
        """Verifica que is_terminal retorna False para estados não-terminais."""
        sm = PipelineStateMachine()
        non_terminal_stages = [
            Stage.IDLE,
            Stage.SETUP,
            Stage.SEARCH,
            Stage.SCREENING,
            Stage.COMPARATIVE_ANALYSIS,
            Stage.WHITESPACE_ANALYSIS,
            Stage.REPORTING,
        ]
        for stage in non_terminal_stages:
            sm = PipelineStateMachine()
            if stage == Stage.SETUP:
                sm.transition_to(Stage.SETUP)
            elif stage == Stage.SEARCH:
                sm.transition_to(Stage.SETUP)
                sm.transition_to(Stage.SEARCH)
            # etc.
            
            self.assertFalse(sm.is_terminal(), 
                           f"Stage {stage} não deveria ser terminal")
    
    def test_happy_path_to_done(self):
        """Verifica caminho completo até DONE."""
        sm = PipelineStateMachine()
        sm.transition_to(Stage.SETUP)
        sm.transition_to(Stage.SEARCH)
        sm.transition_to(Stage.SCREENING)
        sm.transition_to(Stage.COMPARATIVE_ANALYSIS)
        sm.transition_to(Stage.WHITESPACE_ANALYSIS)
        sm.transition_to(Stage.REPORTING)
        sm.transition_to(Stage.DONE)
        
        self.assertEqual(sm.stage, Stage.DONE)
        self.assertEqual(sm.status, Status.COMPLETED)
        self.assertTrue(sm.is_terminal())
    
    def test_no_results_path(self):
        """Verifica caminho até NO_RESULTS."""
        sm = PipelineStateMachine()
        sm.transition_to(Stage.SETUP)
        sm.transition_to(Stage.SEARCH)
        sm.transition_to(Stage.NO_RESULTS)
        
        self.assertEqual(sm.stage, Stage.NO_RESULTS)
        self.assertEqual(sm.status, Status.NO_RESULTS)
        self.assertTrue(sm.is_terminal())
    
    def test_failed_path(self):
        """Verifica caminho até FAILED."""
        sm = PipelineStateMachine()
        sm.transition_to(Stage.FAILED)
        
        self.assertEqual(sm.stage, Stage.FAILED)
        self.assertEqual(sm.status, Status.ERROR)
        self.assertTrue(sm.is_terminal())
    
    def test_error_contains_context(self):
        """Verifica que exceção contém contexto correto."""
        sm = PipelineStateMachine()
        try:
            sm.transition_to(Stage.SEARCH)
            self.fail("Deveria ter lançado InvalidTransitionError")
        except InvalidTransitionError as e:
            self.assertEqual(e.from_stage, "idle")
            self.assertEqual(e.to_stage, "search")
            self.assertIn("setup", e.valid_targets)


class TestPipelineStateMachineHistory(unittest.TestCase):
    """Testes do histórico de transições."""
    
    def test_initial_history_is_empty(self):
        """Verifica que histórico inicial é vazio."""
        sm = PipelineStateMachine()
        self.assertEqual(sm.history, [])
    
    def test_history_records_single_transition(self):
        """Verifica que histórico registra uma transição."""
        sm = PipelineStateMachine()
        sm.transition_to(Stage.SETUP)
        self.assertEqual(len(sm.history), 1)
        self.assertEqual(sm.history[0], (Stage.IDLE, Stage.SETUP))
    
    def test_history_records_multiple_transitions(self):
        """Verifica que histórico registra múltiplas transições."""
        sm = PipelineStateMachine()
        sm.transition_to(Stage.SETUP)
        sm.transition_to(Stage.SEARCH)
        sm.transition_to(Stage.SCREENING)
        
        self.assertEqual(len(sm.history), 3)
        self.assertEqual(sm.history[0], (Stage.IDLE, Stage.SETUP))
        self.assertEqual(sm.history[1], (Stage.SETUP, Stage.SEARCH))
        self.assertEqual(sm.history[2], (Stage.SEARCH, Stage.SCREENING))
    
    def test_history_returns_copy(self):
        """Verifica que history retorna uma cópia, não referência interna."""
        sm = PipelineStateMachine()
        sm.transition_to(Stage.SETUP)
        
        history_copy = sm.history
        history_copy.append((Stage.SETUP, Stage.SEARCH))  # Modifica a cópia
        
        # Histórico interno não deve ser afetado
        self.assertEqual(len(sm.history), 1)
    
    def test_history_not_recorded_for_invalid_transition(self):
        """Verifica que transição inválida não é registrada no histórico."""
        sm = PipelineStateMachine()
        try:
            sm.transition_to(Stage.SEARCH)  # Inválido de IDLE
        except InvalidTransitionError:
            pass
        
        self.assertEqual(len(sm.history), 0)
    
    def test_history_complete_path_to_done(self):
        """Verifica histórico completo até DONE."""
        sm = PipelineStateMachine()
        sm.transition_to(Stage.SETUP)
        sm.transition_to(Stage.SEARCH)
        sm.transition_to(Stage.SCREENING)
        sm.transition_to(Stage.COMPARATIVE_ANALYSIS)
        sm.transition_to(Stage.WHITESPACE_ANALYSIS)
        sm.transition_to(Stage.REPORTING)
        sm.transition_to(Stage.DONE)
        
        self.assertEqual(len(sm.history), 7)
        self.assertEqual(sm.history[0], (Stage.IDLE, Stage.SETUP))
        self.assertEqual(sm.history[-1], (Stage.REPORTING, Stage.DONE))


class TestPipelineStateMachineSerialization(unittest.TestCase):
    """Testes da serialização to_dict()."""
    
    def test_to_dict_initial_state(self):
        """Verifica serialização do estado inicial."""
        sm = PipelineStateMachine()
        result = sm.to_dict()
        
        self.assertEqual(result["stage"], "idle")
        self.assertEqual(result["status"], "idle")
        self.assertEqual(result["history"], [])
        self.assertFalse(result["is_terminal"])
    
    def test_to_dict_intermediate_state(self):
        """Verifica serialização de estado intermediário."""
        sm = PipelineStateMachine()
        sm.transition_to(Stage.SETUP)
        sm.transition_to(Stage.SEARCH)
        
        result = sm.to_dict()
        
        self.assertEqual(result["stage"], "search")
        self.assertEqual(result["status"], "running")
        self.assertEqual(len(result["history"]), 2)
        self.assertEqual(result["history"][0], ("idle", "setup"))
        self.assertEqual(result["history"][1], ("setup", "search"))
        self.assertFalse(result["is_terminal"])
    
    def test_to_dict_terminal_state_done(self):
        """Verifica serialização de estado terminal DONE."""
        sm = PipelineStateMachine()
        sm.transition_to(Stage.SETUP)
        sm.transition_to(Stage.SEARCH)
        sm.transition_to(Stage.SCREENING)
        sm.transition_to(Stage.COMPARATIVE_ANALYSIS)
        sm.transition_to(Stage.WHITESPACE_ANALYSIS)
        sm.transition_to(Stage.REPORTING)
        sm.transition_to(Stage.DONE)
        
        result = sm.to_dict()
        
        self.assertEqual(result["stage"], "done")
        self.assertEqual(result["status"], "completed")
        self.assertTrue(result["is_terminal"])
        self.assertEqual(len(result["history"]), 7)
    
    def test_to_dict_terminal_state_no_results(self):
        """Verifica serialização de estado terminal NO_RESULTS."""
        sm = PipelineStateMachine()
        sm.transition_to(Stage.SETUP)
        sm.transition_to(Stage.SEARCH)
        sm.transition_to(Stage.NO_RESULTS)
        
        result = sm.to_dict()
        
        self.assertEqual(result["stage"], "no_results")
        self.assertEqual(result["status"], "no_results")
        self.assertTrue(result["is_terminal"])
    
    def test_to_dict_terminal_state_failed(self):
        """Verifica serialização de estado terminal FAILED."""
        sm = PipelineStateMachine()
        sm.transition_to(Stage.FAILED)
        
        result = sm.to_dict()
        
        self.assertEqual(result["stage"], "failed")
        self.assertEqual(result["status"], "error")
        self.assertTrue(result["is_terminal"])
    
    def test_to_dict_history_contains_string_values(self):
        """Verifica que histórico em to_dict() contém strings, não Enums."""
        sm = PipelineStateMachine()
        sm.transition_to(Stage.SETUP)
        
        result = sm.to_dict()
        
        # Deve ser strings, não objetos Enum
        self.assertIsInstance(result["history"][0][0], str)
        self.assertIsInstance(result["history"][0][1], str)
    
    def test_to_dict_is_json_serializable(self):
        """Verifica que to_dict() produz resultado serializável em JSON."""
        import json
        
        sm = PipelineStateMachine()
        sm.transition_to(Stage.SETUP)
        sm.transition_to(Stage.SEARCH)
        
        result = sm.to_dict()
        
        # Não deve lançar exceção
        json_str = json.dumps(result)
        self.assertIsInstance(json_str, str)
        
        # Deve ser possível desserializar
        deserialized = json.loads(json_str)
        self.assertEqual(deserialized["stage"], "search")


class TestRunStateIntegration(unittest.TestCase):
    """Testes de integração entre RunState e PipelineStateMachine."""
    
    def test_run_state_has_state_machine(self):
        """Verifica que RunState tem uma máquina de estados."""
        state = RunState(
            query="test",
            max_results=10,
            model="test-model",
            output_dir="/tmp",
        )
        self.assertIsInstance(state._state_machine, PipelineStateMachine)
    
    def test_run_state_initial_state(self):
        """Verifica estado inicial do RunState."""
        state = RunState(
            query="test",
            max_results=10,
            model="test-model",
            output_dir="/tmp",
        )
        self.assertEqual(state._state_machine.stage, Stage.IDLE)
        self.assertEqual(state._state_machine.status, Status.IDLE)
    
    def test_run_state_transition_to(self):
        """Verifica que transition_to atualiza RunState e máquina."""
        state = RunState(
            query="test",
            max_results=10,
            model="test-model",
            output_dir="/tmp",
        )
        
        state.transition_to(Stage.SETUP)
        
        self.assertEqual(state.current_stage, "setup")
        self.assertEqual(state.status, "running")
        self.assertEqual(state._state_machine.stage, Stage.SETUP)
    
    def test_run_state_transition_validates(self):
        """Verifica que transition_to valida transições."""
        state = RunState(
            query="test",
            max_results=10,
            model="test-model",
            output_dir="/tmp",
        )
        
        # Tenta transição inválida (IDLE → SEARCH)
        with self.assertRaises(InvalidTransitionError):
            state.transition_to(Stage.SEARCH)
    
    def test_run_state_transition_updates_status(self):
        """Verifica que status é atualizado automaticamente."""
        state = RunState(
            query="test",
            max_results=10,
            model="test-model",
            output_dir="/tmp",
        )
        
        state.transition_to(Stage.SETUP)
        state.transition_to(Stage.SEARCH)
        state.transition_to(Stage.NO_RESULTS)
        
        self.assertEqual(state.status, "no_results")
        self.assertEqual(state.current_stage, "no_results")
    
    def test_run_state_to_dict_includes_state_machine(self):
        """Verifica que to_dict() inclui snapshot da máquina."""
        state = RunState(
            query="test",
            max_results=10,
            model="test-model",
            output_dir="/tmp",
        )
        
        state.transition_to(Stage.SETUP)
        state.transition_to(Stage.SEARCH)
        
        result = state.to_dict()
        
        self.assertIn("state_machine", result)
        self.assertEqual(result["state_machine"]["stage"], "search")
        self.assertEqual(result["state_machine"]["status"], "running")
        self.assertEqual(len(result["state_machine"]["history"]), 2)
    
    def test_run_state_backward_compatibility(self):
        """Verifica compatibilidade com código antigo."""
        # Código antigo pode tentar ler status e current_stage
        state = RunState(
            query="test",
            max_results=10,
            model="test-model",
            output_dir="/tmp",
        )
        
        # status e current_stage são properties que delegam para a máquina
        self.assertEqual(state.status, "idle")
        self.assertEqual(state.current_stage, "idle")
        
        # to_dict() deve funcionar
        result = state.to_dict()
        self.assertEqual(result["status"], "idle")
        self.assertEqual(result["current_stage"], "idle")
    
    def test_run_state_happy_path(self):
        """Verifica caminho completo do pipeline."""
        state = RunState(
            query="test",
            max_results=10,
            model="test-model",
            output_dir="/tmp",
        )
        
        state.transition_to(Stage.SETUP)
        state.transition_to(Stage.SEARCH)
        state.transition_to(Stage.SCREENING)
        state.transition_to(Stage.COMPARATIVE_ANALYSIS)
        state.transition_to(Stage.WHITESPACE_ANALYSIS)
        state.transition_to(Stage.REPORTING)
        state.transition_to(Stage.DONE)
        
        self.assertEqual(state.current_stage, "done")
        self.assertEqual(state.status, "completed")
        self.assertTrue(state._state_machine.is_terminal())
        
        # Verifica histórico
        result = state.to_dict()
        self.assertEqual(len(result["state_machine"]["history"]), 7)


if __name__ == "__main__":
    unittest.main()
