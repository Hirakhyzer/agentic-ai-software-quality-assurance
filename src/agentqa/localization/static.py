from __future__ import annotations
import ast
from collections import defaultdict
from agentqa.models import LocalizationResult

WEIGHTS = {ast.Return: 3.0, ast.If: 2.5, ast.For: 2.0, ast.Compare: 2.0, ast.BinOp: 1.5, ast.Subscript: 1.5, ast.Call: 1.0}

def static_localize(source: str) -> LocalizationResult:
    tree=ast.parse(source); scores=defaultdict(float)
    for node in ast.walk(tree):
        line=getattr(node,'lineno',None)
        if line is None: continue
        for typ,w in WEIGHTS.items():
            if isinstance(node,typ): scores[line]+=w; break
    ranked=tuple(sorted(scores.items(), key=lambda x:(-x[1],x[0])))
    return LocalizationResult(ranked_lines=ranked, method='static_ast')
