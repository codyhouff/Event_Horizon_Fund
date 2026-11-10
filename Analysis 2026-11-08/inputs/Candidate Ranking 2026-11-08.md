# Event Horizon Fund — Step 3, Phase A: Candidate Ranking (2026-11-08 cycle)

**Step 3 of 4** (`PROMPT_3_SYNTHESIS.md`). **Synthesis model:** Claude (Opus 5.5). **Written:** November 9–10, 2026, after the November 9 close.

**Inputs read in full:**

- `inputs/Claude Deep Dive 2026-11-08.md` (Rev 2) and `inputs/Codex Deep Dive 2026-11-08.md` (Nov 9 research revision), including Codex's `research/codex_initial_deep_dive/valuation_outputs.json` ledger for all 56 names it modeled
- `inputs/Claude Critique of Codex 2026-11-08.md` and `inputs/Codex Critique of Claude 2026-11-08.md`, including Codex's `research/codex_cross_critique/critique_model.py`
- `PROMPT_1_DEEP_DIVE.md`; `Analysis 2026-05-10/Event Horizon Fund Analysis 2026-05-10.md`; V7.3 (for continuity)

**Bias disclosure.** I wrote one of the two deep dives, so I start out biased toward it. Section A6 counts every disputed call by which model it went to, and gives the deciding evidence for each call that went to mine.

**Market data.** All prices are the **November 9, 2026 close**, the latest available at the synthesis date. They come from Yahoo's chart endpoint, last bar confirmed at 21:00 UTC; the snapshot is in the companion model files. Consensus and valuation fields are Yahoo quoteSummary pulls from the same evening. The terminal date is **December 31, 2030**, so **T = 4.1424 years**.

**Method in one line.** Every one of the 58 stocks either model held, fully underwrote or raised as an alternative was re-valued on **one** model (A1). Disputed inputs were resolved by the A4 order: facts, then concessions, then the better-supported judgment, with ties going to the lower value. The portfolio was built from the ranking under explicit constraints (A5). No input or weight is an average of the two models' values.

---

## A1. One Set of Scenario Assumptions

### A1.1 Yearly macro paths (worldwide)

S = a published source value; A = my reconciliation or extension. Probabilities apply to the bear/base/bull **buckets** used in Expected CAGR. The two named scenarios are single conditional paths. They are reported beside Expected CAGR and are never added into it.

| Path | Probability | Resembles | Variable | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|---|---|---|
| **Bust** | 12.5% (half of the bear bucket) | Deep bear | AI capex, $T/yr | 0.7 | 0.8 | 0.6 | 0.5 | 0.45 (≈2025 level) A |
| | | | Supplier earnings | 2026 actual | Peak | Falling | Trough | **= FY2025 owner EPS** A |
| | | | Financing | Hyperscaler OCF < capex | Credit closes to neoclouds | Equity raises at lows | — | — |
| **Plateau / delay** | 12.5% (half of the bear bucket) | Mild bear | AI capex, $T/yr | 0.7 | 0.75 | 0.75 | 0.8 | 0.9 A |
| | | | Supplier earnings | | | | | **= FY2026 owner EPS** (growth resumes 2–3 years late) A |
| **Base** | 50% | Base | AI capex, $T/yr | 0.7 | 1.0 | 1.5 | 2.1 | **2.8** A |
| | | | Installed AI compute (H100e, end of year) | ~40M | ~85M | ~160M | ~270M | ~420M A |
| | | | HBM market, $B | ~60 | ~105 | ~130 | ~150 | **~165** (workbook quantities at a flat +3%/yr price, Codex audit) |
| | | | EUV tool shipments (AI share of fleet) | 65 (27%) S | 80 (45%) S | 95 (60%) A | 110 (70%) A | 120 A |
| | | | Global AI datacenter power, GW | 29–37 S | 55 A | 80 A | 110 A | **~150** A |
| | | | Frontier-lab revenue run-rate, $B | ~130–150 (Nov) | ~300 | ~500 | ~700 | ~900 A |
| | | | Financing | Debt share of AI capex rising toward ~30%; capital, not physics, is the governor (Fed hike Sep 2026; 10y peak ~5.3% Oct) | | | | |
| **Bull** | 25% | Bull | AI capex, $T/yr | 0.7 | 1.1 | 2.0 | 3.1 | **4.5** A |
| **AI-2027 Scenario** | **35%** | Base-to-bull (closer to bull) | AI capex, $T/yr | 0.6 S | 1.0 S | **2.4** S (AI-2040, 38% debt-financed) | 3.2 A | **4.2** A |
| | | | Installed compute (H100e, start of year) | 22M S | 57M S | 135M S | 289M S | ~470M A |
| | | | HBM market, $B | 21 S | 41 S | 71 S | 149 S | 306 S (workbook; price escalation compounds) |
| | | | AI share of EUV fleet | 27% S | 45% S | 65% S | 77% S | EUV wall ~2029–30 S |
| | | | Global AI peak power, GW | 29 S | 62 S | 100 A | 150 A | 230 A |
| | | | Frontier ARR, start of year, $B | 30 S | 180 S | 500 S | 1,000 S | — |
| | | | Capability milestones | Coding automation (on point) | Automated coder (authors' medians Dec 2027–Mar 2029) | Automated AI R&D (Kokotajlo ~50% by end-2028) | Superhuman AI researcher | AI-2040 default for full automation |
| **100GW 2030 Scenario** | **10%** (a subset of the bull bucket) | Bull-plus | Total AI investment, $T/yr | ~0.5 S (actual ~0.9–1.0) | >1 S | ~2 S | ~4 A | **~8** S |
| | | | Largest training cluster | ~1 GW / ~1M H100e S | ~3 GW A | ~10 GW / ~10M S | ~30 GW A | **~100 GW / ~100M H100e / $1T+** S |
| | | | AI accelerator shipments (H100e) | 10s of millions S | — | ~100M S | — | 100s of millions S |
| | | | Total AI power vs US electricity | 5% S | — | 20% S | — | ~100% S (the 100 GW cluster alone >20%) |
| | | | AI chips vs today's leading-edge TSMC capacity | ~25% S | — | ~100% S | — | ~4× S |

**Sources:**

- AI-2027 compute forecast and scenario, read at ai-2027.com.
- AI-2040 compute supplement (Jul 2026).
- The shared AI chip compute workbook (Oct 2024), which Codex audited cell by cell.
- Situational Awareness, *Racing to the Trillion-Dollar Cluster*, Tables 4–5 of the June 2024 PDF.
- AI Futures Project timeline updates of Apr 2, Aug 16 and Sep 30, 2026.

**Distance from the 100GW path today:**

- Total AI investment is about a year *ahead* of Situational Awareness's 2026 marker (~$0.9–1.0T against ~$0.5T).
- The largest-cluster milestone is not verified. Neither model found evidence of an energized, coherently networked ~1 GW training cluster, and announced GW are not operating GW.
- The 2030 destination needs 100× the 2026 single-cluster power and 16× the investment.
- Bottlenecks would bind in this order: interconnection, permits and transformers; then firm generation; then HBM, CoWoS and EUV; then financing.
- Near term, the value goes to owners of energized power and electrical/thermal equipment (NRG, VST, NVT, VRT). Later it goes to memory and lithography.

### A1.2 Where the two models' assumptions differed, and what was adopted

| Assumption | Claude | Codex | Adopted | Why |
|---|---|---|---|---|
| AI-2027 Scenario probability | 35%, base-to-bull | 50%, "closest to base" | **35%** | Codex's 50% describes the broad commercial-expansion family, which is my base path. The named scenario as written reaches ~$4.2T of 2030 capex, above any base case. The authors' own end-2027 odds of transformative AI are 23% (Kokotajlo) and 9% (Lifland), and their automated-coder medians run Dec 2027–Mar 2029. |
| 100GW probability | ~10% | 10% | **10%** | Agreed. |
| AI-2027 path beyond 2027 | AI-2040 2028 ($2.4T) and the workbook | AI-2027 S rows, then A extension to $4.2T | **Codex's rows** for capex and power; AI-2040 for compute, EUV and ARR | Codex's power extension (230 GW in 2030) is consistent with the capex path. The workbook's ~435 GW for 2030, which my deep dive cited, matches the 100GW path, not AI-2027. |
| How named scenarios map to stocks | AI-2027 = bull metric × base multiple; 100GW = × U (1.0–1.3) | Explicit per-stock operating bridges | **Codex's method in rule form:** metric = base + λ·s·(bull − base) at the base multiple, with λ = 0.8 for AI-2027 and 2.5 for 100GW | λ(AI-2027) = (4.2 − 2.8)/(4.5 − 2.8) ≈ 0.8, the path's position between the base and bull capex. λ(100GW) = (8.0 − 2.8)/(4.5 − 2.8) ≈ 3.06 × ~0.8 capture (Codex's own bridges imply 0.68–0.92 capture after dilution and margin give-back). s = each stock's AI-capex sensitivity: 1.0 for the hardware chain, 0.7 for power, 0.6 for hyperscalers, 0.3 for data/defense, 0 for biotech. My U factors had no derivation. Codex's AI-2027 bridges sat *below* its own $4.2T path row. |
| Bear bucket | ½ bust + ½ mild bear | One deep bear | **½ bust + ½ plateau**, with both states defined from observable anchors (A1.3); Codex's deep bear retained as the **bust stress** | The bad quartile's mean isn't its tail. The choice moves portfolio Expected CAGR by 0.8–0.9pp and changes no pick (A5 sensitivity). |
| Default probabilities | 25/50/25, fatter bears for several names | 25/50/25; 30/50/20 for KTOS, MP, BNTX, SNDK | **25/50/25**; 30/50/20 for KTOS, MP, BNTX, SNDK (Codex); **30/45/25 for NRG and VST** (Texas, F3) | Stock-specific risks go into explicit inputs (reserves, dilution, claims), not probabilities, unless the risk is a binary outcome that skews the distribution. |
| Terminal multiples | Peer- and history-anchored | Re-rated (Codex cut its own in Step 2) | **Evidence band** (A1.3) | Rank 1 contested item in both critiques. |

### A1.3 Uniform valuation rules applied to every fully modeled stock

- **States.** Terminal value = 2030 owner EPS × multiple + cumulative dividends + excess cash or credit reserve per share. There are four states:
    - **Bust** = FY2025 owner EPS at 0.70× the base multiple.
    - **Plateau** = FY2026 owner EPS at 0.85×.
    - **Base.**
    - **Bull**, at 1.2× the base multiple.

    Cyclicals (MU) and EV-valued names (NRG, VST, TLN, CRWV) carry explicit state inputs. The fiscal year whose midpoint falls in calendar 2025 counts as FY2025.
- **Owner EPS.** Stock-based compensation is charged only where consensus EPS excludes it. Examples: SNPS ×0.69, CRDO ×0.81, META's GAAP EPS unchanged. Acquired-intangible amortization isn't charged.
- **Multiple evidence band.** The band runs from the stock's own forward P/E to the current forward-P/E median of its peers (Nov 9).
    - A value inside the band beats one outside it.
    - If both values are inside, or both outside, the lower one wins.
    - A single-model value above the band is cut to the band top unless its growth earns a premium.
    - No re-rating above today's sector multiples is assumed. Converting forward multiples to trailing (about +10%) roughly offsets long-run mean reversion, since the S&P 500 trailing P/E is 23.9× against a long-run median near 18–20×.

| Peer group (forward P/E, Nov 9) | Members | Median |
|---|---|---|
| Accelerators / semis | NVDA 11.2, AVGO 16.4, AMD 28.8, MRVL 21.0, QCOM 14.0, TSM 16.6 | ~16.6 (18.7 excluding NVDA) |
| Mega-cap platforms | MSFT 22.5, GOOGL 18.7, AMZN 24.5, META 18.0, AAPL 33.2 | 22.5 |
| Electrical / thermal | ETN 21.8, HUBB 19.2, ABB 22.4, SU 18.1, ROK 23.3, APH 22.3, TT 23.7, JCI 19.1, VRT 20.4, NVT 16.4 | ~21 |
| EMS / integration | CLS 10.0, JBL 11.4, FLEX 10.0, SANM 9.2, FN 15.2 | 10.0 |
| Optics | COHR 14.3, LITE 14.9, FN 15.2 | ~15 |
| Equipment | ASML 23.9, AMAT 20.0, LRCX 18.1, KLAC 21.3, TER 20.5 | 20.5 |
| Data / analytics | VRSK 23.0, SPGI 23.3, MCO 27.4, TRI 23.0, EFX 19.7, RELX 18.7, FICO 14.1 | ~21.4 |
| Memory (cyclical) | MU 3.5, SNDK 3.1, WDC 7.2, STX 7.7, SK hynix 3.2 | n/m (cyclical peak) |

---

## A2. Candidate Pool (58 stocks)

| Source | Stocks |
|---|---|
| Held by either model, before or after its critique (24) | NVDA, AVGO, VRT, CLS, NVT, NRG, VST, COHR, TSM, MU, ASML, SNPS, CEG, ETN, CRDO, PWR, KTOS, MP, BNTX, VRSK, plus V9.1 baseline names AMAT, ANET, DELL, CRWD, PLTR, AVAV, MRNA, INTC, GEV, CCJ, BE |
| Fully underwritten by Claude (37) | All V9.1 holdings plus ETN, CRDO, BNTX, LITE, TLN, GOOGL, LRCX, KLAC, AMD, ALAB, CLS, SNDK, CDNS, MRVL |
| Fully underwritten by Codex (56) | All V9.1 holdings plus CLS, NVT, MSFT, GOOGL, AMZN, META, LRCX, KLAC, CDNS, ETN, MOD, PANW, RELX, VRSK, MSI, AXON, GEN, AMD, ALAB, CRDO, HPE, FN, POWL, NRG, TLN, CORZ, IREN, CRWV, APLD, NBIS, MRVL, LITE |
| Raised in a critique as a better alternative | VRSK, RELX, MOD, META, MSI, GEN (Codex); NRG, NVT, CLS (Claude adopting Codex's); SNDK, BNTX (Claude) |

The pool is the union: Codex's 56 names plus BNTX and SNDK, **58 stocks**.

---

## A3. Ranked Table (Nov 9, 2026 close)

**Valuation depth.**

- **Full A1 re-underwrite (27 names):** every stock either model held after its critique, plus every name within reach of the portfolio hurdle on either model's numbers. Tickers: NVDA, NRG, META, CLS, VRT, NVT, MU, VST, TLN, MSFT, TSM, AVGO, RELX, ASML, VRSK, ETN, CRDO, CEG, COHR, PWR, KTOS, MP, LRCX, SNPS, MOD, CRWV, BNTX.
- **Screen-level (31 names):** where both models' own numbers already put the stock below the hurdle, it is re-priced at Nov 9 on the more conservative model's terminal values. The last column gives the more favorable model's figure as an upper bound. No screen-level name's upper bound reaches the final portfolio's marginal holding (VST, 13.0%).

**Price refresh.** Twelve pool names moved more than 10% between the deep dives' Nov 6 data and Nov 9. Each was re-checked:

- **NRG +10.3% and CEG +10.5%:** Q3 results and guidance (A4 facts F1, F2).
- **COHR +16.8%, CRDO +10.3%, FN +11.9%, LITE +10.7%, AMAT +11.4%, LRCX +10.4%, ALAB +13.7%, BE +11.9% and AVAV +12.6%:** a broad chip and AI-hardware rebound after the sector's worst sell-off since 2020. The SOX rose ~6% intraday. No company-specific fundamental change was found.
- **AMD +13.3%:** a Google Cloud processor announcement and an Oppenheimer upgrade.

In every case the move only lowers the stock's expected CAGR, and none moves into the portfolio. NVDA fell 4.3% the same day on a board probe of its CEO (A4 fact F13).

| Rank | Ticker | Bottleneck | Price (Nov 9) | Valuation status | Expected CAGR | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Bust-case return | Claude % (blind / post) | Codex % (blind / post) | V10.0 % | Disputed inputs and resolution |
|---:|---|---|---:|---|---:|---:|---:|---:|---|---|---:|---|
| 1 | **MOD** | Thermal (post-spin pure play) | $106.15 | Speculative (post-spin) | 18.7% | 35.5% | 60.6% | -71% | 0 / 0 | 0 / 0 | **0** | Codex inputs (only model); x22 kept (within band tolerance); 30/50/20. Left out: post-spin perimeter, H1 FCF negative (A5) |
| 2 | **NVDA** | Accelerators / CUDA platform | $178.67 | Attractive | 17.8% | 26.8% | 41.5% | -63% | 13 / 15 | 15 / 15 | **15** | Base EPS 19 C vs 16.6 X; x18 C vs 22 X (peer band); bull 28 C (tie->lower) |
| 3 | **NRG** | Merchant power + retail (TX/PJM) | $97.40 | Attractive (levered) | 17.1% | 24.9% | 35.6% | -67% | 0 / 11 | 12 / 12 | **12** | X EV bridge (sale proceeds spent once); EV 7.3x C-equiv vs 8x X (tie->lower); 30% bear C (Texas facts) |
| 4 | **CRWV** | Neocloud GPU capacity | $48.98 | Speculative (financing) | 16.5% | 35.5% | 62.2% | -100% | 0 / 0 | 0 / 0 | **0** | X only model; 40% zero-equity bear. Left out: bust -100% (A5) |
| 5 | **META** | AI application + ads (buyer) | $641.37 | Attractive | 15.0% | 20.0% | 33.9% | -34% | 0 / 0 | 0 / 0 | **15** | X base/bull (only model); x20 C vs 23 X (X above own 18.0x/peer 22.5x band) |
| 6 | **CLS** | Rack-scale integration (EMS/HPS) | $222.92 | Attractive | 14.8% | 23.2% | 35.6% | -75% | 0 / 7 | 12 / 12 | **10** | Base 29.1 X (owner, 145m sh); x14 C vs 16 X (EMS peers ~10x); bull 40 C (tie->lower) |
| 7 | **VRT** | Rack power + liquid cooling | $200.47 | Fair | 13.8% | 22.0% | 34.9% | -72% | 9 / 14 | 15 / 15 | **14** | Base 15.0 X (tie->lower); bull 21 C (tie->lower); x23 C (tie->lower) |
| 8 | **NVT** | Electrical distribution + liquid cooling | $114.44 | Attractive | 13.7% | 21.4% | 34.0% | -60% | 0 / 11 | 12 / 12 | **12** | Base 10 C, bull 14 C, x19 C (all tie->lower; peer band 16.4-21.8 contains both) |
| 9 | **MU** | HBM / DRAM | $733.15 | Deep Discount (cyclical) | 13.1% | 26.8% | 45.3% | -64% | 9 / 12 | 0 / 8 | **14** | X base 110 x10 + $150 cash (conceded-to by X; tie->lower vs C 130x9); A1 plateau EPS 45 |
| 10 | **VST** | Merchant power (TX/PJM) | $133.92 | Fair | 13.0% | 20.2% | 26.8% | -67% | 9 / 9 | 11 / 11 | **8** | X EV structure; base EBITDA 11 X; EV 8.3x C-equiv vs 9x X (tie->lower); bull EBITDA 13 C-equiv; 30% bear C |
| 11 | **TLN** | Nuclear/gas power (PJM) | $363.13 | Fair | 12.7% | 19.3% | 27.3% | -60% | 0 / 0 | 0 / 0 | **0** | X EV structure; EV 9x X (C-equiv 8.3x below own 9.9x); bull EBITDA 4.5 C-equiv |
| 12 | **MSFT** | AI platform + cloud (buyer) | $545.18 | Fair | 12.3% | 16.7% | 27.1% | -43% | 0 / 0 | 0 / 0 | **0** | X base/bull (only model); x23.5 A (X 29x is 29% above own/peer 22.5x) |
| 13 | **TSM** | Leading-edge foundry + CoWoS | $388.62 | Fair | 11.8% | 17.9% | 26.6% | -61% | 14 / 5 | 0 / 0 | **0** | Base 33 C vs 30.1 X; x19 C vs 21 X (peer band); bull 41.1 X (tie->lower); bear prob 25% (C conceded) |
| 14 | **AXON** | Public-safety platform | $303.18 | Fair | 11.7% | 19.1% | 31.7% | -75% | 0 / 0 | 0 / 0 | **0** | Screen: X deep-dive TVs (35x base multiple, SBC 84% of adj EPS) |
| 15 | **AVGO** | Custom silicon + networking | $319.48 | Fair | 11.6% | 21.4% | 37.6% | -73% | 6 / 11 | 15 / 0 | **0** | Base 23.5 X (owner, SBC 13%); credit reserve X ($43B max, Oct 27 8-K); bull 37.7 C-owner; x20 B |
| 16 | **RELX** | Proprietary data + analytics | $40.02 | Fair | 11.1% | 12.1% | 17.0% | -36% | 0 / 0 | 0 / 0 | **0** | X base/bull (only model); x21 A (X 24x above own 18.7x and peer 21.4x) |
| 17 | **ASML** | EUV lithography | $1,513.25 | Fair | 11.0% | 17.5% | 26.5% | -66% | 8 / 4 | 0 / 0 | **0** | Base 85.65 X (unit bridge; tie->lower vs C 88); bull 108 C (tie->lower vs X 144); x28 B |
| 18 | **VRSK** | Proprietary insurance data | $200.60 | Fair | 10.7% | 12.3% | 17.3% | -44% | 0 / 0 | 0 / 15 | **0** | X base/bull (only model); x23 A (X 28x is 22% above own 23.0x/peer 21.4x) |
| 19 | **ETN** | Electrical equipment | $359.30 | Fair | 10.5% | 14.6% | 20.3% | -46% | 5 / 0 | 0 / 0 | **0** | Base 22.7 X, bull 27 C (both tie->lower); x24 B |
| 20 | **CRDO** | AECs / SerDes | $132.89 | Fair | 10.3% | 19.7% | 36.6% | -71% | 3 / 0 | 0 / 0 | **0** | Base 8.35 X (owner); bull 13.8 C-owner; x22 B |
| 21 | **GOOGL** | AI platform + TPU (buyer) | $288.15 | Fair | 9.9% | 19.0% | 35.0% | -64% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 10.9% |
| 22 | **HPE** | AI servers + networking | $47.54 | Fair | 8.7% | 24.8% | 48.4% | -68% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 8.7% |
| 23 | **CEG** | Nuclear fleet | $276.09 | Expensive | 8.4% | 12.4% | 18.4% | -60% | 6 / 0 | 0 / 0 | **0** | Base 19.5 C, bull 24 C (tie->lower); 2026 guide raised to $12.50-12.80 (F2) |
| 24 | **AMZN** | Cloud + Trainium (buyer) | $266.93 | Fair | 8.3% | 17.3% | 32.6% | -69% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 8.3% |
| 25 | **FN** | Optical contract manufacturing | $365.94 | Fair | 7.7% | 27.1% | 51.6% | -71% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 7.7% |
| 26 | **MSI** | Public-safety comms | $527.97 | Fair | 7.6% | 11.3% | 18.7% | -52% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 7.6% |
| 27 | **SNDK** | NAND / enterprise SSD | $886.51 | Deep Discount (cyclical) | 7.1% | 18.6% | 35.0% | -44% | 0 / 0 | 0 / 0 | **0** | Screen (both models <10%) |
| 28 | **COHR** | Optical transceivers / lasers | $225.19 | Expensive (after +17%) | 6.6% | 14.8% | 29.1% | -77% | 5 / 0 | 8 / 0 | **0** | Base 15.65 X (owner); x18 C vs 20 X (optics peers ~15x); Nov 9 +16.8% |
| 29 | **CDNS** | EDA | $336.53 | Fair | 6.6% | 12.5% | 21.8% | -32% | 0 / 0 | 0 / 0 | **0** | Screen-level: Claude DD TVs (more conservative model); favorable-model upper bound 6.9% |
| 30 | **GEV** | Gas turbines + grid | $829.34 | Fair | 6.1% | 13.8% | 26.5% | -39% | 0 / 0 | 0 / 0 | **0** | Screen-level: Claude DD TVs (more conservative model); favorable-model upper bound 6.5% |
| 31 | **ANET** | DC Ethernet fabric | $186.17 | Fair | 6.1% | 16.3% | 31.6% | -47% | 0 / 0 | 0 / 0 | **0** | Screen-level: Claude DD TVs (more conservative model); favorable-model upper bound 7.6% |
| 32 | **IREN** | Neocloud / miner | $21.41 | Fair | 5.6% | 32.3% | 61.1% | -100% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 5.6% |
| 33 | **DELL** | AI servers | $346.31 | Fair | 5.6% | 15.4% | 29.1% | -39% | 0 / 0 | 0 / 0 | **0** | Screen-level: Claude DD TVs (more conservative model); favorable-model upper bound 10.2% |
| 34 | **CORZ** | Neocloud hosting | $12.72 | Fair | 5.6% | 28.5% | 53.8% | -100% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 5.6% |
| 35 | **KLAC** | Process control WFE | $151.38 | Fair | 5.5% | 13.9% | 26.6% | -37% | 0 / 0 | 0 / 0 | **0** | Screen-level: Claude DD TVs (more conservative model); favorable-model upper bound 8.3% |
| 36 | **GEN** | Consumer identity | $29.80 | Fair | 5.3% | 5.8% | 8.8% | -53% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 5.3% |
| 37 | **PWR** | Grid construction | $591.48 | Expensive | 5.1% | 9.9% | 15.6% | -80% | 2 / 0 | 0 / 0 | **0** | Base 31 C, bull 37 C (tie->lower); x25 B |
| 38 | **AMAT** | Deposition WFE | $370.55 | Expensive | 4.6% | 15.4% | 30.2% | -49% | 0 / 0 | 0 / 0 | **0** | Screen-level: Claude DD TVs (more conservative model); favorable-model upper bound 6.8% |
| 39 | **AVAV** | Drones / loitering munitions | $126.96 | Expensive | 4.6% | 9.4% | 17.6% | -65% | 0 / 0 | 0 / 0 | **0** | Screen-level: Claude DD TVs (more conservative model); favorable-model upper bound 6.3% |
| 40 | **LITE** | Optical components | $596.16 | Expensive | 4.4% | 22.2% | 44.0% | -78% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 6.2% |
| 41 | **BNTX** | Bio-risk (mRNA + oncology) | $87.51 | Speculative | 4.3% | 4.5% | 4.5% | -49% | 1 / 1 | 0 / 0 | **0** | X SOTP (cash AFTER 4 years of burn) over C's $65 bear on today's cash |
| 42 | **APLD** | Neocloud hosting | $16.72 | Expensive | 3.8% | 28.7% | 54.9% | -100% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 3.8% |
| 43 | **LRCX** | Etch/dep WFE | $221.31 | Fair | 3.6% | 10.0% | 22.3% | -63% | 0 / 0 | 0 / 0 | **0** | Base 12.38 X; x19 C (in band 18.1-20.5; X 22 above); bull 18 C |
| 44 | **POWL** | Switchgear | $141.65 | Expensive | 3.2% | 18.6% | 38.7% | -80% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 3.2% |
| 45 | **MP** | Rare-earth magnets | $37.75 | Speculative | 2.3% | 9.4% | 19.6% | -95% | 2 / 0 | 0 / 0 | **0** | Base 1.8 C, bull 3.0 C (tie->lower); x24 X; 30/50/20 X |
| 46 | **SNPS** | EDA + simulation | $466.97 | Expensive (owner basis) | 2.1% | 6.0% | 11.6% | -66% | 6 / 0 | 0 / 0 | **0** | Owner EPS: SBC ~31% of adjusted EPS -> base 18.9 C-owner vs 24 X |
| 47 | **CCJ** | Uranium | $75.37 | Expensive | 2.1% | 11.4% | 28.3% | -81% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 3.9% |
| 48 | **PLTR** | AI operating software | $169.20 | Expensive | 1.0% | 5.1% | 16.6% | -88% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 4.4% |
| 49 | **MRVL** | Custom silicon / optics DSP | $154.60 | Expensive | 0.5% | 17.7% | 38.8% | -82% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 6.3% |
| 50 | **AMD** | Accelerators (#2) | $508.58 | Expensive | -1.6% | 17.8% | 41.7% | -88% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 2.6% |
| 51 | **ALAB** | PCIe/CXL connectivity | $216.87 | Expensive | -1.6% | 18.1% | 42.1% | -92% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 11.1% |
| 52 | **KTOS** | AI-enabled defense | $37.69 | Speculative | -2.1% | 2.3% | 7.3% | -93% | 2 / 0 | 0 / 0 | **0** | Owner EPS 1.33 C (tie->lower); x28 X (tie->lower); 30/50/20 X |
| 53 | **NBIS** | Neocloud | $141.45 | Expensive | -3.6% | 19.6% | 44.0% | -100% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound -3.6% |
| 54 | **PANW** | Security platform | $330.89 | Expensive | -5.6% | -2.0% | 6.6% | -82% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound -5.6% |
| 55 | **MRNA** | mRNA vaccines | $269.00 | Expensive | -7.1% | -9.7% | -9.7% | -98% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound -6.1% |
| 56 | **BE** | Fuel-cell grid bypass | $193.88 | Expensive | -10.5% | 5.7% | 26.5% | -98% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound 7.2% |
| 57 | **CRWD** | AI-native security | $228.58 | Expensive | -12.5% | -9.0% | 0.7% | -93% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound -9.9% |
| 58 | **INTC** | Domestic foundry | $59.37 | Expensive | -15.1% | -2.9% | 15.6% | -90% | 0 / 0 | 0 / 0 | **0** | Screen-level: Codex DD TVs (more conservative model); favorable-model upper bound -1.2% |

### A3.1 Full A1 inputs for every fully modeled stock

Owner EPS in $/share; terminal values in $/share at Dec 31, 2030. The last column is the robustness run that sets every disputed multiple to Codex's value.

| Ticker | Owner EPS 2030: bust / plateau / base / bull | Base x (bull, plateau, bust) | Cum. div + cash/reserve (base) | TV bust / plateau / base / bull | Probs bear/base/bull | E[TV] | Expected CAGR | AI-2027 TV / CAGR | 100GW TV / CAGR | Delay return | Codex-multiple CAGR |
|---|---|---|---|---|---|---:|---:|---|---|---:|---:|
| **MOD** | 2 / 4.7 / 8.84 / 19.05 | 22 (26.4, 18.7, 15.4) | 0 / 0 | 31 / 88 / 194 / 503 | 30/50/20 | 216 | 18.7% | 374 / 35.5% | 756 / 60.6% | -17% | 18.7% |
| **NVDA** | 4.9 / 9.03 / 19 / 28 | 18 (21.6, 15.3, 12.6) | 5 / 0 | 66 / 142 / 347 / 611 | 25/50/25 | 352 | 17.8% | 477 / 26.8% | 753 / 41.5% | -20% | 23.6% |
| **META** | 29.69 / 29.12 / 49.23 / 87.69 | 20 (24, 17, 14) | 10 / 0 | 424 / 504 / 995 / 2117 | 25/50/25 | 1142 | 15.0% | 1365 / 20.0% | 2150 / 33.9% | -21% | 18.9% |
| **CLS** | 5.63 / 10.75 / 29.14 / 40 | 14 (16.8, 11.9, 9.8) | 0 / 0 | 55 / 128 / 408 / 672 | 25/50/25 | 395 | 14.8% | 530 / 23.2% | 788 / 35.6% | -43% | 18.6% |
| **VRT** | 3.41 / 7.05 / 15 / 21 | 23 (27.6, 19.6, 16.1) | 1.5 / 0 | 56 / 139 / 346 / 582 | 25/50/25 | 343 | 13.8% | 457 / 22.0% | 692 / 34.9% | -31% | 15.0% |
| **NVT** | 3.22 / 5.16 / 10 / 14 | 19 (22.8, 16.1, 13.3) | 4 / 0 | 46 / 87 / 194 / 324 | 25/50/25 | 195 | 13.7% | 256 / 21.4% | 385 / 34.0% | -24% | 17.7% |
| **MU** | 20 / 45 / 110 / 187.5 | 10 (9, 10.5, 11) | 8 / 150 | 264 / 568 / 1258 / 1950 | 25/50/25 | 1220 | 13.1% | 1961 / 26.8% | 3450 / 45.3% | -22% | 13.1% |
| **MSFT** | 17.95 / 20.01 / 34.47 / 52.78 | 23.5 (28.2, 20, 16.4) | 16 / 0 | 309 / 415 / 826 / 1508 | 25/50/25 | 881 | 12.3% | 1035 / 16.7% | 1474 / 27.1% | -24% | 18.0% |
| **TSM** | 10.4 / 17.5 / 33 / 41.1 | 19 (22.8, 16.1, 13.3) | 17 / 0 | 153 / 299 / 644 / 957 | 25/50/25 | 618 | 11.8% | 770 / 17.9% | 1032 / 26.6% | -23% | 14.5% |
| **AVGO** | 5.93 / 10.15 / 23.5 / 37.7 | 20 (24, 17, 14) | 13 / -2 | 86 / 180 / 481 / 921 | 25/50/25 | 504 | 11.6% | 712 / 21.4% | 1199 / 37.6% | -44% | 11.6% |
| **RELX** | 1.47 / 1.89 / 2.53 / 3.69 | 21 (25.2, 17.8, 14.7) | 5 / 0 | 26 / 38 / 58 / 99 | 25/50/25 | 62 | 11.1% | 64 / 12.1% | 77 / 17.0% | -4% | 14.4% |
| **ASML** | 24.71 / 41.41 / 85.65 / 108 | 28 (33.6, 23.8, 19.6) | 40 / 0 | 514 / 1021 / 2438 / 3679 | 25/50/25 | 2331 | 11.0% | 2947 / 17.5% | 4013 / 26.5% | -33% | 11.0% |
| **VRSK** | 6.48 / 7.39 / 12.375 / 17.87 | 23 (27.6, 19.6, 16.1) | 9 / 0 | 112 / 153 / 294 / 503 | 25/50/25 | 306 | 10.7% | 324 / 12.3% | 389 / 17.3% | -24% | 15.9% |
| **ETN** | 10.45 / 13.78 / 22.7 / 27 | 24 (28.8, 20.4, 16.8) | 20 / 0 | 193 / 299 / 565 / 800 | 25/50/25 | 544 | 10.5% | 632 / 14.6% | 773 / 20.3% | -17% | 10.5% |
| **CRDO** | 2.51 / 5.11 / 8.35 / 13.8 | 22 (26.4, 18.7, 15.4) | 0 / 0 | 39 / 96 / 184 / 364 | 25/50/25 | 200 | 10.3% | 280 / 19.7% | 483 / 36.6% | -28% | 10.3% |
| **CEG** | 7.4 / 12.65 / 19.5 / 24 | 20 (24, 17, 14) | 7 / 0 | 110 / 222 / 397 / 584 | 25/50/25 | 386 | 8.4% | 448 / 12.4% | 555 / 18.4% | -20% | 8.4% |
| **COHR** | 4.12 / 9.13 / 15.65 / 23.8 | 18 (21.6, 15.3, 12.6) | 0 / 0 | 52 / 140 / 282 / 514 | 25/50/25 | 293 | 6.6% | 399 / 14.8% | 648 / 29.1% | -38% | 9.3% |
| **PWR** | 6.8 / 17.1 / 31 / 37 | 25 (30, 21.2, 17.5) | 2 / 0 | 121 / 365 / 777 / 1113 | 25/50/25 | 728 | 5.1% | 874 / 9.9% | 1078 / 15.6% | -38% | 5.1% |
| **LRCX** | 5.76 / 9.65 / 12.38 / 18 | 19 (22.8, 16.1, 13.3) | 7 / 0 | 82 / 162 / 242 / 418 | 25/50/25 | 256 | 3.6% | 328 / 10.0% | 510 / 22.3% | -27% | 7.2% |
| **MP** | 0 / 0.73 / 1.8 / 3 | 24 (28.8, 20.4, 16.8) | 0 / 0 | 2 / 15 / 43 / 86 | 30/50/20 | 41 | 2.3% | 55 / 9.4% | 79 / 19.6% | -61% | 2.3% |
| **SNPS** | 8.04 / 10.45 / 18.9 / 23.1 | 28 (33.6, 23.8, 19.6) | 0 / 0 | 158 / 249 / 529 / 776 | 25/50/25 | 509 | 2.1% | 595 / 6.0% | 735 / 11.6% | -47% | 3.8% |
| **KTOS** | 0.13 / 0.66 / 1.33 / 1.96 | 28 (33.6, 23.8, 19.6) | 0 / 0 | 3 / 16 / 37 / 66 | 30/50/20 | 35 | -2.1% | 41 / 2.3% | 50 / 7.3% | -58% | -2.1% |

| Ticker (EV method) | States: EBITDA $bn × EV/EBITDA − net claims $bn, ÷ shares bn, + cum. div | TV bust / plateau / base / bull | Probs | E[TV] | Expected CAGR | AI-2027 TV / CAGR | 100GW TV / CAGR | Delay return | Codex-multiple CAGR |
|---|---|---|---|---:|---:|---|---|---:|---:|
| **NRG** | 4×6−19 ÷0.21 +8; 5×6.75−17 ÷0.2 +8.5; 6.5×7.3−14 ÷0.19 +9; 8.5×8.3−11 ÷0.18 +10 | 32 / 92 / 185 / 341 | 30/45/25 | 187 | 17.1% | 244 / 24.9% | 344 / 35.6% | -5% | 20.6% |
| **CRWV** | 4.8×6−45 ÷0.65 +0; 4.8×6−45 ÷0.65 +0; 17.6×8−65 ÷0.75 +0; 30×10−80 ÷0.85 +0 | 0 / 0 / 101 / 259 | 40/40/20 | 92 | 16.5% | 172 / 35.5% | 363 / 62.2% | -100% | 16.5% |
| **VST** | 6×6.6−26 ÷0.34 +4; 7×7.4−23 ÷0.32 +4.5; 11×8.3−20 ÷0.3 +5; 13×9.3−16 ÷0.29 +6 | 44 / 95 / 243 / 368 | 30/45/25 | 222 | 13.0% | 287 / 20.2% | 358 / 26.8% | -29% | 15.8% |
| **TLN** | 1.75×7−5 ÷0.05 +0; 2.3×8−7 ÷0.048 +0; 3.6×9−5 ÷0.045 +0; 4.5×10−3 ÷0.043 +0 | 145 / 237 / 609 / 977 | 25/50/25 | 596 | 12.7% | 753 / 19.3% | 986 / 27.3% | -35% | 12.7% |

---

## A4. Disputed Inputs and How They Were Resolved

### A4.1 Facts (verified at the primary source; the verified value wins)

| # | Fact | Claude had | Codex had | Primary-source check | Resolved |
|---|---|---|---|---|---|
| F1 | NRG outlook | Not covered (Step 1) | Aug 4 guidance (Step 1) | [NRG Q3 release, Nov 9](https://investors.nrg.com/news-releases/news-release-details/nrg-energy-reports-third-quarter-2026-results-reaffirms-2026): 2026 reaffirmed (EBITDA slightly below midpoint on weak ERCOT prices). 2027 EBITDA $5.5–6.0B and FCF before growth $2.9–3.4B, excluding a $4B, 4.9 GW asset sale (close targeted Q2 2027) | Both critiques use it. Sold-asset EBITDA (~$0.5B) is an assumption, not disclosed |
| F2 | CEG 2026 guidance | ~$12.00 midpoint | Aug guide | [CEG Q3 release, Nov 9](https://www.constellationenergy.com/news/2026/11/constellation-reports-third-quarter-2026-results.html): raised to $12.50–12.80 | Plateau anchor uses $12.65 |
| F3 | Texas data-center politics | Governor-elect pledged a moratorium | Not mentioned | [CNN, Nov 5](https://www.cnn.com/2026/11/05/economy/data-center-texas-election); [ABC13](https://abc13.com/post/governor-elect-gina-hinojosa-vows-ban-future-data-centers-texas/20021143/): a pledge on new approvals that needs the Legislature (session opens Jan 2027); Abbott's September TCEQ permit pause; ~40 of 41 local restrictions passed Nov 3 | Confirmed. Drives the NRG/VST 30% bear and the 20% Texas cap |
| F4 | AVGO financing exposure | ~$29B maximum (10-Q, Sep) | ~$43B maximum undiscounted (Oct 27 8-K) | Codex cites the newer [Oct 27 8-K](https://investors.broadcom.com/static-files/0ee4f6b7-4a23-4de0-8f3e-48f147ae30d3) (72.5% of remaining lease payments less realized rack value). Not re-fetched here | **$43B adopted** as the newer and more conservative figure; flagged as verified by Codex only |
| F5 | VST 2027 guidance scope | Added a Cogentrix increment on top | Consolidated | [Vistra Q3 release, Nov 6](https://www.sec.gov/Archives/edgar/data/1692819/000169281926000023/vistra-20260930xearningsre.htm): 2027 EBITDA $7.7–8.5B is consolidated after the October close | Codex. No extra increment |
| F6 | NVT trajectory | — | 2026 adjusted EPS $5.36–5.39; +44% organic | [NVT Q3 release, Oct 30](https://www.sec.gov/Archives/edgar/data/0001720635/000162828026068391/q32026nvtpressrelease.htm): confirmed; Q4 organic growth guided to 26–29% | Both. The deceleration supports the lower base EPS and multiple (ties) |
| F7 | CLS cash and dilution | FCF cut to $460M; capex $1.5–2.0B; offering closed Aug 7 | 2027 outlook: $40B revenue, $21.50 adjusted EPS | [Celestica Q3 release, Oct 26](https://www.sec.gov/Archives/edgar/data/1030894/000103089426000049/cls-20260930prcondensedfs.htm); FY25 adjusted EPS $6.05 ([Jan 28 release](https://www.sec.gov/Archives/edgar/data/1030894/000103089426000006/cls-20251231prcondensedfs.htm)) | Both facts stand. Explicit dilution (145m shares) plus a 10% weight cap |
| F8 | ASML earnings power | Q3 gross margin 57.5%, operating margin 44.4% | FY26 €44–45B; 2027 low-NA capacity +~30% | [ASML Q3 release, Oct 14](https://www.sec.gov/Archives/edgar/data/0000937966/000162828026065813/pressreleasefinancialresul.htm) | Both facts stand. Base $85.65 (tie) |
| F9 | MU contract book | LTAs cover >50% of 2027–28 capacity | 26 agreements, >35% of revenue through 2030, floors/ceilings | [Micron Q4 FY26 prepared remarks, Sep 30](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf) `[STALE >30d]` | Not a conflict: the same contract book |
| F10 | TSM 2025 EPS (bust anchor) | ~$10, unverified | $8.45 bear (judgment) | Yahoo annual diluted EPS: NT$331.25 per ADR for FY2025, ≈ **$10.4** at ~NT$32/$ | Resolved: $10.4 |
| F11 | AI-2040 "~$1.2M per wafer" | Cited as TSMC pricing power | An all-in cost; the foundry component is ~$25–30k | [AI-2040 compute supplement](https://ai-2040.com/supplements/compute-supplement) | **Codex.** No TSMC price uplift from that figure. My TSM base rests on consensus and volume, not on it |
| F12 | BNTX cash | ~85% of market cap | €16.164B cash, 247.9m shares, continuing losses | [BioNTech Q3, Nov 3](https://www.biontech.com/us/en/home/mediaroom/news/press-releases/2026/11/BioNTech-Announces-Third-Quarter-2026-Financial-Results-and-Corporate-Update.html) | Codex. Value cash *after* burn |
| F13 | NVDA governance (new, Nov 8–9) | — | — | [Yahoo/24/7 Wall St, Nov 9](https://finance.yahoo.com/markets/stocks/articles/nvidia-falls-5-board-probes-134356169.html); [CNN, Nov 9](https://www.cnn.com/2026/11/09/investing/nvidia-stock-huang-investigation). In a Nov 8 memo, Huang admitted an extramarital affair. The board opened an independent review of his relationship with a woman US intelligence reportedly suspects is a Chinese agent. China calls the allegation "unsubstantiated." No 8-K or regulator action reported; Huang has not stepped aside. NVDA −4.3% while the SOX rose ~6% | **New key-person risk.** Not modeled as an input change. Handled by staged deployment around Nov 17 earnings and escalation E2 |
| F14 | Meta 2025 EPS (bust anchor) | — | — | [Meta Q3 2025 8-K](https://www.sec.gov/Archives/edgar/data/1326801/000162828025047114/meta-09302025xexhibit991.htm): one-time non-cash tax charge of $15.93B (+$6.20 EPS) | FY25 EPS $23.49 + $6.20 = $29.69 |
| F15 | NVT and AVGO FY25 adjusted EPS (bust anchors) | — | — | NVT FY25 adjusted EPS $3.35 ([Q4 2025 release](https://s22.q4cdn.com/268397047/files/doc_financials/2025/q4/Q4-2025-NVT-Press-Release.pdf)); AVGO FY25 non-GAAP EPS $6.82 ([8-K, Dec 11, 2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000116/avgo-11022025x8kxex99.htm)) | Used × owner factor |

### A4.2 Concessions made in Step 2 (adopted unless newer evidence contradicts)

| Conceded by | What was conceded | Adopted? |
|---|---|---|
| Claude | NRG, NVT and CLS belong in the pool; owner EPS for CRDO and KTOS; my bears were too mild; the 30% bulls for TSM and ASML were unsupported; exits from SNPS, CEG, ETN, PWR, KTOS, MP; COHR exit at Nov 9 prices | Yes, all |
| Claude | Codex's Step 1 AVGO EPS path ($25.5) | **Superseded.** Codex lowered its own AVGO base to $23.5 on an owner basis in Step 2 |
| Codex | MU deserves capital (replaces COHR); ASML's earnings bridge was too low ($63.5 → $85.65); its own terminal multiples were too high (NVDA 25 → 22, AVGO 24 → 20, VRT 26 → 24, CLS 17 → 16, COHR 24 → 20); AVGO needs an explicit financing reserve; KTOS is the weakest Claude holding; CRDO revenue was too low | Yes. Multiples that remain disputed after the concession go to A4.3 |

### A4.3 Judgment inputs (better-supported value wins; a genuine tie goes to the lower value; nothing averaged)

| # | Ticker | Input | Claude | Codex | Adopted | Went to | Basis | Deciding evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | NVDA | Base 2030 EPS | $19 | $16.64 | $19 | Claude | evidence | Codex's $16.64 is only +4.5% above the FY28 (CY27) consensus of $15.92, i.e. flat 2027-30 earnings while the A1 base path takes AI capex from ~$1.0T to ~$2.8T. $19 (+19%) is still conservative. |
| 2 | NVDA | Base exit P/E | 18x | 22x | 18x | Claude | evidence | Evidence band: own forward 11.2x to semis-peer median ~18.7x (AVGO 16.4, AMD 28.8, MRVL 21.0, QCOM 14.0). 22x sits above the band; Codex itself cut from 25x in Step 2. |
| 3 | NVDA | Bull 2030 EPS | $28 | $30.43 | $28 | Claude | tie | No decisive evidence either way; lower value. |
| 4 | AVGO | Base 2030 EPS | $25.5 (adjusted) | $23.5 (owner) | $23.5 | Codex | evidence | Stock comp is ~13% of adjusted EPS; Codex's 47% common margin is on an owner basis. |
| 5 | AVGO | XPV financing exposure | -$6/sh bear + 30% bear | -$8/-$2/0 reserve, 25% bear | Codex reserve, 25/50/25 | Codex | evidence | Newer primary source (Oct 27 8-K, ~$43B maximum undiscounted exposure, per Codex citation; not re-fetched here, adopted because it is the more conservative figure). One mechanism only, so no double count. |
| 6 | AVGO | Bull 2030 EPS | $37.7 (owner) | $40.4 | $37.7 | Claude | tie | Lower value. |
| 7 | VRT | Base 2030 EPS | $15.5 | $15.0 | $15.0 | Codex | tie | Lower value. |
| 8 | VRT | Bull 2030 EPS | $21 | $26.05 | $21 | Claude | tie | Lower value; Codex's bull needs a 22% owner net margin, above today's ~16-17%. |
| 9 | VRT | Base exit P/E | 23x | 24x | 23x | Claude | tie | Both above the thermal/electrical peer median (~21x); lower value. |
| 10 | CLS | Base 2030 EPS | ~$30 | $29.14 (owner, 145m shares) | $29.14 | Codex | evidence | Owner basis with explicit dilution after the Aug 2026 offering. |
| 11 | CLS | Base exit P/E | 14x | 16x | 14x | Claude | evidence | EMS peers JBL 11.4x, FLEX 10.0x, SANM 9.2x, FN 15.2x; own 10.0x. Both values above the band; 16x is further above it. |
| 12 | CLS | Bull 2030 EPS | $40 | $47.5 | $40 | Claude | tie | Lower value. |
| 13 | CLS | Probabilities | 30/45/25 | 25/50/25 | 25/50/25 | Codex | evidence | Cash conversion and dilution are already in the explicit inputs; a fatter bear would double-count them. |
| 14 | NVT | Base 2030 EPS | $10.0 | $10.63 | $10.0 | Claude | tie | Lower value; Q4 organic growth guided down to 26-29% (Oct 30). |
| 15 | NVT | Base exit P/E | 19x | 22x | 19x | Claude | tie | Both inside the band (own 16.4x, electrical peers ~21.8x); lower value. |
| 16 | NVT | Bull 2030 EPS | $14 | $16.6 | $14 | Claude | tie | Lower value. |
| 17 | MU | Base 2030 EPS / multiple / cash | $130 x 9 | $110 x 10 + $150 cash | Codex | Codex | tie | Codex conceded upward from $80; tie between pairs resolved to the lower terminal value. |
| 18 | MU | Bull | $290 x 7 | $187.5 x 9 + $250 cash | Codex | Codex | tie | Lower value. |
| 19 | TSM | Base 2030 EPS | $33 | $30.1 | $33 | Claude | evidence | CY27 consensus $23.39 (up from $21.28 90 days ago); 2026 EPS +64%. Codex's $30.1 implies 8.8%/yr 2027-30 while A1 base AI capex rises ~2.8x. |
| 20 | TSM | Base exit P/E | 19x | 21x | 19x | Claude | evidence | Own forward 16.6x; semis-peer median ~18.7x. 21x above the band. |
| 21 | TSM | Bull 2030 EPS | $42 | $41.1 | $41.1 | Codex | tie | Lower value. |
| 22 | TSM | Bull probability | 30% | 25% | 25% | Codex | concession | Claude conceded in Step 2 (no stock-specific support for 30%). |
| 23 | ASML | Base 2030 EPS | $88 | $85.65 | $85.65 | Codex | tie | Both built from capacity; lower value. |
| 24 | ASML | Bull 2030 EPS | $108 | $144 | $108 | Claude | tie | Lower value. |
| 25 | NRG | Valuation method | FCF/share x 9 | EV/EBITDA less claims | EV bridge | Codex | evidence | Explicit net claims ($22.8B today), asset-sale proceeds spent once, buybacks in the share count. |
| 26 | NRG | Base EV/EBITDA | ~7.3x (equivalent) | 8x | 7.3x | Claude | tie | Both in the band (own 7.2x on 2027 guidance; IPP peers ~8-10x); lower value. |
| 27 | NRG | Probabilities | 30/45/25 | 25/50/25 | 30/45/25 | Claude | evidence | Texas governor-elect's data-center moratorium pledge, Abbott's TCEQ permit pause, ~40 of 41 local restrictions passed Nov 3. Texas was 51% of NRG's Q3 EBITDA. Codex's critique does not address Texas. |
| 28 | VST | Cogentrix increment | Added on top of guide | None (guide is consolidated) | None | Codex | fact | Vistra Nov 6 release: 2027 EBITDA $7.7-8.5B is consolidated after the October Cogentrix close. |
| 29 | VST | Base EV/EBITDA | ~8.3x (equivalent) | 9x | 8.3x | Claude | tie | Both in band (own 8.1x on 2027 guidance); lower value. |
| 30 | VST | Bull 2030 EBITDA | ~$13B | $14B | $13B | Claude | tie | Lower value. |
| 31 | VST | Probabilities | 30/45/25 | 25/50/25 | 30/45/25 | Claude | evidence | Same Texas evidence as NRG; VST fell 14% on election day. |
| 32 | TLN | Base EV/EBITDA | ~8.3x (equivalent) | 9x | 9x | Codex | evidence | Claude's equivalent sits below the band (own 9.9x on 2027 guidance). |
| 33 | COHR | Base 2030 EPS | $16.7 (owner) | $15.65 | $15.65 | Codex | tie | Lower value. |
| 34 | COHR | Base exit P/E | 18x | 20x | 18x | Claude | evidence | Optics peers LITE 14.9x, FN 15.2x; own 14.3x. Both above the band; 20x further above. |
| 35 | CRDO | Base 2030 EPS | $8.5 | $8.35 | $8.35 | Codex | tie | Both owner basis; lower value. |
| 36 | CRDO | Bull 2030 EPS | $13.8 | $17.6 | $13.8 | Claude | tie | Lower value. |
| 37 | SNPS | Base 2030 owner EPS | $18.9 | $24.0 | $18.9 | Claude | evidence | FY25 stock comp $0.89B is ~31% of adjusted EPS after tax; Codex's 30% margin after stock comp is above the current ~23-25%. |
| 38 | SNPS | Base exit P/E | 28x | 30x | 28x | Claude | tie | Lower value. |
| 39 | CEG | Base / bull 2030 EPS | $19.5 / $24 | $19.7 / $30 | $19.5 / $24 | Claude | tie | Lower values. |
| 40 | ETN | Base / bull 2030 EPS | $23 / $27 | $22.7 / $35.9 | $22.7 / $27 | Split | tie | Lower value on each input (one to each side). |
| 41 | PWR | Base / bull 2030 EPS | $31 / $37 | $32 / $50.7 | $31 / $37 | Claude | tie | Lower values. |
| 42 | KTOS | Base EPS / multiple / probabilities | $1.33 / 30x / 30-45-25 | $1.37 / 28x / 30-50-20 | $1.33 / 28x / 30-50-20 | Split | tie | Lower value on each input. |
| 43 | MP | Base EPS / multiple / probabilities | $1.8 / 26x / 30-45-25 | $2.1 / 24x / 30-50-20 | $1.8 / 24x / 30-50-20 | Split | tie | Lower value on each input. |
| 44 | BNTX | Terminal values | $65 / $120 / $210 | $45 / $105 / $190 | Codex | Codex | evidence | Claude's bear used today's cash; Codex's uses cash after four years of burn (Q3: EUR16.2B cash, 247.9m shares, continuing losses). |
| 45 | LRCX | Base EPS / multiple / bull | $14 / 19x / $18 | $12.38 / 22x / $22.5 | $12.38 / 19x / $18 | Split | tie | Lower value on each input; 19x is inside the band (own 18.1x, equipment peers ~20.5x). |
| 46 | META | Base exit P/E | 20x (Step 2 screen) | 23x | 20x | Claude | evidence | Own forward 18.0x; mega-cap peer median 22.5x. 23x is above the band. |
| 47 | Framework | AI-2027 Scenario probability | 35% | 50% | 35% | Claude | evidence | The authors' own end-2027 TED-AI odds are 23% (Kokotajlo) and 9% (Lifland); automated-coder medians are Dec 2027-Mar 2029; capability pace is 70-90%. The as-written path (2030 capex ~$4.2T) sits above the A1 base. |
| 48 | Framework | Named-scenario construction | Bull metric x base multiple; 100GW = x U (1.0-1.3) | Explicit path-based operating bridges | Codex's method, in rule form | Codex | evidence | Scaling each stock's bull-base spread along the capex axis ties both scenarios to sourced paths; Claude's U factors had no derivation. |
| 49 | Framework | AI-2027 loading | 1.0 (bull metric) | ~0.3-0.5 (implied by bridges) | 0.8 | Neither | evidence | Position of the $4.2T AI-2027 path between the A1 base ($2.8T) and bull ($4.5T). Codex's bridges sat below its own $4.2T path row. |
| 50 | Framework | Bear bucket | 50/50 mix of bust and mild bear | Single deep bear | Mix; Codex's deep bear kept as the bust stress | Claude | evidence | A deep bust is the tail of the bad quartile, not its mean. The choice moves portfolio Expected CAGR by <1pp (sensitivity table). |
| 51 | Construction | Texas merchant-power cap (NRG+VST) | 20% | 23% | 20% | Claude | evidence | Same Texas facts as above. |
| 52 | Construction | CLS weight cap | 7% | 12% | 10% | Neither | evidence | FY26 FCF $460M (~35% of net income), 2027 capex $1.5-2.0B and an Aug equity raise support a below-standard cap; explicit inputs already carry part of the risk. |
| 53 | Multiples (single-model) | VRSK / RELX / MSFT base P/E | not modeled | 28x / 24x / 29x | 23x / 21x / 23.5x | Neither | evidence | A1 multiple policy: above the own/peer band with no growth premium (VRSK own 23.0x; RELX own 18.7x, peers 21.4x; MSFT own and peers 22.5x). |

---

## A5. From Ranking to Portfolio

### A5.1 Constraints

| Constraint | Value | Source |
|---|---|---|
| Single-name cap | 15% | PROMPT_1 default |
| Texas/ERCOT merchant power (NRG + VST) | ≤ 20% | A4 #50 (Texas facts, F3) |
| Confidence / leverage caps | CLS ≤ 10%; NRG ≤ 12%; NVT ≤ 12%; speculative names (confidence 2) start at 0% and enter only through a dated gate | A4 #51; both models capped lower-confidence names (Codex 12%, Claude 7%) |
| AI-silicon and integration cluster (NVDA, MU, CLS, plus any TSM/AVGO/COHR/CRDO) | ≤ 50% | Both critiques |
| Bust case | Better than V9.1 on the same A1 basis (−67.3%) | PROMPT_1: losses are a constraint |
| Tie-break | Within ~2pp of Expected CAGR, prefer the higher AI-2027 Scenario CAGR | PROMPT_1 Goal |

### A5.2 Final weights (V10.0, proposed)

| Ticker | Rank | Expected CAGR | AI-2027 | 100GW | Weight | Why this weight |
|---|---:|---:|---:|---:|---:|---|
| NVDA | 2 | 17.8% | 26.8% | 41.5% | **15** | Highest-ranked eligible name; the cap binds |
| META | 5 | 15.0% | 20.0% | 33.9% | **15** | Next eligible; the mildest bust of any top-10 name (−34%); the cap binds |
| VRT | 7 | 13.8% | 22.0% | 34.9% | **14** | Next by rank after the capped names |
| MU | 9 | 13.1% | **26.8%** | **45.3%** | **14** | Wins the tie-break inside the #7–#14 band (highest AI-2027 and 100GW CAGRs in that band) |
| NRG | 3 | 17.1% | 24.9% | 35.6% | **12** | Leverage cap; Texas cluster |
| NVT | 8 | 13.7% | 21.4% | 34.0% | **12** | Integration cap |
| CLS | 6 | 14.8% | 23.2% | 35.6% | **10** | Cash-conversion cap |
| VST | 10 | 13.0% | 20.2% | 26.8% | **8** | Fills the Texas cap (NRG + VST = 20). Beats TLN (#11) on Expected (+0.3pp) and AI-2027 (+0.9pp) |
| **Total** | | | | | **100** | **Checksum: 15 + 15 + 14 + 14 + 12 + 12 + 10 + 8 = 100.0** |

### A5.3 Exceptions between rank and weight

**Top-ranked stocks left out or capped:**

| Rank | Ticker | Expected CAGR | Treatment | Why |
|---:|---|---:|---|---|
| 1 | **MOD** | 18.7% | **0%, gated** | Only Codex's inputs exist (confidence 2). It ranks first on a post-spin perimeter that is five weeks old: continuing-business guidance is $3.1–3.2B sales and $470–500M adjusted EBITDA (Nov 3). H1 FCF was negative and data-center gross margin fell. Both models excluded it in Steps 1 and 2 on the same evidence, and nothing new has arrived. **Gate:** add 5% (VRT −3, NVT −2, the same thermal/electrical cluster) after the post-spin investor update, which Codex dated Nov 18 and which isn't independently confirmed, if it shows (a) a data-center gross margin that has stabilized, (b) positive H2 FCF guidance and (c) FY28 targets consistent with the $8.84 2030 base EPS. With the gate passed, the portfolio returns 15.2% expected, 24.2% AI-2027, 38.5% 100GW and −62.0% bust. |
| 4 | **CRWV** | 16.5% | 0% | Bust return −100%. A 40% probability of zero equity (claims exceed EV in the bear) means one position can be wiped out in the scenario the portfolio already fears most. Both models reject neoclouds on financing. |
| 3 | NRG | 17.1% | Capped at 12 | Net claims of ~$22.8B against ~$19.5B of equity; asset sale not yet closed; Texas is 51% of Q3 EBITDA |
| 6 | CLS | 14.8% | Capped at 10 | FY26 FCF $460M (~35% of net income); 2027 capex $1.5–2.0B; Aug equity raise; customer concentration |
| 2, 5 | NVDA, META | 17.8%, 15.0% | At the 15% cap | NVDA's new key-person probe (F13) is handled by deployment timing, not weight (E2) |

**Lower-ranked stocks included, and stocks just outside:**

- **VRT, NVT, MU and VST** (ranks 7–10) get capital only because higher-ranked names are capped or excluded. Inside the ~2pp band (VRT 13.8 → AVGO 11.6), MU leads on AI-2027 (26.8%) and 100GW (45.3%), so it gets 14 rather than the 8–12 either model gave it.
- **Just outside:**
    - **TLN (#11):** the named substitute if a Texas moratorium becomes law. It has PJM exposure instead of Texas. Same Expected CAGR (14.9%), bust −61.2%.
    - **MSFT (#12):** 12.3% at a 23.5× exit.
    - **TSM (#13), AVGO (#15), ASML (#17):** 11.0–11.8%, below the eight holdings even with AVGO's 21.4% AI-2027 return.
    - **RELX (#16), VRSK (#18):** low bust losses, but 10.7–11.1% expected at peer multiples.
- **VRSK in particular** was Codex's Step 2 addition at 15%. It ranks 18th once its 28× exit is held to its own 23.0× (peer median 21.4×). Codex's own sensitivity showed that a 20% lower VRSK multiple erases its advantage over AVGO.

### A5.4 Five-portfolio comparison (all on the same A1 assumptions and Nov 9 prices)

Bust = every holding at its bust-state value simultaneously. Delay = every holding at its plateau-state value. The "Codex multiples" column re-runs every portfolio with each disputed multiple set to Codex's value.

| Portfolio | Names | Expected CAGR | Expected total return | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Bust-case return | 2–3 yr delay return | Expected CAGR with Codex multiples | Top-3 weight | HHI |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| V9.1 baseline | 24 | 7.8% | 36% | 15.5% | 27.2% | -67.3% | -41.4% | 9.0% | 28% | 0.057 |
| Claude blind (V10) | 16 | 11.4% | 56% | 19.0% | 30.6% | -66.4% | -29.8% | 13.3% | 36% | 0.085 |
| Codex blind (CX8) | 8 | 14.0% | 72% | 22.4% | 35.2% | -69.1% | -29.2% | 17.1% | 45% | 0.129 |
| Claude post-critique | 11 | 14.2% | 73% | 23.0% | 36.1% | -66.8% | -26.7% | 16.9% | 41% | 0.110 |
| Codex post-critique | 8 | 14.4% | 74% | 22.1% | 34.0% | -63.7% | -24.9% | 17.9% | 45% | 0.129 |
| Arch1 diversified (16) | 16 | 13.6% | 70% | 20.9% | 32.8% | -59.2% | -24.6% | 16.5% | 26% | 0.068 |
| Arch2 concentrated (7) | 7 | 15.2% | 79% | 23.5% | 37.0% | -62.2% | -23.9% | 18.6% | 45% | 0.145 |
| **V10.0 final (proposed)** | 8 | **14.9%** | 78% | 23.4% | 36.9% | -61.8% | -23.9% | 18.2% | 44% | 0.129 |
| V10.0 if MOD gate passes | 9 | 15.2% | 80% | 24.2% | 38.5% | -62.0% | -23.3% | 18.3% | 44% | 0.120 |
| V10.0 if Texas moratorium law (TLN for VST) | 8 | 14.9% | 78% | 23.4% | 36.9% | -61.2% | -24.3% | 17.9% | 44% | 0.129 |
| V10.0 with NVDA 12 (probe) | 8 | 14.8% | 77% | 23.3% | 36.8% | -61.9% | -24.0% | 17.9% | 45% | 0.130 |

**How to read the table:**

- **V10.0 beats both post-critique portfolios** on Expected CAGR (+0.5 to +0.7pp), AI-2027 (+0.4 to +1.3pp), 100GW (+0.8 to +2.9pp), bust (2–5pp better) and delay (1–3pp better).
- **It also wins on Codex's multiples:** 18.2% against Codex's own revised 17.9% and Claude's revised 16.9%.
- **The 7-name concentrated architecture** returns 0.3pp more expected. It needs CLS and NRG at 15%, which the confidence caps reject.
- **The 16-name diversified architecture** gives up 1.3pp of expected return to cut the bust loss by 2.6pp. That's poor value under the stated goal.

### A5.5 Sensitivity

| Portfolio | Primary (A1 bear = ½ bust + ½ plateau) | Codex-style bear (bear = bust only) | +10% common zero-recovery regime | +20% common zero-recovery regime |
|---|---:|---:|---:|---:|
| Claude post-critique | 14.2% | 13.3% | 11.3% | 8.2% |
| Codex post-critique | 14.4% | 13.5% | 11.5% | 8.4% |
| V10.0 final (proposed) | 14.9% | 14.1% | 12.0% | 8.9% |

The bear construction (A1.2) moves every portfolio by under 1pp and leaves the order unchanged. The illustrative zero-recovery overlays (Codex's) cut every portfolio by about the same amount, so they don't change the choice.

---

## A6. Escalated Items and Self-Sided Audit

### A6.1 Escalate to owner (5)

| ID | Question for owner | Option A (best case) | Option B (best case) | Provisional call in the final | Weight at stake |
|---|---|---|---|---|---|
| E1 | **MOD:** add the top-ranked stock now, or after its post-spin update? | **Now at 5%:** captures 18.7% expected (portfolio +0.3pp) before the market re-rates a 10×-forward thermal pure play | **After the update:** avoids underwriting a five-week-old perimeter with negative H1 FCF; costs nothing if the update disappoints | **B: gate (0% now; +5% from VRT/NVT if it passes)** | 5 |
| E2 | **NVDA during the CEO probe:** 15% or 12%? | **15%:** the board review is about one person's judgment, not the business. Nov 17 earnings and a ~$108B quarterly guide are the fundamentals. 12% costs 0.1pp of expected return | **12% until the review concludes:** limits key-person and China-relations tail risk. Huang is "not replaceable" in the market's eyes | **A (15%), deployed in tranches only after Nov 17 earnings and with no adverse finding** | 3 |
| E3 | **Texas power:** keep VST or switch to TLN now? | **Keep VST:** +0.3pp expected, +0.9pp AI-2027; the moratorium is a pledge, not a law, and it targets new approvals, not existing plants | **TLN now:** removes Texas from half the power sleeve (PJM nuclear/gas), bust −61.2% vs −61.8%, at the same 14.9% portfolio expected return | **A, with an automatic switch if a moratorium bill clears a Texas chamber** | 8 |
| E4 | **META at 15%:** is an AI *buyer* inside the infrastructure mandate, given Continuity already owns it through FSKAX? | **Include:** rank #5, mildest bust of the top names (−34%), and it diversifies the hardware cluster. Event Horizon has held AI software (PLTR, CRWD) before | **Exclude:** keep Event Horizon a pure bottleneck-supplier fund. The 15% goes to TLN 8 / TSM 7, with portfolio Expected CAGR 0.4pp lower (14.5%) and a bust 4pp worse (−65.8%) | **A (15%)** | 15 |
| E5 | **Concentration appetite:** 8 names (top-3 44%) or 16? | **8 names (V10.0):** 14.9% expected, bust −61.8% | **16 names (diversified):** 13.6%, bust −59.2%, top-3 26% | **A** | Whole portfolio |

### A6.2 Self-sided audit

**Inputs (53 disputed inputs in A4.3):**

| Went to | Decided on evidence | Decided by the tie rule (lower value) | Concession / fact | Total |
|---|---:|---:|---:|---:|
| Claude's original view | 13 | 16 | 0 | **29** |
| Codex's original view | 8 | 7 | 2 | **17** |
| Split (one input each way) | 0 | 4 | 0 | 4 |
| Neither (A1 rule) | 3 | 0 | 0 | 3 |

**Why the count leans to Claude.**

- **The tie rule.** Codex's bull-case EPS and exit multiples ran systematically higher than mine, so the "tie → lower value" rule hands most ties to my side mechanically (16 of 23 ties). The rule favors conservatism, not me. It would have gone the other way wherever my inputs were higher: MU, ASML base, VRT base, COHR base, TSM bull.
- **The test that matters is whether the picks depend on those calls.** They don't. With **every disputed multiple set to Codex's value**, the same eight names win and V10.0 returns 18.2%, the highest of any compared portfolio (A5.4).

**Every input decided on evidence for Claude's view, with the deciding evidence:**

1. **NVDA base EPS $19:** Codex's $16.64 implies flat 2027–30 earnings against FY28 consensus of $15.92, while A1 base capex rises ~2.8×.
2. **NVDA 18×:** outside-band test. Peers ex-NVDA ~18.7×, own 11.2×.
3. **CLS 14×:** EMS peers ~10×, FN 15.2×.
4. **TSM base EPS $33:** CY27 consensus $23.39, revised up 10% in 90 days; 2026 EPS +64%.
5. **TSM 19×:** own 16.6×, peers ~18.7×.
6. **NRG Texas bear:** F3, which Codex didn't address.
7. **VST Texas bear:** F3; VST fell 14% on election day.
8. **COHR 18×:** optics peers ~15×.
9. **SNPS owner EPS:** stock comp is 31% of adjusted EPS.
10. **META 20×:** own 18.0×, peers 22.5×.
11. **AI-2027 probability 35%:** the authors' own odds and medians.
12. **Bear construction:** under 1pp effect, shown both ways.
13. **Texas cap 20%:** F3.

**Weights.** Compared with the two post-critique portfolios:

| Ticker | Claude post | Codex post | V10.0 | Went to |
|---|---:|---:|---:|---|
| NVDA | 15 | 15 | 15 | Both (agreed) |
| META | 0 | 0 | **15** | Neither (Codex had flagged it as "the preferred replacement" in Step 1) |
| VRT | 14 | 15 | 14 | Claude |
| MU | 12 | 8 | **14** | Neither (A5 tie-break) |
| NRG | 11 | 12 | 12 | Codex |
| NVT | 11 | 12 | 12 | Codex |
| CLS | 7 | 12 | 10 | Neither |
| VST | 9 | 11 | 8 | Neither (the Texas cap binds against NRG 12) |
| AVGO / TSM / ASML / BNTX | 11 / 5 / 4 / 1 | 0 | 0 | **Codex** |
| VRSK | 0 | 15 | 0 | **Claude** (A1 multiple policy) |

Relative to Claude's post-critique portfolio, 22 points of capital were cut. **21 of them moved to Codex's view:** AVGO, TSM, ASML and BNTX went to 0. The one exception was VST −1. The largest addition, META, came from Codex's Step 1 candidate list. Of the two 15-point calls that went against a model, VRSK went against Codex and META against both Step 2 portfolios. **V10.0 overlaps 79% with Codex's post-critique portfolio and 78% with Claude's** (sum of the smaller weight per name).

---

**Companion files:** `inputs/research/claude_synthesis/`. See its `README.md` for the run commands.

- `step3_model.py`: the synthesis model.
- `step3_tables.py` and `extra_tables.py`: table generators.
- `fetch_step3.py`: the Nov 9 data snapshot.
- `data/`: snapshot, model outputs, portfolios and disputed inputs.
- `tables/`: the generated tables used in this file.

Re-running the pipeline reproduces every table byte for byte.

---

## Addendum: Step 4 and Step 5 decisions (added November 10, 2026)

This file is the Step 3 ranking and is not rewritten. **The adopted portfolio is V10.1**, decided in Step 5 on the same model with the input changes below. Full evidence is in `inputs/Step 5 Decision Log 2026-11-08.md`. The adopted final is `Event Horizon Fund Analysis 2026-11-08.md`.

### Merged items and decisions

| ID (sources) | Item | Decision |
|---|---|---|
| D1 (C1) | AVGO base 2030 owner EPS $23.5 → $27.0 (management's FY28 target > $30) | **Accepted** (input correction). AVGO 11.6% → 13.5%; bench #1 |
| D2 (Codex flag) | Double stock-comp charge on VRT and NVT anchors | **Accepted** (input correction). VRT 13.8% → 13.9%; NVT 13.7% → 13.8% |
| D3 (Codex O1) | WCC 8% for VST | **Rejected.** Codex's bridge needs growth and margins above Wesco's own guidance; 7.0% on consistent inputs |
| D4 (Codex O2, Claude C2) | Add STRL | **Accepted at Codex's inputs, 6%, funded by exiting VST**; VRT and MU to the 15% cap. +0.41pp portfolio expected |
| D5 (C3) | Bench for freed capital | **Accepted:** AVGO; VST or TLN; AEIS; TSM |
| D6 (C4, E3) | Texas trigger | **Re-underwrite NRG and STRL within 5 sessions** of a bill clearing a chamber; if confirmed NRG 12 → 8, STRL 6 → 3, TLN +7 |
| D7 (E1) | MOD | **Gate kept**; Nov 18 investor day confirmed; gate restated as FY28 targets bridging to 2030 owner EPS $8.84 |
| D8 (E2) | NVDA during the board review | **15%; no purchase before the Nov 17 report.** Adverse review: NVDA 15 → 8, AVGO +7 |
| D9 (E4) | META 15% | **Kept** |
| D10 (E5) | Holdings count | **8** |
| D11–D13 (Codex flags) | Multiple-policy claim; "upper bound" wording; HBM scorecard | **Accepted** (wording and record corrections) |
| D14 | Other Step 4 names | **Watchlist:** SANM, ONTO. The rest rejected |

### Changed and new rows (60-stock ranking, Nov 9 prices)

STRL and WCC entered the pool in Step 5, fully underwritten on the same model. AVGO, VRT and NVT carry the corrected inputs. VST is shown because it left the portfolio.

| Rank | Ticker | Bottleneck | Price (Nov 9) | Status | Expected CAGR | AI-2027 | 100GW | Bust | Delay | Depth | V9.1 → V10.1 |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | **STRL** | Data-center site development + electrical installation | $290.67 | Attractive (multiple-sensitive) | 19.5% | 28.7% | 43.7% | -65% | -15% | Full A1 | 0 → **6** (Add) |
| 8 | **VRT** | Rack power + liquid cooling | $200.47 | Fair | 13.9% | 22.0% | 34.9% | -72% | -29% | Full A1 | 6 → **15** (Increase) |
| 9 | **NVT** | Electrical distribution + liquid cooling | $114.44 | Attractive | 13.8% | 21.4% | 34.0% | -58% | -21% | Full A1 | 0 → **12** (Add) |
| 10 | AVGO | Custom silicon + networking | $319.48 | Fair | 13.5% | 21.9% | 34.6% | -73% | -44% | Full A1 | 3 → **0** (Remove) |
| 12 | VST | Merchant power (TX/PJM) | $133.92 | Fair | 13.0% | 20.2% | 26.8% | -67% | -29% | Full A1 | 6 → **0** (Remove) |
| 29 | WCC | Electrical / datacom distribution | $316.47 | Fair | 7.0% | 10.5% | 16.9% | -54% | -26% | Full A1 | 0 → **0** (Not added) |

### Weights: V10.0 (A5.2) → V10.1 (adopted)

| Ticker | V10.0 (Step 3) | V10.1 (adopted) | Change |
|---|---:|---:|---|
| NVDA | 15 | 15 | — |
| META | 15 | 15 | — |
| VRT | 14 | **15** | +1 (VST's exit) |
| MU | 14 | **15** | +1 (VST's exit) |
| NRG | 12 | 12 | — |
| NVT | 12 | 12 | — |
| CLS | 10 | 10 | — |
| VST | 8 | **0** | −8 (D4) |
| STRL | 0 | **6** | +6 (D4) |
| **Total** | 100 | **100** | |

Same model, Nov 9 prices: V10.0 14.9% expected / 23.4% AI-2027 / 36.9% 100GW / −61.6% bust; **V10.1 15.4% / 24.0% / 38.1% / −61.5%**.

**Step 5 companion files** (same folder): `step5_model.py` (the Step 3 model plus the decided input changes), `step5_tables.py`, `data/step5_*.json`, `data/ports5.json` and `tables5/`.
