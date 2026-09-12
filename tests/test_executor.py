from agentqa.benchmarks.cases import get_case
from agentqa.runtime.executor import execute_suite,build_runtime_evidence

def test_executor_reproduces_bug():
    c=get_case('mean_wrong_denominator'); obs=execute_suite(c.source,c.function_name,c.public_tests); assert not obs[0].passed

def test_runtime_trace_collected():
    c=get_case('index_shift'); obs=execute_suite(c.source,c.function_name,c.public_tests); assert obs[0].trace_lines and 2 in obs[0].trace_lines

def test_exception_line_captured():
    c=get_case('zero_denominator_guard'); obs=execute_suite(c.source,c.function_name,c.public_tests); assert obs[0].exception_type=='ZeroDivisionError'; assert obs[0].exception_line==4

def test_evidence_has_failing_test():
    c=get_case('missing_trim'); ev=build_runtime_evidence(execute_suite(c.source,c.function_name,c.public_tests)); assert 'surrounding_spaces' in ev.failing_tests
