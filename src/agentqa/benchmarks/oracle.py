from __future__ import annotations

from typing import Any

from agentqa.models import BugCase, TestVector
from agentqa.runtime.executor import _load_function


def expected_for_args(case: BugCase, args: tuple[Any, ...], name: str) -> TestVector:
    fn = _load_function(case.reference_source, case.function_name)
    return TestVector(args=args, expected=fn(*args), name=name)


def hidden_tests(case: BugCase) -> tuple[TestVector, ...]:
    return tuple(expected_for_args(case, args, f"hidden_{i}") for i, args in enumerate(case.hidden_inputs))
