"""Mechanical table insertion and independent arithmetic checks for the report."""
import csv
import json
import math
from pathlib import Path

from valuation_model import BASELINE, FINAL, CORE, calculate, architecture, mdtable, YEARS

ROOT = Path(__file__).resolve().parent
REPORT = ROOT.parent.parent / 'Codex Deep Dive 2026-11-08.md'
ROWS = calculate()
FUNDING = {
 'TSM':{'NVDA':9,'AVGO':2},'ASML':{'AVGO':8},'AMAT':{'AVGO':2,'CLS':2},
 'SNPS':{'CLS':5},'ANET':{'CLS':4},'DELL':{'CLS':1,'NVT':1},'CEG':{'NRG':9},
 'PWR':{'NVT':4},'CRWD':{'NVT':3},'PLTR':{'NVT':2},'AVAV':{'NVT':1},'KTOS':{'NVT':1},
 'MRNA':{'NRG':1},'MP':{'NRG':2,'VST':1},'INTC':{'VST':3},'GEV':{'VST':1,'VRT':4},
 'CCJ':{'VRT':2},'BE':{'VRT':3},'MU':{'COHR':6}}

WHY = {
 'TSM':('Strategic foundry; 13.5% model CAGR loses capital competition.','Higher durable pricing/cash margins or lower price makes return superior.'),
 'NVDA':('24.5% model CAGR; scalable profits and substantial valuation reset.','Sustained margin erosion, unpaid receivables, major program substitution.'),
 'AVGO':('21.4% CAGR; custom silicon plus software cash at reduced multiple.','Anchor-customer loss, structurally sub-mid-40s common margin, leverage deterioration.'),
 'MU':('Peak-cycle cheapness is real but not durable enough; 13.0% CAGR.','HBM sustains high owner margins and cash beyond modeled normalization.'),
 'ASML':('Best lithography franchise, not best stock return; 8.6% CAGR.','Faster profitable shipments or lower price lifts return above selected names.'),
 'AMAT':('9.6% CAGR; LRCX is stronger tool alternative, both below final basket.','Higher process share/cash conversion supports materially higher owner value.'),
 'SNPS':('12.9% CAGR; acquisition/debt/dilution constrain attractive moat.','Integration produces stronger after-compensation cash with controlled shares.'),
 'ANET':('Operating success partly priced; 9.9% modeled CAGR.','Durable share gains and cash growth exceed 2030 assumptions.'),
 'VRT':('23.7% CAGR; improved earnings with sharply lower entry valuation.','Cancellations, weak book-to-bill and structural margin/cash deterioration.'),
 'DELL':('11.6% CAGR; CLS offers higher per-share upside with explicit risk caps.','Cash conversion and sustainable integration margins exceed model.'),
 'CEG':('12.7% CAGR; NRG/VST cheaper expected power cash flows.','Contracted nuclear/acquisition cash improves without offsetting liabilities.'),
 'VST':('20.3% CAGR; dispatchable generation and hedged cash bridge.','Outages, adverse rules or debt/integration undermine owner cash.'),
 'PWR':('10.9% CAGR; great backlog at a demanding earnings entry price.','Profitable backlog conversion and FCF support a superior return.'),
 'CRWD':('After-SBC valuation does not justify new capital despite strong growth.','Growth persists with much less dilution and much stronger owner FCF.'),
 'PLTR':('2.3% CAGR; excellent growth needs excessive future value at this price.','Durable common cash/margins substantially exceed modeled trajectory.'),
 'AVAV':('9.3% CAGR; procurement and integration do not justify token hedge.','Funded growth converts to cash with controlled dilution at attractive price.'),
 'KTOS':('Negative modeled CAGR; financing/cash burden outweighs autonomy story.','Sustained positive FCF and funded production scale beat the assumptions.'),
 'MRNA':('Rally rewards oncology, not reliable pandemic insurance; negative model CAGR.','Approved/commercialized oncology creates much higher sustainable owner cash.'),
 'MP':('8.5% CAGR; processing opportunity is not common-equity insurance.','Recurring magnet cash margins validate stronger independently economic returns.'),
 'INTC':('Development milestones do not offset foundry cash/dilution risk.','Competitive high-volume external foundry economics and FCF are verified.'),
 'GEV':('8.3% CAGR; strategic turbine scarcity already commands a premium.','Profitable deliveries and recurring cash exceed deposit-sensitive model.'),
 'CCJ':('3.4% CAGR; contract/production economics do not match scarcity premium.','Volumes and realized contract cash improve enough to beat power alternatives.'),
 'BE':('Negative modeled CAGR; growth/cash/financing demands exceed entry margin of safety.','Sustained unsubsidized owner cash and deployments exceed model with low dilution.'),
 'COHR':('19.1% CAGR; optical upside but cash demands cap weight at 8%.','Persistent negative operating cash, uncontrolled capex/debt or technology share loss.'),
 'CLS':('23.5% CAGR; low guided-earnings multiple with substantial system growth.','2027 guide fails, margins compress or dilution/working capital consume upside.'),
 'NVT':('23.7% CAGR; electrical distribution at better value than premium peers.','Organic orders/cash weaken or acquisition leverage defeats per-share growth.'),
 'NRG':('24.5% CAGR; inexpensive normalized earnings and customer/power economics.','New results cut cash outlook; integration/leverage or retail margins deteriorate.')}

THEMES = dict(NVDA='Accelerators/platform',AVGO='Custom silicon/networking/software',VRT='Power/thermal infrastructure',
 CLS='Systems/rack integration',NVT='Electrical distribution',NRG='Generation/retail',VST='Generation/retail',COHR='Optical components')

def triple(values, fmt='.1f', scale=1):
    return ' / '.join(format(x*scale,fmt) for x in values)

def check():
    assert len(ROWS)==56
    for name,weights in [('Current',BASELINE),('Concentrated',FINAL),('Core-satellite',CORE)]:
        assert sum(weights.values())==100 and max(weights.values())<=15
        assert set(weights)<=set(ROWS)
        a=architecture(weights,ROWS)
        assert math.isclose((1+a['expected_cagr'])**YEARS,1+a['expected_total_return'])
    assert set(FUNDING)==set(BASELINE)-set(FINAL)
    for source,dests in FUNDING.items():
        assert sum(dests.values())==BASELINE[source]
    for target,w in FINAL.items():
        assert sum(d.get(target,0) for d in FUNDING.values())==w-BASELINE.get(target,0)
    assert sum(sum(d.values()) for d in FUNDING.values())==77
    for row in ROWS.values():
        assert math.isclose(sum(row['probabilities']),1)
        expect=sum(p*v for p,v in zip(row['probabilities'],row['terminal_values']))
        assert math.isclose(expect,row['expected_terminal'])
        assert math.isclose((expect/row['price'])**(1/YEARS)-1,row['expected_cagr'])
    shock=dict(NVDA=-.50,AVGO=-.45,VRT=-.55,CLS=-.60,NVT=-.40,NRG=-.35,VST=-.40,COHR=-.60)
    assert math.isclose(sum(FINAL[t]/100*shock[t] for t in FINAL),-.479)

def make_tables():
    tables={}
    perf=list(csv.DictReader((ROOT/'accountability.csv').open(encoding='utf-8')))
    tables['PERFORMANCE_TABLE']=mdtable(['Ticker','May weight %','May 8 close $','Nov 6 close $','Price return %','Total return %','Contribution pp','Drift weight %'],
      [[p['ticker'],p['weight'],f"{float(p['may_close']):.2f}",f"{float(p['nov_close']):.2f}",f"{float(p['price_return']):+.2f}",f"{float(p['total_return']):+.2f}",f"{float(p['contribution_pp']):+.2f}",f"{float(p['drift_weight']):.2f}"] for p in perf])
    tables['MODEL_INPUT_TABLE']=mdtable(['Ticker / method','2030 revenue $bn B/B/B','Margin % B/B/B','Diluted shares bn B/B/B','Exit multiple B/B/B','Cumulative div $ B/B/B','Net claims $bn OR excess cash $/share B/B/B'],
      [[t+' / '+r['method'],triple(r['revenue'],'g'),triple(r['margin'],'.1f',100),triple(r['shares'],'.3f'),triple(r['multiple'],'g'),triple(r['dividends'],'g'),triple(r.get('net_claims',r.get('excess_cash_per_share',[0,0,0])),'g')] for t,r in ROWS.items()])
    tables['ALL_TERMINAL_TABLE']=mdtable(['Ticker','Nov 6 price $','2030 total wealth $ B/B/B','Probabilities % B/B/B','Expected wealth $','Expected total return %','Implied CAGR %','Status / confidence'],
      [[t,f"{r['price']:.2f}",triple(r['terminal_values'],'.0f'),triple(r['probabilities'],'.0f',100),f"{r['expected_terminal']:.1f}",f"{r['expected_total_return']*100:+.1f}",f"{r['expected_cagr']*100:.1f}",r['status']+' / '+str(r['confidence'])] for t,r in ROWS.items()])
    tables['ALL_TERMINAL_TABLE']+='\n**Scenario total returns (not annualized), including modeled distributions:**\n\n'+mdtable(['Ticker','Bear total return %','Base total return %','Bull total return %'],
      [[t]+[f'{v*100:+.1f}' for v in r['scenario_total_returns']] for t,r in ROWS.items()])
    fcf=[]
    for t,r in ROWS.items():
        if 'base_owner_fcf' in r:
            profit=r['revenue'][1]*r['margin'][1]
            note='Owner FCF is valuation basis' if r['method']=='Owner FCF' else 'Combined MRVL/LITE business; do not add twice' if t in ['MRVL','LITE'] else 'After normalized investment; not extra terminal cash'
            fcf.append([t,f'{profit:.2f}',f"{r['base_owner_fcf']:.2f}",f"{r['base_owner_fcf']/profit*100:.0f}%",note])
    tables['FCF_TABLE']=mdtable(['Ticker','Base common profit / owner FCF $bn','Base owner FCF $bn','Cash conversion','Interpretation'],fcf)
    # Scenario FCF extensions make explicit the cash feasibility of every earnings scenario.
    tables['FCF_TABLE']+='\nFor non-EV cases, the displayed base cash-conversion ratio is also the explicit bear/bull conversion assumption. Applying it to each scenario produces the following cash checks. No separate FCF multiple or incremental asset is added to the earnings valuation. Merger cases change perimeter; LITE base/bull represent the combined business, not standalone LITE.\n\n'
    fcf_cases=[]
    for t,r in ROWS.items():
        if 'base_owner_fcf' not in r: continue
        ratio=r['base_owner_fcf']/(r['revenue'][1]*r['margin'][1])
        vals=[rev*mar*ratio for rev,mar in zip(r['revenue'],r['margin'])]
        fcf_cases.append([t,triple(vals,'.2f')])
    tables['FCF_TABLE']+=mdtable(['Ticker','Bear / base / bull owner FCF $bn'],fcf_cases)
    assumptions={
     'NVDA':'$850bn base revenue; 46% common margin; 25x exit; 23.5bn shares',
     'AVGO':'$250bn base revenue; 50% common margin; 24x; 4.9bn shares',
     'VRT':'$30bn base revenue; 20% common margin; 26x; 0.380bn shares',
     'CLS':'$50bn base revenue; 7% common margin; 22x; 0.150bn shares',
     'NVT':'See full ledger: electrical growth, normalized margins and acquisition cash',
     'NRG':'$7bn base EBITDA; 8x; $14bn net claims; 0.200bn shares',
     'VST':'$11bn base EBITDA; 9x; $20bn net claims; 0.300bn shares',
     'COHR':'See full ledger: optical growth, dilution and positive normalized cash'}
    # Pull key assumptions directly from model rather than hand-maintaining figures.
    for t in FINAL:
        r=ROWS[t]
        if r['method']!='EV/EBITDA':
            assumptions[t]=f"Base revenue ${r['revenue'][1]:g}bn; margin {r['margin'][1]*100:g}%; {r['multiple'][1]:g}x; shares {r['shares'][1]:g}bn"
    tables['RECOMMENDED_VALUATION_TABLE']=mdtable(['Ticker','Current Price + Date','Valuation Status','Bear/Base/Bull Terminal Value','Scenario Probabilities','Expected Terminal Value','Implied Expected CAGR','Confidence','Key Assumptions'],
     [[t,f"${ROWS[t]['price']:.2f}; 2026-11-06",ROWS[t]['status'],'$ '+triple(ROWS[t]['terminal_values'],'.0f'),triple(ROWS[t]['probabilities'],'.0f',100)+'%',f"${ROWS[t]['expected_terminal']:.1f}",f"{ROWS[t]['expected_cagr']*100:.1f}%",str(ROWS[t]['confidence'])+'/5',assumptions[t]] for t in FINAL])
    names=list(dict.fromkeys(list(BASELINE)+list(FINAL)+list(CORE)))
    tables['ARCHITECTURE_WEIGHTS']=mdtable(['Ticker','Current %','Concentrated %','Core-and-satellite %'],[[t,BASELINE.get(t,0),FINAL.get(t,0),CORE.get(t,0)] for t in names]+[['TOTAL',100,100,100]])
    arches={n:architecture(w,ROWS) for n,w in [('Current diversified',BASELINE),('Concentrated — selected',FINAL),('Core-and-satellite',CORE)]}
    tables['ARCHITECTURE_RESULTS']=mdtable(['Architecture','Names','Expected total return %','Implied CAGR %','Bear/Base/Bull total return %','2.5-year delay return %','Top 3 %','HHI'],
      [[n,a['holdings'],f"{a['expected_total_return']*100:.1f}",f"{a['expected_cagr']*100:.1f}",triple(a['bear_base_bull_returns'],'.1f',100),f"{a['delay_return']*100:.1f}",a['top3'],f"{a['HHI']:.4f}"] for n,a in arches.items()])
    tables['FINAL_ALLOCATION_TABLE']=mdtable(['Ticker','Theme','EHF target %','Approx. total net investments %','Modeled CAGR %'],
      [[t,THEMES[t],f'{w:.1f}',f'{w/2:.1f}',f"{ROWS[t]['expected_cagr']*100:.1f}"] for t,w in FINAL.items()]+[['TOTAL','Eight common-stock positions','100.0','50.0','22.8 portfolio']])
    decisions=[]
    for t in list(BASELINE)+[t for t in FINAL if t not in BASELINE]:
        before=BASELINE.get(t,0); after=FINAL.get(t,0)
        action='Add' if before==0 else 'Remove' if after==0 else 'Increase' if after>before else 'Reduce' if after<before else 'Keep'
        # Confidence is confidence in the decision, not the operating forecast.
        conf=4 if t in ['TSM','NVDA','AVGO','VRT','CRWD','PLTR','MRNA','INTC','BE'] else 3
        decisions.append([t,f'{before:.1f}',f'{after:.1f}',f'{after-before:+.1f}',action,str(conf),*WHY[t]])
    tables['DECISION_TABLE']=mdtable(['Ticker','Current % / From','Recommended % / To','Delta pp','Action','Confidence (1–5)','Why','What would falsify this'],decisions)
    return tables

def main():
    check()
    content=REPORT.read_text(encoding='utf-8')
    tables=make_tables()
    for key,value in tables.items():
        start=f'<!-- BEGIN {key} -->'; end=f'<!-- END {key} -->'; marker=f'<!-- {key} -->'
        if marker in content:
            content=content.replace(marker,start+'\n'+value+'\n'+end)
        elif start in content:
            first,rest=content.split(start,1); _,last=rest.split(end,1)
            content=first+start+'\n'+value+'\n'+end+last
        else:
            raise AssertionError('Missing table slot '+key)
    content=content.replace('−48.3%', '−47.9%')
    REPORT.write_text(content,encoding='utf-8')
    report=dict(holdings=8,underwritten=56,allocation_sum=sum(FINAL.values()),funding_sales=77,funding_buys=77,
                probabilities_checked=56,capex_shock_pct=-47.9,top10_excluded=[t for t,r in sorted(ROWS.items(),key=lambda x:x[1]['expected_cagr'],reverse=True) if t not in BASELINE and t not in FINAL][:10])
    (ROOT/'arithmetic_verification.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))
    print('Report words:',len(content.split()))
    print('18% entry ceilings:',{t:round(ROWS[t]['expected_terminal']/1.18**YEARS,2) for t in FINAL})

if __name__=='__main__': main()
