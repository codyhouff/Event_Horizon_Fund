"""Mechanical insertion of generated numerical tables into marked report blocks."""
import json
import re
from pathlib import Path
import critique_model as m

ROOT=Path(__file__).resolve().parent
REPORT=ROOT.parent.parent/'Codex Critique of Claude 2026-11-08.md'
D=json.loads((ROOT/'critique_results.json').read_text())
R=D['stocks']

def pct(x): return 'NR' if x is None else f'{100*x:.1f}%'
def num(x): return f'{x:,.3f}'.rstrip('0').rstrip('.')
def seq(xs,percent=False): return ' / '.join(f'{x*100:g}' if percent else num(x) for x in xs)
def table(headers,rows):
    return '| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+''.join('| '+' | '.join(str(c) for c in row)+' |\n' for row in rows)

NOTES={
 'NVDA':('Base EPS 16.64 vs 19; P/E 25 vs 18; bull P/E 30 vs 22.','Codex weight; reduce my valuation','22x base/26x bull retains platform value without my old premium. Still strongest selected return. H01.'),
 'AVGO':('Base P/E 24 vs 20; margin/share count; financing reserve absent in mine.','Claude on valuation; neither weight','47% margin, 5.0bn shares, 20x and explicit credit reserve. VRSK wins new capital; S06.'),
 'VRT':('Similar base EPS; 26x vs 23x, much larger Codex bull.','Claude valuation; Codex weight','24x base, 19% common margin, lower bull. Still beats lower-return equipment alternatives.'),
 'CLS':('My base $513 vs their $378; their EPS/multiple bridge absent.','Codex','2027 issuer outlook supports growth beyond their terminal hurdle; dilution and cash needs trim my target. F05.'),
 'NVT':('No Claude terminal underwriting; rejected mainly on smaller cooling share.','Codex','Electrical distribution economics and valuation beat ETN; cooling market share is not the entire business. S01.'),
 'NRG':('No Claude terminal underwriting; retail/gas discount dismissed.','Codex, with a stricter debt bridge','Asset-sale earnings removed; proceeds not spent twice. Still beats CEG. S02.'),
 'VST':('My EV bridge vs their FCF/share; acquisition scope misread.','Codex inclusion; lower return than mine','No extra Cogentrix uplift beyond consolidated guide; retain growth-capex and debt charges. F03.'),
 'COHR':('24x vs 18x base P/E; cash conversion and dilution.','Claude caution; both overweight','New 18% margin, 230m shares, 20x. MU wins E and AI returns; exit, S05.'),
 'TSM':('Base EPS 26.83 vs 33; probabilities 25/50/25 vs 20/50/30.','Codex zero; improve my earnings case','Higher revenue, lower exit premium; all-in build cost is not foundry ASP. Taiwan remains a common risk.'),
 'MU':('My EPS 80 plus $150 cash vs their $130 with embedded buybacks.','Claude inclusion','Use $110 EPS, explicit cash, fixed shares, 10x. Beats COHR; wins near-ties on AI return.'),
 'ASML':('My base EPS 63.47 vs 88; capacity/margin/FX bridge.','Claude underwriting direction','New $85.65 base EPS; ASML beats my preferred WFE challenger. MU wins the last allocation slot.'),
 'SNPS':('Base EPS 24 vs 27; 30x vs 28x; similar expected values.','Codex zero','No decisive return edge. VRSK has stronger expected return; not a substitute for EDA technology.'),
 'CEG':('2030 earnings and Nov 9 update; nuclear premium.','Codex zero','Recognize higher guidance; price also rose. NRG/VST remain cheaper power returns.'),
 'ETN':('Similar base EPS; probability tails and quality multiple.','Codex NVT','ETN is credible quality; NVT offers about 6.8pp higher expected CAGR. S01.'),
 'CRDO':('My base EPS 6.36 vs 10.5; compensation and share dilution.','Claude improves my growth view; no add','New base EPS 8.35, after economic compensation; MU wins close expected-return tie on AI CAGR.'),
 'PWR':('Similar base EPS 32 vs 31; price and execution costs.','Codex zero','Strong infrastructure business, only 8.2% expected at current price; equipment wins.'),
 'KTOS':('Base EPS 1.16 vs 1.9; owner margin, share count, bull probability.','Codex','Production investment and dilution prevent adjusted EPS from being owner cash. Weakest Claude holding.'),
 'MP':('Bear floor and state probabilities; subsidy/contract vs common return.','Codex zero','Qualification is progress; expected return still loses and no demonstrated crisis hedge.'),
 'BNTX':('No original Codex model; Claude $65 bear and $120 base total wealth.','Codex exclusion; new explicit model','Cash burns before 2030; lower pipeline SOTP. Not reliable pandemic insurance.'),
 'VRSK':('Previously excluded by me; absent from Claude universe.','New Codex allocation','15.0% E vs AVGO 12.1%; AI 17.4% vs 17.0%. Own existing model now clears the opportunity cost.'),
}

def recon_cell(t,i):
    vals=[]
    for side in ['mine','theirs']:
        tv,kind=R[t]['reconstructions'][side][i]
        flag='†' if 'proxy' in kind else ''
        vals.append(pct(m.cagr(tv,R[t]['price']))+flag)
    return ' / '.join(vals)

blocks={}
head=[]
for i,t in enumerate(D['contested']+['VRSK'],1):
    r=R[t]; gap,call,why=NOTES[t]
    head.append([f'H{i:02d} {t}',D['original_weights'].get(t,0),D['claude_weights'].get(t,0),
                 f'${r["price"]:,.2f}; 2026-11-09',
                 ' / '.join(pct(r[k]) for k in ['mine_cagr','theirs_cagr','new_cagr']),
                 recon_cell(t,0),recon_cell(t,1),gap,call,why])
blocks['HEAD']=table(['Row / ticker','Mine %','Claude %','Price + date','Expected CAGR: mine / theirs / new',
                      'AI-2027 CAGR: mine* / theirs*','100GW CAGR: mine* / theirs*','Input gap','Better call','Why'],head)

rows=[]
for t in m.UNIVERSE:
    r=R[t]; a=r['inputs']
    rows.append([t,f'${r["price"]:,.2f}',seq(r['new_values']),seq(a['probabilities'],True),
                 f'${r["new_expected"]:,.2f}',pct(r['new_cagr']),pct(r['new_named_cagr'][0]),pct(r['new_named_cagr'][1])])
blocks['OUTCOMES']=table(['Ticker','Nov 9 price','Bear / base / bull wealth $','Probabilities %','Expected wealth $','Expected CAGR','AI-2027 CAGR','100GW CAGR'],rows)

rows=[]
for t in m.UNIVERSE:
    a=R[t]['inputs']
    if a['method']!='earnings': continue
    rows.append([t,seq(a['revenue']),seq(a['margin'],True),seq(a['shares']),seq(a['multiple']),seq(a['dividends']),seq(a['cash'])])
blocks['INPUTS']=table(['Ticker','Revenue $bn bear / base / bull','Common margin %','Diluted shares bn','Exit P/E','Dividends $/share','Excess cash / credit reserve $/share'],rows)

rows=[]
for t in ['NRG','VST']:
    a=R[t]['inputs']
    rows.append([t,seq(a['ebitda']),seq(a['multiple']),seq(a['debt']),seq(a['shares']),seq(a['dividends']),seq(a['owner_fcf'])])
blocks['EV']=table(['Ticker','EBITDA $bn','EV/EBITDA','Net financial claims $bn','Diluted shares bn','Dividends $/share','Owner cash before discretionary growth $bn'],rows)

rows=[]
for t in m.UNIVERSE:
    r=R[t]; a=r['inputs']
    bridge=[]
    for x in r['named_inputs']:
        if a['method']=='earnings':
            bridge.append(f'R {num(x[0])}; m {100*x[1]:g}%; S {num(x[2])}; P/E {num(x[3])}; D {num(x[4])}; C {num(x[5])}')
        elif a['method']=='ev':
            bridge.append(f'EBITDA {num(x[0])}; EV {num(x[1])}x; claims {num(x[2])}; S {num(x[3])}; D {num(x[4])}; FCF {num(x[5])}')
        else: bridge.append(f'Net cash {num(x[0])} + pipeline {num(x[1])}; S {num(x[2])}')
    rows.append([t,bridge[0],f'${r["new_named"][0]:,.2f} / {pct(r["new_named_cagr"][0])}',bridge[1],f'${r["new_named"][1]:,.2f} / {pct(r["new_named_cagr"][1])}'])
blocks['NAMED']=table(['Ticker','AI-2027 operating bridge','AI wealth / CAGR','100GW operating bridge','100GW wealth / CAGR'],rows)

PAIRS=[
 ('S01 Electrical distribution','NVT','ETN','Attractive / Fair','NVT','Lower paid multiple; profitable electrical expansion, not simply a cooling market-share contest.'),
 ('S02 Existing generation / retail','NRG','CEG','Attractive, levered / Fair','NRG','Returns still win after asset-sale earnings haircut and explicit debt funding; nuclear quality alone is insufficient.'),
 ('S03 Interconnect','COHR','CRDO','Speculative / Fair, execution-sensitive','CRDO within sleeve; neither held','Credo wins versus Coherent after compensation charges, but loses portfolio capital to MU/VRSK. Different distances/products, not exact substitutes.'),
 ('S04 Semiconductor equipment preference','LRCX','ASML','Fair-low return / Fair','ASML; neither held','My original preferred excluded WFE challenger loses to lithography after capacity/earnings re-underwriting. Both were not held by me.'),
 ('S05 Marginal AI-supplier capital, NOT same bottleneck','COHR','MU','Speculative / Fair, cyclical','MU','Higher E and AI returns; less exposure to optical expansion financed ahead of cash receipts.'),
 ('S06 Marginal profitable-growth capital, NOT same bottleneck','AVGO','VRSK','Fair / Attractive','VRSK','VRSK is my overlooked candidate, not Claude’s pick. Expected advantage exceeds 2pp, and AI return is also slightly higher.'),
 ('S07 Last capital slot: upstream alternatives','ASML','MU','Fair / Fair, cyclical','MU','Expected returns essentially equal; apply required higher-AI-CAGR tie-break. Neither is a hedge.'),
 ('S08 Contracted data vs speculative hedge sleeve','VRSK','BNTX','Attractive / Speculative','VRSK','Not technological substitutes: tested as competing capital uses. Return and modeled bust both favor data cash flow.'),
]
rows=[]
for label,a,b,status,win,why in PAIRS:
    rows.append([label,a,b,f'{pct(R[a]["new_cagr"])} / {pct(R[b]["new_cagr"])}',
                 f'{pct(R[a]["new_named_cagr"][0])} / {pct(R[b]["new_named_cagr"][0])}',
                 f'{pct(R[a]["new_named_cagr"][1])} / {pct(R[b]["new_named_cagr"][1])}',status,win,why])
blocks['PAIRS']=table(['Row / bottleneck or explicitly labeled capital contest','My pick / challenger','Their pick / other candidate',
                       'Expected CAGR each','AI-2027 CAGR each','100GW CAGR each','Valuation status each','Better stock','Why'],rows)

rows=[]
verdicts={'SNDK':'Reject: MU wins on expected and AI return. Useful omission to correct, not a new holding.',
 'RELX':'Reject at margin: VRSK wins E and AI; MU wins AI tie-break versus RELX.',
 'VRSK':'Add 15%; replace AVGO, via H20/S06. No diversification entitlement.',
 'MSI':'Reject: modest E and AI return; no demonstrated disaster payout.',
 'GEN':'Reject: low paid multiple does not overcome low common-earnings growth.'}
for t in ['SNDK','RELX','VRSK','MSI','GEN']:
    r=R[t]
    rows.append([t,'Claude only' if t=='SNDK' else 'Codex only',f'${r["price"]:,.2f}; 2026-11-09',
                 pct(r['new_cagr']),pct(r['new_named_cagr'][0]),pct(r['new_named_cagr'][1]),verdicts[t]])
blocks['UNIQUE']=table(['Ticker','Discovery','Price + date','Expected CAGR','AI-2027 CAGR','100GW CAGR','Verdict'],rows)

justifications={'NVDA':'H01: return advantage survives lower multiple; keep cap.',
 'AVGO':'H02 + H20 + S06: VRSK wins the full 15-point capital contest.',
 'VRT':'H03: lower forecast, still wins its funded slot; keep cap.',
 'CLS':'H04: current guidance supports higher value than Claude’s terminal hurdle.',
 'NVT':'H05 + S01: beats ETN after integration/dilution allowance.',
 'NRG':'H06 + S02: beats CEG after full asset-sale/debt bridge.',
 'VST':'H07: power return wins, combined power cap remains 23%.',
 'COHR':'H08 + H10 + S05: all 8 points to MU.',
 'MU':'H10 + S05/S07: wins COHR replacement and AI tie-break.',
 'VRSK':'H20 + S06: all 15 points from AVGO.'}
rows=[]
for t in list(D['original_weights'])+[t for t in D['revised_weights'] if t not in D['original_weights']]:
    old=D['original_weights'].get(t,0); new=D['revised_weights'].get(t,0)
    rows.append([t,f'{old:.1f}',f'{new:.1f}',f'{new-old:+.1f}',justifications[t]])
rows.append(['TOTAL','100.0','100.0','0.0','100% common stocks; maximum 15%; no external funding.'])
blocks['ALLOCATION']=table(['Ticker','Original %','Revised %','Delta pp','Head-to-head justification'],rows)

rows=[]
for label,p in D['portfolios'].items():
    rows.append([label,pct(p['expected_cagr']),pct(p['ai_cagr']),pct(p['gw_cagr']),pct(p['bust_return']),pct(p['delay_return']),f'{p["HHI"]:.4f}'])
blocks['PORTFOLIOS']=table(['Portfolio, SAME new underwriting','Expected CAGR','AI-2027 CAGR','100GW CAGR','2030 bust total return','2030 delay total return','HHI'],rows)

def sensitivity(weights,ticker,factor):
    w=weights.get(ticker,0)/100
    current=sum(v/100*R[t]['new_expected']/R[t]['price'] for t,v in weights.items())
    a=R[ticker]['inputs']
    # Scale only the equity multiple component; dividends/cash remain unchanged.
    deduction=sum(p*(tv-d-c)*(1-factor) for p,tv,d,c in zip(a['probabilities'],R[ticker]['new_values'],a['dividends'],a['cash']))
    return (current-w*deduction/R[ticker]['price'])**(1/m.YEARS)-1

original=D['portfolios']['Codex original, new underwriting']['expected_cagr']
revised=D['portfolios']['Codex revised']['expected_cagr']
rows=[['Central comparison',pct(original),pct(revised)],
 ['VRSK: every terminal P/E 20% lower',pct(original),pct(sensitivity(D['revised_weights'],'VRSK',.8))],
 ['AVGO: every terminal P/E 20% higher, other inputs unchanged',pct(sensitivity(D['original_weights'],'AVGO',1.2)),pct(revised)],
 ['Extra common 10% zero-recovery regime',pct((1+original)*(.9**(1/m.YEARS))-1),pct((1+revised)*(.9**(1/m.YEARS))-1)],
 ['Extra common 20% zero-recovery regime',pct((1+original)*(.8**(1/m.YEARS))-1),pct((1+revised)*(.8**(1/m.YEARS))-1)]]
blocks['SENSITIVITY']=table(['Assumption change','Original weights CAGR','Revised weights CAGR'],rows)

source=REPORT.read_text(encoding='utf-8')
for name,body in blocks.items():
    pattern=r'<!-- BEGIN '+name+r' -->.*?<!-- END '+name+r' -->'
    source,count=re.subn(pattern,'<!-- BEGIN '+name+' -->\n'+body+'\n<!-- END '+name+' -->',source,flags=re.S)
    assert count==1,(name,count)
REPORT.write_text(source,encoding='utf-8')
(ROOT/'generated_tables.md').write_text('\n\n'.join('## '+k+'\n\n'+v for k,v in blocks.items()),encoding='utf-8')
print('Synchronized',len(blocks),'generated table blocks.')
