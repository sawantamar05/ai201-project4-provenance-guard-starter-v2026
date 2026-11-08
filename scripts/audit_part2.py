#!/usr/bin/env python3
"""Audit recorded Part 2 evidence without sending new requests or changing targets."""
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile

from part2_eval_writeup import table

ROOT=Path(__file__).resolve().parents[1]


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def read(path):return json.loads((ROOT/path).read_text())


def main():
    baseline=read('results/part2_baseline_manifest.json')
    change=read('results/part2_change_manifest.json')
    original=read('attack_set/provenance.json')
    before=read('results/part2_attack_before_reviewed.json')
    after=read('results/part2_attack_after_reviewed.json')
    eb=read('results/part2_eval_before.json');ea=read('results/part2_eval_after.json')
    checks={}
    assert digest(ROOT/'criteria.md')==baseline['files']['criteria.md']
    assert digest(ROOT/'criteria.md')==eb['source_hashes']['criteria.md']==ea['source_hashes']['criteria.md']
    checks['original_criteria_unchanged']=True
    assert digest(ROOT/'attack_set/source.zip')==original['archive_sha256']
    with zipfile.ZipFile(ROOT/'attack_set/source.zip') as z:
        for name,record in original['files'].items():
            matching=[x for x in z.namelist() if Path(x).name==name and '__MACOSX' not in x]
            assert len(matching)==1
            assert z.read(matching[0])==(ROOT/'attack_set'/name).read_bytes()
            assert digest(ROOT/'attack_set'/name)==record['sha256']==before['dataset_hashes'][name]==after['dataset_hashes'][name]
    checks['both_supplied_csvs_match_original_zip_and_both_runs']=True
    campaign_idle_seconds={}
    for label,report,attack in [('before',eb,before),('after',ea,after)]:
        raw=read(attack['source'])
        elapsed=(datetime.fromisoformat(report['started_at_utc'])-datetime.fromisoformat(raw['recorded_at'])).total_seconds()
        assert elapsed>=60,(label,elapsed)
        campaign_idle_seconds[label]=elapsed
    checks['address_minute_window_expired_before_each_criteria_campaign']=True

    for name in ('app.py','audit.py','detector.py','scoring.py','stylometry.py','data/evaluation_inputs.json','data/label_demonstrations.json'):
        assert digest(ROOT/name)==baseline['files'][name]
    assert change['changed_runtime_files']==['config.py']
    actual=subprocess.check_output(['git','diff','6d42fc9','--','app.py','audit.py','config.py','detector.py','scoring.py','stylometry.py'],cwd=ROOT,text=True)
    assert actual==change['runtime_diff']
    assert '-AI_THRESHOLD = 0.75' in actual and '+AI_THRESHOLD = 0.80' in actual
    checks['only_measured_runtime_improvement_is_ai_threshold']=True
    assert before['row_count']==after['row_count']==56
    assert len(before['rows'])==len(after['rows'])==56
    assert len({r['id'] for r in before['rows']})==56
    assert [r['id'] for r in before['rows']]==[r['id'] for r in after['rows']]
    changed=[]
    for b,a in zip(before['rows'],after['rows']):
        assert b['verdict'] in ('HELD','BROKE') and a['verdict'] in ('HELD','BROKE')
        for field in ('model_score','style_score','confidence','status'):assert b[field]==a[field]
        if b['guess']!=a['guess']:changed.append(b['id'])
        for item in (b,a):
            if item['verdict']=='BROKE':assert item['diagnosis_stage'] and item['diagnosis']
    assert changed==['FP03','FP04','FP05']
    checks['all_56_attacks_reviewed_in_each_phase_with_comparable_scores']=True
    for report in (eb,ea):
        assert list(report['criteria'])==list('12345')
        assert report['health_before']['response_json']['rate_limiting']
        assert report['health_after']['response_json']['rate_limiting']
        for n,c in report['criteria'].items():
            assert len(c['trials'])==3
            assert c['verdict']==('MET' if all(t['passed'] for t in c['trials']) else 'MISSED')
            for t in c['trials']:
                if n=='1':
                    assert len(t['cases'])==t['valid_count']==10
                    flags=[x['input_id'] for x in t['cases'] if x['response_json']['guess']=='ai']
                    assert flags==t['flagged_ids'] and t['passed']==(len(flags)<=1)
                elif n=='2':
                    assert len(t['cases'])==8 and t['passed']==(t['gap']>=0.20)
                elif n=='3':
                    assert t['actual_labels']==['ai','human','unsure']
                    assert t['score_sweep']['scores_checked']==10001 and not t['score_sweep']['failures']
                elif n=='4':
                    assert len(t['cases'])==10 and all(x['passed'] for x in t['cases'])
                    assert t['fresh_instance']['passed'] and not t['fresh_instance']['detector_loaded']
                    assert t['unknown_id']['status_code']==404
                    for x in t['cases']:assert len(x['history'])==2 and x['history'][0]==x['original'] and x['history'][1]['status']=='under_review'
                elif n=='5':
                    assert len(t['cases'])==37 and t['groups']==list(range(1,19))
                    assert t['successful_events_unchanged']
                    for x in t['cases']:
                        assert x['passed']==(x['expected_status']==x['http']['status_code'])
                        if not x['passed']:assert x['http']['status_code']==429
        assert [c['verdict'] for c in report['criteria'].values()]==['MET','MET','MET','MET','MISSED']
    checks['five_literal_criteria_have_three_actual_trials_before_and_after']=True
    checks['unmet_exact_status_target_is_retained_as_missed']=True
    log=[json.loads(line) for line in (ROOT/'logs/audit.jsonl').read_text().splitlines() if line.strip()]
    required={'timestamp','content_id','creator_id','guess','model_score','style_score','combined_score','label','status'}
    for event in log:
        if event.get('status')=='decided':
            assert required<=event.keys()
            for name in ('model_score','style_score','combined_score'):assert isinstance(event[name],(int,float)) and 0<=event[name]<=1
    extract=read('results/part2_audit_extract.json')
    assert len(extract)==12 and all(x in log for x in extract)
    assert sum(x.get('http_status')==429 for x in extract)==2
    checks['complete_decisions_and_twelve_real_pasted_audit_events']=True
    readme=(ROOT/'README.md').read_text()
    expected=['What This Does','Signals and Scoring','Label Variants','Sample Run','How I Used AI','Rate Limiting','Attack Run — Before','Run Log and Verdicts','The Improvement',"What's Still Broken"]
    assert re.findall(r'^## (.*)$',readme,re.M)==expected
    assert table(eb) in readme and table(ea) in readme
    before_section=readme.split('## Attack Run — Before')[1].split('## Run Log and Verdicts')[0]
    after_section=readme.split('### Attack Run — After')[1]
    for row in before['rows']:assert '| '+row['id']+' |' in before_section
    for row in after['rows']:assert '| '+row['id']+' |' in after_section
    pasted=re.findall(r'```json\n([\s\S]*?)\n```',before_section)
    assert any(json.loads(x)==extract for x in pasted)
    for block in re.findall(r'```json\n([\s\S]*?)\n```',readme):json.loads(block)
    checks['all_ten_readme_sections_tables_and_json_are_present']=True
    for path in [ROOT/'README.md',ROOT/'RUNNING.md',*(ROOT/'docs').glob('*.md'),ROOT/'SUBMISSION.md']:
        for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
            if '://' in target or target.startswith('#'):continue
            assert (path.parent/target.split('#')[0]).exists(),(str(path),target)
    checks['local_document_links_resolve']=True
    commits=int(subprocess.check_output(['git','rev-list','--count','b152891..HEAD'],cwd=ROOT,text=True))
    assert commits>=4
    checks['at_least_four_new_part2_commits']=True
    report={'recorded_at_utc':datetime.now(timezone.utc).isoformat(),'source_commit_at_audit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'new_commits_at_audit':commits,'checks':checks,'all_evidence_checks_passed':all(checks.values()),'criteria_verdicts':{label:{n:c['verdict'] for n,c in data['criteria'].items()} for label,data in [('before',eb),('after',ea)]},'attack_counts':{'before':before['counts'],'after':after['counts']},'audit_entry_count':len(log),'campaign_idle_seconds':campaign_idle_seconds,'portal_submission':'Performed by the user; repository URL is in SUBMISSION.md.'}
    (ROOT/'results/part2_submission_audit.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
