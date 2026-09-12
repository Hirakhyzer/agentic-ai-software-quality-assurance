# Architecture

The framework separates **agents**, **evidence**, **orchestration**, and **evaluation**. Agents receive a sanitized `AgentContext` that excludes hidden reference implementations and ground-truth bug locations. The research harness alone owns those fields.

The v0.1 flow is reproduce -> collect runtime evidence -> generate boundary tests -> localize -> generate candidate patches -> verify -> accept or escalate. Static-only ablations skip runtime-grounded localization and generated boundary tests.
