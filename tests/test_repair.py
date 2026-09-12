from agentqa.benchmarks.cases import get_case
from agentqa.repair.candidates import generate_candidates
from agentqa.agents.verifier import VerificationAgent
from agentqa.benchmarks.generation import generate_boundary_tests

def test_range_patch_generated():
    c=get_case('inclusive_sum_off_by_one'); cs=generate_candidates(c.source); assert any('range(n + 1)' in x.source for x in cs)

def test_identity_patch_generated():
    c=get_case('identity_vs_equality'); assert any('item == target' in x.source for x in generate_candidates(c.source))

def test_correct_candidate_passes_hidden_tests():
    c=get_case('clamp_upper_return'); p=[x for x in generate_candidates(c.source) if 'return upper' in x.source][0]; v=VerificationAgent().run(c,p); assert v.correct

def test_generated_tests_detect_overfit_ratio_patch():
    c=get_case('zero_denominator_guard'); bad=[x for x in generate_candidates(c.source) if 'denominator <= 0' in x.source][0]; v=VerificationAgent().run(c,bad,generate_boundary_tests(c)); assert not v.generated_passed or not v.hidden_passed
