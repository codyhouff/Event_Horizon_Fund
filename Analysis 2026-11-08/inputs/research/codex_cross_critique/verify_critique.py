"""Independent arithmetic, source transcription, report and optional PDF checks.

Reads only the two original deep dives, never the other model's Step 2 critique.
Writes verification artifacts only inside this critique's research directory.
"""
import datetime as dt
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
REPORT=ROOT.parent.parent/'Codex Critique of Claude 2026-11-08.md'
REPO=ROOT.parents[3]

def same(a,b):
    assert math.isclose(a,b,rel_tol=1e-11,abs_tol=1e-11),(a,b)

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def block(source,name):
    return re.search(r'<!-- BEGIN '+name+r' -->\n(.*?)\n<!-- END '+name+r' -->',source,re.S).group(1)

def rows(body):
    return [[c.strip() for c in line.strip('|').split('|')] for line in body.splitlines()[2:] if line.startswith('|')]

def pdf_check():
    path=REPORT.with_suffix('.pdf')
    if not path.exists(): return {'status':'NOT RENDERED; optional'}
    deps=Path(os.environ.get('EHF_REPORT_DEPS',str(Path(os.environ.get('TEMP','C:/Temp'))/'ehf_report_deps_20261108')))
    sys.path.insert(0,str(deps))
    import pymupdf
    doc=pymupdf.open(path)
    texts=[p.get_text() for p in doc]
    outside=[]
    for i,p in enumerate(doc):
        if len(texts[i].strip())<=80:
            p.get_pixmap(matrix=pymupdf.Matrix(1.3,1.3)).save(str(ROOT/f'preview_short_{i+1:02d}.png'))
            print('Short page:',i+1,repr(texts[i]))
        assert len(texts[i].strip())>80,('nearly empty PDF page',i+1)
        for b in p.get_text('blocks'):
            if b[0]<-1 or b[1]<-1 or b[2]>p.rect.width+1 or b[3]>p.rect.height+1:
                outside.append((i+1,list(b[:4])))
    assert not outside,outside
    joined=' '.join(' '.join(texts).split())
    for label in ['H01 NVDA','H20 VRSK','S01 Electrical','F01','F20','100.0%','17.9%','57.9%']:
        assert label in joined,label
    previews={0}
    for label in ['H01 NVDA','AI-2027 operating bridge','F01','Delta pp','Assumption change']:
        found=[i for i,t in enumerate(texts) if label in ' '.join(t.split())]
        if found: previews.add(found[0])
    for i in sorted(previews):
        doc[i].get_pixmap(matrix=pymupdf.Matrix(1.3,1.3)).save(str(ROOT/f'preview_{i+1:02d}.png'))
    return dict(status='PASS',pages=len(doc),characters=len(joined),
                links=sum(len(p.get_links()) for p in doc),outside_page_bounds=outside,
                preview_pages=[i+1 for i in sorted(previews)],sha256=digest(path))

def main():
    d=json.loads((ROOT/'critique_results.json').read_text(encoding='utf-8'))
    quote_list=json.loads((ROOT/'quotes.json').read_text(encoding='utf-8'))
    quotes={q['ticker']:q for q in quote_list}
    source=REPORT.read_text(encoding='utf-8')
    assert re.findall(r'^## (\d+)\.',source,re.M)==list('1234567')
    assert len(re.findall(r'^- ',source.split('## 2.')[0],re.M))<=10
    assert '\ufffd' not in source and 'TODO' not in source
    assert not re.search(r'turn\d+(?:search|view|fetch)\d+',source)
    assert len(re.findall(r'<!-- BEGIN ',source))==10
    for name in re.findall(r'<!-- BEGIN (\w+) -->',source):
        assert len(block(source,name).strip())>50,name
    disputed={t for t in set(d['original_weights'])|set(d['claude_weights'])
              if abs(d['original_weights'].get(t,0)-d['claude_weights'].get(t,0))>=1}
    assert disputed==set(d['contested']) and len(disputed)==19
    head=rows(block(source,'HEAD'))
    assert len(head)==20
    assert {r[0].split()[1] for r in head}==disputed|{'VRSK'}
    assert all(len(r)==10 and '2026-11-09' in r[3] for r in head)
    for name in ['OUTCOMES','NAMED']:
        assert {r[0] for r in rows(block(source,name))}==set(d['stocks'])
        assert len(rows(block(source,name)))==25
    assert {r[0] for r in rows(block(source,'UNIQUE'))}=={'SNDK','RELX','VRSK','MSI','GEN'}
    years=(dt.date(2030,12,31)-dt.date(2026,11,9)).days/365.25
    same(years,d['years'])
    for t,r in d['stocks'].items():
        q=quotes[t]
        assert q['date']=='2026-11-09' and q['currency']=='USD'
        same(r['price'],q['close'])
        assert (ROOT/f'{t}_chart.json').exists()
        a=r['inputs'];same(sum(a['probabilities']),1)
        if a['method']=='earnings':
            wealth=[max(0,R*M/S*K+C)+D for R,M,S,K,D,C in zip(a['revenue'],a['margin'],a['shares'],a['multiple'],a['dividends'],a['cash'])]
        elif a['method']=='ev':
            wealth=[max(0,E*K-N)/S+D for E,K,N,S,D in zip(a['ebitda'],a['multiple'],a['debt'],a['shares'],a['dividends'])]
        else:
            wealth=[(C+P)/S for C,P,S in zip(a['net_cash_bn'],a['pipeline_bn'],a['shares'])]
        for x,y in zip(wealth,r['new_values']): same(x,y)
        expected=sum(w*p for w,p in zip(wealth,a['probabilities']))
        same(expected,r['new_expected'])
        same((expected/r['price'])**(1/years)-1,r['new_cagr'])
        for i,x in enumerate(r['named_inputs']):
            if a['method']=='earnings': w=max(0,x[0]*x[1]/x[2]*x[3]+x[5])+x[4]
            elif a['method']=='ev': w=max(0,x[0]*x[1]-x[2])/x[3]+x[4]
            else: w=(x[0]+x[1])/x[2]
            same(w,r['new_named'][i])
            same((w/r['price'])**(1/years)-1,r['new_named_cagr'][i])
        for recon in r['reconstructions'].values():
            assert len(recon)==2 and all(v>0 and len(kind)>5 for v,kind in recon)
    # Verify every hand-transcribed original Claude endpoint and probability
    # directly against the original valuation tables, not against a second copy.
    import critique_model as m
    other_path=ROOT.parent.parent/'Claude Deep Dive 2026-11-08.md'
    other=other_path.read_text(encoding='utf-8')
    original_rows={}
    for line in other.splitlines():
        if not line.startswith('|'): continue
        cells=[c.strip() for c in line.strip('|').split('|')]
        if len(cells)<5 or cells[0] not in m.CLAUDE: continue
        if not cells[1].startswith('$') or '/' not in cells[3]: continue
        terminal=[float(x.replace('$','').replace(',','').strip()) for x in cells[3].split('/')]
        probs=[float(x.strip())/100 for x in cells[4].split('/')]
        original_rows[cells[0]]=(terminal,probs)
    assert set(original_rows)==set(m.CLAUDE)
    for t,(wealth,p,*rest) in m.CLAUDE.items():
        assert original_rows[t]==(wealth,p),(t,original_rows[t],wealth,p)
    orig=d['original_weights'];rev=d['revised_weights']
    assert sum(orig.values())==sum(rev.values())==100 and max(rev.values())<=15
    changes={t:rev.get(t,0)-orig.get(t,0) for t in set(orig)|set(rev) if rev.get(t,0)!=orig.get(t,0)}
    assert changes=={'AVGO':-15,'COHR':-8,'VRSK':15,'MU':8}
    assert sum(changes.values())==0
    allocation=rows(block(source,'ALLOCATION'))
    assert allocation[-1][0]=='TOTAL'
    for row in allocation[:-1]:
        t=row[0]
        same(float(row[1]),orig.get(t,0));same(float(row[2]),rev.get(t,0))
        if t in changes: assert re.search(r'H\d{2}',row[4]),row
    for label,weights in [('Codex original, new underwriting',orig),('Codex revised',rev),('Claude weights, new underwriting',d['claude_weights'])]:
        p=d['portfolios'][label]
        ew=sum(w/100*d['stocks'][t]['new_expected']/quotes[t]['close'] for t,w in weights.items())
        same(ew-1,p['expected_total_return']);same(ew**(1/years)-1,p['expected_cagr'])
        for i,key in enumerate(['ai_cagr','gw_cagr']):
            w=sum(v/100*d['stocks'][t]['new_named'][i]/quotes[t]['close'] for t,v in weights.items())
            same(w**(1/years)-1,p[key])
        bust=sum(v/100*d['stocks'][t]['new_values'][0]/quotes[t]['close'] for t,v in weights.items())-1
        same(bust,p['bust_return'])
    # A common split must leave total return unchanged.
    s=d['stocks']['SNDK']
    same((s['new_expected']/8/(s['price']/8))**(1/years)-1,s['new_cagr'])
    originals=[ROOT.parent.parent/f'{model} Deep Dive 2026-11-08.md' for model in ['Codex','Claude']]
    relative=[p.relative_to(REPO).as_posix() for p in originals]
    git=subprocess.run(['git','diff','--exit-code','HEAD','--',*relative],cwd=REPO,capture_output=True,text=True)
    assert git.returncode==0,git.stdout+git.stderr
    urls=sorted(set(re.findall(r'\]\((https?://[^)]+)\)',source)))
    result=dict(status='PASS',report_sha256=digest(REPORT),report_words=len(source.split()),
                sections=7,verdict_bullets=len(re.findall(r'^- ',source.split('## 2.')[0],re.M)),
                required_head_to_heads=19,additional_head_to_heads=1,fully_modeled_names=25,
                generated_blocks=10,original_Claude_models_transcription_checked=len(original_rows),
                quote_date='2026-11-09',allocation_checksum=100,changed_weights=changes,
                original_deep_dives_unchanged_from_HEAD=True,
                original_sha256={p.name:digest(p) for p in originals},
                source_urls=len(urls),pdf=pdf_check())
    (ROOT/'source_links.json').write_text(json.dumps(urls,indent=2),encoding='utf-8')
    (ROOT/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
