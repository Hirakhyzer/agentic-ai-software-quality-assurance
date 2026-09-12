# Baseline Findings

The deterministic v0.1 benchmark contains 8 controlled bug cases. All defects are reproduced by their public tests.

| Metric | Static only | Runtime grounded |
|---|---:|---:|
| Reproduction | 100% | 100% |
| Top-1 localization | 87.5% | 62.5% |
| Top-3 localization | 100% | 100% |
| Plausible patch | 100% | 100% |
| Correct patch | 87.5% | 100% |
| Overfit patch | 12.5% | 0% |
| Human review | 12.5% | 0% |

The runtime heuristic is *worse* at top-1 localization because failing executions often terminate on the symptom line, while the semantic defect can be earlier. However, runtime-grounded orchestration generates extra boundary tests and rejects the `denominator <= 0` overfit in the `safe_ratio` case, selecting the semantically correct `denominator == 0` repair instead.

This is a tiny synthetic benchmark with hand-authored repair transforms. A 100% runtime-grounded repair rate is therefore **not** evidence of general automated repair capability. It is only a sanity-check baseline for the orchestration and measurement framework.
