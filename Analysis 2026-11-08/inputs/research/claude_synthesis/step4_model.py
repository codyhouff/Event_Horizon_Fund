"""Step 4 (Claude optimization pass): value out-of-pool candidates on the SAME A1 rules as step3_model.py.

A1 rules (identical to Step 3):
  bust    = FY2025-equivalent owner EPS x 0.70 x base multiple (+ dividends/cash)
  plateau = FY2026-equivalent owner EPS x 0.85 x base multiple
  base    = 2027 consensus owner EPS x (1+g)^3 at the base multiple (g = stated judgment, evidence in the pass)
  bull    = base EPS x bull factor (1.4 high-growth / 1.3 other) at 1.2 x base multiple
  bear bucket = 1/2 bust + 1/2 plateau; probabilities 25/50/25
  AI-2027 = base + 0.8*s*(bull-base); 100GW = base + 2.5*s*(bull-base); both at the base multiple
  Base multiple chosen inside the evidence band [own forward P/E, peer median forward P/E].
Prices: Nov 9, 2026 close (same date of record as the final). T = 4.1424.

Usage (from this folder):
  python -I step4_model.py data/step3_out.json data/step4_snap.json data/step4_out.json
"""
import json
import sys

R3 = json.load(open(sys.argv[1]))["R"]
SNAP = json.load(open(sys.argv[2]))
OUT = sys.argv[3]
T = 4.1424
L27, L100 = 0.80, 2.50

# ticker: (FY25 owner EPS [bust], FY26 owner EPS [plateau], 2027 consensus EPS, owner factor, g base/yr, bull factor,
#          base multiple, cum. dividends, AI sensitivity s, competes with, band note)
NEW = {
 "STRL":  (9.38, 21.18, 28.10, 0.97, 0.10, 1.4, 14.0, 0.0, 0.9, "NVT/VRT", "own 10.3x, construction peers ~15.5x"),
 "AEIS":  (3.84, 10.80, 17.93, 0.87, 0.12, 1.4, 17.0, 1.6, 1.0, "VRT/NVT", "own 12.2x, electrical/semi peers ~20x"),
 "AAON":  (1.29, 2.37, 3.73, 0.93, 0.10, 1.4, 19.0, 1.6, 0.9, "VRT", "own 16.5x, thermal peers ~21x"),
 "SBGSY": (1.47, 2.30, 2.91, 1.00, 0.10, 1.3, 20.0, 4.0, 0.7, "NVT", "own 18.1x, electrical peers ~21x"),
 "GNRC":  (2.69, 9.09, 13.94, 0.92, 0.12, 1.4, 16.0, 0.0, 0.6, "NVT/VST", "own 13.5x, industrial peers ~18x"),
 "FIX":   (28.88, 50.75, 67.15, 1.00, 0.10, 1.4, 16.6, 16.4, 0.8, "NVT/VRT", "own 16.6x above construction peers ~15.5x -> own"),
 "EME":   (28.19, 34.91, 40.91, 1.00, 0.08, 1.3, 16.0, 6.6, 0.7, "NVT", "own 16.0x, peers ~15.5x"),
 "WCC":   (13.05, 17.65, 21.94, 0.96, 0.09, 1.3, 15.0, 8.2, 0.6, "NVT", "own 14.4x; electrical distribution history ~12-16x"),
 "DY":    (9.56, 15.98, 20.74, 0.94, 0.09, 1.3, 13.0, 0.0, 0.6, "NVT", "own 10.6x, construction peers ~15.5x"),
 "MKSI":  (4.37, 14.09, 19.71, 0.95, 0.06, 1.4, 15.0, 4.1, 1.0, "MU", "own 10.7x, equipment peers ~20.5x"),
 "ON":    (2.00, 3.03, 4.74, 0.92, 0.12, 1.4, 16.0, 0.0, 0.5, "MU", "own 14.6x, semis peers ~18.7x; FY25 GAAP 0.29 distorted by charges -> ~2.0"),
 "APH":   (1.67, 2.84, 3.62, 1.00, 0.12, 1.4, 21.0, 2.5, 0.8, "CLS/NVT", "own 22.3x above electrical peers ~21x -> peer"),
 "CMI":   (20.50, 27.81, 33.51, 1.00, 0.08, 1.3, 15.0, 36.0, 0.4, "VST/NVT", "own 13.7x, industrial peers ~18x"),
 "ORCL":  (3.00, 6.85, 11.06, 0.84, 0.12, 1.4, 15.0, 8.2, 1.0, "META", "own 10.8x, platforms 22.5x; financing discount. Bust 3.0 (OpenAI-failure state, below FY25 GAAP 5.83)"),
 "IFNNY": (0.85, 1.84, 3.40, 0.93, 0.10, 1.3, 17.0, 1.7, 0.5, "MU", "own 16.4x, semis peers ~18.7x"),
 "ASX":   (0.56, 1.25, 2.18, 1.00, 0.10, 1.4, 17.0, 1.7, 1.0, "MU/CLS", "own 15.8x, equipment peers ~20.5x; FY25 NT$17.78/ADR = ~$0.56"),
 "KLIC":  (0.00, 3.24, 5.90, 0.84, 0.06, 1.4, 15.0, 3.4, 1.0, "MU", "own 11.7x, equipment peers ~20.5x"),
}
# Cyclical storage (explicit states, MU-style): (EPS, multiple, cum. div, net cash/sh) for bust, plateau, base, bull
CYC = {
 "WDC": dict(st=((9.0, 12, 2, 10), (24.72, 11.5, 2, 30), (32.0, 11, 3, 50), (48.0, 10, 4, 80)), s=1.0, comp="MU",
             note="FYE Jun. Bust ~FY26 adjusted (GAAP 24.28 includes stake gains); plateau FY27E 24.72; base 2030 = FY28E 40.40 normalized -21% (less than MU's -47%: duopoly, LTAs to 2030-31)"),
 "STX": dict(st=((16.0, 12, 12, 0), (39.98, 11.5, 12, 40), (52.0, 11, 12, 60), (78.0, 10, 14, 100)), s=1.0, comp="MU",
             note="FYE Jun. Bust ~FY26 adjusted; plateau FY27E 39.98; base 2030 = FY28E 65.34 normalized -20%"),
}
# Pool names re-underwritten (the ranking got them wrong): AVGO base owner EPS 23.5 -> 27.0
AVGO_REV = dict(eps=(5.93, 10.15, 27.0, 37.7), x=20, d=(11, 11, 13, 16), c=(-8, -4, -2, 0), s=1.0)


def cagr(tv, p):
    return ((tv / p) ** (1 / T) - 1) * 100 if tv > 0 else -100.0


def pack(k, p, tvs, ai, gw, extra):
    bear = 0.5 * tvs[0] + 0.5 * tvs[1]
    etv = 0.25 * bear + 0.5 * tvs[2] + 0.25 * tvs[3]
    return dict(price=p, tv=dict(bust=tvs[0], plateau=tvs[1], bear=bear, base=tvs[2], bull=tvs[3]), etv=etv, E=cagr(etv, p),
                A27=cagr(ai, p), G100=cagr(gw, p), ai_tv=ai, gw_tv=gw, bust=(tvs[0] / p - 1) * 100, delay=(tvs[1] / p - 1) * 100,
                base_ret=(tvs[2] / p - 1) * 100, pr=[25, 50, 25], **extra)


R = {}
for k, (b25, p26, e27, own, g, bf, x, dv, s, comp, note) in NEW.items():
    p = SNAP[k]["closes"]["2026-11-09"]
    base = e27 * own * (1 + g) ** 3
    bull = base * bf
    xs = (0.70 * x, 0.85 * x, x, 1.20 * x)
    eps = (b25, p26, base, bull)
    tvs = tuple(max(0.0, e * m) + dv for e, m in zip(eps, xs))
    named = lambda L: max(0.0, (base + L * s * (bull - base)) * x) + dv
    R[k] = pack(k, p, tvs, named(L27), named(L100),
                dict(eps=[round(e, 2) for e in eps], mult=[round(m, 1) for m in xs], div=dv, s=s, competes=comp, note=note,
                     g=g, fwdPE=SNAP[k].get("forwardPE"), method="Earnings (A1)"))

for k, c in CYC.items():
    p = SNAP[k]["closes"]["2026-11-09"]
    tvs = tuple(e * m + d + cash for e, m, d, cash in c["st"])
    b, u = c["st"][2], c["st"][3]
    named = lambda L: (b[0] + L * c["s"] * (u[0] - b[0])) * b[1] + b[2] + b[3] + min(L, 1) * c["s"] * (u[3] - b[3])
    R[k] = pack(k, p, tvs, named(L27), named(L100), dict(states=c["st"], s=c["s"], competes=c["comp"], note=c["note"],
                                                         fwdPE=SNAP[k].get("forwardPE"), method="Cyclical explicit (A1)"))

a = AVGO_REV
xm = (0.70 * a["x"], 0.85 * a["x"], a["x"], 1.20 * a["x"])
tvs = tuple(max(0.0, e * m + c) + d for e, m, c, d in zip(a["eps"], xm, a["c"], a["d"]))
e = a["eps"]
named = lambda L: max(0.0, (e[2] + L * (e[3] - e[2])) * a["x"] + a["c"][2] + L * (a["c"][3] - a["c"][2])) + a["d"][2] + min(L, 1) * (a["d"][3] - a["d"][2])
R["AVGO*"] = pack("AVGO", R3["AVGO"]["price"], tvs, named(L27), named(L100),
                  dict(eps=list(e), mult=[round(m, 1) for m in xm], competes="VST/MU", method="Earnings (A1), base EPS revised",
                       note="Base owner EPS 23.5 -> 27.0: management's FY28 adjusted EPS target of >$30 (Sep 2, reaffirmed Sep 14) reached ~2 years late after a ~13% owner (stock comp) haircut"))


def port(w):
    def get(k):
        return R[k] if k in R else R3[k]
    assert abs(sum(w.values()) - 100) < 1e-9
    m = lambda f: sum(wt / 100 * f(get(k)) / get(k)["price"] for k, wt in w.items())
    em = m(lambda r: r["etv"])
    return dict(E=(em ** (1 / T) - 1) * 100, A27=(m(lambda r: r["ai_tv"]) ** (1 / T) - 1) * 100,
                G100=(m(lambda r: r["gw_tv"]) ** (1 / T) - 1) * 100, bust=(m(lambda r: r["tv"]["bust"]) - 1) * 100,
                delay=(m(lambda r: r["tv"]["plateau"]) - 1) * 100, hhi=sum((v / 100) ** 2 for v in w.values()), n=len(w))


V10 = {"NVDA": 15, "META": 15, "VRT": 14, "MU": 14, "NRG": 12, "NVT": 12, "CLS": 10, "VST": 8}
VARIANTS = {
 "V10.0 final (Step 3)": V10,
 "C1: VST 8 -> AVGO 8 (AVGO revised)": {**{k: v for k, v in V10.items() if k != "VST"}, "AVGO*": 8},
 "Alt: VST 8 -> STRL 8": {**{k: v for k, v in V10.items() if k != "VST"}, "STRL": 8},
 "Alt: VST 8 -> AEIS 8": {**{k: v for k, v in V10.items() if k != "VST"}, "AEIS": 8},
 "Alt: VST 8 -> AVGO* 4 + STRL 4": {**{k: v for k, v in V10.items() if k != "VST"}, "AVGO*": 4, "STRL": 4},
 "Alt: VST 8 -> TLN 8 (pool)": {**{k: v for k, v in V10.items() if k != "VST"}, "TLN": 8},
 "Alt: MU 14 -> 10, AVGO* +4": {**V10, "MU": 10, "AVGO*": 4},
}
PO = {k: port(w) for k, w in VARIANTS.items()}
json.dump(dict(R=R, PO=PO, VARIANTS=VARIANTS), open(OUT, "w"), indent=1)

print(f"{'tkr':6}{'price':>9}{'fPE':>6}{'E':>6}{'A27':>6}{'G100':>6}{'bust':>6}{'delay':>6}{'base%':>6}  vs")
for k in sorted(R, key=lambda k: -R[k]["E"]):
    r = R[k]
    print(f"{k:6}{r['price']:9.2f}{(r.get('fwdPE') or 0):6.1f}{r['E']:6.1f}{r['A27']:6.1f}{r['G100']:6.1f}{r['bust']:6.0f}{r['delay']:6.0f}{r['base_ret']:6.0f}  {r['competes']}")
print()
for k, o in PO.items():
    print(f"{k:38} E={o['E']:5.2f} A27={o['A27']:5.2f} G100={o['G100']:5.2f} bust={o['bust']:6.1f} delay={o['delay']:6.1f} hhi={o['hhi']:.3f}")
