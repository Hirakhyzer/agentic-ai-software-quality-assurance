import pytest
from agentqa.benchmarks.cases import get_case
from agentqa.benchmarks.generation import generate_boundary_tests
from agentqa.runtime.executor import execute_test

def test_reference_is_not_exposed_in_agent_context():
    from agentqa.models import AgentContext
    c=get_case('mean_wrong_denominator'); ctx=AgentContext(c.case_id,c.issue,c.function_name,c.source,c.public_tests); assert not hasattr(ctx,'reference_source')

def test_boundary_generator_is_deterministic():
    c=get_case('zero_denominator_guard'); assert generate_boundary_tests(c)==generate_boundary_tests(c)

def test_missing_function_rejected():
    from agentqa.runtime.executor import _load_function
    with pytest.raises(ValueError): _load_function('x=1','missing')
