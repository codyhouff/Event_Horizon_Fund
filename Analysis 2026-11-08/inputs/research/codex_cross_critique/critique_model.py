"""Step 2 only: frozen originals, current prices, explicit new underwriting.

Amounts: USD billions and billions of shares, except per-share amounts.
No original research files are changed. Forecasts are analyst assumptions.
"""
import datetime as dt
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
YEARS = (dt.date(2030, 12, 31)-dt.date(2026, 11, 9)).days/365.25
Q = {x['ticker']: x for x in json.loads((ROOT/'quotes.json').read_text())}
OLD = json.loads((ROOT.parent/'valuation_outputs.json').read_text())['stocks']
MINE = dict(NVDA=15, AVGO=15, VRT=15, CLS=12, NVT=12, NRG=12, VST=11, COHR=8)
THEIRS = dict(TSM=14, NVDA=13, VRT=9, VST=9, MU=9, ASML=8, AVGO=6, SNPS=6,
              CEG=6, COHR=5, ETN=5, CRDO=3, PWR=2, KTOS=2, MP=2, BNTX=1)
CONTESTED = list(MINE)+[t for t in THEIRS if t not in MINE]
EXTRA = ['SNDK','RELX','VRSK','MSI','GEN','LRCX']
UNIVERSE = CONTESTED+EXTRA
# Published rounded total-wealth endpoints and probabilities, not invented consensus.
CLAUDE = {
 'TSM':([287,641,980],[.20,.50,.30],33,19,14),
 'NVDA':([113,343,617],[.25,.50,.25],19,18,1),
 'VRT':([128,358,589],[.25,.50,.25],15.5,23,1.5),
 'VST':([84,244,354],[.30,.45,.25],20,12,4),
 'MU':([497,1172,2032],[.25,.45,.30],130,9,2),
 'COHR':([96,342,594],[.30,.45,.25],19,18,0),
 'CEG':([189,397,583],[.25,.50,.25],19.5,20,7),
 'AVGO':([207,492,924],[.30,.45,.25],24,20,12),
 'SNPS':([361,756,1089],[.25,.50,.25],27,28,0),
 'ASML':([1040,2504,3496],[.20,.50,.30],88,28,40),
 'ETN':([272,569,773],[.25,.50,.25],23,24,17),
 'CRDO':([56,231,476],[.30,.45,.25],10.5,22,0),
 'PWR':([380,777,1075],[.25,.50,.25],31,25,2),
 'KTOS':([12,57,106],[.30,.45,.25],1.9,30,0),
 'MP':([12,47,90],[.30,.45,.25],1.8,26,0),
 'BNTX':([65,120,210],[.30,.45,.25],None,None,None),
 'CLS':([120,378,595],[.30,.45,.25],None,None,None),
 'SNDK':([500,1200,1950],[.30,.45,.25],None,None,None),
 'LRCX':([117,271,419],[.30,.45,.25],None,None,None),
}

def earnings(revenue, margin, shares, multiple, div=(0,0,0), cash=(0,0,0), p=(.25,.50,.25)):
    return dict(method='earnings',revenue=list(revenue),margin=list(margin),shares=list(shares),
                multiple=list(multiple),dividends=list(div),cash=list(cash),probabilities=list(p))

def ev(ebitda, multiple, debt, shares, div, owner_fcf):
    return dict(method='ev',ebitda=list(ebitda),multiple=list(multiple),debt=list(debt),shares=list(shares),
                dividends=list(div),cash=[0,0,0],owner_fcf=list(owner_fcf),probabilities=[.25,.50,.25])

# New estimates: independently selected inputs, NOT arithmetic averages of reports.
NEW = {
 'NVDA':earnings([350,850,1400],[.32,.46,.50],[24,23.5,23],[16,22,26],[4,6,8]),
 'AVGO':earnings([100,250,400],[.35,.47,.50],[5.1,5.0,4.95],[15,20,24],[10,13,16],[-8,-2,0]),
 'VRT':earnings([12,30,45],[.10,.19,.22],[.390,.380,.380],[16,24,27],[1,2,3]),
 'CLS':earnings([25,65,95],[.035,.065,.075],[.145,.145,.150],[10,16,18]),
 'NVT':earnings([5.5,10,14],[.10,.17,.19],[.163,.160,.160],[16,22,25],[3,4,5]),
 'NRG':ev([4.0,6.5,8.5],[6.5,8,9],[19,14,11],[.210,.190,.180],[8,9,10],[1.8,3.5,4.7]),
 'VST':ev([6,11,14],[7,9,10],[26,20,16],[.34,.30,.29],[4,5,6],[2.2,5.5,7.5]),
 'COHR':earnings([7,20,28],[.08,.18,.22],[.23,.23,.24],[14,20,24]),
 'TSM':earnings([140,340,450],[.32,.46,.47],[5.3,5.2,5.15],[15,21,25],[15,20,25]),
 'MU':earnings([120,300,450],[.20,.44,.50],[1.2,1.2,1.2],[11,10,9],[4,8,12],[40,150,250]),
 'ASML':earnings([40,88,130],[.24,.365,.40],[.385,.375,.360],[20,28,30],[30,40,50]),
 'SNPS':earnings([10,16,23],[.18,.30,.34],[.205,.200,.205],[23,30,35]),
 'CEG':earnings([35,53,68],[.08,.13,.15],[.36,.35,.34],[14,20,24],[9,12,15]),
 'ETN':earnings([29,48,65],[.12,.18,.21],[.39,.38,.38],[18,24,28],[18,22,26]),
 'CRDO':earnings([2.4,6,12],[.18,.32,.36],[.220,.230,.245],[16,22,26]),
 'PWR':earnings([32,60,80],[.05,.08,.095],[.15,.15,.15],[18,25,29],[2,3,4]),
 'KTOS':earnings([2.1,4.1,6],[.025,.08,.10],[.23,.24,.25],[18,28,32],p=(.30,.50,.20)),
 'MP':earnings([.6,2,3.5],[.02,.22,.28],[.20,.21,.22],[16,24,28],p=(.30,.50,.20)),
 'BNTX':dict(method='sotp',terminal=[45,105,190],probabilities=[.30,.50,.20],
             net_cash_bn=[6,10,12],pipeline_bn=[5.25,16.25,35.5],shares=[.25,.25,.25]),
 'SNDK':earnings([30,55,85],[.20,.36,.45],[.15,.14,.135],[9,9,8],cash=[30,100,180],p=(.30,.50,.20)),
 'LRCX':earnings([25,45,70],[.24,.33,.38],[1.25,1.20,1.18],[16,22,26],[5,7,9]),
}
for t in ['RELX','VRSK','MSI','GEN']:
    o = OLD[t]
    NEW[t] = earnings(o['revenue'],o['margin'],o['shares'],o['multiple'],o['dividends'])

# Named paths: explicit independent 2030 operating bridges.
# Each earnings tuple: revenue, net common margin, diluted shares, PE, dividends, excess cash/share.
# Each EV tuple: EBITDA, EV multiple, net claims, diluted shares, dividends, owner FCF bn.
NAMED_INPUTS = {
 'NVDA':[(1000,.46,23.5,22,6,0),(2200,.45,24,24,8,0)],
 'AVGO':[(320,.47,5,20,13,-2),(650,.45,5.2,22,16,-4)],
 'VRT':[(36,.20,.38,24,2,0),(80,.21,.40,26,3,0)],
 'CLS':[(80,.065,.145,16,0,0),(170,.065,.16,17,0,0)],
 'NVT':[(12,.18,.16,22,4,0),(25,.18,.175,24,5,0)],
 'NRG':[(7.2,8,14,.19,9,3.9),(10,9,18,.22,10,5.2)],
 'VST':[(12,9,20,.30,5,6.0),(18,10,25,.32,6,8.5)],
 'COHR':[(24,.19,.23,20,0,0),(50,.20,.26,22,0,0)],
 'TSM':[(390,.46,5.2,21,20,0),(700,.45,5.4,24,25,0)],
 'MU':[(360,.46,1.2,10,8,180),(700,.44,1.3,9,12,250)],
 'ASML':[(105,.38,.37,28,40,0),(180,.39,.39,30,50,0)],
 'SNPS':[(18,.31,.20,30,0,0),(28,.32,.22,32,0,0)],
 'CEG':[(58,.14,.35,20,12,0),(90,.15,.38,23,15,0)],
 'ETN':[(55,.19,.38,24,22,0),(90,.20,.40,27,26,0)],
 'CRDO':[(8,.35,.23,22,0,0),(18,.36,.27,24,0,0)],
 'PWR':[(72,.085,.15,25,3,0),(130,.085,.17,27,4,0)],
 'KTOS':[(4.6,.085,.24,28,0,0),(6.5,.10,.27,30,0,0)],
 'MP':[(2.4,.23,.215,24,0,0),(4.5,.25,.25,26,0,0)],
 'BNTX':[(10,20,.25),(10,25,.25)], # net cash, pipeline value, shares
 'SNDK':[(65,.40,.14,9,0,120),(130,.40,.16,8,0,180)],
 'RELX':[(18,.27,1.75,24,5,0),(21,.28,1.78,23,6,0)],
 'VRSK':[(4.8,.34,.12,28,9,0),(5.5,.35,.125,27,10,0)],
 'MSI':[(21,.23,.16,26,24,0),(26,.24,.17,25,28,0)],
 'GEN':[(6.5,.24,.61,14,2.5,0),(7.5,.24,.64,13,3,0)],
 'LRCX':[(56,.35,1.2,23,7,0),(95,.36,1.25,25,9,0)],
}

def cagr(wealth, price):
    return (wealth/price)**(1/YEARS)-1

def values(a):
    if a['method']=='sotp': return a['terminal']
    if a['method']=='ev':
        return [max(0,e*k-n)/s+d for e,k,n,s,d in zip(a['ebitda'],a['multiple'],a['debt'],a['shares'],a['dividends'])]
    return [max(0,r*m/s*k+c)+d for r,m,s,k,d,c in zip(a['revenue'],a['margin'],a['shares'],a['multiple'],a['dividends'],a['cash'])]

def named_value(t, i):
    x = NAMED_INPUTS[t][i]
    if NEW[t]['method']=='sotp': return (x[0]+x[1])/x[2]
    if NEW[t]['method']=='ev': return max(0,x[0]*x[1]-x[2])/x[3]+x[4]
    return max(0,x[0]*x[1]/x[2]*x[3]+x[5])+x[4]

def reconstructed(t, i, model):
    """Transport original base economics to shared named path using disclosed loading.

    Use stock-specific operating EPS change and multiple change relative to NEW base.
    Missing operating bridges use explicit terminal-wealth proxy. Missing entire
    original valuations use NEW proxy, flagged, never presented as historical output.
    """
    a = NEW[t]; x = NAMED_INPUTS[t][i]; v = values(a)
    if model=='mine':
        if t not in OLD: return named_value(t,i), 'new proxy; original not modeled'
        o=OLD[t]
        if a['method']=='earnings':
            metric_loading=(x[0]*x[1]/x[2])/(a['revenue'][1]*a['margin'][1]/a['shares'][1])
            mult_loading=x[3]/a['multiple'][1]
            metric=o['revenue'][1]*o['margin'][1]/o['shares'][1]
            cash=o.get('excess_cash_per_share',[0,0,0])[1]
            cash_loading=x[5]/a['cash'][1] if a['cash'][1]>0 else 1
            return max(0,metric*metric_loading*o['multiple'][1]*mult_loading+cash*cash_loading)+o['dividends'][1], 'operating reconstruction'
        if a['method']=='ev':
            return max(0,o['revenue'][1]*o['margin'][1]*(x[0]/a['ebitda'][1])*o['multiple'][1]*(x[1]/a['multiple'][1])-o['net_claims'][1]*(x[2]/a['debt'][1]))/(o['shares'][1]*x[3]/a['shares'][1])+o['dividends'][1], 'EV reconstruction'
    else:
        if t not in CLAUDE: return named_value(t,i), 'new proxy; original not modeled'
        tv,p,metric,k,d=CLAUDE[t]
        if metric is None:
            return tv[1]*named_value(t,i)/v[1], 'terminal-wealth proxy; original bridge absent'
        if a['method']=='earnings':
            metric_loading=(x[0]*x[1]/x[2])/(a['revenue'][1]*a['margin'][1]/a['shares'][1])
            return metric*metric_loading*k*(x[3]/a['multiple'][1])+d, 'operating reconstruction'
        if t=='VST':
            loading=(x[5]/x[3])/(a['owner_fcf'][1]/a['shares'][1])
            return metric*loading*k*(x[1]/a['multiple'][1])+d, 'FCF/share reconstruction'
    raise ValueError((t,i,model))

def portfolio(weights, results, basis='new'):
    assert abs(sum(weights.values())-100)<1e-10
    assert max(weights.values())<=15
    wealth=sum(w/100*results[t][basis+'_expected']/Q[t]['close'] for t,w in weights.items())
    named=[sum(w/100*results[t]['new_named'][i]/Q[t]['close'] for t,w in weights.items()) for i in range(2)]
    bust=sum(w/100*results[t]['new_values'][0]/Q[t]['close'] for t,w in weights.items())
    # Terminal delay: operating state 40% of progress between NEW bear and base;
    # 10% multiple haircut. This is not a probability-weighted extra outcome.
    delay=sum(w/100*results[t]['delay']/Q[t]['close'] for t,w in weights.items())
    return dict(expected_cagr=wealth**(1/YEARS)-1,expected_total_return=wealth-1,
                ai_cagr=named[0]**(1/YEARS)-1,gw_cagr=named[1]**(1/YEARS)-1,
                bust_return=bust-1,delay_return=delay-1,HHI=sum((w/100)**2 for w in weights.values()))

def delay_value(a):
    """Interpolate operating inputs, not price returns; debt remains above base."""
    if a['method']=='sotp': return .6*a['terminal'][0]+.4*a['terminal'][1]
    mix=lambda key:.6*a[key][0]+.4*a[key][1]
    if a['method']=='ev': return max(0,mix('ebitda')*.9*mix('multiple')-mix('debt'))/mix('shares')+mix('dividends')
    return max(0,mix('revenue')*mix('margin')/mix('shares')*.9*mix('multiple')+mix('cash'))+mix('dividends')

def main():
    assert len(CONTESTED)==19 and set(NEW)==set(UNIVERSE)==set(NAMED_INPUTS)
    results={}
    for t in UNIVERSE:
        assert Q[t]['date']=='2026-11-09'
        a=NEW[t]; vs=values(a); assert abs(sum(a['probabilities'])-1)<1e-10
        e=sum(v*p for v,p in zip(vs,a['probabilities']))
        o=OLD.get(t); c=CLAUDE.get(t)
        oe=o['expected_terminal'] if o else None
        ce=sum(v*p for v,p in zip(c[0],c[1])) if c else None
        named=[named_value(t,i) for i in range(2)]
        recon={m:[reconstructed(t,i,m) for i in range(2)] for m in ['mine','theirs']}
        results[t]=dict(price=Q[t]['close'],mine_expected=oe,theirs_expected=ce,new_expected=e,
                        mine_cagr=cagr(oe,Q[t]['close']) if oe is not None else None,
                        theirs_cagr=cagr(ce,Q[t]['close']) if ce is not None else None,
                        new_cagr=cagr(e,Q[t]['close']),new_values=vs,new_named=named,
                        new_named_cagr=[cagr(x,Q[t]['close']) for x in named],reconstructions=recon,
                        inputs=a,named_inputs=NAMED_INPUTS[t],delay=delay_value(a))
    # Weight choices are finalized only after evaluating the competing returns.
    revised=dict(NVDA=15,VRT=15,CLS=12,NVT=12,NRG=12,VST=11,VRSK=15,MU=8)
    portfolios={k:portfolio(w,results) for k,w in [('Codex original, new underwriting',MINE),('Codex revised',revised),('Claude weights, new underwriting',THEIRS)]}
    frozen={}
    for label,weights,which in [('Codex',MINE,'mine'),('Claude',THEIRS,'theirs')]:
        wealth=sum(w/100*results[t][which+'_expected']/Q[t]['close'] for t,w in weights.items())
        frozen[label]=dict(expected_cagr=wealth**(1/YEARS)-1,expected_total_return=wealth-1)
    for cutoff,use_current in [('Nov6',False),('Nov9',True)]:
        denominator=lambda t:Q[t]['close'] if use_current else (OLD[t]['price'] if t in OLD else 87.51)
        allbear=sum(w/100*CLAUDE[t][0][0]/denominator(t) for t,w in THEIRS.items())-1
        hedgebase=sum(w/100*CLAUDE[t][0][1 if t in ['KTOS','MP','BNTX'] else 0]/denominator(t) for t,w in THEIRS.items())-1
        frozen['Claude stress '+cutoff]=dict(all_bear=allbear,hedges_at_base=hedgebase)
    out=dict(cutoff='2026-11-09',terminal='2030-12-31',years=YEARS,contested=CONTESTED,
             stocks=results,original_weights=MINE,claude_weights=THEIRS,revised_weights=revised,portfolios=portfolios)
    out['frozen_comparison']=frozen
    (ROOT/'critique_results.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    for t,r in sorted(results.items(),key=lambda z:z[1]['new_cagr'],reverse=True):
        fmt=lambda v:'NR' if v is None else f'{v*100:.2f}'
        print(t, 'price',round(r['price'],2),'old M/C',fmt(r['mine_cagr']),fmt(r['theirs_cagr']),
              'new E/AI/100GW',*[fmt(v) for v in [r['new_cagr']]+r['new_named_cagr']],
              'TV',*[round(v,1) for v in r['new_values']])
    print(json.dumps(portfolios,indent=2))
    print(json.dumps(frozen,indent=2))
    other=(ROOT.parent.parent/'Claude Deep Dive 2026-11-08.md').read_text(encoding='utf-8')
    only_mine=[t for t in OLD if not re.search(r'\b'+t+r'\b',other)]
    print('Underwritten by Codex, absent from Claude:',only_mine)

if __name__=='__main__': main()
