from __future__ import annotations
from agentqa.models import AgentContext, QAResult
from agentqa.agents.reproducer import ReproducerAgent
from agentqa.agents.test_generator import TestGenerationAgent
from agentqa.agents.fault_localizer import FaultLocalizationAgent
from agentqa.agents.repairer import RepairAgent
from agentqa.agents.verifier import VerificationAgent

class QACoordinator:
    def __init__(self, max_candidates: int=4):
        self.max_candidates=max_candidates
        self.reproducer=ReproducerAgent(); self.tests=TestGenerationAgent(); self.localizer=FaultLocalizationAgent(); self.repairer=RepairAgent(); self.verifier=VerificationAgent()

    def run(self, case, mode='runtime_grounded') -> QAResult:
        context=AgentContext(case.case_id,case.issue,case.function_name,case.source,case.public_tests)
        evidence=self.reproducer.run(context)
        reproduced=bool(evidence.failing_tests)
        runtime = mode != 'static_only'
        loc=self.localizer.run(case.source, evidence=evidence, mode='runtime' if runtime else 'static')
        generated=self.tests.run(case) if runtime else ()
        candidates=self.repairer.run(case.source, loc)
        selected=None; verification=None; considered=0
        for cand in candidates[:self.max_candidates]:
            considered += 1
            vr=self.verifier.run(case,cand,generated_tests=generated)
            if vr.plausible:
                selected=cand; verification=vr; break
        human = selected is None or verification is None or not verification.correct
        return QAResult(case.case_id,mode,reproduced,loc,considered,selected,verification,tuple(generated),human)
