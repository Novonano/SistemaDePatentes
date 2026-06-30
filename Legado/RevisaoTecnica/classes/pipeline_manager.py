from pipeline.ablation import run_ablation_suite
from pipeline.features import PipelineFeatures
from pipeline.frozen_benchmark import build_frozen_components, build_frozen_scrapers_from_run_state
from pipeline.orchestrator import run_agent
from pipeline.upgrade_benchmark import run_today_upgrade_benchmark

class PipelineManager():

    _scrapers = None
    _evaluator_factory = None
    _state = None

    def create_agent(self, fixture_path):
        _scrapers, _evaluator_factory = build_frozen_components(fixture_path)
        _state = run_agent(
        with tempfile.TemporaryDirectory() as tmpdir:
            _state = run_agent(
                query="carbon dioxide thermal energy storage",
                max_results=5,
                model="frozen-model",
                output_dir=tmpdir,
                features=PipelineFeatures(),
                scrapers=scrapers,
                evaluator_factory=evaluator_factory,
            )
        )
        return _state