from agentqa.localization.static import static_localize
from agentqa.localization.runtime import runtime_localize

class FaultLocalizationAgent:
    name='fault_localizer'
    def run(self, source, evidence=None, mode='runtime'):
        return static_localize(source) if mode=='static' else runtime_localize(source,evidence)
