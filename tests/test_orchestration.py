from agentqa.benchmarks.cases import CASES,get_case
from agentqa.orchestration.coordinator import QACoordinator

def test_runtime_pipeline_repairs_most_cases():
    results=[QACoordinator().run(c,'runtime_grounded') for c in CASES]; assert sum(bool(r.verification and r.verification.correct) for r in results) >= 7

def test_pipeline_requires_review_when_no_correct_patch():
    c=get_case('zero_denominator_guard'); r=QACoordinator(max_candidates=1).run(c,'static_only'); assert r.human_review_required or (r.verification and r.verification.correct)

def test_generated_tests_used_in_runtime_mode():
    c=get_case('zero_denominator_guard'); r=QACoordinator().run(c,'runtime_grounded'); assert len(r.generated_tests)>0

def test_static_mode_uses_no_generated_tests():
    c=get_case('mean_wrong_denominator'); r=QACoordinator().run(c,'static_only'); assert r.generated_tests==()
