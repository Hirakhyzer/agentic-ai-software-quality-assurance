from __future__ import annotations

def summarize(results, cases):
    case_map={c.case_id:c for c in cases}; n=len(results) or 1
    reproduced=sum(r.reproduced for r in results)
    top1=sum(r.localization.top1==case_map[r.case_id].bug_line for r in results)
    top3=sum(case_map[r.case_id].bug_line in r.localization.topk(3) for r in results)
    plausible=sum(bool(r.verification and r.verification.plausible) for r in results)
    correct=sum(bool(r.verification and r.verification.correct) for r in results)
    overfit=sum(bool(r.verification and r.verification.plausible and not r.verification.hidden_passed) for r in results)
    return {
        'cases':len(results), 'reproduction_rate':reproduced/n, 'top1_localization_accuracy':top1/n, 'top3_localization_accuracy':top3/n,
        'plausible_patch_rate':plausible/n, 'correct_patch_rate':correct/n, 'overfit_patch_rate':overfit/n,
        'human_review_rate':sum(r.human_review_required for r in results)/n,
        'mean_candidates_considered':sum(r.candidates_considered for r in results)/n,
    }
