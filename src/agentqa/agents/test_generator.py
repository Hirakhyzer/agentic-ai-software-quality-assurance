from agentqa.models import BugCase
from agentqa.benchmarks.generation import generate_boundary_tests

class TestGenerationAgent:
    name = "test_generator"
    def run(self, case: BugCase, limit: int = 6):
        return generate_boundary_tests(case, limit=limit)
