from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class TestVector:
    args: tuple[Any, ...] = ()
    kwargs: dict[str, Any] = field(default_factory=dict)
    expected: Any = None
    name: str = "test"


@dataclass(frozen=True)
class BugCase:
    case_id: str
    issue: str
    function_name: str
    source: str
    reference_source: str
    public_tests: tuple[TestVector, ...]
    hidden_inputs: tuple[tuple[Any, ...], ...]
    bug_line: int
    category: str


@dataclass(frozen=True)
class AgentContext:
    case_id: str
    issue: str
    function_name: str
    source: str
    public_tests: tuple[TestVector, ...]


@dataclass(frozen=True)
class ExecutionObservation:
    test_name: str
    passed: bool
    expected: Any
    actual: Any = None
    exception_type: str | None = None
    exception_message: str | None = None
    exception_line: int | None = None
    trace_lines: tuple[int, ...] = ()


@dataclass(frozen=True)
class RuntimeEvidence:
    observations: tuple[ExecutionObservation, ...]
    failing_tests: tuple[str, ...]
    line_hits: dict[int, int]
    terminal_lines: tuple[int, ...]
    exception_lines: tuple[int, ...]


@dataclass(frozen=True)
class LocalizationResult:
    ranked_lines: tuple[tuple[int, float], ...]
    method: str

    @property
    def top1(self) -> int | None:
        return self.ranked_lines[0][0] if self.ranked_lines else None

    def topk(self, k: int) -> tuple[int, ...]:
        return tuple(line for line, _ in self.ranked_lines[:k])


@dataclass(frozen=True)
class PatchCandidate:
    patch_id: str
    source: str
    changed_line: int
    rationale: str


@dataclass(frozen=True)
class VerificationResult:
    patch_id: str
    public_passed: bool
    generated_passed: bool
    hidden_passed: bool
    public_failures: int
    generated_failures: int
    hidden_failures: int

    @property
    def plausible(self) -> bool:
        return self.public_passed and self.generated_passed

    @property
    def correct(self) -> bool:
        return self.plausible and self.hidden_passed


@dataclass(frozen=True)
class QAResult:
    case_id: str
    mode: str
    reproduced: bool
    localization: LocalizationResult
    candidates_considered: int
    selected_patch: PatchCandidate | None
    verification: VerificationResult | None
    generated_tests: tuple[TestVector, ...] = ()
    human_review_required: bool = False
