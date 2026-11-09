"""Independent EHF scenario model. All forecasts are analyst assumptions, not consensus.

USD billions for revenue, profit and shares; USD per share for distributions.
No trading/account access. Run from any directory to reproduce the tables.
"""
import csv
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
YEARS = (dt.date(2030, 12, 31) - dt.date(2026, 11, 6)).days / 365.25
MARKET = {r['ticker']: r for r in json.loads((ROOT/'market_snapshot.json').read_text())}
MARKET['NBIS'] = {'last_close':129.49,'last_date':'2026-11-06','source':'https://financecharts.com/stocks/NBIS/summary/price'}
BASELINE = dict(TSM=11,NVDA=6,AVGO=3,MU=6,ASML=8,AMAT=4,SNPS=5,ANET=4,VRT=6,DELL=2,
                CEG=9,VST=6,PWR=4,CRWD=3,PLTR=2,AVAV=1,KTOS=1,MRNA=1,MP=3,INTC=3,GEV=5,CCJ=2,BE=3,COHR=2)
FINAL = dict(NVDA=15,AVGO=15,VRT=15,CLS=12,NVT=12,NRG=12,VST=11,COHR=8)
CORE = dict(NVDA=12,AVGO=10,VRT=10,CLS=8,NVT=8,VST=8,NRG=8,COHR=6,MSFT=6,GOOGL=6,TSM=5,ASML=4,MU=3,PWR=3,SNPS=3)

# ticker, revenue B/B/B, after-tax earnings margin B/B/B, diluted shares B/B/B,
# terminal P/E B/B/B, cumulative cash dividends B/B/B, probabilities, confidence.
# FCF rows substitute owner FCF AFTER an SBC economic charge for earnings.
ROWS = [
('TSM',[140,310,430],[.32,.45,.47],[5.30,5.20,5.15],[15,23,28],[15,20,25],[.25,.50,.25],4),
('NVDA',[350,850,1400],[.32,.46,.50],[24,23.5,23],[18,25,30],[4,6,8],[.25,.50,.25],4),
('AVGO',[100,250,400],[.38,.50,.52],[5,4.9,4.8],[18,24,28],[10,13,16],[.25,.50,.25],4),
('MU',[120,240,360],[.20,.40,.50],[1.20,1.20,1.20],[12,12,15],[4,8,12],[.30,.50,.20],3),
('ASML',[40,70,100],[.24,.34,.37],[.385,.375,.365],[20,30,35],[30,40,50],[.25,.50,.25],4),
('AMAT',[25,50,70],[.20,.28,.31],[.78,.72,.70],[16,24,28],[8,10,12],[.25,.50,.25],3),
('SNPS',[10,16,23],[.18,.30,.34],[.205,.200,.205],[23,30,35],[0,0,0],[.25,.50,.25],3),
('ANET',[13,30,46],[.28,.35,.38],[1.30,1.30,1.32],[22,30,35],[0,0,0],[.25,.50,.25],4),
('VRT',[12,30,48],[.10,.20,.23],[.390,.380,.375],[18,26,30],[1,2,3],[.25,.50,.25],4),
('DELL',[130,300,450],[.030,.055,.065],[.65,.60,.57],[10,17,20],[10,12,14],[.25,.50,.25],3),
('CEG',[35,50,65],[.07,.12,.15],[.36,.35,.34],[14,22,26],[9,12,15],[.25,.50,.25],3),
('PWR',[32,60,80],[.05,.08,.095],[.150,.150,.150],[18,25,30],[2,3,4],[.25,.50,.25],4),
('CRWD',[9,16,24],[.10,.23,.28],[1.12,1.10,1.10],[20,35,45],[0,0,0],[.25,.50,.25],3),
('PLTR',[12,28,45],[.22,.38,.45],[2.80,2.75,2.70],[22,40,50],[0,0,0],[.25,.50,.25],3),
('AVAV',[2.3,4,6],[.04,.10,.14],[.060,.060,.062],[16,24,28],[0,0,0],[.30,.50,.20],2),
('KTOS',[2.1,3.8,6],[.02,.07,.10],[.22,.23,.24],[18,28,35],[0,0,0],[.30,.50,.20],2),
('MRNA',[4,12,25],[0,.25,.35],[.44,.45,.46],[15,25,30],[0,0,0],[.35,.45,.20],2),
('MP',[.6,2,3.5],[.02,.22,.28],[.20,.21,.22],[16,24,30],[0,0,0],[.35,.45,.20],2),
('INTC',[55,85,130],[0,.10,.17],[6,5.8,6],[12,18,22],[0,0,0],[.35,.45,.20],2),
('GEV',[40,75,105],[.05,.13,.16],[.270,.265,.260],[18,28,32],[8,12,16],[.25,.50,.25],3),
('CCJ',[2.5,5,8],[.12,.25,.30],[.440,.440,.445],[18,25,30],[2,3,4],[.25,.50,.25],3),
('BE',[3,10,18],[.02,.15,.19],[.35,.36,.38],[18,28,35],[0,0,0],[.30,.50,.20],2),
('COHR',[7,20,30],[.08,.20,.23],[.22,.22,.23],[15,24,28],[0,0,0],[.30,.50,.20],3),
('CLS',[25,65,100],[.035,.065,.080],[.140,.140,.145],[10,17,20],[0,0,0],[.30,.50,.20],3),
('NVT',[5.5,10,15],[.10,.17,.20],[.160,.160,.160],[16,22,26],[3,4,5],[.25,.50,.25],3),
('MSFT',[380,680,950],[.30,.37,.40],[7.5,7.3,7.2],[22,29,33],[16,20,24],[.25,.50,.25],4),
('GOOGL',[430,800,1150],[.18,.27,.32],[13.3,13.1,13.0],[17,24,28],[4,5,6],[.25,.50,.25],3),
('AMZN',[850,1350,1800],[.05,.10,.13],[11.3,11.4,11.5],[22,30,34],[0,0,0],[.25,.50,.25],3),
('META',[230,400,600],[.20,.32,.38],[2.65,2.60,2.60],[16,23,27],[9,12,15],[.25,.50,.25],3),
('LRCX',[25,50,70],[.24,.35,.38],[1.25,1.20,1.18],[16,25,29],[5,7,9],[.25,.50,.25],4),
('KLAC',[13,25,34],[.30,.38,.40],[1.33,1.28,1.25],[20,28,32],[4,5,6],[.25,.50,.25],4),
('CDNS',[6.5,10,14],[.22,.34,.37],[.28,.27,.27],[25,35,40],[0,0,0],[.25,.50,.25],3),
('ETN',[29,48,65],[.12,.18,.21],[.39,.38,.38],[18,25,29],[18,22,26],[.25,.50,.25],4),
('MOD',[2.8,5.5,8.5],[.04,.09,.13],[.056,.056,.058],[13,22,26],[0,0,0],[.30,.50,.20],2),
('PANW',[16,27,39],[.16,.26,.31],[.93,.92,.93],[22,32,38],[0,0,0],[.25,.50,.25],3),
('RELX',[12,17,22],[.20,.26,.29],[1.80,1.75,1.73],[18,24,28],[4,5,6],[.25,.50,.25],4),
('VRSK',[3.4,4.5,5.7],[.25,.33,.37],[.130,.120,.118],[20,28,32],[8,9,10],[.25,.50,.25],4),
('MSI',[13,19,25],[.16,.22,.25],[.17,.16,.16],[19,26,30],[20,24,28],[.25,.50,.25],4),
('AXON',[4.5,8,12],[.06,.16,.22],[.090,.095,.100],[25,35,42],[0,0,0],[.30,.50,.20],2),
('GEN',[4.5,6,7.5],[.17,.24,.28],[.64,.61,.60],[10,14,17],[2,2.5,3],[.25,.50,.25],3),
('AMD',[45,125,230],[.13,.25,.30],[1.80,1.90,2.00],[18,28,33],[0,0,0],[.30,.50,.20],2),
('ALAB',[1.5,5,9],[.12,.26,.30],[.20,.21,.22],[20,32,40],[0,0,0],[.30,.50,.20],2),
('CRDO',[2,5,9],[.15,.28,.32],[.21,.22,.23],[18,28,35],[0,0,0],[.30,.50,.20],2),
('HPE',[40,70,100],[.05,.085,.11],[1.40,1.35,1.35],[9,13,16],[2.3,2.8,3.2],[.25,.50,.25],3),
('FN',[5,10,16],[.06,.09,.11],[.037,.037,.038],[13,20,24],[0,0,0],[.30,.50,.20],3),
('POWL',[1.1,2.2,3.3],[.08,.14,.17],[.038,.038,.038],[12,20,24],[1,1.5,2],[.30,.50,.20],3),
]

# EV rows: revenue; EBITDA margin; enterprise multiple; NET debt + preferred/NCI claims;
# diluted shares. Equity value floored at zero. Debt is subtracted exactly once.
EV_ROWS = [
('VST',[20,28,36],[.30,11/28,15/36],[7,9,10],[26,20,15],[.34,.30,.28],[4,5,6],[.25,.50,.25],4),
('NRG',[25,32,40],[.18,7/32,.225],[6.5,8,9],[18,14,10],[.22,.20,.19],[7,8,9],[.25,.50,.25],3),
('TLN',[5,8,11],[.35,.45,.50],[7,9,10],[5,4,3],[.050,.045,.043],[0,0,0],[.25,.50,.25],3),
('CORZ',[.7,2.2,3.5],[.35,.55,.60],[8,12,14],[5,5,5],[.50,.55,.60],[0,0,0],[.35,.45,.20],2),
('IREN',[2,7,12],[.25,.45,.50],[6,9,11],[12,13,15],[.50,.55,.65],[0,0,0],[.40,.40,.20],2),
('CRWV',[12,32,50],[.40,.55,.60],[6,8,10],[45,65,80],[.65,.75,.85],[0,0,0],[.40,.40,.20],2),
('APLD',[1,3,5],[.35,.55,.60],[8,12,14],[6,10,15],[.40,.45,.50],[0,0,0],[.40,.40,.20],2),
('NBIS',[6,25,45],[.35,.50,.55],[6,9,11],[18,45,70],[.40,.50,.60],[0,0,0],[.40,.40,.20],2),
]

STATUS = dict(NVDA='Attractive',AVGO='Attractive',VRT='Attractive',CLS='Deep Discount',NVT='Attractive',NRG='Deep Discount',VST='Attractive',COHR='Attractive')
FCF_RATIOS = {'TSM':.70,'NVDA':.95,'AVGO':.95,'MU':.65,'ASML':.90,'AMAT':.95,'SNPS':.85,
 'ANET':.95,'VRT':.85,'DELL':.65,'CEG':.70,'PWR':.80,'PLTR':.85,'AVAV':.65,'KTOS':.55,
 'MRNA':.80,'MP':.65,'INTC':.25,'GEV':.80,'CCJ':.75,'BE':.65,'COHR':.75,'CLS':.65,
 'NVT':.85,'MSFT':.70,'GOOGL':.65,'AMZN':.60,'META':.70,'LRCX':.95,'KLAC':.95,'CDNS':.85,
 'ETN':.90,'MOD':.65,'RELX':.90,'VRSK':.90,'MSI':.90,'AXON':.70,'GEN':.95,'AMD':.80,
 'ALAB':.80,'CRDO':.85}
FCF_RATIOS.update(HPE=.80,FN=.90,POWL=.85)

def calculate():
    out = {}
    for t,r,m,s,k,d,p,c in ROWS:
        cash = [40,150,250] if t=='MU' else [5,10,15] if t=='MRNA' else [6,0,0] if t=='INTC' else [0,0,0]
        vals = [max(0,r[i]*m[i]/s[i]*k[i])+d[i]+cash[i] for i in range(3)]
        out[t] = dict(ticker=t,method='Owner FCF' if t in ['CRWD','PANW'] else 'Earnings',revenue=r,
            margin=m,shares=s,multiple=k,dividends=d,excess_cash_per_share=cash,probabilities=p,confidence=c,
            terminal_values=vals,base_owner_fcf=r[1]*m[1]*FCF_RATIOS.get(t,1))
    for t,r,m,k,debt,s,d,p,c in EV_ROWS:
        vals = [max(0,r[i]*m[i]*k[i]-debt[i])/s[i]+d[i] for i in range(3)]
        out[t] = dict(ticker=t,method='EV/EBITDA',revenue=r,margin=m,shares=s,multiple=k,net_claims=debt,
            dividends=d,probabilities=p,confidence=c,terminal_values=vals)
    # Transaction-aware combined-company model. Includes Lumentum conversion and dilution.
    # MRVL bear assumes deal failure and standalone normalization; base/bull assume completion.
    out['MRVL'] = dict(ticker='MRVL',method='Merger earnings',revenue=[9,30,47],margin=[.15,.30,.34],
        shares=[.90,1.38,1.42],multiple=[18,25,30],dividends=[1,1,1],probabilities=[.30,.50,.20],confidence=2,
        terminal_values=[28,30*.30/1.38*25+1,47*.34/1.42*30+1],base_owner_fcf=30*.30*.8)
    out['LITE'] = dict(ticker='LITE',method='Merger conversion',revenue=[4.5,30,47],margin=[.18,.30,.34],
        shares=[.110,1.38,1.42],multiple=[18,25,30],dividends=[0,4.5,4.5],probabilities=[.30,.50,.20],confidence=2,
        terminal_values=[4.5*.18/.110*18,4.5*out['MRVL']['terminal_values'][1],4.5*out['MRVL']['terminal_values'][2]],
        base_owner_fcf=30*.30*.8)
    for t,a in out.items():
        assert abs(sum(a['probabilities'])-1)<1e-9
        a['price']=MARKET[t]['last_close']
        a['expected_terminal']=sum(v*p for v,p in zip(a['terminal_values'],a['probabilities']))
        a['expected_total_return']=a['expected_terminal']/a['price']-1
        a['expected_cagr']=(1+a['expected_total_return'])**(1/YEARS)-1
        a['scenario_total_returns']=[v/a['price']-1 for v in a['terminal_values']]
        a['status']=STATUS.get(t,'Speculative' if a['confidence']==2 else 'Fair' if a['expected_cagr']>=.08 else 'Expensive')
    return out

def architecture(weights, rows):
    assert sum(weights.values())==100
    assert max(weights.values())<=15
    ratio=sum(w/100*rows[t]['expected_terminal']/rows[t]['price'] for t,w in weights.items())
    cases=[sum(w/100*rows[t]['terminal_values'][i]/rows[t]['price'] for t,w in weights.items())-1 for i in range(3)]
    # A delay loses 2.5 years of base-case operating growth before applying a 15% multiple haircut.
    # It is a deterministic stress, not an additional probability-weighted forecast.
    delay=sum(w/100*(.85*(rows[t]['terminal_values'][1]/rows[t]['price'])**((YEARS-2.5)/YEARS)) for t,w in weights.items())-1
    return dict(weights=weights,expected_total_return=ratio-1,expected_cagr=ratio**(1/YEARS)-1,
                bear_base_bull_returns=cases,delay_return=delay,holdings=len(weights),HHI=sum((w/100)**2 for w in weights.values()),
                top3=sum(sorted(weights.values(),reverse=True)[:3]))

def mdtable(header, rows):
    return '| '+' | '.join(header)+' |\n| '+' | '.join(['---']*len(header))+' |\n'+''.join('| '+' | '.join(map(str,r))+' |\n' for r in rows)

def main():
    rows=calculate()
    perf=[]
    total=sum(w/100*MARKET[t]['total_return_pct'] for t,w in BASELINE.items())
    for t,w in BASELINE.items():
        q=MARKET[t]
        assert q['first_date']=='2026-05-08' and q['last_date']=='2026-11-06'
        perf.append(dict(ticker=t,weight=w,may_close=q['first_close'],nov_close=q['last_close'],price_return=q['price_return_pct'],
                         total_return=q['total_return_pct'],contribution_pp=w/100*q['total_return_pct'],
                         drift_weight=w*(1+q['total_return_pct']/100)/(1+total/100)))
    with (ROOT/'accountability.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=perf[0].keys()); writer.writeheader();writer.writerows(perf)
    arches={n:architecture(w,rows) for n,w in [('Current',BASELINE),('Concentrated',FINAL),('Core-satellite',CORE)]}
    out=dict(asof='2026-11-06',terminal='2030-12-31',years=YEARS,baseline_return_pct=total,stocks=rows,architectures=arches)
    (ROOT/'valuation_outputs.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    blocks=['# Reproducible numerical tables\n',f'Horizon {YEARS:.6f} years. Baseline modeled total return {total:.4f}%.\n']
    blocks.append(mdtable(['Ticker','May 8 $','Nov 6 $','Price %','TR %','Contribution pp','Drift %'],
                 [[p['ticker'],f"{p['may_close']:.2f}",f"{p['nov_close']:.2f}",f"{p['price_return']:+.2f}",f"{p['total_return']:+.2f}",f"{p['contribution_pp']:+.2f}",f"{p['drift_weight']:.2f}"] for p in perf]))
    for title,names in [('Final',FINAL),('All',rows)]:
        blocks.append('\n## '+title+' terminal values\n')
        blocks.append(mdtable(['Ticker','Price $','B/B/B total wealth $','p %','Expected $','CAGR %','Confidence'],
         [[t,f"{rows[t]['price']:.2f}",'/'.join(f'{v:.0f}' for v in rows[t]['terminal_values']),'/'.join(f'{p*100:.0f}' for p in rows[t]['probabilities']),f"{rows[t]['expected_terminal']:.1f}",f"{rows[t]['expected_cagr']*100:.1f}",rows[t]['confidence']] for t in names]))
    blocks.append('\n## Model inputs\n')
    blocks.append(mdtable(['Ticker / method','Revenue $bn B/B/B','Margin % B/B/B','Shares bn B/B/B','Multiple B/B/B','Div $ B/B/B','Net claims $bn / excess cash $'],
     [[t+' '+a['method'],'/'.join(f'{v:g}' for v in a['revenue']),'/'.join(f'{v*100:g}' for v in a['margin']),'/'.join(f'{v:g}' for v in a['shares']),'/'.join(f'{v:g}' for v in a['multiple']),'/'.join(f'{v:g}' for v in a['dividends']),'/'.join(f'{v:g}' for v in a.get('net_claims',a.get('excess_cash_per_share',[0,0,0])))] for t,a in rows.items()]))
    blocks.append('\n## Architecture results\n'+mdtable(['Architecture','Names','Expected TR %','CAGR %','Bear/Base/Bull TR %','Delay %','HHI','Top3 %'],
      [[n,a['holdings'],f"{a['expected_total_return']*100:.1f}",f"{a['expected_cagr']*100:.1f}",'/'.join(f'{v*100:.1f}' for v in a['bear_base_bull_returns']),f"{a['delay_return']*100:.1f}",f"{a['HHI']:.4f}",a['top3']] for n,a in arches.items()]))
    (ROOT/'analysis_tables.md').write_text('\n'.join(blocks),encoding='utf-8')
    print('Baseline return:',total,'Horizon:',YEARS,'Underwritten stocks:',len(rows))
    for t,a in sorted(rows.items(),key=lambda z:z[1]['expected_cagr'],reverse=True):
        print(t,round(a['expected_cagr']*100,2),a['status'])
    print(json.dumps(arches,indent=2))

if __name__=='__main__': main()
