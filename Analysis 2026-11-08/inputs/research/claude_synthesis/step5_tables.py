"""Step 5 tables for the adopted final (V10.1) and the Deployment Strategy.

Usage (from this folder):
  python -I step5_tables.py data/step5_out.json data/step5_out_cxmult.json data/step5_snap.json tables5 data
"""
import json
import sys

OUT, CXO, SNAPF, TDIR, DDIR = sys.argv[1:6]
D = json.load(open(OUT)); DX = json.load(open(CXO)); SNAP = json.load(open(SNAPF))
R, P, PO = D["R"], D["PORTS"], D["PO"]
T = D["T"]
FINAL = P["V10.1 final (adopted)"]
STEP3 = P["V10.0 Step 3 proposal"]
CODEX4 = P["Codex O1+O2 (WCC 8 for VST; STRL 5 from NVT)"]
V91 = P["V9.1 baseline"]
src = open("step3_tables.py", encoding="utf-8").read()
ns = {}
exec(src[src.index("BOTTLENECK = {"):src.index("CB = {")], ns)
B, S = ns["BOTTLENECK"], ns["STATUS"]
B.update({"STRL": "Data-center site development + electrical installation", "WCC": "Electrical / datacom distribution"})
S.update({"STRL": "Attractive (multiple-sensitive)", "WCC": "Fair", "VST": "Fair", "AVGO": "Fair"})
rank = {k: i for i, k in enumerate(sorted(R, key=lambda k: -R[k]["E"]), 1)}


def w(path, lines):
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")


def decision(k):
    a, o = FINAL.get(k, 0), V91.get(k, 0)
    if o == 0 and a > 0: return "Add"
    if a > o: return "Increase"
    if a == o and a > 0: return "Keep"
    if 0 < a < o: return "Reduce"
    if o > 0: return "Remove"
    return "Not added"


# Pool table (Part III.C)
L = ["| Rank | Ticker | Bottleneck | Price (Nov 9) | Status | Expected CAGR | AI-2027 | 100GW | Bust | Delay | Depth | V9.1 → V10.1 |",
     "|---:|---|---|---:|---|---:|---:|---:|---:|---:|---|---|"]
for k in sorted(R, key=lambda k: -R[k]["E"]):
    r = R[k]
    depth = "Full A1" if not r["method"].startswith("Screen") else f"Screen (favorable-model estimate {r['E_upper']:.1f}%)"
    st = S.get(k, "Fair" if r["E"] > 5 else "Expensive")
    tk = f"**{k}**" if FINAL.get(k) else k
    L.append(f"| {rank[k]} | {tk} | {B.get(k, '')} | ${r['price']:,.2f} | {st} | {r['E']:.1f}% | {r['A27']:.1f}% | {r['G100']:.1f}% | "
             f"{r['bust']:.0f}% | {r['delay']:.0f}% | {depth} | {V91.get(k, 0)} → **{FINAL.get(k, 0)}** ({decision(k)}) |")
w(f"{TDIR}/pool5.md", L)

# Model Reconciliation (adds Step 4 columns and the adopted column)
cols = [("V9.1 baseline", "V9.1"), ("Claude blind (V10)", "Claude blind"), ("Codex blind (CX8)", "Codex blind"),
        ("Claude post-critique", "Claude post-critique"), ("Codex post-critique", "Codex post-critique"),
        ("V10.0 Step 3 proposal", "Step 3 proposal (V10.0)")]
names = set(FINAL) | set(CODEX4)
for c, _ in cols:
    names |= set(P[c])
rows = sorted(names, key=lambda k: (-FINAL.get(k, 0), rank[k]))
L = ["| Ticker | Rank (of 60) | Expected CAGR | " + " | ".join(lbl + " %" for _, lbl in cols) + " | Claude Step 4 % | Codex Step 4 % | **Adopted V10.1 %** |",
     "|---|---:|---:|" + "---:|" * (len(cols) + 3)]
for k in rows:
    v = [P[c].get(k, 0) for c, _ in cols]
    L.append(f"| {k} | {rank[k]} | {R[k]['E']:.1f}% | " + " | ".join(str(x) for x in v) + f" | {STEP3.get(k, 0)} | {CODEX4.get(k, 0)} | **{FINAL.get(k, 0)}** |")
L.append("| **Total** | | | " + " | ".join(str(sum(P[c].values())) for c, _ in cols) + f" | 100 | {sum(CODEX4.values())} | **{sum(FINAL.values())}** |")
w(f"{TDIR}/recon5.md", L)

# Portfolio comparison
order = ["V9.1 baseline", "Claude blind (V10)", "Codex blind (CX8)", "Claude post-critique", "Codex post-critique",
         "Arch1 diversified (16)", "Arch2 concentrated (7)", "V10.0 Step 3 proposal", "Codex O1+O2 (WCC 8 for VST; STRL 5 from NVT)",
         "O1 only (WCC 8 for VST)", "O2 only (STRL 5 from NVT)", "Alt: STRL 8 for VST (VRT/MU stay 14)", "V10.1 final (adopted)",
         "V10.1 if MOD gate passes", "V10.1 if Texas hit (NRG 8, STRL 3, TLN 7)", "V10.1 if NVDA review adverse (NVDA 8, AVGO 7)"]
L = ["| Portfolio | Names | Expected CAGR | Expected total return | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Bust-case return | 2–3 yr delay return | Expected CAGR with Codex multiples | Top-3 weight | HHI |",
     "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
for n in order:
    o, ox = PO[n], DX["PO"][n]
    b = "**" if n.startswith("V10.1 final") else ""
    L.append(f"| {b}{n}{b} | {o['n']} | {b}{o['E']:.1f}%{b} | {o['E_total']:.0f}% | {o['A27']:.1f}% | {o['G100']:.1f}% | {o['bust']:.1f}% | "
             f"{o['delay']:.1f}% | {ox['E']:.1f}% | {o['top3']}% | {o['hhi']:.3f} |")
w(f"{TDIR}/portfolios5.md", L)

# Drift and trades (drift basis, Nov 9) for the adopted weights
MAY8 = {"TSM": 411.68, "NVDA": 215.20, "AVGO": 430.00, "MU": 746.81, "ASML": 1592.02, "AMAT": 435.44, "SNPS": 516.48,
        "ANET": 141.77, "VRT": 339.97, "DELL": 260.46, "CEG": 303.63, "VST": 147.72, "PWR": 745.00, "CRWD": 131.94,
        "PLTR": 137.80, "AVAV": 168.29, "KTOS": 57.89, "MRNA": 54.35, "MP": 67.43, "INTC": 124.92, "GEV": 1040.15,
        "CCJ": 116.75, "BE": 261.03, "COHR": 335.26}
px = lambda k: SNAP[k]["closes"]["2026-11-09"]
val = {k: V91[k] * px(k) / MAY8[k] for k in V91}
tot = sum(val.values())
dr = {k: v / tot * 100 for k, v in val.items()}
json.dump(dr, open(f"{DDIR}/drift_nov9.json", "w"), indent=1)
SELL = {**{k: {"T1": 1} for k in ["CRWD", "PLTR", "MRNA", "INTC", "AVAV", "CCJ", "BE", "DELL", "ANET", "GEV", "PWR", "KTOS",
                                  "COHR", "CEG", "AMAT", "SNPS", "MP", "VST"]},
        "AVGO": {"T3": 1}, "TSM": {"T2": 0.5, "T3": 0.5}, "ASML": {"T2": 0.5, "T3": 0.5}}
BUY = {"NVT": {"T1": 0.6, "T2": 0.4}, "META": {"T1": 0.5, "T2": 0.5}, "NRG": {"T1": 0.6, "T2": 0.4},
       "CLS": {"T1": 0.5, "T2": 0.25, "T4": 0.25}, "VRT": {"T1": 0.5, "T2": 0.2, "T3": 0.3},
       "MU": {"T1": 0.4, "T2": 0.3, "T4": 0.3}, "NVDA": {"T3": 0.6, "T4": 0.4}, "STRL": {"T1": 0.5, "T2": 0.5}}
cash, path = 0.0, []
for t in ["T1", "T2", "T3", "T4"]:
    s = sum(dr[k] * f.get(t, 0) for k, f in SELL.items())
    b = sum((FINAL[k] - dr.get(k, 0)) * f.get(t, 0) for k, f in BUY.items())
    cash += s - b
    path.append((t, round(s, 2), round(b, 2), round(cash, 2)))
L = ["| Ticker | V9.1 target | Drifted weight (Nov 9) | V10.1 target | Trade | Price vs May 8 close (lot gain/loss guide) | Tranche schedule (% of the sleeve) |",
     "|---|---:|---:|---:|---:|---:|---|"]
allk = sorted(set(dr) | set(FINAL), key=lambda k: (-(FINAL.get(k, 0) - dr.get(k, 0)), k))
for k in allk:
    tgt, cur = FINAL.get(k, 0), dr.get(k, 0)
    tr = tgt - cur
    pc = f"{(px(k) / MAY8[k] - 1) * 100:+.0f}%" if k in MAY8 else "new"
    sch = " · ".join(f"{t} +{tr * f:.2f}" for t, f in BUY[k].items()) if k in BUY else " · ".join(f"{t} −{cur * f:.2f}" for t, f in SELL[k].items())
    L.append(f"| {k} | {V91.get(k, 0)} | {cur:.2f} | {tgt} | **{tr:+.2f}** | {pc} | {sch} |")
buys = sum(max(0, FINAL.get(k, 0) - dr.get(k, 0)) for k in allk)
sells = sum(max(0, dr.get(k, 0) - FINAL.get(k, 0)) for k in allk)
L.append(f"| **Totals** | 100 | 100.00 | 100 | **Buys +{buys:.2f} / Sells −{sells:.2f}** | | Turnover ≈ {buys:.1f}% |")
w(f"{TDIR}/trades5.md", L)

# Destination table with buy limits
L = ["| Ticker | V10.1 target | Role | Expected CAGR | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Maximum buy price (expected return falls to 12%) | \"Strong buy\" price (expected return 18%) |",
     "|---|---:|---|---:|---:|---:|---:|---:|"]
role = {"NVDA": "Core", "META": "Core", "VRT": "Core", "MU": "Core", "NRG": "Core", "NVT": "Core", "CLS": "Satellite", "STRL": "Satellite"}
for k in ["NVDA", "META", "VRT", "MU", "NRG", "NVT", "CLS", "STRL"]:
    r = R[k]
    L.append(f"| {k} | {FINAL[k]}% | {role[k]} | {r['E']:.1f}% | {r['A27']:.1f}% | {r['G100']:.1f}% | **${r['etv'] / 1.12 ** T:,.0f}** | ${r['etv'] / 1.18 ** T:,.0f} |")
o = PO["V10.1 final (adopted)"]
L.append(f"| **Total** | **100%** | | **{o['E']:.1f}%** | **{o['A27']:.1f}%** | **{o['G100']:.1f}%** | | |")
w(f"{TDIR}/destination5.md", L)
print("cash path", path, "turnover", round(buys, 1))
