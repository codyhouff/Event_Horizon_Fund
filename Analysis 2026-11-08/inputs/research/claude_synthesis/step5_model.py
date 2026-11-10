"""Event Horizon Fund - Step 5 final-assembly model (Claude, cycle 2026-11-08).

Identical to step3_model.py except for the Step 5 input decisions (see the Step 5 Decision Log):
  D1 (Claude C1) AVGO base owner EPS 23.5 -> 27.0 (management FY28 adjusted EPS > $30 target)
  D2 (Codex sanity #5) no double SBC haircut: VRT plateau 7.05 -> 7.19; NVT bust 3.22 -> 3.35, plateau 5.16 -> 5.38
  D3 (Codex O1) WCC added with Claude's consensus-anchored inputs (Codex bridge rejected; see log)
  D4 (Codex O2, Claude C2) STRL added with Codex's explicit operating bridge (base $9.0B revenue x 15% / 31.5m sh)


ONE consistent model for the whole candidate pool at the Nov 9, 2026 close.

Terminal date 2030-12-31.  T = (2030-12-31 - 2026-11-09) / 365.25 = 4.1424 years.

A1 states per stock (2030 owner earnings; per-share terminal value TV = EPS x multiple + cum. dividends + cash/reserve):
  bust    : AI capex falls back toward the 2025 level by 2030. EPS = FY2025 owner EPS. Multiple = 0.70 x base.
  plateau : AI capex stalls near the 2026 level, growth resumes 2-3 years late. EPS = FY2026 owner EPS. Multiple = 0.85 x base.
  base    : judgment input resolved per PROMPT_3 A4.          Multiple = base (A4-resolved, peer-band policy).
  bull    : judgment input resolved per PROMPT_3 A4.          Multiple = 1.20 x base.
  Bear bucket TV = 0.5 bust + 0.5 plateau.  Default probabilities bear/base/bull = 25/50/25.
  Cyclicals (MU, SNDK) and EV-valued power/neoclouds carry explicit state inputs (documented per ticker).
Named scenarios (single conditional paths, never folded into E):
  AI-2027 : metric = base + 0.80 * s * (bull - base) at the base multiple      (2030 AI capex $4.2T vs base $2.8T / bull $4.5T)
  100GW   : metric = base + 2.50 * s * (bull - base) at the base multiple      (SA $8T; linear 3.06 x 0.8 capture)
  s = AI-capex sensitivity of the stock's bull-base spread (1.0 AI hardware chain ... 0 biotech).
E[TV] = sum(p * TV); CAGR = (E[TV]/P)^(1/T) - 1.  CAGRs are never averaged.
Tags: C = Claude value adopted, X = Codex value adopted, B = both agreed, A = A1 rule / neither model.
"""
import json, sys, datetime as dt

SNAP = json.load(open(sys.argv[1]))
CXV = json.load(open(sys.argv[2]))["stocks"]          # Codex deep-dive ledger (56 names)
OUT = sys.argv[3]
T = (dt.date(2030, 12, 31) - dt.date(2026, 11, 9)).days / 365.25
P = {k: v["closes"]["2026-11-09"] for k, v in SNAP.items() if "closes" in v and "2026-11-09" in v["closes"]}
P6 = {k: v["closes"].get("2026-11-06") for k, v in SNAP.items() if "closes" in v}

L27, L100 = 0.80, 2.50   # named-scenario loadings (A1)

# ---------------------------------------------------------------- full A1 contenders (earnings method)
# eps: (bust, plateau, base, bull) owner EPS ; x: base multiple ; d: cum dividends per state ; c: cash/reserve per state
# xm: optional explicit multiples per state (cyclicals) ; pr: (bear, base, bull) ; s: AI sensitivity
E = {
 "NVDA": dict(eps=(4.90, 9.03, 19.0, 28.0), x=18, d=(4, 4, 5, 6), pr=(25, 50, 25), s=1.0, cl="C1",
             tag="bust FY26(Jan) GAAP 4.90; plat FY27E 9.31x0.97 SBC; base 19 C (X 16.64 implies flat 2027-30 EPS vs FY28E 15.92); bull 28 C (tie->lower vs X 30.4); x18 C (in peer band 11.2-18.7; X 22 above)"),
 "AVGO": dict(eps=(5.93, 10.15, 27.0, 37.7), x=20, d=(11, 11, 13, 16), c=(-8, -4, -2, 0), pr=(25, 50, 25), s=1.0, cl="C1",
             tag="bust FY25 adj 6.82x0.87 owner; plat FY26 11.67x0.87; base 23.5 X (owner, after 13% SBC); bull 43.3x0.87=37.7 C-owner (tie->lower vs X 40.4); x20 B; credit reserve X (Oct 27 8-K ~$43B max exposure); probs 25/50/25 X (reserve, not prob, carries XPV)"),
 "VRT":  dict(eps=(3.41, 7.19, 15.0, 21.0), x=23, d=(1, 1, 1.5, 2), pr=(25, 50, 25), s=1.0, cl="C3",
             tag="bust FY25 GAAP 3.41; plat 2026E 7.19x0.98; base 15.0 X (tie->lower vs C 15.5); bull 21 C (tie->lower vs X 26.1); x23 C (tie->lower vs X 24)"),
 "CLS":  dict(eps=(5.63, 10.75, 29.14, 40.0), x=14, d=(0, 0, 0, 0), pr=(25, 50, 25), s=1.0, cl="C1",
             tag="bust FY25 adj 6.05x0.93; plat 2026E 11.56x0.93; base 29.14 X (owner, 145m sh); bull 40 C (tie->lower vs X 47.5); x14 C (EMS peers ~10, FN 15; X 16 further above band); probs 25/50/25 X (dilution/cash in inputs)"),
 "NVT":  dict(eps=(3.35, 5.38, 10.0, 14.0), x=19, d=(3, 3.5, 4, 5), pr=(25, 50, 25), s=1.0, cl="C3",
             tag="bust FY25 adj 3.35x0.96; plat 2026 guide 5.36-5.39 x0.96; base 10.0 C (tie->lower vs X 10.6); bull 14 C (tie->lower vs X 16.6); x19 C (both in band 16.4-21.8; tie->lower vs X 22)"),
 "MU":   dict(eps=(20, 45, 110, 187.5), xm=(11, 10.5, 10, 9), d=(4, 6, 8, 12), c=(40, 90, 150, 250), pr=(25, 50, 25), s=1.0, cl="C1",
             tag="cyclical explicit: bust X bear (EPS20 x11 +cash40); plat EPS45 A (2026 demand plateau vs ~15-20%/yr bit supply growth); base 110 x10 +cash150 X (conceded-to, tie->lower vs C 130x9); bull X (tie->lower vs C)"),
 "TSM":  dict(eps=(10.4, 17.5, 33.0, 41.1), x=19, d=(15, 16, 17, 20), pr=(25, 50, 25), s=1.0, cl="C1",
             tag="bust 2025 ADR EPS NT$331/~32 = $10.4; plat 2026E 17.50; base 33 C (X 30.1 = 8.8%/yr from CY27E 23.4 understates base path); bull 41.1 X (tie->lower vs C 42); x19 C (in band 16.6-19; X 21 above); probs 25/50/25 (C conceded 30% bull)"),
 "ASML": dict(eps=(24.71, 41.41, 85.65, 108.0), x=28, d=(30, 35, 40, 50), pr=(25, 50, 25), s=1.0, cl="C2",
             tag="bust FY25 GAAP 24.71; plat 2026E 41.41; base 85.65 X (unit bridge; tie->lower vs C 88); bull 108 C (tie->lower vs X 144); x28 B"),
 "CEG":  dict(eps=(7.40, 12.65, 19.5, 24.0), x=20, d=(6, 6.5, 7, 8), pr=(25, 50, 25), s=0.7, cl="C4",
             tag="bust FY25 GAAP 7.40; plat 2026 guide 12.50-12.80 (raised Nov 9); base 19.5 C (tie->lower vs X 19.7); bull 24 C (tie->lower vs X 30); x20 B"),
 "COHR": dict(eps=(4.12, 9.13, 15.65, 23.8), x=18, d=(0, 0, 0, 0), pr=(25, 50, 25), s=1.0, cl="C1",
             tag="bust FY26(Jun) GAAP 4.12; plat FY27E 10.38x0.88; base 15.65 X (owner; tie->lower vs C 19x0.88=16.7); bull 27x0.88=23.8 C (tie->lower vs X 25.7); x18 C (optics peers ~15; X 20 further above)"),
 "CRDO": dict(eps=(2.51, 5.11, 8.35, 13.8), x=22, d=(0, 0, 0, 0), pr=(25, 50, 25), s=1.0, cl="C1",
             tag="bust FY26(Apr) GAAP 2.51; plat FY27E 6.31x0.81; base 8.35 X (owner); bull 13.8 C-owner (tie->lower vs X 17.6); x22 B"),
 "SNPS": dict(eps=(8.04, 10.45, 18.9, 23.1), x=28, d=(0, 0, 0, 0), pr=(25, 50, 25), s=0.7, cl="C2",
             tag="bust FY25 GAAP 8.04; plat FY26E 15.14x0.69 (SBC ~31% of adj EPS); base 27x0.70=18.9 C-owner (X 24 assumes 30% margin AFTER SBC, above current ~23-25%); bull 33x0.70 C; x28 C (tie->lower vs X 30)"),
 "ETN":  dict(eps=(10.45, 13.78, 22.7, 27.0), x=24, d=(17, 18, 20, 22), pr=(25, 50, 25), s=0.8, cl="C3",
             tag="bust FY25 GAAP 10.45; plat 2026E 13.78; base 22.7 X (tie->lower vs C 23); bull 27 C (tie->lower vs X 35.9); x24 B"),
 "PWR":  dict(eps=(6.80, 17.1, 31.0, 37.0), x=25, d=(2, 2, 2, 3), pr=(25, 50, 25), s=0.8, cl="C3",
             tag="bust FY25 GAAP 6.80; plat 2026E 18.17x0.94; base 31 C (tie->lower vs X 32); bull 37 C (vs X 50.7); x25 B"),
 "KTOS": dict(eps=(0.13, 0.66, 1.33, 1.96), x=28, d=(0, 0, 0, 0), pr=(30, 50, 20), s=0.3, cl="C6",
             tag="bust FY25 GAAP 0.13; plat 2026E 0.84x0.78; base 1.33 C-owner (tie->lower vs X 1.37); bull 1.96 C (vs X 2.4); x28 X (tie->lower vs C 30); probs 30/50/20 X"),
 "MP":   dict(eps=(0.0, 0.73, 1.8, 3.0), x=24, d=(0, 0, 0, 0), c=(2, 0, 0, 0), pr=(30, 50, 20), s=0.5, cl="C6",
             tag="bust: 2025 loss -> net cash $2/sh floor; plat 2027E 0.73 (ramp; 2026 ~0); base 1.8 C (vs X 2.1); bull 3.0 C (vs X 4.45); x24 X (tie->lower vs C 26); probs 30/50/20 X"),
 "LRCX": dict(eps=(5.76, 9.65, 12.38, 18.0), x=19, d=(5, 6, 7, 8), pr=(25, 50, 25), s=1.0, cl="C2",
             tag="bust FY26(Jun) GAAP 5.76; plat FY27E 9.65; base 12.38 X (tie->lower vs C 14); bull 18 C (vs X 22.5); x19 C (in band 18.1-20.5; X 22 above)"),
 "META": dict(eps=(29.69, 29.12, 49.23, 87.69), x=20, d=(8, 9, 10, 12), pr=(25, 50, 25), s=0.6, cl="C5",
             tag="bust FY25 GAAP 23.49 + 6.20 one-time tax charge; plat 2026E 29.12; base 49.23 X (only model); bull 87.69 X (only model); x20 C-critique (in band 18.0-22.5; X 23 above)"),
 "MSFT": dict(eps=(17.95, 20.01, 34.47, 52.78), x=23.5, d=(14, 15, 16, 20), pr=(25, 50, 25), s=0.6, cl="C5",
             tag="bust FY26(Jun) GAAP 17.95; plat FY27E 20.01; base/bull X (only model); x23.5 A (X 29 is 29% above band 22.5 -> band top + 1)"),
 "MOD":  dict(eps=(2.0, 4.70, 8.84, 19.05), x=22, d=(0, 0, 0, 0), pr=(30, 50, 20), s=1.0, cl="C3",
             tag="post-spin perimeter: bust X bear EPS 2.0; plat FY27E 4.99x0.94; base/bull X (only model); x22 X (8% above band top 20.4, within 15% tolerance); probs 30/50/20 X"),
 "VRSK": dict(eps=(6.48, 7.39, 12.375, 17.87), x=23, d=(8, 8.5, 9, 10), pr=(25, 50, 25), s=0.3, cl="C5",
             tag="bust FY25 GAAP 6.48; plat 2026E 7.70x0.96; base/bull X (only model); x23 A (X 28 is 22% above band 21.4-23.0; ~8% growth earns no premium over own 23.0x)"),
 "STRL": dict(eps=(10.2586, 20.8525, 42.8571, 63.0303), x=14, d=(0, 0, 0, 0), pr=(25, 50, 25), s=1.0, cl="C3",
             tag="Step 5 D3: Codex operating bridge (base rev $9.0B, 15% owner margin, 31.5m sh; bull $13B/16%/33m); bust/plateau = 2025/2026 adjusted EPS less SBC; x14 B (both passes; band 10.3-15.5)"),
 "WCC":  dict(eps=(13.05, 17.65, 27.28, 35.46), x=15, d=(7, 8, 10, 12), pr=(25, 50, 25), s=0.6, cl="C3",
             tag="Step 5 D4: Claude consensus-anchored base (2027E 21.94 x0.96 x1.09^3); Codex $44 bridge needs 11.3%/yr revenue vs company 2027 guide mid-high single digits and 5-8% long-run aspiration; x15 (band 14.4 own)"),
 "RELX": dict(eps=(1.47, 1.89, 2.53, 3.69), x=21, d=(4, 4.5, 5, 6), pr=(25, 50, 25), s=0.3, cl="C5",
             tag="bust FY25 ~GBP1.12 GAAP ~ $1.47; plat 2026E 1.89; base/bull X (only model); x21 A (X 24 is above own 18.7x and data-peer median 21.4x; ~6%/yr EPS growth earns no premium)"),
}

# ---------------------------------------------------------------- EV-valued (power, neocloud)
# per state: (EBITDA $bn, EV/EBITDA, net claims $bn, diluted shares bn, cum dividends $/sh)
EV = {
 "NRG": dict(st=((4.0, 6.0, 19, 0.21, 8), (5.0, 6.75, 17, 0.20, 8.5), (6.5, 7.3, 14, 0.19, 9), (8.5, 8.3, 11, 0.18, 10)),
            pr=(30, 45, 25), s=0.7, cl="C4",
            tag="X EV structure (sale proceeds spent once; claims 22.8->14); base EV 7.3x C-equiv (tie->lower; own 7.2x 2027 guide, X 8x); plat 2026-level EBITDA ~5.0 post-sale A; bust = X bear at 6x; probs 30/45/25 C (Texas moratorium pledge, F3)"),
 "VST": dict(st=((6.0, 6.6, 26, 0.34, 4), (7.0, 7.4, 23, 0.32, 4.5), (11.0, 8.3, 20, 0.30, 5), (13.0, 9.3, 16, 0.29, 6)),
            pr=(30, 45, 25), s=0.7, cl="C4",
            tag="X EV structure; base EBITDA 11 X; base EV 8.3x C-equiv (tie->lower vs X 9; own 8.1x on 2027 guide); bull EBITDA 13 C-equiv (tie->lower vs X 14); plat 2026 guide-level 7.0; probs 30/45/25 C (Texas)"),
 "TLN": dict(st=((1.75, 7.0, 5, 0.05, 0), (2.3, 8.0, 7, 0.048, 0), (3.6, 9.0, 5, 0.045, 0), (4.5, 10.0, 3, 0.043, 0)),
            pr=(25, 50, 25), s=0.7, cl="C4",
            tag="X EV structure; base EV 9x X (in band; C-equiv 8.3 below own 9.9x); base claims 5 (tie->higher claims vs X 4); bull EBITDA 4.5 C-equiv (vs X 5.5); plat 2026-level 2.3 A"),
 "CRWV": dict(st=((4.8, 6, 45, 0.65, 0), (4.8, 6, 45, 0.65, 0), (17.6, 8, 65, 0.75, 0), (30.0, 10, 80, 0.85, 0)),
             pr=(40, 40, 20), s=1.0, cl="C1",
             tag="X only model; bear = zero equity (claims exceed EV); probs 40/40/20 X"),
}

# ---------------------------------------------------------------- SOTP
SOTP = {"BNTX": dict(tv=(45, 45, 105, 190), pr=(30, 50, 20), s=0.0, cl="C6",
                     tag="X SOTP (net cash AFTER modeled burn + risk-adjusted pipeline): C's $65 bear used today's cash, ignoring 4 years of burn -> X better supported")}

# ---------------------------------------------------------------- screen-level names (both models far below hurdle)
CLAUDE_DD = {  # Claude deep-dive terminal values (bear, base, bull), probs
 "AMAT": ((190, 464, 721), (30, 45, 25)), "ANET": ((99, 238, 375), (25, 50, 25)), "DELL": ((210, 452, 670), (30, 45, 25)),
 "CRWD": ((70, 145, 234), (25, 50, 25)), "PLTR": ((80, 190, 350), (25, 50, 25)), "AVAV": ((45, 154, 280), (30, 45, 25)),
 "MRNA": ((70, 180, 420), (30, 45, 25)), "INTC": ((20, 52, 108), (30, 45, 25)), "GEV": ((508, 1054, 1624), (25, 50, 25)),
 "CCJ": ((40, 90, 143), (30, 45, 25)), "BE": ((72, 260, 480), (30, 45, 25)), "GOOGL": ((199, 445, 679), (25, 50, 25)),
 "KLAC": ((96, 192, 276), (25, 50, 25)), "CDNS": ((230, 448, 627), (25, 50, 25)), "AMD": ((144, 572, 1064), (30, 45, 25)),
 "ALAB": ((81, 351, 612), (30, 45, 25)), "MRVL": ((68, 210, 338), (30, 45, 25)), "LITE": ((240, 816, 1302), (30, 45, 25)),
 "SNDK": ((500, 1200, 1950), (30, 45, 25)),
}
SCREEN = ["GOOGL", "AMZN", "DELL", "HPE", "KLAC", "FN", "ANET", "MSI", "BE", "CDNS", "AMAT", "GEV", "MRVL", "AVAV", "LITE",
          "IREN", "CORZ", "GEN", "PLTR", "CCJ", "APLD", "POWL", "AMD", "INTC", "NBIS", "PANW", "MRNA", "CRWD", "AXON", "ALAB", "SNDK"]
S_SENS = {"GOOGL": .6, "AMZN": .6, "DELL": 1, "HPE": 1, "KLAC": 1, "FN": 1, "ANET": 1, "MSI": .3, "BE": .8, "CDNS": .7,
          "AMAT": 1, "GEV": .8, "MRVL": 1, "AVAV": .3, "LITE": 1, "IREN": 1, "CORZ": 1, "GEN": .1, "PLTR": .3, "CCJ": .6,
          "APLD": 1, "POWL": .8, "AMD": 1, "INTC": .6, "NBIS": 1, "PANW": .3, "MRNA": 0, "CRWD": .3, "AXON": .3, "ALAB": 1, "SNDK": 1}
CLUSTER = {"GOOGL": "C5", "AMZN": "C5", "DELL": "C1", "HPE": "C1", "KLAC": "C2", "FN": "C1", "ANET": "C1", "MSI": "C5", "BE": "C3",
           "CDNS": "C2", "AMAT": "C2", "GEV": "C3", "MRVL": "C1", "AVAV": "C6", "LITE": "C1", "IREN": "C1", "CORZ": "C1", "GEN": "C5",
           "PLTR": "C5", "CCJ": "C4", "APLD": "C1", "POWL": "C3", "AMD": "C1", "INTC": "C2", "NBIS": "C1", "PANW": "C5", "MRNA": "C6",
           "CRWD": "C5", "AXON": "C5", "ALAB": "C1", "SNDK": "C1"}
SNDK_CX = ((390, 1372.857, 2446.667), (30, 50, 20))   # Codex Step-2 model for SNDK (pre-split basis)


def cagr(tv, p):
    return ((tv / p) ** (1 / T) - 1) * 100 if tv > 0 else -100.0


def res_from_tvs(k, tvs, pr, ai, gw, method, tag, cl, s, extra=None):
    """tvs = (bust, plateau, base, bull)."""
    p = P[k]
    bear = 0.5 * tvs[0] + 0.5 * tvs[1]
    etv = (pr[0] * bear + pr[1] * tvs[2] + pr[2] * tvs[3]) / 100
    # Codex-style sensitivity: bear bucket = bust state only
    etv_deep = (pr[0] * tvs[0] + pr[1] * tvs[2] + pr[2] * tvs[3]) / 100
    r = dict(price=p, price6=P6.get(k), move=(p / P6[k] - 1) * 100 if P6.get(k) else None,
             tv=dict(bust=tvs[0], plateau=tvs[1], bear=bear, base=tvs[2], bull=tvs[3]), pr=pr, etv=etv,
             E=cagr(etv, p), E_deepbear=cagr(etv_deep, p), A27=cagr(ai, p), G100=cagr(gw, p), ai_tv=ai, gw_tv=gw,
             bust=(tvs[0] / p - 1) * 100, delay=(tvs[1] / p - 1) * 100, base_ret=(tvs[2] / p - 1) * 100,
             method=method, tag=tag, cl=cl, s=s)
    if extra:
        r.update(extra)
    return r


# Robustness switch: argv[5] == "codexmult" -> every disputed base multiple set to Codex's value
CODEX_MULT = {"NVDA": 22, "VRT": 24, "CLS": 16, "NVT": 22, "COHR": 20, "TSM": 21, "SNPS": 30, "LRCX": 22, "META": 23,
              "MSFT": 29, "VRSK": 28, "RELX": 24, "WCC": 14}
CODEX_EV = {"NRG": 8.0, "VST": 9.0}
if len(sys.argv) > 5 and sys.argv[5] == "codexmult":
    for k, v in CODEX_MULT.items():
        E[k]["x"] = v
    for k, v in CODEX_EV.items():
        st = [list(x) for x in EV[k]["st"]]; base = st[2][1]
        for x in st:
            x[1] = x[1] * v / base
        EV[k]["st"] = tuple(tuple(x) for x in st)

R = {}
for k, d in E.items():
    x = d.get("x") or d["xm"][2]
    xm = d.get("xm", (0.70 * x, 0.85 * x, x, 1.20 * x))
    dv = d.get("d", (0, 0, 0, 0)); c = d.get("c", (0, 0, 0, 0)); e = d["eps"]
    tvs = tuple(max(0.0, e[i] * xm[i] + c[i]) + dv[i] for i in range(4))
    s = d["s"]
    def named(L):
        eps = e[2] + L * s * (e[3] - e[2]); cash = c[2] + L * s * (c[3] - c[2]); div = dv[2] + min(L, 1) * s * (dv[3] - dv[2])
        return max(0.0, eps * xm[2] + cash) + div
    R[k] = res_from_tvs(k, tvs, d["pr"], named(L27), named(L100), "Earnings (A1)", d["tag"], d["cl"], s,
                        dict(eps=e, mult=[round(v, 1) for v in xm], div=dv, cash=c))

for k, d in EV.items():
    st = d["st"]
    tvs = tuple(max(0.0, a * m - n) / sh + dv for a, m, n, sh, dv in st)
    s = d["s"]; b, u = st[2], st[3]
    def named(L):
        eb = b[0] + L * s * (u[0] - b[0]); n = b[2] + min(L, 1) * s * (u[2] - b[2])
        sh = b[3] + min(L, 1) * s * (u[3] - b[3]); dv = b[4] + min(L, 1) * s * (u[4] - b[4])
        return max(0.0, eb * b[1] - n) / sh + dv
    R[k] = res_from_tvs(k, tvs, d["pr"], named(L27), named(L100), "EV/EBITDA (A1)", d["tag"], d["cl"], s, dict(ev_states=st))

for k, d in SOTP.items():
    tv = d["tv"]; s = d["s"]
    R[k] = res_from_tvs(k, tv, d["pr"], tv[2] + L27 * s * (tv[3] - tv[2]), tv[2] + L100 * s * (tv[3] - tv[2]),
                        "SOTP (A1)", d["tag"], d["cl"], s)

for k in SCREEN:
    p = P[k]
    opts = []
    if k in CXV:
        v = CXV[k]; opts.append(("Codex DD", tuple(v["terminal_values"]), tuple(int(round(q * 100)) for q in v["probabilities"])))
    if k in CLAUDE_DD:
        tv, pr = CLAUDE_DD[k]; opts.append(("Claude DD", tv, pr))
    if k == "SNDK":
        opts.append(("Codex Step 2", SNDK_CX[0], SNDK_CX[1]))
    ev = [(sum(a * b for a, b in zip(o[1], o[2])) / 100, o) for o in opts]
    ev.sort(key=lambda z: z[0])
    lo, hi = ev[0], ev[-1]
    src, tv3, pr = lo[1]
    s = S_SENS[k]
    bear, base, bull = tv3
    ai = base + L27 * s * (bull - base); gw = base + L100 * s * (bull - base)
    r = res_from_tvs(k, (bear, bear, base, bull), pr, ai, gw, "Screen: " + src + " TVs (more conservative model)",
                     "screen-level re-price; bear = conservative model's bear for both bust and plateau", CLUSTER[k], s,
                     dict(E_upper=cagr(hi[0], p), upper_src=hi[1][0]))
    R[k] = r

# ---------------------------------------------------------------- portfolios
def port(w):
    tot = sum(w.values()); assert abs(tot - 100) < 1e-9, (w, tot)
    m = lambda f: sum(wt / 100 * f(R[k]) / R[k]["price"] for k, wt in w.items())
    em = m(lambda r: r["etv"]); dm = m(lambda r: (r["pr"][0] * r["tv"]["bust"] + r["pr"][1] * r["tv"]["base"] + r["pr"][2] * r["tv"]["bull"]) / 100)
    out = dict(n=len(w), E=(em ** (1 / T) - 1) * 100, E_total=(em - 1) * 100, E_deepbear=(dm ** (1 / T) - 1) * 100,
               A27=(m(lambda r: r["ai_tv"]) ** (1 / T) - 1) * 100, G100=(m(lambda r: r["gw_tv"]) ** (1 / T) - 1) * 100,
               bust=(m(lambda r: r["tv"]["bust"]) - 1) * 100, delay=(m(lambda r: r["tv"]["plateau"]) - 1) * 100,
               base=(m(lambda r: r["tv"]["base"]) - 1) * 100, maxw=max(w.values()),
               top3=sum(sorted(w.values(), reverse=True)[:3]), hhi=sum((v / 100) ** 2 for v in w.values()))
    for z in (10, 20):   # extra common zero-recovery regime overlay (Codex sensitivity), not in primary E
        out[f"E_zero{z}"] = (((1 - z / 100) * em) ** (1 / T) - 1) * 100
    cl = {}
    for k, wt in w.items():
        cl[R[k]["cl"]] = cl.get(R[k]["cl"], 0) + wt
    out["clusters"] = dict(sorted(cl.items()))
    return out


PORTS = json.loads(sys.argv[4]) if len(sys.argv) > 4 else {}
PO = {name: port(w) for name, w in PORTS.items()}
json.dump(dict(T=T, L27=L27, L100=L100, R=R, PORTS=PORTS, PO=PO), open(OUT, "w"), indent=1)

rank = sorted(R, key=lambda k: -R[k]["E"])
print(f"T={T:.4f}")
print(f"{'#':>2} {'tkr':5} {'price':>8} {'mv%':>5} {'E':>6} {'Edeep':>6} {'A27':>6} {'G100':>6} {'bust%':>6} {'dly%':>6} {'base%':>6}  cl  method")
for i, k in enumerate(rank, 1):
    r = R[k]
    up = f" (upper {r['E_upper']:.1f})" if "E_upper" in r else ""
    print(f"{i:2} {k:5} {r['price']:8.2f} {r['move'] or 0:5.1f} {r['E']:6.1f} {r['E_deepbear']:6.1f} {r['A27']:6.1f} {r['G100']:6.1f} {r['bust']:6.0f} {r['delay']:6.0f} {r['base_ret']:6.0f}  {r['cl']}  {r['method'][:22]}{up}")
for name, o in PO.items():
    print(f"{name:28} n={o['n']:2} E={o['E']:5.1f} Edeep={o['E_deepbear']:5.1f} A27={o['A27']:5.1f} G100={o['G100']:5.1f} bust={o['bust']:6.1f} delay={o['delay']:6.1f} z10={o['E_zero10']:5.1f} top3={o['top3']} hhi={o['hhi']:.3f} {o['clusters']}")
