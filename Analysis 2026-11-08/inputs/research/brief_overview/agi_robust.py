"""AGI-conditional robustness check (Nov 11, 2026).
Assumes AI-2027 lands within ~2 years, then applies stock-specific failure modes
(judgment parameters, documented below) to the V10.2 model's terminal values.
Usage: python agi_robust.py ../codex_final_review/data/step6_out.json
"""
import sys, json, itertools
exec(open('owner2.py',encoding='utf-8').read().split("if __name__")[0])
# --- timing mix conditional on "AI-2027 within ~2 years" (points on the model's AI-pace path)
TIMING=[('base',0.20),('late1',0.25),('ai',0.35),('early1',0.15),('gw',0.05)]
def agi_tv(k):  # timing-weighted terminal multiple on the AI path
    x=mult(k); return sum(w*x[s] for s,w in TIMING)
SUPPL={'NVDA','AVGO','MU','VRT','NVT','MOD','CLS','TSM','ASML','AMAT','LRCX','KLAC','ANET','COHR','CRDO','LITE','FN','HPE','DELL','MRVL','AMD','ALAB','SNDK','ETN','PWR','GEV','POWL','WCC','AEIS'}
PLAT={'META','GOOGL','MSFT','AMZN'}
POWER={'NRG','VST','TLN','CEG','CCJ','BE'}
TAIWAN={'NVDA','MU','CLS','TSM','AVGO','AMD','MRVL','ANET','DELL','HPE','FN','COHR','LITE','CRDO','ALAB','SNDK'}
def modes(k):
    x=mult(k); A=agi_tv(k); base=x['base']; plat=x['plateau']
    out=[]
    out.append(('captured',0.45,A))
    out.append(('multiples -30% (rates)',0.15,0.70*A))
    vs = 1.20*A if k in PLAT else (1.0*A if k in POWER else (0.85*base if k in SUPPL else (0.9*base if k=='STRL' else A)))
    out.append(('value shifts to labs/platforms',0.12,vs))
    if k in ('MU','SNDK','CLS'): sc=plat
    elif k in SUPPL or k=='STRL': sc=0.8*base if k!='NVDA' else base
    elif k in PLAT: sc=1.1*A
    else: sc=base
    out.append(('supply catches up',0.10,sc))
    pp = plat if k in POWER else (0.8*base if k=='STRL' else A)
    out.append(('power politics',0.08,pp))
    tail = 0.5*A*(0.6 if k in TAIWAN else 1.0)
    out.append(('regime / Taiwan tail',0.10,tail))
    return out
def em(k): return sum(p*v for _,p,v in modes(k))
R=d
rows=[]
for k in R:
    if R[k]['tv']['bust']/R[k]['price']<=0.001: neg=True
    else: neg=False
    rows.append((k,c(em(k)),c(agi_tv(k)),R[k]['method'][:6],neg))
rows.sort(key=lambda r:-r[1])
if __name__=='__main__':
    print("AGI-conditional ranking (expected per yr across failure modes | if captured):")
    for i,(k,e,a,m,neg) in enumerate(rows[:30],1): print(f"{i:2d} {k:5s} {e:5.1f}%  captured {a:5.1f}%  {m} {'ZERO-BUST' if neg else ''}")
