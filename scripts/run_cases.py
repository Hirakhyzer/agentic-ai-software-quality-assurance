from agentqa.benchmarks.cases import CASES
from agentqa.orchestration.coordinator import QACoordinator
for case in CASES:
    r=QACoordinator().run(case,'runtime_grounded')
    print(case.case_id, 'reproduced=',r.reproduced,'top1=',r.localization.top1,'patch=',r.selected_patch.patch_id if r.selected_patch else None,'correct=',bool(r.verification and r.verification.correct),'review=',r.human_review_required)
