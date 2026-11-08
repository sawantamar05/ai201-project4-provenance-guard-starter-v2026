"""The five original criteria and their fixed input groups for Part 2."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
CORPUS=json.loads((ROOT/'data/evaluation_inputs.json').read_text())
SUPPLEMENT=json.loads((ROOT/'data/label_demonstrations.json').read_text())['demonstrations']
HUMAN=CORPUS['human']
AI=CORPUS['ai']
BY_ID={x['id']:x for x in HUMAN+AI+CORPUS['calibration']+SUPPLEMENT}
SCENARIOS=[
 {'criterion':1,'name':'Limit false accusations','kind':'false_positives',
  'target':'At most 1/10 sourced human passages labeled AI in every trial',
  'inputs':HUMAN},
 {'criterion':2,'name':'Separate contrasting inputs','kind':'score_spread',
  'target':'Four-AI median minus first-four-human median >= 0.20 in every trial',
  'human_inputs':[BY_ID[x] for x in CORPUS['metadata']['score_spread_human_ids']],
  'ai_inputs':[BY_ID[x] for x in CORPUS['metadata']['score_spread_ai_ids']]},
 {'criterion':3,'name':'Cover all labels and scores','kind':'label_coverage',
  'target':'Actual human/unsure/ai labels and all 10,001 scores mapped; 0.51 differs from 0.95',
  'inputs':HUMAN+AI+CORPUS['calibration']+SUPPLEMENT},
 {'criterion':4,'name':'Preserve usable appeals','kind':'appeals',
  'target':'10/10 exact appeals, immutable decisions, fresh-process status, no rescoring; unknown ID404',
  'inputs':HUMAN},
 {'criterion':5,'name':'Reject bad input before scoring','kind':'bad_input',
  'target':'All 18 validation groups return specified JSON400/404/413/415; no success events',
  'matrix_file':'docs/design.md','case_factory':'scripts.verify_project.validation_cases'},
]


def validate():
    problems=[]
    if [s.get('criterion') for s in SCENARIOS]!=[1,2,3,4,5]:
        problems.append('Exactly the original five criteria must be configured once each.')
    for s in SCENARIOS:
        if not s.get('name') or not s.get('target') or not s.get('kind'):
            problems.append(f"Incomplete criterion {s.get('criterion')}")
        inputs=s.get('inputs',s.get('human_inputs',[])+s.get('ai_inputs',[]))
        if s['kind']!='bad_input' and not inputs:
            problems.append(f"No inputs for criterion {s['criterion']}")
        for item in inputs:
            if not all(item.get(k) for k in ('id','text','provenance')):
                problems.append(f"Missing ID/text/provenance in criterion {s['criterion']}")
    return problems
