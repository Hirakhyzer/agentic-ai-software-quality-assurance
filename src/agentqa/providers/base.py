from __future__ import annotations
from typing import Protocol

class LanguageModelProvider(Protocol):
    """Future extension point for LLM-backed agents. v0.1 ships no model calls."""
    def complete(self, system_prompt: str, user_prompt: str) -> str: ...
