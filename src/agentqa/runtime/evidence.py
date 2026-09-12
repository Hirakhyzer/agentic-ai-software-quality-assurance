from __future__ import annotations

from agentqa.models import RuntimeEvidence


def compact_evidence(evidence: RuntimeEvidence, max_lines: int = 12) -> dict:
    """Return a compact, serializable evidence view for an agent.

    Raw traces can be large and repetitive. v0.1 keeps only the most frequently
    executed failing-path lines plus terminal/exception anchors.
    """
    ranked = sorted(evidence.line_hits.items(), key=lambda x: (-x[1], x[0]))
    anchors = list(dict.fromkeys((*evidence.exception_lines, *evidence.terminal_lines)))
    selected: list[int] = []
    for line in anchors + [line for line, _ in ranked]:
        if line not in selected:
            selected.append(line)
        if len(selected) >= max_lines:
            break
    return {
        "failing_tests": list(evidence.failing_tests),
        "selected_lines": selected,
        "terminal_lines": list(evidence.terminal_lines),
        "exception_lines": list(evidence.exception_lines),
        "line_hits": {str(k): evidence.line_hits[k] for k in selected if k in evidence.line_hits},
    }
