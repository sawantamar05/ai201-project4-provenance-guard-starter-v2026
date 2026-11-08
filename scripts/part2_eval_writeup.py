"""Render measured five-row criterion tables and actual JSON excerpts."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]


def table(report):
    lines=['| Criterion | Original target | Run 1 | Run 2 | Run 3 | Verdict |','|---|---|---|---|---|---|']
    for n,c in report['criteria'].items():
        values=' | '.join(x['summary'] for x in c['trials'])
        lines.append(f'| {n}. {c["name"]} | {c["target"]} | {values} | {c["verdict"]} |')
    return '\n'.join(lines)


def excerpts(report):
    lines=[]
    for n,c in report['criteria'].items():
        t=c['trials'][0]
        if n=='4':
            payload=t['cases'][0]['appeal']['response_json']
        elif n=='5':
            sample=next((x for x in t['cases'] if not x['passed']),t['cases'][0])
            payload=sample['http']['response_json']
        else:
            sample=t['cases'][0]
            if n=='3':sample=next(x for x in t['cases'] if x['response_json'].get('guess')=='human')
            payload=sample['response_json']
        lines += [f'**Criterion {n}, actual trial-1 response.** Produced by `run_eval.py::trial_result` via the live API.','', '```json',json.dumps(payload,indent=2,ensure_ascii=False),'```','']
    return '\n'.join(lines)


def main():
    report=json.loads((ROOT/'results/part2_eval_before.json').read_text())
    text='''

## Run Log and Verdicts

These are the **original five targets from Part 1**, tested three times with no
service changes between trials. `scenarios.py` configures each criterion once;
`run_eval.py::main` / `run_eval.py::trial_result` perform all HTTP calls and save
[the full before JSON](results/part2_eval_before.json) and
[the run log](results/part2_eval_before.md). Every miss is retained. Historical
human passages are the original fixed sourced corpus, not personal writing.
Supplemental synthetic label demonstrations remain excluded from score-spread
and false-positive groups.

### Before the improvement

'''+table(report)+'''

The model scores are identical across trials. Criterion 5 differs because
invalid requests with missing/unusable creator IDs share an address quota:
the first trial consumes it and later trials are still inside the minute.
A 429 is safe rejection, but the original criterion explicitly requires
400/404/413/415, so it is **MISSED** rather than generously reinterpreted.
Valid scenario IDs are distinct per criterion/trial; no rejected call is
silently retried. The rate limiter remains enabled throughout.

'''+excerpts(report)+'''

The complete per-case responses, 10-appeal histories, fresh-process content
checks, 10,001-score sweep, and exact-status validation cases are in the JSON.
Fresh-process checks show all ten appealed items under review with the detector
unloaded. Isolated service tests separately assert zero detector calls for
appeals and invalid input; a JSON response alone cannot establish call counts.
'''
    p=ROOT/'README.md';p.write_text(p.read_text()+text)
    p=ROOT/'docs/progress_part2.md';s=p.read_text().replace('| 3. Five criteria, three trials | Pending | Complete scenarios and before report against unchanged targets |','| 3. Five criteria, three trials | Complete before fix | Criteria 1–4 MET in all trials; criterion 5 MISSED (36/37, 26/37, 26/37); all raw responses saved |');p.write_text(s)


if __name__=='__main__':main()
