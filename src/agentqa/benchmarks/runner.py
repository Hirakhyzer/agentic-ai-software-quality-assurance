from __future__ import annotations
from agentqa.benchmarks.cases import CASES
from agentqa.orchestration.coordinator import QACoordinator
from agentqa.metrics.evaluation import summarize

def run_benchmark(mode='runtime_grounded'):
    coordinator=QACoordinator()
    results=tuple(coordinator.run(case,mode=mode) for case in CASES)
    return results, summarize(results,CASES)

def compare_modes():
    _, static=run_benchmark('static_only'); _, runtime=run_benchmark('runtime_grounded')
    return {'static_only':static,'runtime_grounded':runtime,'runtime_evidence_gain':{k:runtime[k]-static[k] for k in ('top1_localization_accuracy','correct_patch_rate','plausible_patch_rate')}}
