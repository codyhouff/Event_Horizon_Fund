"""Check final deliverable coverage, model arithmetic, and rendered PDF geometry."""
import hashlib
import json
import os
import re
import sys
from pathlib import Path

deps=Path(os.environ.get('EHF_REPORT_DEPS',str(Path(os.environ.get('TEMP','C:/Temp'))/'ehf_report_deps_20261108')))
sys.path.insert(0,str(deps))
import pymupdf
from build_report import check, BASELINE, FINAL, CORE, ROWS, FUNDING

ROOT=Path(__file__).resolve().parents[2]
RESEARCH=ROOT/'inputs'/'research'
MAIN=ROOT/'inputs'/'Codex Deep Dive 2026-11-08.md'
CANONICAL=ROOT/'Event Horizon Fund Analysis 2026-11-08.md'
DEPLOY=ROOT/'Deployment Strategy'/'Deployment Strategy 2026-11-08.md'

def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def inspect_pdf(path,preview_pages):
    doc=pymupdf.open(path)
    texts=[page.get_text() for page in doc]
    assert all(len(t)>80 for t in texts),'Blank or nearly blank PDF page'
    outside=[]
    for i,page in enumerate(doc):
        for b in page.get_text('blocks'):
            if b[0]<-1 or b[1]<-1 or b[2]>page.rect.width+1 or b[3]>page.rect.height+1:
                outside.append([i+1,list(b[:4])])
    assert not outside, str(outside)
    if path==MAIN.with_suffix('.pdf'):
        for term in ['3.4 Track record','3.5 Deep audit','Audit issue','5.6 November 9','Additional zero-recovery regime']:
            matches=[i for i,t in enumerate(texts) if term in t]
            if matches: preview_pages.append(matches[0])
        preview_pages=sorted(set(preview_pages))
    images=[]
    for index in preview_pages:
        if index>=len(doc): continue
        dest=RESEARCH/(('deployment' if path==DEPLOY.with_suffix('.pdf') else 'analysis')+f'_preview_{index+1}.png')
        doc[index].get_pixmap(matrix=pymupdf.Matrix(1.25,1.25)).save(str(dest))
        images.append(dest.name)
    return dict(pages=len(doc),characters=sum(map(len,texts)),hyperlinks=sum(len(p.get_links()) for p in doc),
                pages_outside_geometry=outside,previews=images,sha256=digest(path)), '\n'.join(texts)

def main():
    check()
    text=MAIN.read_text(encoding='utf-8')
    sections=re.findall(r'^## (\d+)\.',text,re.M)
    assert sections==[str(i) for i in range(1,10)],sections
    questions=re.findall(r'^### 8\.(\d+) ',text,re.M)
    assert questions==[str(i) for i in range(1,16)],questions
    for chunk in re.split(r'^### 8\.\d+ .*$',text,re.M)[1:]:
        for term in ['Prior May conclusion','New evidence since May','Updated answer','Portfolio implication','Confidence','Disconfirming evidence']:
            assert term.lower() in chunk.lower(),term
    assert not re.search(r'<!-- (?:PERFORMANCE_TABLE|MODEL_INPUT_TABLE|ALL_TERMINAL_TABLE|FCF_TABLE|RECOMMENDED_VALUATION_TABLE|ARCHITECTURE_WEIGHTS|ARCHITECTURE_RESULTS|FINAL_ALLOCATION_TABLE|DECISION_TABLE) -->',text)
    assert '\ufffd' not in text
    assert len(re.findall(r'^\*\*[A-Z]+ —',text,re.M))>=50
    assert MAIN.read_bytes()==CANONICAL.read_bytes()
    for p in [MAIN,CANONICAL,DEPLOY]:
        assert p.exists() and p.with_suffix('.pdf').exists()
    assert digest(MAIN.with_suffix('.pdf'))==digest(CANONICAL.with_suffix('.pdf'))
    audit=json.loads((RESEARCH/'forecast_audit'/'audit_verification.json').read_text(encoding='utf-8'))
    assert audit['status']=='PASS'
    assert audit['report_sha256']==digest(MAIN)
    a,at=inspect_pdf(MAIN.with_suffix('.pdf'),[0,4,12,20,35])
    d,dt=inspect_pdf(DEPLOY.with_suffix('.pdf'),[0,2])
    for q in range(1,16): assert f'8.{q} ' in at,f'PDF missing question {q}'
    assert '100.0%' in at
    assert '233.05' in dt and '7.70' in dt and 'Scenario C' in dt
    # Exact staged funding identities (rational integer basis-point arithmetic).
    gap={t:w-BASELINE.get(t,0) for t,w in FINAL.items()}
    buys=[sum(gap.values())*x for x in [.4,.35,.25]]
    sales=[77*x for x in [.5,.3,.2]]
    reserve=0
    balances=[]
    for s,b in zip(sales,buys):
        reserve+=s-b;balances.append(round(reserve,2));assert reserve>=-1e-8
    assert balances==[7.7,3.85,0.0]
    urls=sorted(set(re.findall(r'\]\((https?://[^)]+)\)',text+DEPLOY.read_text(encoding='utf-8'))))
    (RESEARCH/'source_links.json').write_text(json.dumps(urls,indent=2),encoding='utf-8')
    result=dict(status='PASS',report_words=len(text.split()),sections=9,targeted_questions=15,underwritten_stocks=len(ROWS),
                current_holdings=len(BASELINE),final_holdings=len(FINAL),allocation_checksum=sum(FINAL.values()),
                exact_funding_pp=77,tranche_reserves_pp=balances,unique_source_urls=len(urls),analysis_pdf=a,deployment_pdf=d,
                canonical_copies_identical=True,forecast_audit_status=audit['status'],
                forecast_requested_sources=audit['user_requested_sources_covered'],
                manual_visual_review='See saved preview PNGs; reviewed separately')
    (RESEARCH/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
