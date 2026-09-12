from agentqa.repair.candidates import generate_candidates

class RepairAgent:
    name='repairer'
    def run(self, source, localization):
        candidates=list(generate_candidates(source))
        ranks={line:i for i,(line,_) in enumerate(localization.ranked_lines)}
        candidates.sort(key=lambda c:(ranks.get(c.changed_line,999), c.patch_id))
        return tuple(candidates)
