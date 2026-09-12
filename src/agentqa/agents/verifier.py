from agentqa.benchmarks.oracle import hidden_tests
from agentqa.models import VerificationResult
from agentqa.runtime.executor import execute_suite

class VerificationAgent:
    name='verifier'
    def run(self, case, patch, generated_tests=()):
        pub=execute_suite(patch.source, case.function_name, case.public_tests, trace=False)
        gen=execute_suite(patch.source, case.function_name, tuple(generated_tests), trace=False) if generated_tests else ()
        hid=execute_suite(patch.source, case.function_name, hidden_tests(case), trace=False)
        pf=sum(not x.passed for x in pub); gf=sum(not x.passed for x in gen); hf=sum(not x.passed for x in hid)
        return VerificationResult(patch.patch_id,pf==0,gf==0,hf==0,pf,gf,hf)
