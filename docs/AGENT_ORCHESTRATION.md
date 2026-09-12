# Agent Orchestration

`QACoordinator` controls five deterministic agent roles: reproducer, test generator, fault localizer, repairer, and verifier. Runtime evidence is treated as shared evidence, not as unquestioned truth.

The coordinator accepts only a patch that passes the configured visible/generated verification stage. Held-out correctness is measured by the research harness and is never available to patch selection. In real deployment the hidden oracle would be replaced by specifications, trusted regression tests, metamorphic properties, independent review, or other assurance mechanisms.
