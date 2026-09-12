from __future__ import annotations

import sys
import traceback
from collections import Counter
from types import FrameType
from typing import Any

from agentqa.models import ExecutionObservation, RuntimeEvidence, TestVector

SYNTHETIC_FILENAME = "agentqa_candidate.py"


def _load_function(source: str, function_name: str):
    namespace: dict[str, Any] = {}
    code = compile(source, SYNTHETIC_FILENAME, "exec")
    exec(code, namespace, namespace)
    fn = namespace.get(function_name)
    if not callable(fn):
        raise ValueError(f"function {function_name!r} not found")
    return fn


def execute_test(source: str, function_name: str, test: TestVector, trace: bool = True) -> ExecutionObservation:
    fn = _load_function(source, function_name)
    lines: list[int] = []

    def tracer(frame: FrameType, event: str, arg):
        if frame.f_code.co_filename == SYNTHETIC_FILENAME and event == "line":
            lines.append(frame.f_lineno)
        return tracer

    actual = None
    exc_type = exc_message = None
    exc_line = None
    try:
        if trace:
            sys.settrace(tracer)
        actual = fn(*test.args, **test.kwargs)
        passed = actual == test.expected
    except Exception as exc:
        passed = False
        exc_type = type(exc).__name__
        exc_message = str(exc)
        tb = traceback.extract_tb(exc.__traceback__)
        candidate_frames = [x for x in tb if x.filename == SYNTHETIC_FILENAME]
        exc_line = candidate_frames[-1].lineno if candidate_frames else None
    finally:
        sys.settrace(None)
    return ExecutionObservation(
        test_name=test.name,
        passed=passed,
        expected=test.expected,
        actual=actual,
        exception_type=exc_type,
        exception_message=exc_message,
        exception_line=exc_line,
        trace_lines=tuple(lines),
    )


def execute_suite(source: str, function_name: str, tests: tuple[TestVector, ...], trace: bool = True) -> tuple[ExecutionObservation, ...]:
    return tuple(execute_test(source, function_name, t, trace=trace) for t in tests)


def build_runtime_evidence(observations: tuple[ExecutionObservation, ...]) -> RuntimeEvidence:
    failing = tuple(o for o in observations if not o.passed)
    hits: Counter[int] = Counter()
    terminals: list[int] = []
    exceptions: list[int] = []
    for obs in failing:
        hits.update(obs.trace_lines)
        if obs.trace_lines:
            terminals.append(obs.trace_lines[-1])
        if obs.exception_line is not None:
            exceptions.append(obs.exception_line)
    return RuntimeEvidence(
        observations=observations,
        failing_tests=tuple(o.test_name for o in failing),
        line_hits=dict(hits),
        terminal_lines=tuple(terminals),
        exception_lines=tuple(exceptions),
    )
