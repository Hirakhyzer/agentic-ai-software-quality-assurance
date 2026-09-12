# Runtime Evidence

The current executor records failing-test outcomes, exception type/message/line, ordered executed source lines, line-hit counts, and terminal executed lines. `compact_evidence` reduces repetitive traces to a bounded evidence view.

The executor directly executes trusted synthetic functions in the Python process. It is **not** a production sandbox. Running arbitrary generated code requires process/container isolation, resource limits, filesystem/network controls, and a separate threat model.
