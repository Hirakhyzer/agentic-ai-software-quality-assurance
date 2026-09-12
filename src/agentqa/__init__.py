"""Runtime-grounded agentic software quality assurance research framework."""

from .models import (
    AgentContext, BugCase, ExecutionObservation, LocalizationResult,
    PatchCandidate, QAResult, TestVector, VerificationResult,
)

__all__ = [
    "AgentContext", "BugCase", "ExecutionObservation", "LocalizationResult",
    "PatchCandidate", "QAResult", "TestVector", "VerificationResult",
]

__version__ = "0.1.0"
