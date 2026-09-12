# Limitations

- Only small single-function Python programs are benchmarked.
- Repair transforms are deterministic and hand-authored.
- No LLM or learned agent is evaluated in v0.1.
- Generated tests depend on a benchmark-only executable reference oracle.
- Line tracing is much weaker than full data/control dependency analysis.
- No concurrency, I/O, package-management, build-system, or multi-file repair is evaluated.
- Direct in-process execution is suitable only for trusted synthetic programs.
- Held-out tests approximate correctness but cannot prove semantic equivalence.
- The benchmark is intentionally too small for statistical claims.
