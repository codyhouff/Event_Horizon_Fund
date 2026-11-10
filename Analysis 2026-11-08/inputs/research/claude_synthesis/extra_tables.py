"""Step 3 (Claude synthesis): secondary tables not produced by step3_tables.py.

Reproduces, from the model output and snapshot:
  tables/reconciliation.md  - Model Reconciliation weights table (final analysis)
  tables/pool.md            - 58-stock ranked pool table (final analysis Part III.C)
  tables/disputes.md        - A4.3 disputed-input table (Candidate Ranking) + side counts
  data/drift_nov9.json      - V9.1 weights drifted May 8 -> Nov 9 (price only)
  tables/trades.md          - Deployment trade list and tranche schedule (drift basis)

Usage (from this folder):
  python -I extra_tables.py data/step3_out.json data/step3_snap.json data/disputes.json tables data
"""
import collections
import json
import re
import sys

OUT_JSON, SNAP_JSON, DISPUTES_JSON, TABLES, DATA = sys.argv[1:6]
D = json.load(open(OUT_JSON))
R, P = D["R"], D["PORTS"]
SNAP = json.load(open(SNAP_JSON))
FINAL = P["V10.0 final (proposed)"]
V91 = P["V9.1 baseline"]
rank = {k: i for i, k in enumerate(sorted(R, key=lambda k: -R[k]["E"]), 1)}


def write(path, lines):
    open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")


# --- Model Reconciliation table
cols = ["V9.1 baseline", "Claude blind (V10)", "Codex blind (CX8)", "Claude post-critique", "Codex post-critique", "V10.0 final (proposed)"]
names = set().union(*(set(P[c]) for c in cols))
rows = sorted(names, key=lambda k: (-FINAL.get(k, 0), rank[k]))
L = ["| Ticker | Rank (of 58) | Expected CAGR | Baseline V9.1 % | Claude blind % | Codex blind % | Claude post-critique % | Codex post-critique % | **Final V10.0 %** |",
     "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
for k in rows:
    v = [P[c].get(k, 0) for c in cols]
    L.append(f"| {k} | {rank[k]} | {R[k]['E']:.1f}% | " + " | ".join(str(x) for x in v[:-1]) + f" | **{v[-1]}** |")
L.append("| **Total** | | | " + " | ".join(str(sum(P[c].values())) for c in cols[:-1]) + f" | **{sum(FINAL.values())}** |")
write(f"{TABLES}/reconciliation.md", L)

# --- Pool table (reuses labels from step3_tables.py)
src = open("step3_tables.py", encoding="utf-8").read()
ns = {}
exec(src[src.index("BOTTLENECK = {"):src.index("CB = {")], ns)
B, S = ns["BOTTLENECK"], ns["STATUS"]


def decision(k):
    w, o = FINAL.get(k, 0), V91.get(k, 0)
    if o == 0 and w > 0: return "Add"
    if w > o: return "Increase"
    if w == o and w > 0: return "Keep"
    if 0 < w < o: return "Reduce"
    if o > 0: return "Remove"
    return "Not added"


L = ["| Rank | Ticker | Bottleneck | Price (Nov 9) | Status | Expected CAGR | AI-2027 | 100GW | Bust | Delay | Depth | V9.1 → V10.0 |",
     "|---:|---|---|---:|---|---:|---:|---:|---:|---:|---|---|"]
for k in sorted(R, key=lambda k: -R[k]["E"]):
    r = R[k]
    depth = "Full A1" if not r["method"].startswith("Screen") else f"Screen (upper {r['E_upper']:.1f}%)"
    st = S.get(k, "Fair" if r["E"] > 5 else "Expensive")
    tk = f"**{k}**" if FINAL.get(k) else k
    L.append(f"| {rank[k]} | {tk} | {B.get(k, '')} | ${r['price']:,.2f} | {st} | {r['E']:.1f}% | {r['A27']:.1f}% | {r['G100']:.1f}% | "
             f"{r['bust']:.0f}% | {r['delay']:.0f}% | {depth} | {V91.get(k, 0)} → **{FINAL.get(k, 0)}** ({decision(k)}) |")
write(f"{TABLES}/pool.md", L)

# --- Disputed-input table and self-sided audit counts
d = json.load(open(DISPUTES_JSON))
side = {"C": "Claude", "X": "Codex", "neither": "Neither", "both": "Split"}
L = ["| # | Ticker | Input | Claude | Codex | Adopted | Went to | Basis | Deciding evidence |", "|---:|---|---|---|---|---|---|---|---|"]
for i, r in enumerate(d, 1):
    L.append(f"| {i} | {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {side[r[5]]} | {r[6]} | {r[7]} |")
write(f"{TABLES}/disputes.md", L)
print("disputes:", len(d), dict(collections.Counter((r[5], r[6]) for r in d)))

# --- Drift since May 8 (price only) and trade list
MAY8 = {"TSM": 411.68, "NVDA": 215.20, "AVGO": 430.00, "MU": 746.81, "ASML": 1592.02, "AMAT": 435.44, "SNPS": 516.48,
        "ANET": 141.77, "VRT": 339.97, "DELL": 260.46, "CEG": 303.63, "VST": 147.72, "PWR": 745.00, "CRWD": 131.94,
        "PLTR": 137.80, "AVAV": 168.29, "KTOS": 57.89, "MRNA": 54.35, "MP": 67.43, "INTC": 124.92, "GEV": 1040.15,
        "CCJ": 116.75, "BE": 261.03, "COHR": 335.26}
px = lambda k: SNAP[k]["closes"]["2026-11-09"]
val = {k: V91[k] * px(k) / MAY8[k] for k in V91}
tot = sum(val.values())
dr = {k: v / tot * 100 for k, v in val.items()}
json.dump(dr, open(f"{DATA}/drift_nov9.json", "w"), indent=1)
print(f"V9.1 basket since May 8 (price only): {(tot / 100 - 1) * 100:.1f}%")

SELL = {**{k: {"T1": 1} for k in ["CRWD", "PLTR", "MRNA", "INTC", "AVAV", "CCJ", "BE", "DELL", "ANET", "GEV", "PWR", "KTOS",
                                  "COHR", "CEG", "AMAT", "SNPS", "MP"]},
        "AVGO": {"T2": 1}, "TSM": {"T2": 0.5, "T3": 0.5}, "ASML": {"T2": 0.5, "T3": 0.5}}
BUY = {"NVT": {"T1": 0.6, "T2": 0.4}, "META": {"T1": 0.5, "T2": 0.5}, "NRG": {"T1": 0.6, "T2": 0.4},
       "CLS": {"T1": 0.5, "T2": 0.25, "T4": 0.25}, "VRT": {"T1": 0.5, "T2": 0.2, "T3": 0.3},
       "MU": {"T1": 0.4, "T2": 0.3, "T4": 0.3}, "NVDA": {"T1": 0.2, "T3": 0.5, "T4": 0.3}, "VST": {"T1": 0.5, "T3": 0.5}}
cash = 0.0
for t in ["T1", "T2", "T3", "T4"]:
    s = sum(dr[k] * f.get(t, 0) for k, f in SELL.items())
    b = sum((FINAL[k] - dr.get(k, 0)) * f.get(t, 0) for k, f in BUY.items())
    cash += s - b
    print(f"{t}: sells {s:.2f}, buys {b:.2f}, reserve {cash:.2f}")

L = ["| Ticker | V9.1 target | Drifted weight (Nov 9) | V10.0 target | Trade | Price vs May 8 close (lot gain/loss guide) | Tranche schedule (% of the sleeve) |",
     "|---|---:|---:|---:|---:|---:|---|"]
allk = sorted(set(dr) | set(FINAL), key=lambda k: (-(FINAL.get(k, 0) - dr.get(k, 0)), k))
for k in allk:
    tgt, cur = FINAL.get(k, 0), dr.get(k, 0)
    tr = tgt - cur
    pc = f"{(px(k) / MAY8[k] - 1) * 100:+.0f}%" if k in MAY8 else "new"
    if k in BUY:
        sch = " · ".join(f"{t} +{tr * f:.2f}" for t, f in BUY[k].items())
    else:
        sch = " · ".join(f"{t} −{cur * f:.2f}" for t, f in SELL[k].items())
    L.append(f"| {k} | {V91.get(k, 0)} | {cur:.2f} | {tgt} | **{tr:+.2f}** | {pc} | {sch} |")
buys = sum(max(0, FINAL.get(k, 0) - dr.get(k, 0)) for k in allk)
sells = sum(max(0, dr.get(k, 0) - FINAL.get(k, 0)) for k in allk)
L.append(f"| **Totals** | 100 | 100.00 | 100 | **Buys +{buys:.2f} / Sells −{sells:.2f}** | | Turnover ≈ {buys:.1f}% |")
write(f"{TABLES}/trades.md", L)

# Buy-price limits (expected return falls to 12% / reaches 18%)
T = D["T"]
for k in FINAL:
    e = R[k]["etv"]
    print(f"{k}: max buy (12%) ${e / 1.12 ** T:.2f}; strong buy (18%) ${e / 1.18 ** T:.2f}")
