#!/usr/bin/env python3
"""Check bilingual editorial invariants. Copyright 2026 @ykbballer91. MIT.

This checks publication structure and preserved scope, not mathematical proofs.
"""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import urlsplit, unquote
from build_site import ROOT, legacy_anchors, render_markdown
from site_routes import LANGUAGES, NAV, editorial_info, legacy_info, route, source_for, url_for

class Document(HTMLParser):
    def __init__(self):
        super().__init__();self.lang=None;self.metadata=[];self.links=[];self.ids=[];self.main=False;self.text=[];self.redirect=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html':self.lang=a.get('lang')
        if tag=='link':self.metadata.append(a)
        if tag=='a':self.links.append(a)
        if a.get('id'):self.ids.append(a['id'])
        if tag=='main':self.main=True
        if tag=='meta' and a.get('http-equiv')=='refresh':self.redirect=True
    def handle_endtag(self,tag):
        if tag=='main':self.main=False
    def handle_data(self,text):
        if self.main:self.text.append(text)

def load(p):
    d=Document();d.feed(p.read_text());return d

def check():
    errors=[];site=ROOT/'_site'
    sources={lc:{p.relative_to(ROOT/'docs'/lc).with_suffix('').as_posix() for p in (ROOT/'docs'/lc).rglob('*.md')} for lc in LANGUAGES}
    if sources['ja'] != sources['en']:errors.append('Unpaired editorial source')
    if len(sources['en'])!=33:errors.append('Expected 33 editorial page pairs')
    def require(ok,msg):
        if not ok:errors.append(msg)
    for lc in LANGUAGES:
        for key in sorted(sources[lc]):
            path=site/route(lc,key)
            if not path.is_file():errors.append(f'Missing route {lc}/{key}');continue
            d=load(path);body=' '.join(d.text)
            require(d.lang==lc,f'Wrong html lang: {lc}/{key}')
            require('STATUS: RIEMANN HYPOTHESIS OPEN' in path.read_text(),f'No OPEN status: {lc}/{key}')
            require(any(x.get('rel')=='canonical' and x.get('href')==url_for(route(lc,key)) for x in d.metadata),f'Canonical mismatch: {lc}/{key}')
            for other in LANGUAGES:
                target=site/route(other,key)
                require(any(x.get('rel')=='alternate' and x.get('hreflang')==other and x.get('href')==url_for(route(other,key)) for x in d.metadata),f'hreflang mismatch: {lc}/{key}/{other}')
                switches=[x for x in d.links if x.get('lang')==other and x.get('hreflang')==other]
                require(len(switches)==1 and (path.parent/unquote(urlsplit(switches[0]['href']).path)).resolve()==target.resolve(),f'Page pair switch mismatch: {lc}/{key}/{other}')
            for label,navkey in NAV[lc]:
                require(any((path.parent/unquote(urlsplit(x.get('href','')).path)).resolve()==(site/route(lc,navkey)).resolve() for x in d.links if not urlsplit(x.get('href','')).scheme),f'Navigation absent: {lc}/{key}/{navkey}')
            require(len(d.ids)==len(set(d.ids)),f'Duplicate heading IDs: {lc}/{key}')
            if lc=='en':require(not re.search(r'[ぁ-んァ-ン一-龥]',body),f'Japanese prose in English main: {key}')
            snapshot=ROOT/'archive/editorial/pre-bilingual-2026-10-01'
            old=snapshot/'README.md' if key=='home' else snapshot/'docs'/(key+'.md')
            if old.is_file():
                oldids=set(re.findall(r'\bid="([^"]+)"',render_markdown(old.read_text())))
                require(oldids.issubset(set(d.ids)),f'Legacy heading lost: {lc}/{key}')
    legacy_count=0
    for p in [ROOT/'README.md',ROOT/'README.ja.md',*(ROOT/'docs').glob('*.md'),*(ROOT/'docs/tracks').glob('*.md'),*(ROOT/'docs/updates').glob('*.md')]:
        rel=p.relative_to(ROOT);info=legacy_info(rel);dest=site/rel.with_suffix('.html');legacy_count+=1
        if not dest.is_file():errors.append('Missing compatibility '+str(rel));continue
        d=load(dest);require(d.redirect,'No compatibility redirect: '+str(rel))
        require(any(x.get('rel')=='canonical' and x.get('href')==url_for(route(*info)) for x in d.metadata),'Wrong legacy target: '+str(rel))
    require(load(site/'index.html').redirect,'Root does not redirect')
    # The current research update is frozen; compare the displayed formulas and scope in both languages.
    formula_sets=[]
    for lc in LANGUAGES:
        src=(ROOT/source_for(lc,'updates/2026-10-01-cmp-es')).read_text()
        formula_sets.append([re.sub(r'\s+','',x).rstrip('.') for x in re.findall(r'\$\$(.*?)\$\$',src,re.S)])
        for marker in ['CASE D — CMP OPEN + ES OPEN','19','12','**0**','CMP-R','N=4','13','0<r<1/2','EVEN FULL-GROUND CAPTURE: NOT ESTABLISHED.']:
            require(marker in src,f'Missing update scope marker: {lc}: {marker}')
        overview=(ROOT/source_for(lc,'current-state')).read_text()
        require('CASE D — CMP OPEN + ES OPEN' in overview,'Current-state status drift: '+lc)
    require(formula_sets[0]==formula_sets[1],'Paired update display formulas differ')
    joint_formulas=[]
    for lc in LANGUAGES:
        src=(ROOT/source_for(lc,'updates/2026-10-05-joint-transfer')).read_text()
        joint_formulas.append([re.sub(r'\s+','',x) for x in re.findall(r'\$\$(.*?)\$\$',src,re.S)])
        for marker in ['2026-10-05','CASE D — CMP OPEN + ES OPEN','19','12','**0**','CMP-R','i/4','Clunie','1.3','5.10','EVEN FULL-GROUND CAPTURE: NOT ESTABLISHED.']:
            require(marker in src,f'Missing joint-update scope: {lc}: {marker}')
        for key in ['home','index','current-state','roadmap','timeline','source-map']:
            require('2026-10-05-joint-transfer.md' in (ROOT/source_for(lc,key)).read_text(),f'Latest update not reachable from {lc}/{key}')
    require(joint_formulas[0]==joint_formulas[1],'Joint-transfer display formulas differ')
    current=json.loads((ROOT/'data/current-state-2026-10-05.json').read_text())
    require(current['rh_status']==current['CMP']==current['ES']=='OPEN','Latest status drift')
    require(current['conditional_joint_transfer']=='ACCEPTED_CONDITIONAL_ONLY','Joint implication scope drift')
    for key in ['rh_closed','full_even_ground_capture_proved','actual_strong_L2_capture_proved','actual_eventual_ES_proved','same_cofinal_sequence_established','ordinary_L2_alone_suffices','source_bundle_published','new_research_automatically_started']:
        require(current[key] is False,'Unexpected proved/action flag: '+key)
    require(current['new_actual_asymptotic_obligations_discharged']==0,'Actual asymptotic count drift')
    require(current['old_ES_independent_CMP_R_preserved'] is True,'Old sufficient route lost')
    readme=(ROOT/'README.md').read_text();readme_without_switch='\n'.join(line for line in readme.splitlines() if '日本語版はこちら' not in line)
    require(not re.search(r'[ぁ-んァ-ン一-龥]',readme_without_switch),'Japanese body text in canonical README')
    state=json.loads((ROOT/'data/research-state.json').read_text())
    require(state['rh_status']=='OPEN' and state['latest_update']['CMP']['status']=='OPEN' and state['latest_update']['ES']['status']=='OPEN','Research state changed')
    require(state['latest_update']['import_audit']['generic_or_fixed_scope_items_delegated']==12 and state['latest_update']['import_audit']['new_actual_moving_weil_asymptotic_obligations_discharged']==0,'Import count changed')
    return {'status':'FAIL' if errors else 'PASS','scope':'Editorial routing, language metadata, preserved scope and formula consistency; no mathematical verification','paired_pages':len(sources['en']),'canonical_language_pages':sum(map(len,sources.values())),'compatibility_pages_including_root':legacy_count+1,'errors':errors}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--report',type=Path);a=p.parse_args();result=check()
    if a.report:
        existing=json.loads(a.report.read_text()) if a.report.exists() else {}
        existing['bilingual_checks']=result
        a.report.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(result['status']!='PASS')
