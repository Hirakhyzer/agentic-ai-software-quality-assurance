from __future__ import annotations
from agentqa.models import PatchCandidate

TRANSFORMS = [
    ('range(n)', 'range(n + 1)', 'include the upper range boundary'),
    ('(len(values) - 1)', 'len(values)', 'use the full collection length'),
    ('[index + 1]', '[index]', 'remove the index shift'),
    ('name.lower()', 'name.strip().lower()', 'normalize surrounding whitespace before lowercasing'),
    ('denominator < 0', 'denominator <= 0', 'guard non-positive denominators'),
    ('denominator < 0', 'denominator == 0', 'guard only zero denominators'),
    ('return upper - 1', 'return upper', 'return the configured upper clamp'),
    ('item is target', 'item == target', 'use value equality'),
    ('value < 0', 'value <= 0', 'reject zero at the positive-integer boundary'),
]

def generate_candidates(source: str) -> tuple[PatchCandidate, ...]:
    out=[]
    lines=source.splitlines()
    for i,line in enumerate(lines, start=1):
        for j,(old,new,why) in enumerate(TRANSFORMS):
            if old in line:
                changed=source.replace(old,new,1)
                out.append(PatchCandidate(f'p{i}_{j}', changed, i, why))
    return tuple(out)
