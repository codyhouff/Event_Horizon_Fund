"""Step 2 cross-critique model: Claude inputs vs Codex inputs vs Claude re-underwrite.

Per-share terminal value (TV) at 2030-12-31 = metric x multiple + extras (dividends, excess cash).
E[TV] = sum p*TV ; CAGR = (E[TV]/P)^(1/T) - 1 (never averaged).
Named scenarios (PROMPT_1 definitions, rules stated in the critique):
  AI-2027 Scenario  : bull-case 2030 metric x BASE multiple (+ bull-case extras).
                      Cyclicals with inverse multiples (MU) use the bull (peak) multiple.
  100GW 2030 Scenario: bull-case metric x U(ticker) x same multiple (+ bull extras).
"""
import json, sys

T6 = 4.150582  # Nov 6 2026 close -> Dec 31 2030
T9 = 4.142     # Nov 9 2026 close -> Dec 31 2030

P6 = {"TSM":375.44,"NVDA":186.64,"AVGO":293.69,"MU":690.00,"ASML":1424.75,"SNPS":450.46,"CEG":249.95,
      "VST":124.80,"VRT":182.86,"COHR":192.81,"ETN":341.72,"CRDO":120.51,"PWR":540.90,"KTOS":35.10,
      "MP":35.41,"BNTX":87.51,"CLS":206.68,"NVT":106.22,"NRG":88.29}
P9 = {"TSM":388.62,"NVDA":178.67,"AVGO":319.48,"MU":733.15,"ASML":1513.25,"SNPS":466.97,"CEG":276.09,
      "VST":133.92,"VRT":200.47,"COHR":225.19,"ETN":359.30,"CRDO":132.89,"PWR":591.48,"KTOS":37.69,
      "MP":37.75,"BNTX":87.51,"CLS":222.92,"NVT":114.44,"NRG":97.40}

# 100GW uplift on the bull metric (bottleneck capture in SA's path; judgment, stated in critique)
U = {"TSM":1.3,"ASML":1.3,"MU":1.3,"NVDA":1.2,"AVGO":1.2,"COHR":1.2,"CRDO":1.2,"CLS":1.2,"VRT":1.3,
     "NVT":1.3,"ETN":1.3,"PWR":1.3,"VST":1.3,"NRG":1.3,"CEG":1.3,"SNPS":1.1,"KTOS":1.0,"MP":1.1,"BNTX":1.0}
INVERSE = {"MU"}          # cyclical: named scenarios use the bull (peak) multiple
CASHBACKED = {"BNTX"}     # TV given directly

# ---- Claude original (valuation_model.py, Rev 2) : m metric, x multiple, e extras (same all states)
MINE = {
 "TSM":  dict(m=(21,33,42), x=(13,19,23), e=(14,14,14), pr=(20,50,30)),
 "NVDA": dict(m=(8,19,28), x=(14,18,22), e=(1,1,1), pr=(25,50,25)),
 "AVGO": dict(m=(13,24,38), x=(15,20,24), e=(12,12,12), pr=(30,45,25)),
 "MU":   dict(m=(45,130,290), x=(11,9,7), e=(2,2,2), pr=(25,45,30)),
 "ASML": dict(m=(50,88,108), x=(20,28,32), e=(40,40,40), pr=(20,50,30)),
 "SNPS": dict(m=(19,27,33), x=(19,28,33), e=(0,0,0), pr=(25,50,25)),
 "VRT":  dict(m=(8.5,15.5,21), x=(15,23,28), e=(1,1,1), pr=(25,50,25)),
 "CEG":  dict(m=(13,19.5,24), x=(14,20,24), e=(7,7,7), pr=(25,50,25)),
 "VST":  dict(m=(10,20,25), x=(8,12,14), e=(4,4,4), pr=(30,45,25)),
 "PWR":  dict(m=(21,31,37), x=(18,25,29), e=(2,2,2), pr=(25,50,25)),
 "KTOS": dict(m=(0.6,1.9,2.8), x=(20,30,38), e=(0,0,0), pr=(30,45,25)),
 "MP":   dict(m=(0.5,1.8,3.0), x=(25,26,30), e=(0,0,0), pr=(30,45,25)),
 "COHR": dict(m=(8,19,27), x=(12,18,22), e=(0,0,0), pr=(30,45,25)),
 "ETN":  dict(m=(15,23,27), x=(17,24,28), e=(17,17,17), pr=(25,50,25)),
 "CRDO": dict(m=(4,10.5,17), x=(14,22,28), e=(0,0,0), pr=(30,45,25)),
 "BNTX": dict(tv=(65,120,210), pr=(30,45,25)),
 "CLS":  dict(m=(12,27,35), x=(10,14,17), e=(0,0,0), pr=(30,45,25)),
}

# ---- Codex inputs (Codex Deep Dive 4.4 ledger). Earnings: rev, margin%, shares, mult, div, cash/sh
CX_E = {
 "TSM":  ((140,310,430),(32,45,47),(5.3,5.2,5.15),(15,23,28),(15,20,25),(0,0,0),(25,50,25)),
 "NVDA": ((350,850,1400),(32,46,50),(24,23.5,23),(18,25,30),(4,6,8),(0,0,0),(25,50,25)),
 "AVGO": ((100,250,400),(38,50,52),(5,4.9,4.8),(18,24,28),(10,13,16),(0,0,0),(25,50,25)),
 "MU":   ((120,240,360),(20,40,50),(1.2,1.2,1.2),(12,12,15),(4,8,12),(40,150,250),(30,50,20)),
 "ASML": ((40,70,100),(24,34,37),(0.385,0.375,0.365),(20,30,35),(30,40,50),(0,0,0),(25,50,25)),
 "SNPS": ((10,16,23),(18,30,34),(0.205,0.2,0.205),(23,30,35),(0,0,0),(0,0,0),(25,50,25)),
 "VRT":  ((12,30,48),(10,20,23),(0.39,0.38,0.375),(18,26,30),(1,2,3),(0,0,0),(25,50,25)),
 "CEG":  ((35,50,65),(7,12,15),(0.36,0.35,0.34),(14,22,26),(9,12,15),(0,0,0),(25,50,25)),
 "PWR":  ((32,60,80),(5,8,9.5),(0.15,0.15,0.15),(18,25,30),(2,3,4),(0,0,0),(25,50,25)),
 "KTOS": ((2.1,3.8,6),(2,7,10),(0.22,0.23,0.24),(18,28,35),(0,0,0),(0,0,0),(30,50,20)),
 "MP":   ((0.6,2,3.5),(2,22,28),(0.2,0.21,0.22),(16,24,30),(0,0,0),(0,0,0),(35,45,20)),
 "COHR": ((7,20,30),(8,20,23),(0.22,0.22,0.23),(15,24,28),(0,0,0),(0,0,0),(30,50,20)),
 "ETN":  ((29,48,65),(12,18,21),(0.39,0.38,0.38),(18,25,29),(18,22,26),(0,0,0),(25,50,25)),
 "CRDO": ((2,5,9),(15,28,32),(0.21,0.22,0.23),(18,28,35),(0,0,0),(0,0,0),(30,50,20)),
 "CLS":  ((25,65,100),(3.5,6.5,8),(0.14,0.14,0.145),(10,17,20),(0,0,0),(0,0,0),(30,50,20)),
 "NVT":  ((5.5,10,15),(10,17,20),(0.16,0.16,0.16),(16,22,26),(3,4,5),(0,0,0),(25,50,25)),
}
# EV models: rev, ebitda margin%, shares, EV mult, div, net claims $bn
CX_EV = {
 "VST": ((20,28,36),(30,39.3,41.7),(0.34,0.30,0.28),(7,9,10),(4,5,6),(26,20,15),(25,50,25)),
 "NRG": ((25,32,40),(18,21.9,22.5),(0.22,0.20,0.19),(6.5,8,9),(7,8,9),(18,14,10),(25,50,25)),
}

# ---- Claude re-underwrite (inputs chosen per row in the critique; same units as MINE)
# bear = 50/50 mixture of a bust (earnings back to ~2025 level) and Claude's original mild bear
RE = {
 "NVDA": dict(m=(6.4,19,28), x=(14,18,25), e=(1,1,1), pr=(25,50,25)),
 "TSM":  dict(m=(15.5,33,42), x=(13,19,23), e=(14,14,14), pr=(25,50,25)),
 "AVGO": dict(m=(9.9,25.5,43.3), x=(15,20,24), e=(6,12,12), pr=(30,45,25)),   # bear e: 12 divs - ~6/sh XPV guarantee loss
 "MU":   dict(m=(25,130,290), x=(11,9,7), e=(42,152,252), pr=(25,50,25)),      # adds Codex excess-cash reserve
 "ASML": dict(m=(39,88,108), x=(20,28,32), e=(30,40,40), pr=(25,50,25)),
 "SNPS": dict(m=(16,27,33), x=(19,28,33), e=(0,0,0), pr=(25,50,25)),
 "VRT":  dict(m=(6.3,15.5,21), x=(15,23,28), e=(1,1,1), pr=(25,50,25)),
 "CEG":  dict(m=(11.2,19.5,24), x=(14,20,24), e=(7,7,7), pr=(25,50,25)),
 "VST":  dict(m=(9.4,20,25), x=(8,12,14), e=(4,4,4), pr=(30,45,25)),
 "NRG":  dict(m=(10.5,19,25), x=(6,9,11), e=(7,8,9), pr=(30,45,25)),        # FCFbG/share
 "NVT":  dict(m=(4.8,10,14), x=(14,19,23), e=(3,3,4), pr=(25,50,25)),
 "CLS":  dict(m=(9,30,40), x=(10,14,17), e=(0,0,0), pr=(30,45,25)),
 "COHR": dict(m=(5.75,19,27), x=(12,18,22), e=(0,0,0), pr=(30,45,25)),
 "ETN":  dict(m=(13.5,23,27), x=(17,24,28), e=(17,17,17), pr=(25,50,25)),
 "CRDO": dict(m=(2.8,8.5,13.8), x=(14,22,28), e=(0,0,0), pr=(30,45,25)),      # owner EPS after SBC (~0.81x adjusted)
 "PWR":  dict(m=(15.8,31,37), x=(18,25,29), e=(2,2,2), pr=(25,50,25)),
 "KTOS": dict(m=(0.42,1.33,1.96), x=(20,30,38), e=(0,0,0), pr=(30,45,25)),   # owner EPS after SBC (~0.7x adjusted)
 "MP":   dict(m=(0.5,1.8,3.0), x=(25,26,30), e=(0,0,0), pr=(30,45,25)),
 "BNTX": dict(tv=(65,120,210), pr=(30,45,25)),
}

def cagr(tv, p, t):
    return ((tv / p) ** (1 / t) - 1) * 100 if tv > 0 else -100.0

def simple(d, k):
    if "tv" in d:
        tvs = list(d["tv"]); a27 = tvs[1]; g100 = tvs[1]
    else:
        m, x, e = d["m"], d["x"], d["e"]
        tvs = [m[i] * x[i] + e[i] for i in range(3)]
        mx = x[2] if k in INVERSE else x[1]
        a27 = m[2] * mx + e[2]
        g100 = m[2] * U[k] * mx + e[2]
    pr = [q / 100 for q in d["pr"]]
    etv = sum(a * b for a, b in zip(pr, tvs))
    return dict(tv=[round(v, 1) for v in tvs], pr=d["pr"], etv=round(etv, 1), a27=round(a27, 1), g100=round(g100, 1),
                base_m=(d.get("m") or [None]*3)[1], base_x=(d.get("x") or [None]*3)[1])

def codex_e(k):
    rv, mg, sh, mu, dv, ca, pr = CX_E[k]
    eps = [rv[i] * mg[i] / 100 / sh[i] for i in range(3)]
    tvs = [eps[i] * mu[i] + dv[i] + ca[i] for i in range(3)]
    mx = mu[2] if k in INVERSE else mu[1]
    a27 = eps[2] * mx + dv[2] + ca[2]
    g100 = eps[2] * U[k] * mx + dv[2] + ca[2]
    p = [q / 100 for q in pr]
    etv = sum(a * b for a, b in zip(p, tvs))
    return dict(tv=[round(v, 1) for v in tvs], pr=pr, etv=round(etv, 1), a27=round(a27, 1), g100=round(g100, 1),
                base_m=round(eps[1], 2), base_x=mu[1], eps=[round(v, 2) for v in eps])

def codex_ev(k):
    rv, mg, sh, mu, dv, cl, pr = CX_EV[k]
    eb = [rv[i] * mg[i] / 100 for i in range(3)]
    tvs = [max(0, eb[i] * mu[i] - cl[i]) / sh[i] + dv[i] for i in range(3)]
    a27 = max(0, eb[2] * mu[1] - cl[2]) / sh[2] + dv[2]
    g100 = max(0, eb[2] * U[k] * mu[1] - cl[2]) / sh[2] + dv[2]
    p = [q / 100 for q in pr]
    etv = sum(a * b for a, b in zip(p, tvs))
    return dict(tv=[round(v, 1) for v in tvs], pr=pr, etv=round(etv, 1), a27=round(a27, 1), g100=round(g100, 1),
                base_m=round(eb[1], 2), base_x=mu[1])

TICKERS = list(P6)
OUT = {"mine": {}, "codex": {}, "re": {}}
for k in TICKERS:
    if k in MINE:
        r = simple(MINE[k], k)
        r.update(cagr6=round(cagr(r["etv"], P6[k], T6), 1), a27_6=round(cagr(r["a27"], P6[k], T6), 1),
                 g100_6=round(cagr(r["g100"], P6[k], T6), 1))
        OUT["mine"][k] = r
    if k in CX_E or k in CX_EV:
        r = codex_e(k) if k in CX_E else codex_ev(k)
        r.update(cagr6=round(cagr(r["etv"], P6[k], T6), 1), a27_6=round(cagr(r["a27"], P6[k], T6), 1),
                 g100_6=round(cagr(r["g100"], P6[k], T6), 1))
        OUT["codex"][k] = r
    r = simple(RE[k], k)
    r.update(cagr6=round(cagr(r["etv"], P6[k], T6), 1), cagr9=round(cagr(r["etv"], P9[k], T9), 1),
             a27_9=round(cagr(r["a27"], P9[k], T9), 1), g100_9=round(cagr(r["g100"], P9[k], T9), 1),
             bear9=round((r["tv"][0] / P9[k] - 1) * 100, 1))
    OUT["re"][k] = r

HEDGE = {"KTOS", "MP", "BNTX"}  # AI-independent: base TV in an AI bust

def port(w, model, prices, t):
    tot = sum(w.values()); assert abs(tot - 100) < 1e-9, tot
    src = OUT[model]
    def mult(key):
        s = 0
        for k, wt in w.items():
            r = src[k]
            v = r["tv"][1] if (key == "bust" and k in HEDGE) else (r["tv"][0] if key == "bust" else r[key])
            s += wt / 100 * v / prices[k]
        return s
    e = mult("etv"); a = mult("a27"); g = mult("g100"); b = mult("bust")
    c = lambda m: round(((m ** (1 / t)) - 1) * 100, 1)
    return dict(E=c(e), A27=c(a), G100=c(g), bust_total=round((b - 1) * 100, 1), n=len(w))

V10 = {"TSM":14,"NVDA":13,"VRT":9,"VST":9,"MU":9,"ASML":8,"AVGO":6,"SNPS":6,"CEG":6,"COHR":5,"ETN":5,"CRDO":3,"PWR":2,"KTOS":2,"MP":2,"BNTX":1}
CX8 = {"NVDA":15,"AVGO":15,"VRT":15,"CLS":12,"NVT":12,"NRG":12,"VST":11,"COHR":8}
REV = json.loads(sys.argv[2]) if len(sys.argv) > 2 else None

PORT = {}
PORT["V10 | Claude inputs | Nov6"] = port(V10, "mine", P6, T6)
PORT["V10 | Codex inputs | Nov6"] = None  # BNTX not modeled by Codex
PORT["CX8 | Codex inputs | Nov6"] = port(CX8, "codex", P6, T6)
PORT["V10 | re-underwrite | Nov6"] = port(V10, "re", P6, T6)
PORT["CX8 | re-underwrite | Nov6"] = port(CX8, "re", P6, T6)
PORT["V10 | re-underwrite | Nov9"] = port(V10, "re", P9, T9)
PORT["CX8 | re-underwrite | Nov9"] = port(CX8, "re", P9, T9)
if REV:
    PORT["REVISED | re-underwrite | Nov9"] = port(REV, "re", P9, T9)
    PORT["REVISED | re-underwrite | Nov6"] = port(REV, "re", P6, T6)
json.dump({"OUT": OUT, "PORT": PORT, "P6": P6, "P9": P9}, open(sys.argv[1], "w"), indent=1)

print(f"{'tkr':5} | {'mine E/A27/G100 @6':22} | {'codex E/A27/G100 @6':22} | {'RE E@6':6} {'RE E@9':6} {'A27@9':6} {'G100@9':6} {'bear9%':6}")
for k in sorted(TICKERS, key=lambda k: -OUT["re"][k]["cagr9"]):
    m = OUT["mine"].get(k); c = OUT["codex"].get(k); r = OUT["re"][k]
    ms = f"{m['cagr6']:5}/{m['a27_6']:5}/{m['g100_6']:5}" if m else "n/a"
    cs = f"{c['cagr6']:5}/{c['a27_6']:5}/{c['g100_6']:5}" if c else "n/a"
    print(f"{k:5} | {ms:22} | {cs:22} | {r['cagr6']:6} {r['cagr9']:6} {r['a27_9']:6} {r['g100_9']:6} {r['bear9']:6}")
print()
for n, v in PORT.items():
    print(n, v)
