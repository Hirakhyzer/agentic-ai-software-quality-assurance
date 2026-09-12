# Agentic AI Software Quality Assurance

[![CI](https://github.com/Hirakhyzer/agentic-ai-software-quality-assurance/actions/workflows/ci.yml/badge.svg)](https://github.com/Hirakhyzer/agentic-ai-software-quality-assurance/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-research%20prototype-orange)

A reproducible research framework for **runtime-grounded agentic AI in software quality assurance**. It studies whether specialized QA agents can improve test generation, fault localization, repair, and verification when they use execution evidence rather than source code alone.

> **Research boundary:** v0.1 contains deterministic, inspectable agent baselines rather than autonomous LLM calls. The execution engine is intended only for the repository's trusted synthetic benchmark programs; it is **not** a security sandbox for arbitrary untrusted code.

## Core research question

**Can specialized software-QA agents collaborate more reliably when their decisions are grounded in runtime evidence such as failing executions, stack traces, and line traces, rather than relying mainly on static source artifacts?**

```text
Developer / issue specification
          |
          v
     QA Coordinator
          |
   +------+------+----------------+
   |             |                |
Reproducer   Test Generator   Runtime Analyst
   |             |                |
   +-------------+----------------+
                 |
           Evidence Store
                 |
          Fault Localizer
                 |
            Repair Agent
                 |
         Verification Agent
                 |
        +--------+---------+
        |                  |
   accept patch       human review
```

## Implemented in v0.1

- reproducible synthetic bug benchmark with 8 defect categories;
- issue reproduction and failing-test capture;
- Python line-trace and exception evidence;
- compact runtime-evidence selection;
- static AST fault-localization baseline;
- runtime-grounded localization baseline;
- deterministic boundary-oriented test generation;
- benchmark-controlled executable test oracle;
- interpretable patch-candidate generation;
- public/generated/hidden regression verification;
- explicit plausible-vs-correct patch distinction;
- human-review escalation when correctness is not established;
- static-only vs runtime-grounded ablation;
- LLM-provider protocol for later model-backed agents;
- Python 3.10/3.11/3.12 CI.

## Quick start

```bash
git clone https://github.com/Hirakhyzer/agentic-ai-software-quality-assurance.git
cd agentic-ai-software-quality-assurance
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
python scripts/run_demo.py
python scripts/run_benchmark.py
```

## Frozen v0.1 baseline

The controlled 8-case benchmark produces:

| Metric | Static only | Runtime grounded |
|---|---:|---:|
| Reproduction rate | 100% | 100% |
| Top-1 localization accuracy | **87.5%** | 62.5% |
| Top-3 localization accuracy | 100% | 100% |
| Plausible patch rate | 100% | 100% |
| Correct patch rate | 87.5% | **100%** |
| Overfit patch rate | 12.5% | **0%** |
| Human-review rate | 12.5% | **0%** |

This result is intentionally not presented as evidence that runtime traces universally improve localization. In this small benchmark, the runtime heuristic actually reduces top-1 line accuracy because terminal/exception lines can identify symptoms rather than root causes. Yet the runtime-grounded pipeline improves final repair correctness by **12.5 percentage points** because generated boundary tests reject an overfitting patch. That tension is one of the research questions this repository is designed to study.

These are synthetic deterministic results, not claims about real repositories, LLM agents, or industrial developer productivity. See [`docs/BASELINE_FINDINGS.md`](docs/BASELINE_FINDINGS.md).

## Benchmark bug classes

`off_by_one`, `arithmetic`, `indexing`, `string_normalization`, `wrong_condition`, `boundary`, and `operator` errors are represented. The benchmark keeps reference implementations and held-out tests outside the agent context to prevent direct oracle leakage.

## Research roadmap

v0.2 should add real repository adapters, subprocess/container execution isolation, coverage/spectrum evidence, mutation testing, richer test oracles, patch-diff minimization, and calibrated agent confidence. Later versions can plug in LLM-backed agents through the provider interface and evaluate on Defects4J/SWE-bench-style tasks without changing the measurement model.

## Scientific integrity

Report the exact commit, Python version, benchmark version, agent mode, evidence budget, candidate budget, generated-test policy, and held-out evaluation protocol. Never equate "tests pass" with semantic correctness; v0.1 therefore reports plausible and held-out-correct patches separately.

See `docs/` for architecture, runtime evidence, orchestration, benchmark protocol, limitations, safety, reproducibility, references, and roadmap.
