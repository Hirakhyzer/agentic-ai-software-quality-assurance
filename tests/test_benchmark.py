from agentqa.benchmarks.runner import run_benchmark,compare_modes

def test_benchmark_runs():
    results,summary=run_benchmark(); assert len(results)==summary['cases']==8

def test_reproduction_rate_is_complete():
    _,s=run_benchmark(); assert s['reproduction_rate']==1.0

def test_runtime_mode_has_strong_patch_rate():
    _,s=run_benchmark('runtime_grounded'); assert s['correct_patch_rate']>=0.875

def test_mode_comparison_has_gain_fields():
    c=compare_modes(); assert 'runtime_evidence_gain' in c
