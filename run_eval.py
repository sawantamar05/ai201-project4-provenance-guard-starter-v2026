#!/usr/bin/env python3
"""Run the original five criteria in three real HTTP trials, before or after.

Every outcome is saved, including missed targets. Limiter responses are not
silently retried or treated as validation successes. Scenarios and target
membership come from scenarios.py; criteria.md is never rewritten by this tool.
"""
import argparse
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import statistics
import subprocess
import sys
import time
import uuid

import requests
import config
import scenarios
from scripts.verify_project import capture,score_sweep,settings_snapshot,package_versions,validation_cases

ROOT=Path(__file__).resolve().parent


def send(session,args,method,path,**kwargs):
    start=time.monotonic()
    result=capture(session,method,args.url+path,args.timeout,**kwargs)
    result['elapsed_ms']=round((time.monotonic()-start)*1000,2)
    return result


def submit_items(session,args,items,trial,criterion):
    records=[]
    for item in items:
        body={'text':item['text'],'creator_id':f'eval-{args.label}-c{criterion}-t{trial}-{item["id"]}'}
        r=send(session,args,'POST','/submit',json=body)
        r.update(input_id=item['id'],input_provenance=item)
        records.append(r)
    return records


def valid(record):
    r=record.get('response_json',{})
    return record['status_code']==200 and r.get('status')=='decided' and r.get('guess') in ('human','unsure','ai')


def events(session,args):
    r=send(session,args,'GET','/log')
    if r['status_code']!=200:raise RuntimeError('Audit log unavailable during evaluation')
    return r['response_json']['entries']


def fresh_instance(ids):
    code="""
import json,sys
import app
client=app.app.test_client()
rows=[]
for identity in sys.argv[1:]:
 r=client.get('/content/'+identity)
 rows.append({'content_id':identity,'status_code':r.status_code,'response':r.get_json()})
print(json.dumps({'detector_loaded':app.detector._model is not None,'items':rows}))
"""
    p=subprocess.run([sys.executable,'-c',code,*ids],cwd=ROOT,capture_output=True,text=True,timeout=30)
    if p.returncode:return {'error':p.stderr,'returncode':p.returncode,'passed':False}
    r=json.loads(p.stdout)
    r['passed']=not r['detector_loaded'] and len(r['items'])==10 and all(x['status_code']==200 and x['response']['status']=='under_review' for x in r['items'])
    return r


def trial_result(session,args,scenario,trial):
    number=scenario['criterion'];kind=scenario['kind']
    out={'trial':trial,'criterion':number,'kind':kind,'cases':[]}
    if kind in ('false_positives','label_coverage'):
        cases=submit_items(session,args,scenario['inputs'],trial,number);out['cases']=cases
        good=[r for r in cases if valid(r)]
        if kind=='false_positives':
            flagged=[r['input_id'] for r in good if r['response_json']['guess']=='ai']
            out.update(flagged_ids=flagged,valid_count=len(good),summary=f'{len(flagged)}/10 AI flags; {len(good)}/10 valid',passed=len(good)==10 and len(flagged)<=1)
        else:
            labels=sorted({r['response_json']['guess'] for r in good})
            sweep=score_sweep();out.update(actual_labels=labels,score_sweep=sweep,summary=f'{len(labels)}/3 labels; {sweep["scores_checked"]} scores',passed=len(good)==len(cases) and set(labels)=={'human','unsure','ai'} and sweep['passed'])
    elif kind=='score_spread':
        humans=submit_items(session,args,scenario['human_inputs'],trial,number)
        ais=submit_items(session,args,scenario['ai_inputs'],trial,number)
        out['cases']=humans+ais
        hs=[r['response_json']['combined_score'] for r in humans if valid(r)]
        ac=[r['response_json']['combined_score'] for r in ais if valid(r)]
        hm=statistics.median(hs) if len(hs)==4 else None
        am=statistics.median(ac) if len(ac)==4 else None
        gap=round(am-hm,10) if hm is not None and am is not None else None
        out.update(human_median=hm,ai_median=am,gap=gap,summary=f'median gap {gap}',passed=gap is not None and gap>=0.20)
    elif kind=='appeals':
        submissions=submit_items(session,args,scenario['inputs'],trial,number)
        out['submissions']=submissions
        originals={e.get('content_id'):e for e in events(session,args) if e.get('status')=='decided'}
        checked=[];ids=[]
        for r in submissions:
            if not valid(r):checked.append({'submission':r,'passed':False});continue
            identity=r['response_json']['content_id'];ids.append(identity)
            reasoning=f'Part 2 criterion review {args.label}, trial {trial}: please inspect this estimate.'
            appeal=send(session,args,'POST','/appeal',json={'content_id':identity,'reasoning':reasoning})
            current=send(session,args,'GET','/content/'+identity)
            old=originals[identity];cur=current.get('response_json',{})
            matching=all(cur.get(k)==v for k,v in old.items() if k!='status')
            ok=appeal['status_code']==200 and appeal.get('response_json',{}).get('reasoning')==reasoning and cur.get('status')=='under_review' and matching
            checked.append({'content_id':identity,'original':old,'appeal':appeal,'current':current,'passed':ok})
        after=events(session,args)
        for item in checked:
            if not item.get('content_id'):continue
            history=[x for x in after if x.get('content_id')==item['content_id']]
            item['history']=history
            item['passed']=item['passed'] and len(history)==2 and history[0]==item['original'] and history[1].get('event')=='appeal'
        unknown=str(uuid.uuid4())
        unknown_response=send(session,args,'POST','/appeal',json={'content_id':unknown,'reasoning':'Unknown-ID development check.'})
        unknown_ok=unknown_response['status_code']==404 and not any(x.get('event')=='appeal' and x.get('content_id')==unknown for x in events(session,args))
        fresh=fresh_instance(ids)
        count=sum(x['passed'] for x in checked)
        out.update(cases=checked,unknown_id=unknown_response,fresh_instance=fresh,summary=f'{count}/10 appeals; persistence {fresh["passed"]}',passed=len(checked)==10 and count==10 and unknown_ok and fresh['passed'],no_rescoring_evidence='Fresh instance remains detector_loaded=false; isolated service tests separately patch the detector and assert zero appeal calls.')
    elif kind=='bad_input':
        before=events(session,args)
        existing=next((x['content_id'] for x in reversed(before) if x.get('status')=='decided'),str(uuid.uuid4()))
        cases=[]
        for index,case in enumerate(validation_cases(existing)):
            kwargs=case['kwargs'].copy()
            if isinstance(kwargs.get('json'),dict):
                body=kwargs['json'].copy();creator=body.get('creator_id')
                if isinstance(creator,str) and creator.strip() and len(creator)<=128:
                    body['creator_id']=f'eval-{args.label}-c5-t{trial}-case{index}'
                kwargs['json']=body
            r=send(session,args,'POST',case['route'],**kwargs)
            payload=r.get('response_json',{})
            ok=r['status_code']==case['expected_status'] and isinstance(payload,dict) and bool(payload.get('error')) and bool(payload.get('message'))
            cases.append({'matrix_group':case['matrix_group'],'name':case['name'],'expected_status':case['expected_status'],'http':r,'passed':ok})
        after=events(session,args)
        success=lambda rows:[r for r in rows if r.get('status') in ('decided','under_review')]
        unchanged=success(before)==success(after)
        coverage=sorted({x['matrix_group'] for x in cases});count=sum(x['passed'] for x in cases)
        out.update(cases=cases,groups=coverage,successful_events_unchanged=unchanged,summary=f'{count}/{len(cases)} exact responses; {len(coverage)}/18 groups',passed=count==len(cases) and coverage==list(range(1,19)) and unchanged,no_scoring_evidence='Isolated validation tests assert zero detector calls; the live log contains no added successful events.')
    else:raise ValueError(kind)
    out['verdict']='MET' if out['passed'] else 'MISSED'
    return out


def write_report(report,path):
    path.write_text(json.dumps(report,indent=2,ensure_ascii=True)+'\n')
    lines=[f'# Criteria run — {report["label"]}','',
           '- Produced by `run_eval.py::main` and `run_eval.py::trial_result`.',
           '- Five original criteria; three real HTTP trials each. Full capture: '+path.name+'.',
           '- No request is silently retried. A 429 differs from a required 400/413/415.',
           '', '| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |','|---|---|---|---|---|---|']
    for number,c in report['criteria'].items():
        values=[x['summary'] for x in c['trials']]
        lines.append(f'| {number}. {c["name"]} | {c["target"]} | '+ ' | '.join(values)+f' | {c["verdict"]} |')
    lines+=['','## Actual output, trial 1','']
    for number,c in report['criteria'].items():
        t=c['trials'][0]
        lines += [f'### Criterion {number}','',f'Produced by `run_eval.py::trial_result` ({t["kind"]}).','', '```json',json.dumps(t,indent=2,ensure_ascii=True),'```','']
    path.with_suffix('.md').write_text('\n'.join(lines).rstrip()+'\n')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--label',required=True,choices=['before','after']);p.add_argument('--trials',type=int,default=3)
    p.add_argument('--url',default=f'http://{config.HOST}:{config.PORT}');p.add_argument('--timeout',type=float,default=120)
    args=p.parse_args();args.url=args.url.rstrip('/')
    if args.trials!=3:p.error('This evidence run requires exactly three trials.')
    problems=scenarios.validate()
    if problems:raise ValueError(problems)
    files=('app.py','audit.py','config.py','detector.py','scoring.py','stylometry.py','criteria.md','scenarios.py','data/evaluation_inputs.json','data/label_demonstrations.json')
    report={'label':args.label,'started_at_utc':datetime.now(timezone.utc).isoformat(),
            'source_hashes':{f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files},
            'scoring_settings':settings_snapshot(),'packages':package_versions(),
            'scope':'Original fixed historical-human/generated development corpus and previously disclosed synthetic reachability examples. Not independent human-authorship validation.',
            'rate_limit_policy':'Limiter remains enabled. Valid scenario IDs are distinct by criterion/trial. Invalid requests without usable IDs share the real address quota and may expose a criterion miss.',
            'criteria':{str(s['criterion']):{'name':s['name'],'kind':s['kind'],'target':s['target'],'trials':[]} for s in scenarios.SCENARIOS}}
    with requests.Session() as session:
        report['health_before']=send(session,args,'GET','/health')
        if not report['health_before'].get('response_json',{}).get('rate_limiting'):raise RuntimeError('Rate limiting must remain on for Part 2 evidence.')
        for trial in range(1,4):
            for s in scenarios.SCENARIOS:
                result=trial_result(session,args,s,trial)
                report['criteria'][str(s['criterion'])]['trials'].append(result)
                print(f'Trial {trial}, criterion {s["criterion"]}: {result["summary"]} — {result["verdict"]}',flush=True)
        report['health_after']=send(session,args,'GET','/health')
    for c in report['criteria'].values():
        c['verdict']='MET' if all(x['passed'] for x in c['trials']) else 'MISSED'
    report['finished_at_utc']=datetime.now(timezone.utc).isoformat()
    write_report(report,ROOT/'results'/f'part2_eval_{args.label}.json')
    print(f'Saved results/part2_eval_{args.label}.json and .md; missed targets are retained.',flush=True)


if __name__=='__main__':main()
