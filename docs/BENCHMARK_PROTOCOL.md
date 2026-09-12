# Benchmark Protocol

The controlled benchmark contains eight synthetic Python defects. Each case includes an issue description, buggy implementation, public tests, a hidden reference implementation used only by the evaluator, held-out inputs, and a ground-truth defect line for localization scoring.

Report reproduction rate, top-1/top-3 localization accuracy, plausible patch rate, held-out correct patch rate, overfit rate, human-review rate, and candidate count. Compare `static_only` and `runtime_grounded` under the same candidate budget.

Reference implementations are excluded from `AgentContext`. Generated candidate inputs are labelled by the controlled benchmark oracle; this is a major simplification and must not be described as solved real-world test-oracle generation.
