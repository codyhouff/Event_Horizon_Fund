import sys, json
sys.stdout.reconfigure(encoding="utf-8")
R=json.load(open(sys.argv[1])); d=R['R']; T=R['T']
# Owner view: AI-2027 +/- ~1 year central. Points on the model's named-scenario path (L = AI-pace lever):
# L=0 base (~1.5-2y late, $2.8T 2030 capex); L=0.25 (~1y late, ~$3.2T); L=0.8 AI-2027 on time ($4.2T); L=1.4 (~1y early, ~$5.5T); L=2.5 100GW ($8T)
OV=[('bust',7.5),('plateau',7.5),('base',15),('late1',20),('ai',30),('early1',12.5),('gw',7.5)]
def pts(k):
    r=d[k]; t=r['tv']; b=t['base']; a=r['ai_tv']; g=r['gw_tv']
    return dict(bust=t['bust'],plateau=t['plateau'],base=b,late1=b+(0.25/0.8)*(a-b),ai=a,early1=a+(0.6/1.7)*(g-a),gw=g)
def mult(k):
    p=d[k]['price']; x={s:max(v,0)/p for s,v in pts(k).items()}
    x['OV']=sum(w*x[s] for s,w in OV)/100; x['E']=d[k]['etv']/p; return x
c=lambda x:(x**(1/T)-1)*100 if x>0 else -100.0
if __name__=='__main__':
    rows=[]
    for k in d:
        x=mult(k); rows.append((k,c(x['E']),c(x['OV']),c(x['base']),c(x['late1']),c(x['ai']),c(x['early1']),c(x['gw']),(x['bust']-1)*100,(x['plateau']-1)*100,d[k].get('method','')[:14]))
    rows.sort(key=lambda r:-r[2])
    print("rk|tk|ModelE|OwnerE|base|1yLate|AI27|1yEarly|100GW|bust|delay|method")
    for i,r in enumerate(rows,1): print(i,'|'.join([r[0]]+[f"{v:.1f}" for v in r[1:10]]+[r[10]]))
    base=dict(NVDA=15,META=15,VRT=14,MU=14,NRG=12,NVT=12,CLS=10,STRL=8)
    P={"V10.2":base,"D7 MOD5":{**base,'VRT':11,'NVT':10,'MOD':5},"MOD8":{**base,'VRT':10,'NVT':8,'MOD':8},
       "MOD5+tilt":dict(NVDA=15,META=15,VRT=15,MU=15,NRG=10,NVT=5,CLS=10,STRL=10,MOD=5),
       "noMOD tilt":dict(NVDA=15,META=15,VRT=15,MU=15,NRG=10,NVT=10,CLS=10,STRL=10),
       "META->AVGO":{**base,'META':0,'AVGO':15},
       "META10 MU15 AVGO..":dict(NVDA=15,META=10,VRT=15,MU=15,NRG=10,NVT=10,CLS=10,STRL=10,AVGO=5),
       "MOD8 + MU15 STRL10 NRG10":dict(NVDA=15,META=15,VRT=10,MU=15,NRG=10,NVT=7,CLS=10,STRL=10,MOD=8)}
    print()
    for n,w in P.items():
        assert sum(w.values())==100,n
        a={s:sum(w[k]*mult(k)[s] for k in w)/100 for s in ['E','OV','base','late1','ai','early1','gw','bust','plateau']}
        print(f"{n:26s} E {c(a['E']):.2f} OV {c(a['OV']):.2f} | base {c(a['base']):.1f} late1 {c(a['late1']):.1f} ai {c(a['ai']):.1f} early1 {c(a['early1']):.1f} gw {c(a['gw']):.1f} | bust {(a['bust']-1)*100:.1f} delay {(a['plateau']-1)*100:.1f} | $100k: OV {a['OV']*100:.0f} base {a['base']*100:.0f} late1 {a['late1']*100:.0f} ai {a['ai']*100:.0f} early1 {a['early1']*100:.0f} gw {a['gw']*100:.0f} E {a['E']*100:.0f}")
