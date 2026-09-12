import json
from agentqa.benchmarks.runner import compare_modes
print(json.dumps(compare_modes(),indent=2,sort_keys=True))
