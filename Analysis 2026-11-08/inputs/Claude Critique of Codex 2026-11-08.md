# Event Horizon Fund — Step 2 Cross-Critique: Claude Critique of Codex

**Step 2 of 4** (`PROMPT_2_CROSS_CRITIQUE.md`). **Author:** Claude (Opus 5.5). **Written:** November 9, 2026, after the close.

**Inputs read:**

- `Analysis 2026-11-08/inputs/Claude Deep Dive 2026-11-08.md` (mine, Rev 2)
- `Analysis 2026-11-08/inputs/Codex Deep Dive 2026-11-08.md` (Codex, Nov 9 research revision), read in full
- `PROMPT_1_DEEP_DIVE.md`, for the valuation framework and the two named-scenario definitions

Codex's Step 2 critique did not exist when this was written and was not read.

**Market data.** Both deep dives priced every stock at the **November 6, 2026 close**, and the prices match to the cent. So every gap in §2–§4 is analytical, not a timing artifact. My re-underwriting is shown at the Nov 6 close, so it compares directly with both reports. It is also shown at the **November 9 close**, which is used for the revised allocation in §6. Nov 9 closes come from Yahoo's chart endpoint, with the last bar confirmed at 21:00 UTC Nov 9. Several contested names moved 8–17% on Nov 9:

- COHR +16.8%
- NRG +10.3%, on Q3 results
- CEG +10.5%, on Q3 results
- VRT +9.6%
- AVGO +8.8%
- CLS +7.9%
- NVDA −4.3%

**Method.** Everything uses one script (`step2_model.py`). It reproduces Codex's published numbers exactly from Codex's §4.4 inputs: 22.8% portfolio CAGR, −56.6% all-bear, and every per-stock CAGR to within 0.1pp. It also reproduces mine exactly: 14.7% and −26.6%. That confirms I read Codex's inputs correctly before criticizing them.

Neither deep dive reported named-scenario returns, which postdate both reports, so I computed them for every stock on both sides using one rule:

- **AI-2027 Scenario:** each stock's bull-case 2030 earnings metric at its base exit multiple, plus bull-case dividends and cash. MU, a cyclical, uses its bull (peak) multiple.
- **100GW 2030 Scenario:** the same, with the bull metric scaled by a bottleneck-capture factor U from Situational Awareness's path:
    - U = 1.3 for foundry, EUV, HBM, power generation and electrical/thermal;
    - U = 1.2 for chips, optics and integrators;
    - U = 1.1 for EDA and rare earths;
    - U = 1.0 for defense and bio.

I put about **35%** on an AI-2027-like path through 2030, which resembles base-to-bull for compute-chain names. That's the most likely single path, but not a majority. I put about **10%** on the 100GW 2030 path, which resembles bull-plus: it needs roughly $8T a year of AI investment by 2030, against about $1T in 2026. Neither named scenario is folded into the probability-weighted Expected CAGR.

---

## 1. Verdict

- **Codex picked better stocks than I did.** On one consistent valuation framework (§2, "re-underwritten"), Codex's 8-stock portfolio returns about **16.3%** a year at Nov 6 prices, against **14.0%** for my 16-stock V10. At Nov 9 prices the figures are 14.5% and 12.6%. Codex also leads on both named scenarios. Its edge comes from **NRG and NVT**, which I never underwrote, and from concentrating instead of holding a long tail of ~12%-return names.
- **The best Codex pick I missed is NRG.** It trades at about 6x 2027 free cash flow before growth, against about 9x for VST. Even on my more conservative inputs it ranks #2–3 by expected return. **NVT beats my ETN** on the same electrical bottleneck: 15.8% vs 11.6% re-underwritten, at 16x vs 22x 2027 EPS.
- **My own bear cases were too mild, and Codex was right to be harsher.** My TSM bear assumed 2030 EPS above the 2026 run rate. My MU, ASML and VRT bears never revisited pre-boom earnings. My 30% bull weights on TSM and ASML had no stock-specific support. Corrected, my V10 bust case is **about −42%, not −26.6%**. My report understated portfolio risk.
- **Codex's weakest point is its 22.8% headline.** It is inflated by terminal P/E multiples above both peer and company history, on exactly the stocks it selected:
    - NVDA 25x, against a mega-cap peer median of ~18x forward and NVDA's own 11.2x today;
    - AVGO 24x, COHR 24x and CLS 17x.

    Those stocks are top-ranked partly *because* their assumed re-rating is largest. That is a winner's-curse selection effect. Keeping Codex's earnings bases where they are better supported but using peer-anchored multiples cuts the 8-stock portfolio from **22.8% to about 16%**.

- **Codex's TSM and ASML bases contradict near-term evidence.**
    - TSM's base 2030 EPS of $26.8 implies 4.7% a year of growth after a CY27 consensus of $23.4.
    - ASML's $70B / 34%-margin base sits barely above its Q4-2026 guided run rate (€14.2–15.2B a quarter, about €59B annualized) and well below its Q3 operating margin of 44.4%.

    Codex's 0% upstream weight rests partly on these inputs.

- **Codex holds 0% memory against its own evidence.** Its workbook audit finds **HBM is the binding constraint in every year 2024–2030**. It cites Micron's 26 long-term agreements covering more than 35% of revenue through 2030, with price floors. MU ranks **#2 by Expected CAGR and #1 by AI-2027 Scenario CAGR** (31.5%) after my re-underwrite.
- **Codex misses the political and financing facts that bear directly on its picks:**
    - the Texas governor-elect's moratorium pledge on new data centers, plus the September TCEQ permit pause;
    - the Nov 3 local data-center votes;
    - ERCOT and PJM dynamics. NRG's Texas segment was 51% of its Q3 EBITDA, and Codex holds 23% Texas-heavy merchant power;
    - AVGO's XPV residual-value guarantee (about $29B maximum exposure on the first deal, with Anthropic as tenant) and the rate backdrop.

- **COHR has moved through its value.** After a +16.8% move on Nov 9, its expected CAGR falls to 9.1% on my inputs and 14.7% on Codex's. Both are below Codex's own 18% "model-implied return ceiling", so even Codex's rules say not to chase it.
- **Net change:** my allocation moves substantially toward Codex's. It goes from **16 names to 11**, and my overlap with Codex's portfolio rises from **42% to 78%**:
    - I add NRG, NVT and CLS;
    - I raise NVDA, VRT, AVGO and MU;
    - I cut TSM and ASML to small upstream positions;
    - I exit SNPS, CEG, COHR, ETN, CRDO, PWR, KTOS and MP.

    At Nov 9 prices this lifts expected CAGR from **12.6% to 14.7%**, AI-2027 Scenario CAGR from **22.3% to 25.2%** and 100GW 2030 Scenario CAGR from **28.9% to 32.3%**. The bust case worsens slightly, from −44.7% to −46.1%, on the same corrected bear inputs.

---

## 2. Head-to-Head: Every Stock Where the Portfolios Differ

All 19 tickers in either portfolio differ by at least 1pp, so all are covered. "Re-underwritten" uses one framework for both sides:

- **Bear bucket:** a 50/50 mix of a bust (2030 earnings back to roughly 2025 levels) and my original mild bear.
- **Probabilities:** 25/50/25 unless there is stock-specific evidence for a fatter bear.
- **Exit multiples:** anchored to peer and own-history forward P/E medians.
- **Earnings bases:** whichever side's base is better supported. The source and reason are in the last two columns.

All CAGRs are in % per year. The re-underwritten figure is at Nov 6, with Nov 9 in brackets.

| Ticker | Mine % | Codex % | Price + date | Expected CAGR (mine / Codex / re-underwritten) | AI-2027 Scenario CAGR (mine / Codex) | 100GW 2030 Scenario CAGR (mine / Codex) | Input driving the gap | Better call | Why |
|---|---:|---:|---|---|---|---|---|---|---|
| NVDA | 13 | 15 | $186.64 (Nov 6); $178.67 (Nov 9) | 16.7 / 24.5 / **17.9 [19.2]** | 27.1 / 40.6 | 32.8 / 46.9 | Base exit multiple 18x vs 25x. Codex's base EPS is *lower* ($16.6 vs $19) | **Codex on size; mine on multiple** | 25x is above the mega-cap peer median (MSFT 22.5, GOOGL 19.0, META 18.0, TSM 16.6, AVGO 16.4 forward) and 2.2x NVDA's own 11.2x forward. My $19 base is better supported: the FY28 consensus is $15.92 and the AI-2040 capex path reaches $2.4T in 2028. Even at 18x, NVDA is the #1 stock in either portfolio, so the 15% cap should bind |
| AVGO | 6 | 15 | $293.69; $319.48 | 14.5 / 21.4 / **16.0 [13.7]** | 26.2 / 36.1 | 31.8 / 42.1 | Multiple 20x vs 24x; bear probability 30% vs 25%; Codex's higher EPS path | **Split: Codex's EPS path, my multiple and bear** | I adopt Codex's base ($25.5) and bull ($43.3) EPS, which better match AVGO's FY28 AI-revenue target. I keep 20x (AVGO's 16.4x forward; own history in the high teens). I keep a 30% bear and a −$6/sh bear adjustment for the XPV residual-value guarantee (about $29B maximum exposure, Anthropic tenant). Codex never mentions it |
| VRT | 9 | 15 | $182.86; $200.47 | 17.6 / 23.7 / **16.9 [14.4]** | 26.4 / 41.3 | 34.7 / 50.5 | Bull revenue $48B vs about $33B implied; multiple 26x vs 23x | **Codex on size; mine on inputs** | The base EPS is the same on both sides ($15.5 vs $15.8). Codex's bull needs revenue to rise 3.3x from 2026's ~$14.7B, with 44% a year EPS growth from the 2027 consensus. I keep my 29% a year. VRT is still #4 by re-underwritten return |
| VST | 9 | 11 | $124.80; $133.92 | 15.1 / 20.3 / **14.9 [13.0]** | 23.9 / 35.1 | 31.9 / 44.8 | Codex's bull EBITDA of $15B vs 2027 guidance of $7.7–8.5B; my 30% bear | **Mine** | Codex's bull nearly doubles 2027-guided EBITDA by 2030. My 30% bear reflects ERCOT and Texas politics: VST fell 14% on election day and the governor-elect pledged a moratorium. Codex does not discuss either |
| COHR | 5 | 8 | $192.81; **$225.19** | 13.9 / 19.0 / **13.2 [9.1]** | 24.9 / 37.4 | 30.6 / 43.5 | Multiple 18x vs 24x (base EPS ~$19 vs $18.2, the same) | **Neither, at Nov 9 prices** | The optics peers LITE (13.5x FY28) and FN (18.8x) support 18x. After a +16.8% move on Nov 9, COHR returns 9.1% on my inputs and 14.7% on Codex's, below Codex's own 18% chase ceiling. Exit for now; re-enter below ~$190 |
| TSM | 14 | 0 | $375.44; $388.62 | 15.1 / 13.5 / **12.8 [11.9]** | 20.4 / 24.3 | 28.2 / 32.3 | Base EPS $33 vs $26.8; bear EPS $21 vs $8.45; bull probability 30% vs 25% | **Split: my base, Codex's harsher bear and 25% bull** | Codex's base implies 4.7% a year growth after the CY27 consensus of $23.4, which contradicts ~47% growth in 2026, the capacity build and the AI-2040 path for AI's share of EUV. My bear ($21, above 2026 EPS) was too mild, and my 30% bull had no support. The corrected TSM ranks #9 |
| MU | 9 | 0 | $690.00; $733.15 | 15.6 / 13.0 / **16.7 [15.1]** | 29.7 / 36.5 | 38.2 / 44.6 | Base EPS $130 vs $80 (normalization); bear probability 25% vs 30%; Codex's excess-cash reserve | **Mine on the base; Codex on cash and bear depth** | The LTAs (>35% of revenue through 2030, with floors, as Codex cites) and Codex's own HBM-binding audit support a shallower normalization than Codex's. I adopt Codex's $40/150/250 excess-cash reserve and a deeper bust bear ($25 EPS). MU is #2 by Expected and #1 by AI-2027 Scenario CAGR |
| ASML | 8 | 0 | $1,424.75; $1,513.25 | 14.6 / 8.6 / **12.6 [11.0]** | 20.3 / 20.5 | 28.0 / 28.3 | Base EPS $88 vs $63.5; bear; bull probability 30% vs 25% | **Split: my base, Codex's bear depth and 25% bull** | Q3 2026: gross margin 57.5%, operating margin 44.4%, net income about €4.5B ex-Mistral gain. Q4 guidance annualizes to about €59B. Codex's base ($70B, 34% net margin) is close to today's run rate, so my base holds. My bear ($50 EPS) and 30% bull were generous. The corrected ASML (11.0%) loses to the top eight; a small position is kept only as residual (§6) |
| SNPS | 6 | 0 | $450.46; $466.97 | 12.7 / 12.9 / **12.2 [11.2]** | 18.9 / 25.2 | 21.7 / 28.1 | Codex's harsher bear ($8.8 EPS); otherwise the same | **Codex** | Both models put SNPS at about 12.8%. It fails capital competition. Its lower bust loss (−35%) is not enough to justify 6% under the stated goal |
| CEG | 6 | 0 | $249.95; **$276.09** | 11.4 / 12.7 / **11.0 [8.4]** | 17.4 / 25.7 | 25.0 / 33.7 | Only small input gaps; the Nov 9 +10.5% move is decisive | **Codex** | Q3 beat and raise (2026 guidance $12.50–12.80), but at $276 the expected CAGR is 8.4%. NRG offers the same power exposure at about 6x FCF |
| ETN | 5 | 0 | $341.72; $359.30 | 11.9 / 14.8 / **11.6 [10.3]** | 17.4 / 27.1 | 24.9 / 35.2 | Similar inputs; NVT dominates | **Codex** | NVT beats ETN by 4pp on the same electrical-distribution bottleneck (§3, B2) |
| CRDO | 3 | 0 | $120.51; $132.89 | 18.0 / 10.8 / **11.9 [9.4]** | 31.4 / 29.3 | 37.3 / 35.1 | Adjusted EPS vs SBC-burdened owner EPS ($10.5 vs $6.4 base) | **Codex** | I capitalized adjusted EPS. Codex charges stock compensation, which is the right owner-economics basis for a high-SBC small cap. Converting my inputs (×0.81) drops CRDO to 11.9%, with a −70% bear |
| PWR | 2 | 0 | $540.90; $591.48 | 8.3 / 10.9 / **7.5 [5.2]** | 13.9 / 22.8 | 21.3 / 30.8 | Both low | **Codex** | Neither model clears 11%; after a +9% move it is 5.2% |
| KTOS | 2 | 0 | $35.10; $37.69 | 11.9 / −0.3 / **2.6 [0.9]** | 23.4 / 18.1 | 23.4 / 18.1 | Adjusted vs owner EPS; FCF burn | **Codex** | FY26 FCF use of $110–120M despite growth (Nov 5). My adjusted-EPS basis overstated owner value. As a "hedge" it has a −78% bear |
| MP | 2 | 0 | $35.41; $37.75 | 7.2 / 8.5 / **7.2 [5.6]** | 21.0 / 30.5 | 23.8 / 33.5 | Similar | **Codex** | Both below 9%. It hedges a China rare-earth escalation, not an AI bust. China's suspension of its Oct-2025 notices lapses Nov 10, which is a binary event, not a reason to hold through it at 5.6% expected |
| BNTX | 1 | 0 | $87.51; $87.51 | 9.2 / n/a / **9.2 [9.2]** | 7.9 / n/a | 7.9 / n/a | Codex screened it but never underwrote it | **Mine (1%)** | Net cash is about 85% of market value (−26% bear). It is the only holding whose value *rises* in an AI bust in my model. At 1% it costs <0.1pp of expected return |
| CLS | 0 | 12 | $206.68; $222.92 | 13.9 / 23.5 / **16.2 [14.2]** | 23.1 / 44.0 | 28.6 / 50.4 | Base EPS $27 vs $30.2; multiple 14x vs 17x; bull EPS $35 vs $55 | **Split: Codex on base and inclusion, mine on multiple and size** | The 2027 guidance (revenue $40B, EPS $21.50) plus "meaningfully higher" 2028 demand supports Codex's ~$30 base. But 2026 FCF was cut to $460M (~33% of net income), 2027 capex is $1.5–2.0B and $3.45B of equity was raised in August. That supports an EMS-peer 14x and a 30% bear, not 17x. Add at 7% |
| NVT | 0 | 12 | $106.22; $114.44 | n/a / 23.7 / **15.8 [13.8]** | n/a / 39.1 | n/a / 48.0 | Never underwritten by me; multiple 19x vs 22x; bull $18.75 vs $14 EPS | **Codex on inclusion** | 2026 adjusted EPS guidance $5.36–5.39 (Oct 30); 2027 consensus $7.00 (16.4x). Q4 organic growth slows to 26–29%. Even at my 19x it beats ETN. Add at 11% |
| NRG | 0 | 12 | $88.29; **$97.40** | n/a / 24.5 / **17.5 [14.8]** | n/a / 37.9 | n/a / 48.0 | Never underwritten by me; Codex's anchor was stale (Aug 4); its $7B 2030 EBITDA vs the new 2027 guidance of $5.75B | **Codex on inclusion; mine on inputs** | Nov 9: 2027 guidance of EBITDA ~$5.75B, FCF before growth $3.15B and EPS $9.05; a $4B asset sale; 2026 EBITDA slightly below midpoint (weak ERCOT prices). About 15.4% FCF yield at $97. I value it on FCF per share with buybacks (base $19 × 9x) and a 30% bear for Texas exposure. Add at 11% |

### Sleeve and shared-driver cluster comparison

| Cluster (shared economic driver) | Claude V10 % | Codex 8 % | Claude revised % (§6) | Comment |
|---|---:|---:|---:|---|
| C1 AI silicon and interconnect (NVDA, AVGO, MU, TSM, COHR, CRDO, CLS) | 50 | 50 | 50 | Same total; Codex's mix is higher-return per my re-underwrite, except it leaves out MU |
| C2 Fab tools and design (ASML, SNPS) | 14 | 0 | 4 | Codex is closer to right at current prices |
| C3 DC physical and electrical (VRT, NVT, ETN, PWR) | 16 | 27 | 25 | NVT and VRT are the best value in this cluster |
| C4 Power generation (VST, CEG, NRG) | 15 | 23 | 20 | The Texas/ERCOT driver is shared by NRG and VST, so I cap the cluster at 20 |
| C5 Software | 0 | 0 | 0 | Both reports agree |
| C6 AI-independent hedges (KTOS, MP, BNTX) | 5 | 0 | 1 | Codex is mostly right: KTOS and MP were not hedges at their expected returns |
| **Names / top-3 weight** | **16 / 36%** | **8 / 45%** | **11 / 41%** | — |

---

## 3. Their Picks vs Mine (Same Bottleneck)

Expected CAGRs here are re-underwritten at the **Nov 9** close. They are the basis for §6.

| # | Bottleneck | My pick | Codex pick | Expected CAGR each | AI-2027 Scenario CAGR each | 100GW 2030 Scenario CAGR each | Valuation status each | Better stock | Why |
|---|---|---|---|---|---|---|---|---|---|
| B1 | Merchant power generation | CEG (6%) | NRG (12%) | CEG 8.4 / NRG 14.8 | 14.7 / 23.6 | 22.1 / 31.4 | CEG Fair-to-Expensive after +10.5%; NRG Attractive | **NRG** | About 6x 2027 FCF before growth vs about 21x CEG 2027 EPS. CEG's nuclear premium is real but already priced in. NRG's Texas exposure is why I size it at 11, not 15 |
| B2 | Electrical distribution and protection | ETN (5%) | NVT (12%) | ETN 10.3 / NVT 13.8 | 16.0 / 23.0 | 23.4 / 31.0 | ETN Fair; NVT Attractive | **NVT** | 16.4x vs 21.8x 2027 EPS with faster organic growth (38–39% in 2026 vs ETN's high-teens data-center growth). ETN is the higher-quality fallback if Maverick integration fails |
| B3 | Optical and scale-up interconnect | COHR (5%) + CRDO (3%) | COHR (8%) | COHR 9.1 / CRDO 9.4 | 20.4 / 22.1 | 25.8 / 27.6 | Both Fair at Nov 9 | **Neither at Nov 9 prices** | Codex was right that COHR beats CRDO after stock comp. But COHR's Nov 9 move takes it below both reports' hurdles. Optics exposure stays through NVDA and AVGO networking |
| B4 | Rack and system integration | none (VRT only) | CLS (12%) | CLS 14.2 | 24.9 | 30.5 | CLS Attractive (10x 2027 guidance) | **CLS, at a smaller size** | I wrongly excluded CLS on an "integrator" label and the C1 cap. Its guidance supports a ~$30 base. Cash conversion and dilution justify 7%, not 12% |
| B5 | Upstream foundry, lithography and EDA | TSM 14 + ASML 8 + SNPS 6 = 28% | none (0%) | TSM 11.9 / ASML 11.0 / SNPS 11.2 | 19.5 / 18.6 / 17.9 | 27.2 / 26.2 / 20.7 | Fair / Fair / Fair | **Codex is closer** | With corrected bears and 25% bulls, all three rank #9–11. I keep only TSM 5 and ASML 4 as residual capital after the caps bind (§6). They are the cheapest way to own the 100GW path's binding inputs (4x TSMC leading-edge capacity; the EUV wall). SNPS goes to 0 |
| B6 | HBM and memory | MU (9%) | none (0%) | MU 15.1 | **31.5 (highest)** | 39.3 | Deep Discount (cyclical): 3.5x FY28 consensus | **MU** | Codex's own audit: HBM is the minimum (binding) input in every year 2024–2030. LTAs with price floors cover more than 35% of revenue through 2030. Codex's 0% contradicts its own evidence. Raise to 12 |
| B7 | AI-independent hedges | KTOS 2 + MP 2 + BNTX 1 | none | KTOS 0.9 / MP 5.6 / BNTX 9.2 | 11.3 / 19.1 / 7.9 | 11.3 / 21.9 / 7.9 | Speculative | **Mostly Codex** | KTOS and MP have high expected-loss tails and low expected returns. BNTX alone has a cash floor and a positive bust payoff, so keep 1% |
| B8 | Grid construction and labor | PWR (2%) | none | PWR 5.2 | 11.5 | 18.7 | Expensive after a +9% move | **Codex** | No version of PWR clears the hurdle |
| B9 | Custom silicon | AVGO (6%) | AVGO (15%) | 13.7 | 27.6 | 33.3 | Attractive | **Raise toward Codex: 11%** | Codex's EPS path is better supported (FY28 AI target). XPV guarantees and the 30% bear keep it below the cap |
| B10 | Accelerators | NVDA (13%) | NVDA (15%) | 19.2 | 28.5 | 34.3 | Attractive (11.2x forward) | **Codex: 15%** | The #1 stock on every method. My C1 cap, not valuation, kept it at 13 |

---

## 4. Candidates Only One of Us Found

### 4a. Names Codex underwrote that I never considered, with my verdict

For names I never modeled, the CAGRs are quick screens using my peer-anchored multiples on Codex's revenue paths at Nov 6 prices. They are indicative only.

| Ticker | Codex CAGR | My quick-screen CAGR | Verdict | Reason |
|---|---:|---:|---|---|
| NRG | 24.5 | 17.5 (14.8 at Nov 9) | **Add (11%)** | See B1. This is the most important name I missed |
| NVT | 23.7 | 15.8 (13.8 at Nov 9) | **Add, replacing ETN (11%)** | See B2 |
| MOD (post-spin) | 19.7 | ~19 | **Watchlist** | Cheap (about 10x FY28 EPS). But the continuing-business perimeter is new, H1 FCF was negative and data-center gross margin fell. Revisit after the Nov 18 investor update with a clean post-spin cash bridge |
| META | 18.6 | ~11 | **Reject** | My 20x multiple vs Codex's 23x explains most of the gap. It is already about 2–3% of Continuity's FSKAX sleeve, and owning it adds no new bottleneck |
| MSFT | 17.6 | ~10 | **Reject** | 22.5x forward already prices agent monetization. Continuity overlap |
| TLN | 17.2 | 11.3 (my original model) | **Reject** | NRG gives the same power-rent exposure at a lower FCF multiple |
| LRCX | 16.1 | 6.6 (my original model) | **Reject** | My 19x base multiple vs Codex's 25x explains the gap. I agree it is the best WFE alternative if WFE is reopened |
| RELX, VRSK, AXON, MSI, GEN | 8–14 | not modeled | **Reject** | These are not AI-infrastructure bottlenecks. Their returns don't clear the top-eight hurdle on either side's numbers |
| CRWV, NBIS, IREN, CORZ, APLD | −1.5 to 18 | qualitative only | **Reject (agree)** | Both reports reject neoclouds on financing and zero-equity bears. Codex's explicit EV/net-claims modeling is better work than my qualitative screen |
| HPE, FN, POWL, GOOGL, AMZN, KLAC, CDNS, AMD, ALAB, MRVL/LITE | 1–11 | where modeled, similar | **Reject (agree)** | No change |

### 4b. Names I underwrote that Codex never considered

| Ticker | Why it matters | Status |
|---|---|---|
| BNTX | Codex screened it as "comparable" but never underwrote it. Net cash is about 85% of market value, so the downside is cash-backed, and it is the only holding with a positive AI-bust payoff in my model | Keep 1% (contested, low stakes) |
| SNDK | A second memory name that Codex never mentions. 2.9x FY28 EPS, but my model gives 8.6% because NAND normalization is deeper than DRAM/HBM | Agree it doesn't beat MU; no change |

### 4c. Evidence each report found that the other missed

**Codex found, and I missed:**

- **Owner-earnings discipline for high-SBC names.** It charges stock compensation for CRDO, KTOS, PLTR and CRWD. This changes two of my holdings (CRDO, KTOS) to 0.
- **A cell-level audit of the compute workbook.** It found HBM binding in every year, HBM price escalation compounding to about $306B in 2030 vs about $165B at a flat 3%, a double-counted packaging share, and kW/GW unit labels. It also corrected the inherited "9 Palo Verdes" framing to 2028, not 2027. This is better forecast hygiene than mine, though it changes no pick.
- **The August 2026 AI Futures comparison workbook distributions:**
    - TED-AI by end-2027: Daniel 23%, Eli 9%;
    - model automated-coder medians: Daniel Dec 2027, Brendan Jul 2028, Eli Mar 2029.

    These are more precise than my "AC mid-2028 or earlier" (Senate testimony). I use them to set the ~35% AI-2027 Scenario probability.

- **An explicit capex-shock vector** (−47.9% for Codex's 8) and a **zero-recovery regime overlay**. My report had no equivalent near-term shock table.
- **Tax and turnover drag.** Codex's plan turns over about 77% of the portfolio, and it shows a 5% tax cost removes about 1.5pp of CAGR. My revised plan turns over about 44% vs my V10, and more vs V9.1. The same caution applies.

**I found, and Codex missed (each bears on a Codex pick):**

- **Texas politics.** Governor-elect Hinojosa pledged a statewide moratorium on new data-center approvals. Governor Abbott ordered TCEQ to stop issuing new data-center permits in September. Voters backed about 40 of 41 local data-center restrictions on Nov 3. Codex holds **23% in NRG and VST** without mentioning Texas, ERCOT or the midterms once. NRG's Texas segment was **$1,018M of $2,013M** Q3 adjusted EBITDA.
- **PJM:** the 2028/29 auction cleared at the cap, 6.8 GW short. The next auction is Dec 9. FERC suspended backstop procurement. This bears on VST and NRG East (Q3 East EBITDA +$507M year over year).
- **AVGO as financier.** The XPV residual-value guarantee (about $29B maximum exposure on the first transaction per the 10-Q; tenant concentration in Anthropic; BofA cut its bond rating) and a $60B debt raise. Codex's 15% AVGO weight and 25% bear don't price this.
- **The rate and financing regime:** the Fed hiked in September, the 10-year peaked near 5.3% in October, CoreWeave bonds yield about 15%, and OpenAI reportedly cut its funding target. Codex discusses financing qualitatively but has no rate facts.

### 4d. How each report read the frameworks

| Item | Claude | Codex | Assessment |
|---|---|---|---|
| AI-2027 pace scorecard | Capabilities at ~70–90% of pace; capex, revenue and chips at or ahead | 70–90% (mean 0.693, median 0.885) from a recomputed grading workbook; compute 1.08, revenue 1.43 | **Agree.** Codex's recomputation is stronger evidence |
| Situational Awareness 100GW path | AI investment about a year ahead of SA's 2024 path (~$1T vs ~$500B in 2026) | 100 GW is an "aggressive individual-cluster scenario"; carry it as an upside/stress branch | **Compatible.** SA Table 5's ~$500B in 2026 is already exceeded; its 2028 ~$2T matches AI-2040's $2.4T |
| AI-2040 binding constraint | EUV is the 2027–30 wall; HBM is about 2/3 of AI's EUV draw | Same, plus "exposure intensity" | **Agree.** Codex then holds no EUV or HBM exposure, which my named-scenario CAGRs show is the most scenario-sensitive gap |
| Use in valuation | Raised ASML and MU (Rev 2) | Changed monitoring, not weights | **Both incomplete.** Neither translated the forecasts into named-scenario returns. That gap is what §2's AI-2027 and 100GW columns fill |

---

## 5. Facts That Change a Pick

| # | Claim | Mine | Codex | Primary-source check (source + date) | Resolved | Pick affected |
|---|---|---|---|---|---|---|
| F1 | NRG earnings anchor | Not covered | Aug 4 guidance; "don't buy before Nov 9" | [NRG Q3 2026 release](https://investors.nrg.com/news-releases/news-release-details/nrg-energy-reports-third-quarter-2026-results-reaffirms-2026), Nov 9: Q3 adjusted EPS $4.68; 2026 reaffirmed but EBITDA "slightly below midpoint" on weak ERCOT prices; **2027 guidance midpoint about $5.75B EBITDA, $3.15B FCF before growth, $9.05 EPS**; $4B generation asset sale; stock about +10% | Codex's 2030 base EBITDA of $7B needs +22% from 2027 guidance while selling assets. That is aggressive | NRG: add, but at 14.8%, not 24.5% |
| F2 | CEG outlook | 2027 EPS $13.40 (CY27E) | Aug 6 guidance $11.50–12.50 | [CEG Q3 2026 release](https://www.constellationenergy.com/news/2026/11/constellation-reports-third-quarter-2026-results.html), Nov 9: adjusted EPS $5.06; **2026 guidance raised to $12.50–12.80**; DOE loan commitment up to $5B for uprates; stock +10.5% | Fundamentals better, price higher; net expected CAGR 8.4% | CEG: exit (agree with Codex) |
| F3 | Texas data-center policy | Governor-elect proposed a statewide ban | Not mentioned | [ABC13, Nov 2026](https://abc13.com/post/governor-elect-gina-hinojosa-vows-ban-future-data-centers-texas/20021143/); [CNN, Nov 5](https://www.cnn.com/2026/11/05/economy/data-center-texas-election): a pledged moratorium on *new* approvals pending legislation; Abbott's Sept TCEQ permit pause | **Confirmed.** It is a pledge and needs the Legislature (session starts January); existing and under-construction projects are likely exempt | NRG and VST: 30% bear; power cluster capped at 20% |
| F4 | AVGO financing exposure | XPV with residual-value guarantees; "first $35B tranche" | Leverage mentioned; XPV not mentioned | Coverage of the AVGO 10-Q and S&P/BofA (Aug 2026, **STALE >30d**): **maximum exposure about $29B** on the first transaction at zero recovery; dual trigger (tenant default and residual value); Anthropic the primary tenant | Both mine ($35B tranche size) and the $29B maximum exposure stand; they measure different things | AVGO: bear −$6/sh; 30% bear; 11% not 15% |
| F5 | ASML earnings power | Base 2030 EPS $88 | Base $63.5 ($70B, 34% net margin) | [ASML Q3 2026 release](https://www.sec.gov/Archives/edgar/data/0000937966/000162828026065813/pressreleasefinancialresul.htm), Oct 14: sales €11.66B, **gross margin 57.5%, operating margin 44.4%, net income €4.96B** (about €4.5B ex-Mistral gain); **Q4 guidance €14.2–15.2B**; 2027–28 supply < demand | Codex's 2030 base is about the Q4-2026 run rate at a below-run-rate margin | ASML base kept at $88; still ranks #11 after the bear fix |
| F6 | CLS cash conversion and dilution | 2027 EPS $21.76 (consensus) | 2027 guidance $21.50, $40B; "after $3.45B equity offering" | [Celestica Q3 2026 release](https://finviz.com/news/408117/celestica-announces-third-quarter-2026-financial-results-and-will-hold-2026-investor-and-analyst-day), Oct 26: 2027 revenue $40B, 9.0% adjusted operating margin, EPS $21.50. **2026 FCF outlook cut to $460M from $600M; 2027 capex $1.5–2.0B; the $3.45B offering closed Aug 7** | The timing nuance doesn't matter. The FCF cut does: owner cash is about 1/3 of net income | CLS: 14x and a 30% bear; size 7% |
| F7 | NVT growth trajectory | Not covered | 2026 adjusted EPS $5.36–5.39; 44% organic | [NVT Q3 2026 release](https://www.sec.gov/Archives/edgar/data/0001720635/000162828026068391/q32026nvtpressrelease.htm), Oct 30: **confirmed**; **Q4 organic growth guidance 26–29%**; Maverick adds about 19pts to Q4; margins pressured in Q4 and improving in 2027; stock −8.8% that day | Codex's numbers are correct. The deceleration supports my 19x / $10 base over 22x / $10.6 | NVT: add at 11% |
| F8 | MU durability | LTAs over >50% of 2027–28 capacity; HBM sold out to 2029 | 26 strategic agreements, >35% of revenue through 2030, price floors and ceilings | [Micron Q4 FY26 prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf), Sep 30, **STALE >30d** (Codex's citation) | Not a factual conflict. The two describe the same contract book. The conflict is in *application*: Codex cites it, then models a 30% bear and $80 base EPS | MU: hold and raise |
| F9 | TSM bust anchor | Bear EPS $21 | Bear EPS $8.45 | 2025 ADR EPS ≈ $10 (approximate, from TSMC's 2025 reported EPS of about NT$63–66 per share ÷ ~32.5 NT$/USD × 5; **not independently re-verified this session**) | My $21 bear sat above 2026 run-rate EPS. A bust-to-2025 sub-case (~$10) belongs in the bear bucket | TSM: E 15.1% → 12.8%; weight 14 → 5 |
| F10 | Frontier-lab revenue | Anthropic about $65B run rate (Jul), $16.8B Q3 revenue; OpenAI about $50B | Anthropic $81B run rate at Oct 31 (Epoch, "Likely"); OpenAI $50B at Sep 30 | Epoch dataset (Nov 6) as cited by Codex | **No conflict.** The figures are consistent with growth through Q3–Q4. Codex's is more recent | None |

---

## 6. Revised Allocation (Mine, After Critique)

**Construction rule:** rank by re-underwritten Expected CAGR at the Nov 9 close. Within about 2pp, prefer the higher AI-2027 Scenario CAGR. Then apply these risk limits:

- 15% single-name cap;
- C1 AI-silicon cluster ≤ 50%;
- CLS ≤ 7%, for its low cash conversion and customer concentration;
- Texas/ERCOT-exposed merchant power (NRG + VST) ≤ 20%.

Capital that the caps block goes to the next names by rank, TSM (#9) and then ASML (#11 by expected return; it beats #10 SNPS on the AI-2027 tie-break).

| Ticker | Original % (V10) | Revised % | Delta | Head-to-head row that justifies it |
|---|---:|---:|---:|---|
| NVDA | 13 | **15** | +2 | §2 NVDA; B10 (the cap binds; #1 on every method) |
| VRT | 9 | **14** | +5 | §2 VRT (#4; Codex right on size, not on inputs) |
| MU | 9 | **12** | +3 | §2 MU; B6 (#2 by Expected, #1 by AI-2027 Scenario CAGR) |
| AVGO | 6 | **11** | +5 | §2 AVGO; B9 (Codex's EPS path adopted; XPV keeps it below the cap) |
| NRG | 0 | **11** | +11 | §2 NRG; B1 (replaces CEG) |
| NVT | 0 | **11** | +11 | §2 NVT; B2 (replaces ETN) |
| VST | 9 | **9** | 0 | §2 VST (my inputs hold; the power cap of 20 with NRG binds) |
| CLS | 0 | **7** | +7 | §2 CLS; B4 (add at the cash-conversion cap) |
| TSM | 14 | **5** | −9 | §2 TSM; B5 (corrected bear and bull weight → #9; residual capital) |
| ASML | 8 | **4** | −4 | §2 ASML; B5 (corrected bear → #11; residual capital) |
| BNTX | 1 | **1** | 0 | §2 BNTX; B7 (the only positive-bust holding) |
| SNPS | 6 | 0 | −6 | §2 SNPS; B5 |
| CEG | 6 | 0 | −6 | §2 CEG; B1; F2 |
| COHR | 5 | 0 | −5 | §2 COHR; B3 (Nov 9 price moved through value) |
| ETN | 5 | 0 | −5 | §2 ETN; B2 |
| CRDO | 3 | 0 | −3 | §2 CRDO; B3 (owner-EPS correction) |
| PWR | 2 | 0 | −2 | §2 PWR; B8 |
| KTOS | 2 | 0 | −2 | §2 KTOS; B7 |
| MP | 2 | 0 | −2 | §2 MP; B7 |
| **Total** | **100** | **100** | **0** | Increases +44 = decreases −44 |

**Checksum:** 15 + 14 + 12 + 11 + 11 + 11 + 9 + 7 + 5 + 4 + 1 = **100.0%**. 11 names; largest 15%; C1 50%; C3 25%; C4 20%; C2 4%; C6 1%.

| Portfolio (all on the re-underwritten inputs unless noted) | Expected CAGR | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Bust-case total return to 2030 |
|---|---:|---:|---:|---:|
| Claude V10, original inputs, Nov 6 (as published) | 14.7% | 23.5% | 30.2% | −26.6% (understated; see §1) |
| Codex 8, Codex inputs, Nov 6 (as published) | 22.8% | 39.2% | 47.0% | −56.6% |
| Claude V10, re-underwritten, Nov 6 | 14.0% | 23.8% | 30.5% | −41.7% |
| Codex 8, re-underwritten, Nov 6 | 16.3% | 26.7% | 33.6% | −44.5% |
| **Claude revised, re-underwritten, Nov 6** | **16.2%** | **26.9%** | **34.1%** | −42.8% |
| Claude V10, re-underwritten, **Nov 9** (before) | 12.6% | 22.3% | 28.9% | −44.7% |
| Codex 8, re-underwritten, **Nov 9** | 14.5% | 24.7% | 31.4% | −48.2% |
| **Claude revised, re-underwritten, Nov 9 (after)** | **14.7%** | **25.2%** | **32.3%** | **−46.1%** |

**Bust case:** every AI-linked holding at its re-underwritten bear terminal value, and BNTX at its base value.

**Reading the table:**

- My revised portfolio and Codex's 8 are within about 0.2pp of each other on expected return. The difference is that mine adds MU and small upstream positions (TSM, ASML) instead of COHR, plus a smaller power cluster and CLS. That buys about +0.5pp on the AI-2027 Scenario and +0.9pp on the 100GW Scenario, and about 2pp less bust loss.
- Against my own V10, the revision adds 2.1pp a year of expected return for 1.4pp more bust loss.
- **The bigger correction is to my risk disclosure, not my weights.** The −26.6% bust I published was built on bears that were too mild.

---

## 7. Picks Still Contested

Ranked by portfolio impact: weight at stake times the gap in expected return, or an in/out decision.

| Rank | Ticker or bottleneck | My position | Codex position | Weight at stake | What evidence would settle it |
|---|---|---|---|---|---|
| 1 | **Terminal exit multiples on AI hardware** (NVDA, AVGO, VRT, CLS, COHR) | Peer- and history-anchored (NVDA 18x, AVGO 20x, VRT 23x, CLS 14x, COHR 18x) | Re-rating (25x / 24x / 26x / 17x / 24x) | Not a weight; **~6pp of the portfolio's headline CAGR** (22.8% vs ~16%) | 10-year forward-P/E percentile data for each name and for mega-cap and semis peers. Neither report has it. Step 3 should source it (for example from Koyfin, FactSet or company histories) and set one multiple policy for every stock |
| 2 | **MU** | 12% (#2 Expected, #1 AI-2027) | 0% ("peak-cycle cheapness") | 12pp | MU FQ1 FY27 results on **Dec 23**: HBM4 2027 pricing, LTA floor coverage, capex vs FCF, buyback/cash policy. Also DRAM contract prices through year-end and SK hynix's 2027 capacity plans |
| 3 | **Upstream: TSM + ASML** | 9% combined (residual) | 0% | 9pp | TSMC's January 2027 guidance (2027 growth, capex, N2/A16 pricing) and ASML's Q4 report (January 2027) with a 2027 sales outlook. If 2027 EPS rises ≥10% above today's consensus, the corrected bears still leave them close to the top eight |
| 4 | **AVGO size** | 11% | 15% | 4pp | AVGO FQ4 report (**Dec 9**): disclosed XPV exposure, any second tranche, and whether non-Anthropic tenants join |
| 5 | **Texas-exposed power (NRG + VST)** | 20% total; NRG 11 | 23%; NRG 12 | 3pp, but a shared-driver risk on the whole 20–23% | Texas Legislature session (starts January 2027): whether the moratorium becomes law and covers *new load* or only *new approvals*; ERCOT forward prices for 2027; the **PJM 2029/30 auction on Dec 9** |
| 6 | **CLS size** | 7% | 12% | 5pp | Q4 FCF (Jan 2027) against the $460M 2026 outlook; whether 2027 capex is funded without new equity |
| 7 | **COHR** | 0% at $225 | 8% | 8pp | Price: re-entry below about $190 on my inputs. Two quarters of positive operating cash flow after the capacity build would justify an 18x → 20x multiple |
| 8 | **BNTX** | 1% | 0% | 1pp | Low stakes. Any re-underwrite of BNTX's oncology pipeline vs cash; whether a pandemic-hedge sleeve is wanted at all (owner preference) |

**For Step 3.** The fastest way to settle rank 1 is to set **one terminal-multiple policy**, for example base = the company's 10-year median forward P/E capped at the peer median, and re-run every candidate. Most of the 22.8% vs 14.7% headline gap between the two reports comes from that single choice, not from stock selection. On selection, Codex was right more often than I was.

---

## Final Verification

- The critique is saved at `Analysis 2026-11-08/inputs/Claude Critique of Codex 2026-11-08.md`. ✓
- §2 covers all 19 tickers held by either portfolio. Every one differs by at least 1pp. ✓
- §6 sums to **100.0%** (11 names), and every change cites a §2 row and a §3 bottleneck row. Increases +44pp = decreases −44pp. ✓
- Every §5 factual conflict has a primary-source check with a date. F4 relies on August coverage, flagged **STALE**. F8 relies on a September filing, flagged **STALE**. F9 is approximate and flagged unverified. ✓
- Named-scenario CAGRs were calculated for every stock in §2–§4 on both sides, because neither deep dive reported them. ✓
- Codex's published numbers were reproduced exactly from its inputs before critiquing them (22.8% / −56.6%; per-stock within 0.1pp). ✓
- Codex's Step 2 critique was not read. ✓

**Model files:** `inputs/research/claude_synthesis/step2/`

- `step2_model.py`
- `fund_step2.json` (Nov 9 fundamentals)
- `step2_out.json`
