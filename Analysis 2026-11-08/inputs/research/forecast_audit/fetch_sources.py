"""Archive public forecast sources and extract readable text/link inventories."""
import concurrent.futures
import datetime
import json
import os
import sys
import urllib.request
from pathlib import Path
from sanitize_snapshots import redact_mapbox_tokens

sys.path.insert(0,str(Path(os.environ.get('TEMP','C:/Temp'))/'ehf_report_deps_20261108'))
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parent
SOURCES={
 'race':'https://ai-2027.com/race',
 'summary':'https://ai-2027.com/summary',
 'compute':'https://ai-2027.com/research/compute-forecast',
 'timelines':'https://ai-2027.com/research/timelines-forecast',
 'takeoff':'https://ai-2027.com/research/takeoff-forecast',
 'goals':'https://ai-2027.com/research/ai-goals-forecast',
 'security':'https://ai-2027.com/research/security-forecast',
 'plan_a':'https://ai-2040.com/',
 'plan_a_compute':'https://ai-2040.com/supplements/compute-supplement',
 'plan_a_economics':'https://ai-2040.com/supplements/economics-of-plan-a',
 'trillion_cluster':'https://situational-awareness.ai/racing-to-the-trillion-dollar-cluster/',
 'timelines_update':'https://blog.aifutures.org/p/q1-2026-timelines-update',
 'old_track_record':'https://www.lesswrong.com/posts/u9Kr97di29CkMvjaj/evaluating-what-2026-looks-like-so-far',
 'software_explosion':'https://www.forethought.org/research/will-ai-r-and-d-automation-cause-a-software-intelligence-explosion',
 'model_app':'https://www.aifuturesmodel.com/',
 'scorecard':'https://blog.aifutures.org/p/grading-ai-2027s-2025-predictions',
 'forecast_history':'https://blog.aifutures.org/p/clarifying-how-our-ai-timelines-forecasts',
 'metr_11':'https://metr.org/blog/2026-01-29-time-horizon-1-1/',
 'metr_live':'https://metr.org/time-horizons/',
 'epoch_companies':'https://epoch.ai/data/ai-companies',
 'epoch_revenue_csv':'https://epoch.ai/data/ai_companies_revenue_reports.csv',
 'epoch_compute_csv':'https://epoch.ai/data/ai_companies_compute_spend.csv',
 'august_update':'https://blog.aifutures.org/p/q25-2026-timelines-update-uplift',
 'august_forecast_table':'https://datawrapper.dwcdn.net/4aHow/2/',
 'metr_uplift_update':'https://metr.org/blog/2026-02-24-uplift-update/',
 'plan_a_full':'https://ai-2040.com/?choices=plan-a-root',
 'epoch_chip_sales':'https://epoch.ai/data/ai-chip-sales',
 'epoch_chip_types_csv':'https://epoch.ai/data/ai_chip_sales_chip_types.csv',
 'epoch_chip_timelines_csv':'https://epoch.ai/data/ai_chip_sales_timelines_by_chip.csv',
 'august_table_csv':'https://datawrapper.dwcdn.net/4aHow/2/dataset.csv',
 'metr_data':'https://metr.org/assets/benchmark_results_1_1.yaml',
 'metr_survey':'https://metr.org/blog/2026-05-11-ai-usage-survey/',
 'plan_a_pdf':'https://ai-2040.com/AI-2040.pdf',
 'micron_2024_anchor':'https://micron.gcs-web.com/static-files/21b50828-dd30-429f-9502-b1ebc452c6e3',
 'micron_q4_2026':'https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf',
 'asml_2025':'https://www.asml.com/investors/annual-report/2025',
 'asml_q3_2026':'https://investor.asml.com/news-releases/news-release-details/asml-reports-eu11.7-billion-total-net-sales-and-eu5.0-billion-net-income-q3-2026',
 'model_about':'https://www.aifuturesmodel.com/about',
}

def fetch(item):
    name,url=item
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (public research archive)'})
        with urllib.request.urlopen(request,timeout=45) as response:
            raw=response.read(); final=response.url
            content_type=response.headers.get('Content-Type','')
        if url.endswith('.pdf') or 'application/pdf' in content_type or raw.startswith(b'%PDF-'):
            from pypdf import PdfReader
            from io import BytesIO
            (ROOT/(name+'.pdf')).write_bytes(raw)
            pages=PdfReader(BytesIO(raw)).pages
            (ROOT/(name+'.txt')).write_text('\n'.join(p.extract_text() for p in pages),encoding='utf-8')
            return dict(name=name,url=url,final_url=final,bytes=len(raw),pages=len(pages),retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
        response_bytes=len(raw)
        raw,token_redactions=redact_mapbox_tokens(raw)
        (ROOT/(name+'.html')).write_bytes(raw)
        soup=BeautifulSoup(raw,'html.parser')
        links=[dict(text=a.get_text(' ',strip=True),url=a.get('href')) for a in soup.find_all('a',href=True)]
        for tag in soup(['script','style','nav','noscript']): tag.decompose()
        body=soup.find('main') or soup.find('article') or soup.body or soup
        lines=[x.strip() for x in body.get_text('\n',strip=True).splitlines() if x.strip()]
        (ROOT/(name+'.txt')).write_text('\n'.join(lines),encoding='utf-8')
        (ROOT/(name+'_links.json')).write_text(json.dumps(links,indent=2),encoding='utf-8')
        return dict(name=name,url=url,final_url=final,bytes=response_bytes,archived_bytes=len(raw),embedded_token_redactions=token_redactions,text_characters=sum(map(len,lines)),lines=len(lines),links=len(links),retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    except Exception as exc: return dict(name=name,url=url,error=str(exc))

if __name__=='__main__':
    selected={k:v for k,v in SOURCES.items() if not sys.argv[1:] or k in sys.argv[1:]}
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(fetch,selected.items()))
    manifest=ROOT/'source_manifest.json'
    previous=json.loads(manifest.read_text(encoding='utf-8')) if manifest.exists() else []
    combined=[r for r in previous if r['name'] not in selected]+results
    manifest.write_text(json.dumps(combined,indent=2),encoding='utf-8')
    print(json.dumps(results,indent=2))
