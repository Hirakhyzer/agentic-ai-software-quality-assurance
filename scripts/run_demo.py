from agentqa.benchmarks.cases import get_case
from agentqa.orchestration.coordinator import QACoordinator

case=get_case('zero_denominator_guard')
for mode in ('static_only','runtime_grounded'):
    r=QACoordinator().run(case,mode)
    print(f'[{mode}]')
    print('reproduced:',r.reproduced)
    print('top lines:',r.localization.ranked_lines[:3])
    print('generated tests:',len(r.generated_tests))
    print('patch:',r.selected_patch.patch_id if r.selected_patch else None)
    print('correct:',bool(r.verification and r.verification.correct))
    print('human review:',r.human_review_required)
