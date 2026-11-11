"""Read-only consistency tests; writes only this review's validation artifact."""
import collections
import hashlib
import json
from pathlib import Path
import re

HERE=Path(__file__).resolve().parent
CYCLE=HERE.parents[2]
ROOT=CYCLE.parent
DATA=HERE/'data'
checks=[]
def check(name,test):
    checks.append({'check':name,'pass':bool(test)})
def read(p): return p.read_text(encoding='utf-8')
def rows(text):
    return [[x.strip().replace('**','') for x in line.strip('|').split('|')] for line in text.splitlines() if line.startswith('|')]
def section(text,start,end): return text.split(start,1)[1].split(end,1)[0]

d=json.loads(read(DATA/'step6_out.json'))
old=json.loads(read(HERE.parent/'claude_synthesis/data/step5_out.json'))
key='V10.2 final (adopted after Step 6)'
w=d['PORTS'][key]; p=d['PO'][key]
f=read(CYCLE/'Event Horizon Fund Analysis 2026-11-08.md')
dep=read(CYCLE/'Deployment Strategy/Deployment Strategy 2026-11-08.md')
rm=read(ROOT/'README.md')
log=read(CYCLE/'inputs/Step 6 Review Log 2026-11-08.md')
check('Baseline exact expected weights',w==dict(NVDA=15,META=15,VRT=14,MU=14,NRG=12,NVT=12,CLS=10,STRL=8))
check('100 percent and unchanged constraints',sum(w.values())==100 and max(w.values())<=15 and w['NRG']+w['STRL']==20 and p['clusters']['C1']<=50)
diff={k:p[k]-old['PO']['V10.1 final (adopted)'][k] for k in ['E','A27','G100','bust']}
check('Rule 2 lower branch passes',diff['E']>=.1 and diff['A27']>0 and diff['bust']>=-1)
check('Exact already-tested alternative',p==old['PO']['Alt: STRL 8 for VST (VRT/MU stay 14)'])
check('All held numeric inputs unchanged',all({k:v for k,v in d['R'][t].items() if k!='tag'}=={k:v for k,v in old['R'][t].items() if k!='tag'} for t in w))
check('Only WCC has changed numerical stock output',all({k:v for k,v in d['R'][t].items() if k!='tag'}=={k:v for k,v in old['R'][t].items() if k!='tag'} for t in old['R'] if t!='WCC'))
check('Frozen pool symbols and horizon',set(d['R'])==set(old['R']) and d['T']==old['T'])
pool_rows=rows(read(HERE/'tables6/pool6.md'))
check('Full/screen depth 29/31',sum('Full A1' in r for r in pool_rows)==29 and sum(any(x.startswith('Screen') for x in r) for r in pool_rows)==31)
for name,txt in [('final',f),('deployment',dep),('README',rm)]:
    check(name+' adopted V10.2', 'V10.2' in txt)
    check(name+' no template placeholders','@@' not in txt)
for name,txt in [('recon6',f),('pool6',f),('portfolios6',f),('trades6',dep)]:
    check(name+' generated table exact',read(HERE/'tables6'/f'{name}.md').strip() in txt)
# Destination heading is expanded to make STRL's stricter limit clear.
dst=read(HERE/'tables6/destination6.md').strip().splitlines()
check('destination6 generated body exact','\n'.join(dst[1:]) in dep)
for title,txt,tickercol,weightcol in [
    ('Part I',section(f,'### B. Allocation:','### C. The decisive'),1,4),
    ('Selection',section(f,'### Chosen','### Considered'),0,1),
    ('Part V.C',section(f,'### C. Cross-Portfolio Capital','### D. Three-Fund'),0,1),
    ('Part VI.A',section(f,'### A. Final Event Horizon','**Delta checksum:**'),1,3),
    ('Part VI.C',section(f,'### C. Per-Ticker','## Part VII'),0,2),
    ('Deployment',section(dep,'## 1. Destination','**STRL\'s buy limit'),0,1)]:
    got={r[tickercol]:int(r[weightcol].strip('%')) for r in rows(txt) if len(r)>weightcol and r[tickercol] in w}
    check(title+' weights equal model',got==w)
for t,weight in w.items(): check('README '+t, f'{t} ({weight}%)' in rm)
check('15 targeted questions retained',len(re.findall(r'^### Q\d+\)',f,re.M))==15)
check('All D1-D14 verdicts',len(re.findall(r'^\| D\d+ \|',log,re.M))==14)
check('Verdict counts 3/10/1',len(re.findall(r'\| \*\*Upheld\*\* \|',log))==3 and len(re.findall(r'\| \*\*Upheld with correction\*\* \|',log))==10 and len(re.findall(r'\| \*\*Overturned',log))==1)
check('31 fixed findings',len(re.findall(r'^\| F\d+.*\*\*Fixed:',log,re.M))==31)
check('No unfinished log inserts','@@' not in log)
check('Core/satellite and clusters','82%' in f and '18%' in f and p['clusters']=={'C1':39,'C3':34,'C4':12,'C5':15})
for label,k in [('AI-2027 path','A27'),('100GW 2030 path','G100')]:
    total=((1+p[k]/100)**d['T']-1)*100
    expected=f'**+{total:.0f}% ({p[k]:.1f}%/yr)**'
    row=next(line for line in f.splitlines() if line.startswith('| **'+label+'**'))
    check(label+' total return/CAGR',expected in row)
valuation=rows(section(f,'### IV.D Forward-Return','**Detailed assumptions'))
for row in valuation:
    if row[0] not in w: continue
    r=d['R'][row[0]]
    check(row[0]+' published return triplet',row[6:9]==[f'{r[k]:.1f}%' for k in ['E','A27','G100']])
for row in rows(section(f,'### Chosen','### Considered')):
    if row[0] not in w: continue
    r=d['R'][row[0]]
    check(row[0]+' selection return triplet',row[3:6]==[f'{r[k]:.1f}%' for k in ['E','A27','G100']])
for name in [k for k in d['PORTS'] if k.startswith('V10.2')]:
    v=d['PORTS'][name]
    check(name+' conditional caps',sum(v.values())==100 and max(v.values())<=15 and v.get('NRG',0)+v.get('STRL',0)<=20 and v.get('NVT',0)<=12 and v.get('CLS',0)<=10)
ledger=json.loads(read(DATA/'tranche_ledger.json'))
cash=json.loads(read(DATA/'cash_path.json'))
check('Cash path nonnegative and zero final',min(r[3] for r in cash)>=0 and cash[-1][3]==0)
check('No pre-earnings NVDA buy',not ledger['buys']['NVDA'].get('T1',0) and not ledger['buys']['NVDA'].get('T2',0))
protected=json.loads(read(DATA/'protected_records.json'))
bad=[k for k,v in protected.items() if hashlib.sha256((CYCLE/'inputs'/k).read_bytes()).hexdigest()!=v]
check('All protected records unchanged',not bad)
check('Eight-artifact exact reproduction',all(v['byte_identical'] for v in json.loads(read(DATA/'reproduction.json'))['checks']))
check('Quotes no missing or over10pct',all('error' not in v and abs(v['change_percent'])<=10 for v in json.loads(read(DATA/'quote_audit.json')).values()))
for fn in ['Event Horizon Fund Analysis 2026-11-08 (V10.1 before Step 6)','Deployment Strategy/Deployment Strategy 2026-11-08 (V10.1 before Step 6)']:
    for ext in ['md','pdf']: check('Backup '+fn+'.'+ext,(CYCLE/'inputs/superseded'/f'{fn}.{ext}').exists())
result={'checks':checks,'protected_count':len(protected),'protected_changes':bad,'passed':all(v['pass'] for v in checks)}
(DATA/'validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
raise SystemExit(0 if result['passed'] else 1)
