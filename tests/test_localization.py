from agentqa.benchmarks.cases import CASES,get_case
from agentqa.localization.static import static_localize
from agentqa.localization.runtime import runtime_localize
from agentqa.runtime.executor import execute_suite,build_runtime_evidence

def test_static_localizer_returns_ranked_lines():
    c=get_case('clamp_upper_return'); r=static_localize(c.source); assert r.ranked_lines

def test_runtime_localizer_uses_exception_anchor():
    c=get_case('zero_denominator_guard'); ev=build_runtime_evidence(execute_suite(c.source,c.function_name,c.public_tests)); r=runtime_localize(c.source,ev); assert 4 in r.topk(2)

def test_runtime_top3_localization_reasonable_across_suite():
    hits=0
    for c in CASES:
        ev=build_runtime_evidence(execute_suite(c.source,c.function_name,c.public_tests)); r=runtime_localize(c.source,ev); hits += c.bug_line in r.topk(3)
    assert hits >= 6
