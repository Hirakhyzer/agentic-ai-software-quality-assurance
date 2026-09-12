from agentqa.models import AgentContext
from agentqa.runtime.executor import execute_suite, build_runtime_evidence

class ReproducerAgent:
    name = "reproducer"
    def run(self, context: AgentContext):
        observations = execute_suite(context.source, context.function_name, context.public_tests, trace=True)
        return build_runtime_evidence(observations)
