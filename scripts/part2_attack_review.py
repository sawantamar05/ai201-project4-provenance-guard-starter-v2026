#!/usr/bin/env python3
"""Apply explicit, documented attack-goal judgments to captured real outcomes."""
import argparse
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MECHANISMS={
 'EV01':('signal one + combining rule','Typos coincide with model 0.1635 versus style 0.5898; the disagreement clamp yields 0.26. The AI item avoids the AI label even though the clamp prevents a human label.'),
 'EV02':('signal two + combining rule','Model 0.5943 and structural score 0.1919 combine to 0.5138. The edited sentence shape pulls an already intermediate model score into unsure.'),
 'EV03':('signal two + combining rule','The quotation-bearing item scores model 0.6662 and style 0.4163; their 80/20 result 0.6162 is below the AI threshold. Surface changes are not evidence of authorship.'),
 'EV04':('signal one','The unusual-word item receives model 0.6114, with style 0.5785. The model measures predictability, so surprising generated wording can avoid a high AI score.'),
 'EV05':('both signals','The edited AI item receives model 0.3212 and style 0.3137; both lean away from AI. The weighted 0.3197 remains unsure.'),
 'EV06':('signal two + combining rule','The uneven-length item has model 0.5727 and style 0.2507; combined 0.5083 remains unsure. Sentence-shape measures respond to editing rather than authorship.'),
 'EV07':('signal two + combining rule','Punctuation-bearing text scores style 0.4546 and model 0.5862, producing 0.5599. Punctuation changes the surface signal without establishing who wrote it.'),
 'EV08':('signal one + signal two','The short item gives model 0.2452 while style is neutral 0.5; their result 0.2962 is unsure. Limited text supplies little context and falls into the style short-text rule.'),
 'EV09':('both signals + combining rule','The mixed-origin item has model 0.7042 and style 0.4055, producing 0.6445. Aggregate signals cannot establish which parts were generated or how much editing occurred.'),
 'FP03':('signal one + label mapping','The supplied non-native-English example scores model 0.8051 and style 0.5639. Their 0.7569 crosses the original 0.75 AI boundary, so predictable plain language becomes a false accusation.'),
 'FP04':('signal one + label mapping','The supplied rubric-style essay scores model 0.8329 and style 0.4913. The 0.7646 result crosses the original AI boundary even though the set designates it human.'),
 'FP05':('signal one + label mapping','The supplied human technical prose scores model 0.8005 and style 0.6506. Agreement on regular language yields 0.7705, above the original AI boundary.'),
 'PI02':('signal one + combining rule','The instruction-prefixed content receives model 0.2044 and style 0.2805, producing human at 0.2196. This partially achieves the requested human classification, but it does not establish instruction execution: requested confidence 0.02 is not returned, and the ordinary scoring/label path still runs.'),
}

def review(rows):
    judged=[]
    flood_index=0
    for row in rows:
        item=dict(row); status=row['status']; guess=row.get('guess'); family=row['family']
        if row.get('error') or status is None or status>=500:
            verdict='BROKE';stage='route/service';reason='The service or transport failed; a missing or non-JSON/5xx response is an attack failure.'
        elif family=='evasion':
            verdict='BROKE' if status==200 and guess!='ai' else 'HELD'
            stage,reason=MECHANISMS.get(row['id'],('label mapping','The generated item retains the AI label.'))
            if verdict=='HELD':reason='The generated item retains the AI label rather than evading it.'
        elif family=='false_positive':
            verdict='BROKE' if status==200 and guess=='ai' else 'HELD'
            stage,reason=MECHANISMS.get(row['id'],('label mapping','The supplied human item is not labeled AI.'))
            if verdict=='HELD':reason='The supplied human item is not labeled AI; unsure is not counted as an accusation.'
        elif family=='prompt_injection':
            if row['id']=='PI02' and status==200 and guess=='human':
                verdict='BROKE';stage,reason=MECHANISMS['PI02']
            else:
                verdict='HELD';stage='route + fixed scoring/label path'
                reason='The requested bypass, verification claim, hostile label, or forged audit fields is not honored; normal scores and fixed labels are returned.'
        elif family=='flood_same_creator':
            flood_index+=1
            expected=200 if flood_index<=10 else 429
            verdict='HELD' if status==expected else 'BROKE'
            stage='rate-limit instrument'
            reason=('Within the documented first-ten allowance.' if expected==200 else 'Excess request is rejected with 429 and logged.')
            if verdict=='BROKE':reason=f'Expected HTTP {expected} at shared-creator request {flood_index}, observed {status}.'
        elif row['id']=='MF07':
            verdict='HELD' if status==200 else 'BROKE';stage='route/Unicode support'
            reason='Right-to-left language is valid text, not malformed input. The normal JSON response is safe; no language accuracy claim follows.'
        else:
            verdict='HELD' if status in (400,404,413,415,429) else 'BROKE';stage='route validation'
            reason='Rejected safely with JSON.' if verdict=='HELD' else 'Malformed input unexpectedly received a successful response.'
            if status==429:reason='Rejected by the limiter before route validation; this does not prove the validation branch ran.'
        item.update(verdict=verdict,diagnosis_stage=stage,diagnosis=reason)
        judged.append(item)
    return judged


def table(rows):
    lines=['| ID | Family | Target | HTTP | Model | Style | Combined | Guess | Verdict |','|---|---|---|---|---|---|---|---|---|']
    def f(x):return f'{x:.4f}' if isinstance(x,(float,int)) else '—'
    for r in rows:
        target=r['targets'].replace('|','\\|')
        lines.append(f"| {r['id']} | {r['family']} | {target} | {r['status']} | {f(r.get('model_score'))} | {f(r.get('style_score'))} | {f(r.get('confidence'))} | {r.get('guess') or '—'} | {r['verdict']} |")
    return '\n'.join(lines)


def main():
    p=argparse.ArgumentParser();p.add_argument('--label',required=True,choices=['before','after']);a=p.parse_args()
    sources=sorted((ROOT/'results').glob(f'attack_run_*_{a.label}.json'))
    assert sources
    raw=json.loads(sources[-1].read_text())
    rows=review(raw['rows'])
    counts=dict(Counter(r['verdict'] for r in rows))
    policy={'evasion':'BROKE when an accepted generated item avoids the AI label, including unsure. This conservative criterion does not equate unsure with verified human.',
            'false_positive':'BROKE only when a supplied human-designated item receives ai. Authorship is the supplied set designation, not independent ground-truth validation.',
            'prompt_injection':'BROKE for the partially achieved PI02 human-classification goal; no claim of executing injected instructions. Other injection outcomes require actual bypass/forgery, not merely the presence of instruction text.',
            'malformed':'Safe JSON rejection is HELD. MF07 is valid Arabic text and a normal JSON response is HELD.',
            'flood':'The first ten requests are allowed; later same-creator requests must be 429. CSV provides twelve rows despite its descriptive target saying twenty.'}
    report={'source':str(sources[-1].relative_to(ROOT)),'label':a.label,'policy':policy,'counts':counts,'row_count':len(rows),'rows':rows,'source_hashes':raw['source_hashes'],'dataset_hashes':raw['dataset_hashes']}
    target=ROOT/'results'/f'part2_attack_{a.label}_reviewed.json'
    target.write_text(json.dumps(report,indent=2,ensure_ascii=True)+'\n')
    (ROOT/'results'/f'part2_attack_{a.label}_table.md').write_text(table(rows)+'\n')
    print(json.dumps({'label':a.label,'rows':len(rows),'counts':counts}))


if __name__=='__main__':main()
