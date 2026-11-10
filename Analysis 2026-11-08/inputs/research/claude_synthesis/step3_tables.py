"""Render markdown tables for the Step 3 Candidate Ranking and final analysis from step3_out.json."""
import json, sys

D = json.load(open(sys.argv[1]))
DX = json.load(open(sys.argv[2]))   # codex-multiple robustness run
OUTDIR = sys.argv[3]
R, PO, PORTS = D["R"], D["PO"], D["PORTS"]

BOTTLENECK = {
 "NVDA": "Accelerators / CUDA platform", "AVGO": "Custom silicon + networking", "MU": "HBM / DRAM", "TSM": "Leading-edge foundry + CoWoS",
 "ASML": "EUV lithography", "VRT": "Rack power + liquid cooling", "CLS": "Rack-scale integration (EMS/HPS)", "NVT": "Electrical distribution + liquid cooling",
 "NRG": "Merchant power + retail (TX/PJM)", "VST": "Merchant power (TX/PJM)", "TLN": "Nuclear/gas power (PJM)", "CEG": "Nuclear fleet",
 "COHR": "Optical transceivers / lasers", "CRDO": "AECs / SerDes", "SNPS": "EDA + simulation", "ETN": "Electrical equipment", "PWR": "Grid construction",
 "KTOS": "AI-enabled defense", "MP": "Rare-earth magnets", "BNTX": "Bio-risk (mRNA + oncology)", "SNDK": "NAND / enterprise SSD", "LRCX": "Etch/dep WFE",
 "META": "AI application + ads (buyer)", "MSFT": "AI platform + cloud (buyer)", "MOD": "Thermal (post-spin pure play)", "VRSK": "Proprietary insurance data",
 "RELX": "Proprietary data + analytics", "CRWV": "Neocloud GPU capacity", "GOOGL": "AI platform + TPU (buyer)", "AMZN": "Cloud + Trainium (buyer)",
 "DELL": "AI servers", "HPE": "AI servers + networking", "KLAC": "Process control WFE", "FN": "Optical contract manufacturing", "ANET": "DC Ethernet fabric",
 "MSI": "Public-safety comms", "BE": "Fuel-cell grid bypass", "CDNS": "EDA", "AMAT": "Deposition WFE", "GEV": "Gas turbines + grid", "MRVL": "Custom silicon / optics DSP",
 "AVAV": "Drones / loitering munitions", "LITE": "Optical components", "IREN": "Neocloud / miner", "CORZ": "Neocloud hosting", "GEN": "Consumer identity",
 "PLTR": "AI operating software", "CCJ": "Uranium", "APLD": "Neocloud hosting", "POWL": "Switchgear", "AMD": "Accelerators (#2)", "INTC": "Domestic foundry",
 "NBIS": "Neocloud", "PANW": "Security platform", "MRNA": "mRNA vaccines", "CRWD": "AI-native security", "AXON": "Public-safety platform", "ALAB": "PCIe/CXL connectivity",
}
STATUS = {
 "NVDA": "Attractive", "NRG": "Attractive (levered)", "META": "Attractive", "CLS": "Attractive", "VRT": "Fair", "NVT": "Attractive", "MU": "Deep Discount (cyclical)",
 "VST": "Fair", "TLN": "Fair", "MSFT": "Fair", "TSM": "Fair", "AVGO": "Fair", "ASML": "Fair", "RELX": "Fair", "VRSK": "Fair", "ETN": "Fair", "CRDO": "Fair",
 "CEG": "Expensive", "COHR": "Expensive (after +17%)", "SNPS": "Expensive (owner basis)", "PWR": "Expensive", "KTOS": "Speculative", "MP": "Speculative",
 "BNTX": "Speculative", "MOD": "Speculative (post-spin)", "CRWV": "Speculative (financing)", "LRCX": "Fair", "SNDK": "Deep Discount (cyclical)",
}
CB = {"TSM": 14, "NVDA": 13, "VRT": 9, "VST": 9, "MU": 9, "ASML": 8, "AVGO": 6, "SNPS": 6, "CEG": 6, "COHR": 5, "ETN": 5, "CRDO": 3, "PWR": 2, "KTOS": 2, "MP": 2, "BNTX": 1}
CP = {"NVDA": 15, "VRT": 14, "MU": 12, "AVGO": 11, "NRG": 11, "NVT": 11, "VST": 9, "CLS": 7, "TSM": 5, "ASML": 4, "BNTX": 1}
XB = {"NVDA": 15, "AVGO": 15, "VRT": 15, "CLS": 12, "NVT": 12, "NRG": 12, "VST": 11, "COHR": 8}
XP = {"NVDA": 15, "VRT": 15, "VRSK": 15, "CLS": 12, "NVT": 12, "NRG": 12, "VST": 11, "MU": 8}
V91 = PORTS["V9.1 baseline"]
FINAL = PORTS["V10.0 final (proposed)"]
RESOLVED = {
 "MOD": "Codex inputs (only model); x22 kept (within band tolerance); 30/50/20. Left out: post-spin perimeter, H1 FCF negative (A5)",
 "NVDA": "Base EPS 19 C vs 16.6 X; x18 C vs 22 X (peer band); bull 28 C (tie->lower)",
 "NRG": "X EV bridge (sale proceeds spent once); EV 7.3x C-equiv vs 8x X (tie->lower); 30% bear C (Texas facts)",
 "CRWV": "X only model; 40% zero-equity bear. Left out: bust -100% (A5)",
 "META": "X base/bull (only model); x20 C vs 23 X (X above own 18.0x/peer 22.5x band)",
 "CLS": "Base 29.1 X (owner, 145m sh); x14 C vs 16 X (EMS peers ~10x); bull 40 C (tie->lower)",
 "VRT": "Base 15.0 X (tie->lower); bull 21 C (tie->lower); x23 C (tie->lower)",
 "NVT": "Base 10 C, bull 14 C, x19 C (all tie->lower; peer band 16.4-21.8 contains both)",
 "MU": "X base 110 x10 + $150 cash (conceded-to by X; tie->lower vs C 130x9); A1 plateau EPS 45",
 "VST": "X EV structure; base EBITDA 11 X; EV 8.3x C-equiv vs 9x X (tie->lower); bull EBITDA 13 C-equiv; 30% bear C",
 "TLN": "X EV structure; EV 9x X (C-equiv 8.3x below own 9.9x); bull EBITDA 4.5 C-equiv",
 "MSFT": "X base/bull (only model); x23.5 A (X 29x is 29% above own/peer 22.5x)",
 "TSM": "Base 33 C vs 30.1 X; x19 C vs 21 X (peer band); bull 41.1 X (tie->lower); bear prob 25% (C conceded)",
 "AXON": "Screen: X deep-dive TVs (35x base multiple, SBC 84% of adj EPS)",
 "AVGO": "Base 23.5 X (owner, SBC 13%); credit reserve X ($43B max, Oct 27 8-K); bull 37.7 C-owner; x20 B",
 "RELX": "X base/bull (only model); x21 A (X 24x above own 18.7x and peer 21.4x)",
 "ASML": "Base 85.65 X (unit bridge; tie->lower vs C 88); bull 108 C (tie->lower vs X 144); x28 B",
 "VRSK": "X base/bull (only model); x23 A (X 28x is 22% above own 23.0x/peer 21.4x)",
 "ETN": "Base 22.7 X, bull 27 C (both tie->lower); x24 B",
 "CRDO": "Base 8.35 X (owner); bull 13.8 C-owner; x22 B",
 "CEG": "Base 19.5 C, bull 24 C (tie->lower); 2026 guide raised to $12.50-12.80 (F2)",
 "COHR": "Base 15.65 X (owner); x18 C vs 20 X (optics peers ~15x); Nov 9 +16.8%",
 "SNPS": "Owner EPS: SBC ~31% of adjusted EPS -> base 18.9 C-owner vs 24 X",
 "PWR": "Base 31 C, bull 37 C (tie->lower); x25 B",
 "KTOS": "Owner EPS 1.33 C (tie->lower); x28 X (tie->lower); 30/50/20 X",
 "MP": "Base 1.8 C, bull 3.0 C (tie->lower); x24 X; 30/50/20 X",
 "BNTX": "X SOTP (cash AFTER 4 years of burn) over C's $65 bear on today's cash",
 "LRCX": "Base 12.38 X; x19 C (in band 18.1-20.5; X 22 above); bull 18 C",
 "SNDK": "Screen (both models <10%)",
}


def f(x, n=1, sign=False):
    if x is None:
        return "–"
    return (f"{x:+.{n}f}" if sign else f"{x:.{n}f}")


def pct(w, k):
    return f"{w.get(k, 0)}"


rank = sorted(R, key=lambda k: -R[k]["E"])
lines = ["| Rank | Ticker | Bottleneck | Price (Nov 9) | Valuation status | Expected CAGR | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Bust-case return | Claude % (blind / post) | Codex % (blind / post) | V10.0 % | Disputed inputs and resolution |",
         "|---:|---|---|---:|---|---:|---:|---:|---:|---|---|---:|---|"]
for i, k in enumerate(rank, 1):
    r = R[k]
    res = RESOLVED.get(k) or ("Screen-level: " + r["method"].replace("Screen: ", "") + f"; favorable-model upper bound {r.get('E_upper', 0):.1f}%")
    lines.append(f"| {i} | **{k}** | {BOTTLENECK.get(k, '')} | ${r['price']:,.2f} | {STATUS.get(k, 'Fair' if r['E'] > 5 else 'Expensive')} | {f(r['E'])}% | {f(r['A27'])}% | {f(r['G100'])}% | {f(r['bust'], 0)}% | {pct(CB, k)} / {pct(CP, k)} | {pct(XB, k)} / {pct(XP, k)} | **{FINAL.get(k, 0)}** | {res} |")
open(OUTDIR + "/ranked.md", "w", encoding="utf-8").write("\n".join(lines) + "\n")

# contender detail table (full A1 names)
lines = ["| Ticker | Owner EPS 2030: bust / plateau / base / bull | Base x (bull, plateau, bust) | Cum. div + cash/reserve (base) | TV bust / plateau / base / bull | Probs bear/base/bull | E[TV] | Expected CAGR | AI-2027 TV / CAGR | 100GW TV / CAGR | Delay return | Codex-multiple CAGR |",
         "|---|---|---|---|---|---|---:|---:|---|---|---:|---:|"]
for k in rank:
    r = R[k]
    if not r["method"].startswith("Earnings"):
        continue
    e = r["eps"]; m = r["mult"]; tv = r["tv"]
    lines.append(f"| **{k}** | {e[0]:g} / {e[1]:g} / {e[2]:g} / {e[3]:g} | {m[2]:g} ({m[3]:g}, {m[1]:g}, {m[0]:g}) | {r['div'][2]:g} / {r['cash'][2]:g} | {tv['bust']:.0f} / {tv['plateau']:.0f} / {tv['base']:.0f} / {tv['bull']:.0f} | {'/'.join(str(x) for x in r['pr'])} | {r['etv']:.0f} | {f(r['E'])}% | {r['ai_tv']:.0f} / {f(r['A27'])}% | {r['gw_tv']:.0f} / {f(r['G100'])}% | {f(r['delay'], 0)}% | {f(DX['R'][k]['E'])}% |")
lines.append("")
lines.append("| Ticker (EV method) | States: EBITDA $bn × EV/EBITDA − net claims $bn, ÷ shares bn, + cum. div | TV bust / plateau / base / bull | Probs | E[TV] | Expected CAGR | AI-2027 TV / CAGR | 100GW TV / CAGR | Delay return | Codex-multiple CAGR |")
lines.append("|---|---|---|---|---:|---:|---|---|---:|---:|")
for k in rank:
    r = R[k]
    if not r["method"].startswith("EV"):
        continue
    st = r["ev_states"]; tv = r["tv"]
    sts = "; ".join(f"{a:g}×{b:g}−{c:g} ÷{d:g} +{e:g}" for a, b, c, d, e in st)
    lines.append(f"| **{k}** | {sts} | {tv['bust']:.0f} / {tv['plateau']:.0f} / {tv['base']:.0f} / {tv['bull']:.0f} | {'/'.join(str(x) for x in r['pr'])} | {r['etv']:.0f} | {f(r['E'])}% | {r['ai_tv']:.0f} / {f(r['A27'])}% | {r['gw_tv']:.0f} / {f(r['G100'])}% | {f(r['delay'], 0)}% | {f(DX['R'][k]['E'])}% |")
open(OUTDIR + "/detail.md", "w", encoding="utf-8").write("\n".join(lines) + "\n")

# portfolios
order = ["V9.1 baseline", "Claude blind (V10)", "Codex blind (CX8)", "Claude post-critique", "Codex post-critique", "Arch1 diversified (16)",
         "Arch2 concentrated (7)", "V10.0 final (proposed)", "V10.0 if MOD gate passes", "V10.0 if Texas moratorium law (TLN for VST)", "V10.0 with NVDA 12 (probe)"]
lines = ["| Portfolio | Names | Expected CAGR | Expected total return | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Bust-case return | 2–3 yr delay return | Expected CAGR with Codex multiples | Top-3 weight | HHI |",
         "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
for name in order:
    o = PO[name]; ox = DX["PO"][name]
    b = "**" if name.startswith("V10.0 final") else ""
    lines.append(f"| {b}{name}{b} | {o['n']} | {b}{f(o['E'])}%{b} | {f(o['E_total'], 0)}% | {f(o['A27'])}% | {f(o['G100'])}% | {f(o['bust'])}% | {f(o['delay'])}% | {f(ox['E'])}% | {o['top3']}% | {o['hhi']:.3f} |")
open(OUTDIR + "/portfolios.md", "w", encoding="utf-8").write("\n".join(lines) + "\n")

# sensitivity
lines = ["| Portfolio | Primary (A1 bear = ½ bust + ½ plateau) | Codex-style bear (bear = bust only) | +10% common zero-recovery regime | +20% common zero-recovery regime |", "|---|---:|---:|---:|---:|"]
for name in ["Claude post-critique", "Codex post-critique", "V10.0 final (proposed)"]:
    o = PO[name]
    lines.append(f"| {name} | {f(o['E'])}% | {f(o['E_deepbear'])}% | {f(o['E_zero10'])}% | {f(o['E_zero20'])}% |")
open(OUTDIR + "/sensitivity.md", "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("ok", len(rank))
