from __future__ import annotations
from collections import defaultdict
from agentqa.models import LocalizationResult, RuntimeEvidence
from .static import static_localize

def runtime_localize(source: str, evidence: RuntimeEvidence) -> LocalizationResult:
    scores=defaultdict(float)
    for line,score in static_localize(source).ranked_lines: scores[line]+=0.35*score
    for line,hits in evidence.line_hits.items(): scores[line]+=min(3.0,0.35*hits)
    for line in evidence.terminal_lines: scores[line]+=4.0
    for line in evidence.exception_lines: scores[line]+=6.0
    ranked=tuple(sorted(scores.items(), key=lambda x:(-x[1],x[0])))
    return LocalizationResult(ranked_lines=ranked, method='runtime_grounded')
