from agentqa.runtime.evidence import compact_evidence

class RuntimeEvidenceAgent:
    name = "runtime_analyst"
    def run(self, evidence, max_lines: int = 12):
        return compact_evidence(evidence, max_lines=max_lines)
