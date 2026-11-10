# Event Horizon Fund Analysis — November 2026 Cycle

**Date:** November 8, 2026 cycle; synthesis completed November 9–10, 2026.
**Version:** **V10.0 (proposed)**. Supersedes V9.1 (May 10, 2026) only if adopted.
**Status:** **Proposal pending the Step 4 optimization pass (`PROMPT_4_OPTIMIZATION_PASS.md`) and the owner's decisions on the five escalated items in Part I.D.** This is not an adopted allocation. `README.md`'s active allocation has not been changed.

**How this report was made.** This is Step 3 of the four-step analysis flow (`PROMPT_3_SYNTHESIS.md`), synthesized by Claude (Opus 5.5):

- Claude and Codex each produced an independent deep dive.
- Each then critiqued the other stock by stock.
- This report pools every stock either model held, fully underwrote or proposed (58 in total) and values them on **one** consistent model at current prices.
- It ranks the pool and builds the portfolio from the ranking.

The full ranking, every disputed input and how it was resolved, and a self-sided audit of the synthesizer's own bias are in `inputs/Candidate Ranking 2026-11-08.md`. Conclusions taken from either model's work were re-checked at the primary source. Sources are cited inline and in Appendix B.

> **Market-data timestamp:** all prices are **closing prices from Monday, November 9, 2026** (Yahoo chart endpoint; last bar confirmed 21:00 UTC). "Since May" means the **May 8, 2026 close**, the last session before the V9.1 decision. Consensus estimates and multiples are Yahoo quoteSummary snapshots from the evening of Nov 9. **Inputs older than 30 days are flagged `[STALE >30d]`.**
>
> **Model convention:** terminal date **Dec 31, 2030** (T = 4.142 years). Expected terminal value = Σ(probability × scenario value); implied CAGR = (E[TV] / price)^(1/T) − 1. CAGRs are never averaged. Each stock has four 2030 states (bust, plateau, base, bull). The 25% bear bucket is half bust, half plateau. All values are model estimates, not consensus or guarantees. Portfolio-level error bands are about ±2pp.

---

## Part I: Executive Verdict

### A. The thesis held; the prices broke; the binding constraints are now capital and permission

The AI buildout's fundamentals beat almost every May assumption:

- NVIDIA guided $108B for its October quarter.
- Micron printed an 87% gross margin.
- TSMC's 2026 growth runs about 47%.
- PJM's capacity auction cleared at its cap, about 6.8 GW short.
- Transformer lead times run past 160 weeks.
- Frontier-lab revenue reached roughly $130–150B annualized.

The stocks went the other way. The V9.1 basket lost about **12.3% from May 8 to Nov 6** while SPY was flat. SMH fell about 11% in a single session on Nov 5, the sector's worst sell-off since 2020, before rebounding on Nov 9. Almost all of the damage was multiple compression, not thesis failure.

Two non-physical layers now gate the whole stack:

1. **Capital:**
    - the Fed hiked in September and the 10-year peaked near 5.3%;
    - neocloud bonds yield about 15%;
    - Broadcom now guarantees its customers' chip financing.
2. **Permission:**
    - voters backed about 40 of 41 local data-center restrictions on Nov 3;
    - Texas's governor-elect pledged a moratorium on new data-center approvals.

At Nov 9 prices, **V9.1 offers only about 7.8% a year to 2030** on the synthesis model. Twenty of its 24 positions return less than the capital's next use. The highest-quality bottleneck owners, meanwhile, trade at the lowest multiples of the cycle:

- NVDA at 11.2× next year's earnings;
- MU at 3.5×;
- CLS at 10.0×;
- NRG at about 6× 2027 free cash flow.

### B. Recommendation: V10.0, eight positions

| # | Ticker | Bottleneck | V9.1 | **V10.0** | Expected CAGR | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Why |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | **NVDA** | Accelerators / CUDA platform | 6% | **15%** | 17.8% | 26.8% | 41.5% | #2 of 58. 11.2× FY28 consensus after +24% estimate revisions in 90 days. The 15% cap binds |
| 2 | **META** | AI application + ads (buyer of compute) | 0% | **15%** | 15.0% | 20.0% | 33.9% | #5 of 58, 18.0× forward. The mildest bust of any top-10 name (−34%): it diversifies the hardware cluster without giving up return |
| 3 | **VRT** | Rack power + liquid cooling | 6% | **14%** | 13.8% | 22.0% | 34.9% | Q3 sales +61%, orders more than doubled; down 41% since May on de-rating alone |
| 4 | **MU** | HBM / DRAM | 6% | **14%** | 13.1% | **26.8%** | **45.3%** | 3.5× forward. Wins the AI-2027 tie-break in its band; HBM is the binding input in every year 2024–2030 of the AI-2027 compute model |
| 5 | **NRG** | Merchant power + retail (Texas/PJM) | 0% | **12%** | 17.1% | 24.9% | 35.6% | #3 of 58. ~6× 2027 FCF before growth, $4B asset sale funding deleveraging. Capped for leverage and Texas |
| 6 | **NVT** | Electrical distribution + liquid cooling | 0% | **12%** | 13.7% | 21.4% | 34.0% | +44% organic growth at 16.4× forward against ~21× for electrical peers. Replaces GEV, PWR and BE |
| 7 | **CLS** | Rack-scale integration | 0% | **10%** | 14.8% | 23.2% | 35.6% | #6 of 58. 2027 outlook $40B revenue, $21.50 EPS, at 10.0× forward. Capped for cash conversion |
| 8 | **VST** | Merchant power (Texas/PJM) | 6% | **8%** | 13.0% | 20.2% | 26.8% | Fills the Texas cap (NRG + VST = 20%). Beats TLN by 0.3pp expected and 0.9pp on AI-2027 |
| | **Total** | | | **100%** | | | | **Checksum: 15 + 15 + 14 + 14 + 12 + 12 + 10 + 8 = 100.0%** |

Event Horizon stays at about 50% of total net investments. Foundation and Continuity are unchanged, and Moonshot stays at 0%. There are no options, leverage, shorts, private holdings or ETFs.

**Portfolio results.** All on the same model and at Nov 9 prices; detailed in Part V.

| Portfolio | Expected CAGR | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Bust case to 2030 | 2–3 year delay to 2030 |
|---|---:|---:|---:|---:|---:|
| V9.1 (current) | 7.8% | 15.5% | 27.2% | −67.3% | −41.4% |
| **V10.0 (proposed)** | **14.9%** | **23.4%** | **36.9%** | **−61.8%** | **−23.9%** |
| V10.0 on Codex's higher terminal multiples | 18.2% | 26.7% | 40.5% | −56.0% | −14.1% |

V10.0 roughly **doubles V9.1's expected return**, and it does so while *reducing* the loss in both the bust and the delay scenarios. V9.1's apparent diversification was illusory: its most expensive names (CRWD, PLTR, MRNA, CCJ, INTC) add bust-case loss rather than reduce it.

### C. The decisive changes

1. **Exit the upstream "toll roads" at today's prices: TSM 11 → 0, ASML 8 → 0, SNPS 5 → 0, AVGO 3 → 0.**
    - The companies are excellent. On one consistent model, though, they return 11.0–11.8% (TSM, ASML, AVGO) and 2.1% (SNPS once its stock compensation is charged), against 13–18% for the holdings.
    - **What drives the gap:**
        - TSM trades at 16.6× forward, below the holdings on expected return but not cheap enough to clear them.
        - ASML's 23.9× already prices the EUV wall.
        - AVGO's financing guarantees (up to ~$43B of exposure) and 13% stock comp hold it to 11.6%.
    - **What V10.0 keeps:** exposure to the binding *upstream* constraint through **MU**, which has the highest AI-2027 (26.8%) and 100GW (45.3%) scenario CAGRs of any name in the portfolio's competitive band.
2. **Move power from the nuclear premium to cash yield: CEG 9 → 0, CCJ 2 → 0, BE 3 → 0; NRG 0 → 12, VST 6 → 8.**
    - CEG beat and raised on Nov 9 but rose 10.5% to 20.6× forward, leaving 8.4% expected.
    - NRG offers the same scarcity at ~6× 2027 FCF before growth, with a funded deleveraging path.
    - Texas exposure is capped at 20% because of the moratorium pledge.
3. **Replace the expensive electrical and grid names with the cheap one: GEV 5 → 0, PWR 4 → 0; NVT 0 → 12, VRT 6 → 14.**
    - GEV (32.1×) and PWR (27.3×) are priced for their backlogs.
    - NVT grew 44% organically at 16.4×.
    - VRT is a third cheaper than in May despite orders that more than doubled.
4. **Add the cheapest integrator and the cheapest platform: CLS 0 → 10, META 0 → 15.**
    - CLS: 10× forward with a 2027 outlook of $40B revenue.
    - META: 18× forward with 26% revenue growth.
    - Both entered the pool from Codex's candidate list, and both survive the synthesis model's stricter multiples.
5. **Sell everything priced for perfection or broken:**
    - CRWD (−12.5% expected), PLTR, MRNA (the oncology windfall), INTC (falsifier triggered), AVAV (restatement), CCJ (execution), KTOS and MP (owner economics), AMAT, ANET, DELL, COHR (+17% on Nov 9).

### D. Five decisions escalated to the owner (provisional calls are in V10.0)

| ID | Question | Provisional call | Weight at stake |
|---|---|---|---|
| E1 | **MOD** ranks #1 of 58 (18.7% expected) on a five-week-old post-spin perimeter with negative H1 FCF. Add now, or after its post-spin investor update? | **Gate: 0% now; +5% (VRT −3, NVT −2) if the update confirms margins and cash** | 5 |
| E2 | **NVDA during the board's review of CEO Jensen Huang** (opened Nov 8–9; see Part II.B3): 15% or 12%? | **15%, deployed only after Nov 17 earnings and with no adverse finding** | 3 |
| E3 | **Texas power:** keep VST, or switch to PJM-based TLN now? | **Keep VST; switch automatically if a moratorium bill clears a Texas chamber** | 8 |
| E4 | **META:** is an AI *buyer* inside the mandate, given Continuity already owns it through FSKAX? | **Include at 15%. Without it, expected return falls 0.4pp and the bust worsens 4pp** | 15 |
| E5 | **Concentration:** 8 names (top-3 = 44%) or a 16-name diversified build (13.6% expected, bust −59.2%)? | **8 names** | All |

### E. Additional risks accepted in pursuing maximum expected return

- **Concentration.** Eight names; top three = 44%; HHI 0.129, against 0.057 for V9.1. A single-name blow-up moves the fund 10–15 points.
- **Shared driver.** Every holding except META depends on AI infrastructure spending. In a deep AI-capex bust (2030 earnings back to 2025 levels for every holding simultaneously), the fund loses about 62%. That is better than V9.1's ~67% on the same stress, but it is a large loss for a sleeve that is half of household investments.
- **No upstream monopolies and no hedges.** TSM, ASML, SNPS and the defense, materials and bio hedges are gone:
    - The hedges returned 2–4% expected with 49–95% bust losses, so they didn't hedge.
    - The upstream monopolies are fully priced.
    - If the AI-2027 compute path proves EUV-limited *and* the market pays monopoly multiples again, V10.0 will lag.
- **Leverage and politics in power.** NRG carries ~$22.8B of net financial claims against ~$19.5B of equity. NRG + VST are 20% Texas-exposed merchant power, where the governor-elect has pledged a moratorium.
- **Key-person and governance risk at NVDA.** The new board review is unresolved.
- **Turnover.** Moving from the drifted V9.1 holdings to V10.0 turns over about 79% of the sleeve. Taxable-account gains could cost 1–1.5pp of CAGR. The deployment plan stages trades and uses losses first.
- **Model risk.** The headline depends on terminal multiples. On Codex's higher multiples V10.0 returns 18.2%; on the synthesis model, 14.9%. **The holdings are the same under both**, which is the more important result.

**Confidence in the recommendation: 3.5/5.** Confidence that V10.0 beats V9.1 and both models' Step 2 portfolios is 4/5. Confidence in exact weights is 3/5.

---

## Model Reconciliation

This section is the record the next cycle uses to grade each model separately.

### Weights by source

| Ticker | Rank (of 58) | Expected CAGR | Baseline V9.1 % | Claude blind % | Codex blind % | Claude post-critique % | Codex post-critique % | **Final V10.0 %** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| NVDA | 2 | 17.8% | 6 | 13 | 15 | 15 | 15 | **15** |
| META | 5 | 15.0% | 0 | 0 | 0 | 0 | 0 | **15** |
| VRT | 7 | 13.8% | 6 | 9 | 15 | 14 | 15 | **14** |
| MU | 9 | 13.1% | 6 | 9 | 0 | 12 | 8 | **14** |
| NRG | 3 | 17.1% | 0 | 0 | 12 | 11 | 12 | **12** |
| NVT | 8 | 13.7% | 0 | 0 | 12 | 11 | 12 | **12** |
| CLS | 6 | 14.8% | 0 | 0 | 12 | 7 | 12 | **10** |
| VST | 10 | 13.0% | 6 | 9 | 11 | 9 | 11 | **8** |
| TSM | 13 | 11.8% | 11 | 14 | 0 | 5 | 0 | **0** |
| AVGO | 15 | 11.6% | 3 | 6 | 15 | 11 | 0 | **0** |
| ASML | 17 | 11.0% | 8 | 8 | 0 | 4 | 0 | **0** |
| VRSK | 18 | 10.7% | 0 | 0 | 0 | 0 | 15 | **0** |
| ETN | 19 | 10.5% | 0 | 5 | 0 | 0 | 0 | **0** |
| CRDO | 20 | 10.3% | 0 | 3 | 0 | 0 | 0 | **0** |
| CEG | 23 | 8.4% | 9 | 6 | 0 | 0 | 0 | **0** |
| COHR | 28 | 6.6% | 2 | 5 | 8 | 0 | 0 | **0** |
| GEV | 30 | 6.1% | 5 | 0 | 0 | 0 | 0 | **0** |
| ANET | 31 | 6.1% | 4 | 0 | 0 | 0 | 0 | **0** |
| DELL | 33 | 5.6% | 2 | 0 | 0 | 0 | 0 | **0** |
| PWR | 37 | 5.1% | 4 | 2 | 0 | 0 | 0 | **0** |
| AMAT | 38 | 4.6% | 4 | 0 | 0 | 0 | 0 | **0** |
| AVAV | 39 | 4.6% | 1 | 0 | 0 | 0 | 0 | **0** |
| BNTX | 41 | 4.3% | 0 | 1 | 0 | 1 | 0 | **0** |
| MP | 45 | 2.3% | 3 | 2 | 0 | 0 | 0 | **0** |
| SNPS | 46 | 2.1% | 5 | 6 | 0 | 0 | 0 | **0** |
| CCJ | 47 | 2.1% | 2 | 0 | 0 | 0 | 0 | **0** |
| PLTR | 48 | 1.0% | 2 | 0 | 0 | 0 | 0 | **0** |
| KTOS | 52 | -2.1% | 1 | 2 | 0 | 0 | 0 | **0** |
| MRNA | 55 | -7.1% | 1 | 0 | 0 | 0 | 0 | **0** |
| BE | 56 | -10.5% | 3 | 0 | 0 | 0 | 0 | **0** |
| CRWD | 57 | -12.5% | 3 | 0 | 0 | 0 | 0 | **0** |
| INTC | 58 | -15.1% | 3 | 0 | 0 | 0 | 0 | **0** |
| **Total** | | | 100 | 100 | 100 | 100 | 100 | **100** |

### Every portfolio on the same assumptions (Nov 9 prices)

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

**Reading the comparison:**

- **V10.0 beats both post-critique portfolios on every metric:**
    - Expected CAGR +0.5 to +0.7pp;
    - AI-2027 +0.4 to +1.3pp;
    - 100GW +0.8 to +2.9pp;
    - bust 2–5pp better;
    - delay 1–3pp better.

    It also wins under Codex's multiples (18.2% vs 17.9% and 16.9%).
- **The 7-name concentrated architecture** returns 0.3pp more expected. It needs CLS and NRG at 15%, which the confidence caps reject.
- **Each model's blind (Step 1) portfolio** scores 11.4% (Claude) and 14.0% (Codex) on the shared model. Codex's stock selection was the better starting point, and its terminal multiples explain most of the gap between its published 22.8% and the 14.0% here.

### How the two models' disagreements were resolved

| Dispute | Claude's view | Codex's view | Resolution (evidence) |
|---|---|---|---|
| Terminal exit multiples (the largest driver of the headline gap) | Peer- and history-anchored (NVDA 18×, CLS 14×, NVT 19×) | Re-rated (NVDA 25 → 22×, CLS 17 → 16×, NVT 22×) | **One policy:** a value inside the evidence band (own forward P/E to peer median) beats one outside; if both are in or both out, the lower wins. The same eight holdings win under either side's multiples |
| MU | Hold 9–12% | 0% in Step 1, 8% in Step 2 | **14%.** Codex's conceded inputs ($110 EPS, 10×, explicit cash) still rank MU #9, and it wins the AI-2027 tie-break |
| Upstream (TSM, ASML) | 22% in Step 1, 9% in Step 2 | 0% | **0%.** 11.0–11.8% expected on the shared model |
| AVGO vs VRSK | AVGO 6 → 11% | AVGO 15 → 0%; VRSK 0 → 15% | **Both 0%.** AVGO 11.6% after owner EPS and the financing reserve; VRSK 10.7% at its own 23.0× multiple (Codex used 28×) |
| CLS size | 0 → 7% | 12% | **10%** (cash-conversion cap) |
| Texas power | Cap 20%, 30% bear | 23%, Texas not analyzed | **Cap 20%, 30% bear** (governor-elect's pledge, Nov 3 votes, Texas = 51% of NRG Q3 EBITDA) |
| META | Rejected at 20× (~11%) in Step 2 | "Preferred replacement," not held | **15%.** 15.0% at 20×; it ranks higher once both models' bear construction is replaced by the shared rule |
| MOD | Watchlist | Excluded (confidence 2) | **Gated** (E1) |
| Bear construction | ½ deep bust + ½ mild bear | Single deep bear | **Mixture, with the deep bear kept as the bust stress.** It moves portfolio expected return by under 1pp and changes no pick |

**Self-sided audit (detail in the Candidate Ranking):**

- **Inputs:** of 53 disputed inputs, 29 went to Claude's original view, 17 to Codex's, 4 split and 3 to neither. Sixteen of Claude's 29 were mechanical "tie → lower value" outcomes, because Codex's bull cases and multiples ran systematically higher. The robustness run with every disputed multiple set to Codex's value leaves the holdings unchanged.
- **Weights:** 21 of the 22 points cut from Claude's post-critique portfolio moved to Codex's view (AVGO, TSM, ASML and BNTX to zero). V10.0 overlaps 79% with Codex's post-critique portfolio and 78% with Claude's.

---

## Part II: Prior-Cycle Accountability and What Changed Since May 10, 2026

### A. V9.1 Scorecard: May 8 → Nov 6, 2026

Total return assumes buy-and-hold at V9.1 target weights, dividends included. "Forward E[CAGR]" is each stock's expected return from the Nov 9 price on the synthesis model.

| Ticker | V9.1 wt | May 8 px | Nov 6 px | Nov 9 px | Total return (to Nov 6) | Contribution (pts) | Next-FY EPS revision (90d) | Primary driver | Forward E[CAGR] (Nov 9) | Was the May decision right, for the right reason? |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| TSM | 11% | $411.68 | $375.44 | $388.62 | −8.3% | −0.91 | +9.9% | De-rating while EPS rose | 11.8% | **Thesis yes** (2026 growth ~47%). Bought near peak multiple |
| NVDA | 6% | $215.20 | $186.64 | $178.67 | −13.1% | −0.79 | **+24.2%** | De-rating on financing fears | **17.8%** | **Thesis yes, size no.** 6% was far too small for today's valuation |
| AVGO | 3% | $430.00 | $293.69 | $319.48 | −31.5% | −0.94 | −0.6% | De-rating; it became a financier (XPV guarantees) | 11.6% | **Partly.** AI targets rose, but the financing risk was not foreseen |
| MU | 6% | $746.81 | $690.00 | $733.15 | −7.6% | −0.46 | **+24.5%** | Peak-cycle de-rating against a ~2.4× EPS upgrade | 13.1% | **Thesis yes; "fully priced" was wrong** |
| ASML | 8% | $1,592.02 | $1,424.75 | $1,513.25 | −10.3% | −0.82 | +10.5% | De-rating | 11.0% | **Yes** (2026 guidance €36–40B → €44–45B) |
| AMAT | 4% | $435.44 | $332.72 | $370.55 | −23.4% | −0.94 | +9.2% | De-rating + China affiliate rule | 4.6% | **Partly** |
| SNPS | 5% | $516.48 | $450.46 | $466.97 | −12.8% | −0.64 | +7.9% | De-rating | 2.1% (owner basis) | **Thesis yes.** Stock comp (~31% of adjusted EPS) was never charged |
| ANET | 4% | $141.77 | $170.80 | $186.17 | **+20.5%** | **+0.82** | +16.4% | **Fundamental** (Q3 +58.5%) | 6.1% | **Yes, right reasons.** The return is now spent |
| VRT | 6% | $339.97 | $182.86 | $200.47 | **−46.2%** | **−2.77** | +8.2% | **Pure de-rating** from ~48× forward | 13.8% | **Thesis yes, price no.** The largest detractor despite +61% sales |
| DELL | 2% | $260.46 | $328.53 | $346.31 | **+26.5%** | +0.53 | **+45.2%** | Fundamental (FY27 guide $192B) | 5.6% | **No.** The trim was wrong in hindsight |
| CEG | 9% | $303.63 | $249.95 | $276.09 | −17.4% | −1.57 | +0.4% | Political/regulatory de-rating | 8.4% | **Yes on the trim** (11 → 9). Thesis confirmed (Google 3.6 GW) |
| VST | 6% | $147.72 | $124.80 | $133.92 | −15.3% | −0.92 | −3.1% | Texas politics + softer ERCOT | 13.0% | **Thesis yes, timing no** |
| PWR | 4% | $745.00 | $540.90 | $591.48 | −27.4% | −1.10 | +11.9% | De-rating from ~40× | 5.1% | **Thesis yes; bought at peak multiple** |
| CRWD | 3% | $131.94 | $216.90 | $228.58 | **+64.4%** | **+1.93** | −1.0% | **Multiple expansion** | −12.5% | **Yes, but the return is now spent** |
| PLTR | 2% | $137.80 | $160.38 | $169.20 | +16.4% | +0.33 | +10.2% | Fundamental with compression | 1.0% | **Yes** |
| AVAV | 1% | $168.29 | $112.76 | $126.96 | −33.0% | −0.33 | −0.3% | **Thesis damage** (restatement; SCAR loss) | 4.6% | **No** |
| KTOS | 1% | $57.89 | $35.10 | $37.69 | −39.4% | −0.39 | +0.9% | De-rating | −2.1% (owner basis) | **Thesis yes; owner economics weak** (FY26 FCF use $110–120M) |
| MRNA | 1% | $54.35 | $254.19 | $269.00 | **+367.7%** | **+3.68** | n/m | **Event:** Phase 3 melanoma vaccine | −7.1% | **Right for the wrong reason** |
| MP | 3% | $67.43 | $35.41 | $37.75 | −47.5% | −1.43 | −20.1% | Détente erased the scarcity premium | 2.3% | **No (timing)** |
| INTC | 3% | $124.92 | $56.28 | $59.37 | **−54.9%** | −1.65 | −11.6% | **Thesis failure** (no anchor foundry customer) | −15.1% | **No.** The May falsifier never triggered |
| GEV | 5% | $1,040.15 | $774.11 | $829.34 | −25.5% | −1.27 | +4.8% | De-rating; gas orders slowed | 6.1% | **Thesis yes; bought at a peak multiple** |
| CCJ | 2% | $116.75 | $71.30 | $75.37 | −38.9% | −0.78 | −6.7% | **Execution miss** (Key Lake) | 2.1% | **Commodity yes, company no** |
| BE | 3% | $261.03 | $173.24 | $193.88 | −33.6% | −1.01 | +8.7% | De-rating; no backlog disclosure | −10.5% | **Thesis yes; extended entry** |
| COHR | 2% | $335.26 | $192.81 | $225.19 | −42.5% | −0.85 | +17.8% | October optics crash | 6.6% | **Thesis yes.** After +16.8% on Nov 9, the price is ahead of the model |
| **Total** | **100%** | | | | **−12.3%** | **−12.27** | | | **7.8% (portfolio)** | |

**Benchmarks, May 8 → Nov 6 (total return):** SPY +0.2% · QQQ −7.6% · SMH −18.1% · SOXX −21.2% · XLU −2.2% · ITA −7.2% · IBB +25.7% · URA −41.4%. Through Nov 9, the V9.1 basket is about **−6.8%** on price alone, with the Nov 9 chip rebound recovering part of the loss.

**Accountability conclusions:**

1. **The thesis was right; the entry prices were wrong.** Fourteen of 24 holdings had material upward estimate revisions. May bought several bottleneck owners at peak multiples (VRT ~48×, PWR ~40×, GEV ~40×), and the de-rating cost about 10 points.
2. **The four genuine failures were small positions with slow falsifier discipline:** INTC, AVAV, CCJ and MP (a timing failure). Together they cost about 4.2 points.
3. **The biggest gains came from outside the core thesis.** MRNA's oncology event and CRWD's multiple expansion are not repeatable, and both now carry negative expected returns.
4. **New lesson from the cross-model process: owner economics.**
    - Charging stock compensation where consensus excludes it changes several verdicts. SNPS falls from ~12% to 2%; KTOS and CRDO fall below the hurdle; AXON's 84% stock-comp load makes it uninvestable at 32×.
    - V9.1's sizing never made this adjustment.
5. **Lesson for V10.0: size on valuation-adjusted forward return**, not on "bottleneck owner vs integrator" labels. The May labels excluded CLS (integrator) and NRG (retail mix), which are now two of the six highest-ranked stocks in the pool.

### B. What Changed Since May 10 (new evidence only)

#### B1. Earnings reality vs May expectations

| Metric | May 10 baseline | Nov 9 reality | Delta |
|---|---|---|---|
| NVDA quarterly revenue | Q1 FY27 guide $78B | **Q2 $96.2B; Q3 guide $108B ±2%; FY28 growth "~70%"** `[Q2 STALE >30d: Aug 26]`; Q3 report ~Nov 17 | Far exceeded |
| Micron revenue / gross margin | Q3 FY26 guide $33.5B, 81% | **Q4 FY26 $54.2B, 87%; Q1 FY27 guide $61.5B; 26 strategic agreements covering >35% of revenue through 2030** `[STALE >30d: Sep 30]` | Far exceeded |
| TSMC 2026 growth | ">30%" | **~47%; Q3 net margin 51.1%; CY27 consensus EPS $23.39 (+10% in 90 days)** | Far exceeded |
| ASML | 2026 €36–40B | **€44–45B; Q3 gross margin 57.5%, operating margin 44.4%; 2027 low-NA capacity +~30%; 2027–28 supply < demand** | Exceeded |
| Broadcom | AI ">>$100B in 2027" | **FY27 $115B, FY28 $230B AI targets; XPV customer financing with guarantees: ~$29B maximum on the first transaction (10-Q, Sep 10), ~$43B maximum undiscounted exposure (8-K, Oct 27)** | Exceeded, plus new credit risk |
| Vertiv 2026 revenue | $13.5–14.0B | **~$14.45–14.85B; Q3 +61%; organic orders >2×; order disclosure discontinued** | Exceeded |
| nVent | Not covered | **Q3 sales +44% (all organic); 2026 adjusted EPS $5.36–5.39; Maverick Power closed Oct 1; Q4 organic growth guided 26–29%** (Oct 30) | New |
| Celestica | Not covered | **2027 outlook: revenue $40B, adjusted EPS $21.50, 9% adjusted operating margin; 2026 FCF cut to $460M; 2027 capex $1.5–2.0B; $3.45B equity offering closed Aug 7** (Oct 26) | New |
| NRG | Not covered | **Q3 (Nov 9): 2026 reaffirmed, EBITDA slightly below midpoint on weak ERCOT prices; 2027 EBITDA $5.5–6.0B and FCF before growth $2.9–3.4B, excluding a $4B, 4.9 GW asset sale targeted to close in Q2 2027** | New |
| Constellation | 2026 EPS $11–12 | **$12.50–12.80 (raised Nov 9); Google 3.6 GW package; DOE loan commitment up to $5B for uprates** | Exceeded |
| Vistra | 2026 EBITDA $6.8–7.6B | **2026 $7.1–7.5B; 2027 $7.7–8.5B consolidated after the October Cogentrix close; 2027 FCF before growth $4.3–5.1B** | Met/exceeded |
| Meta | Not covered | **Q3 (Oct 21): revenue +26%; a large litigation charge; capex above quarterly operating cash flow** | New |
| Modine | Not covered | **Spin-off completed Oct 1; continuing-business FY27 guide $3.1–3.2B sales, $470–500M adjusted EBITDA (Nov 3); H1 FCF negative** | New (perimeter changed) |
| Coherent | FQ3 $1.81B | **FQ1 FY27 $2.37B (+50%); operating cash flow −$92.7M, capex $775.5M** (Nov 4) | Growth exceeded; cash did not |
| Kratos | — | **2027 revenue $2.1–2.2B, EBITDA $230–240M; 2026 FCF use $110–120M; Q3 GAAP EPS $0.00 vs adjusted $0.24** (Nov 5) | Growth without owner cash |
| BioNTech | — | **Cash €16.164B, 247.9m shares, continuing losses** (Nov 3) | Burn continues |
| Intel / Cameco / AeroVironment | Foundry wins / production / BADGER | **Failed / missed / restated** | Failed |
| Frontier-lab revenue | n/a | **Anthropic ~$81B run-rate (Oct 31, Epoch "likely"); OpenAI ~$50B (Sep 30)** | Ahead of every published path |
| Hyperscaler capex | 2026 $725–830B | **Big-4 2026 ≈ $720–745B; 2027 consensus ≈ $935B (+~28%)** | In line / up |

#### B2. The regime shift: four constraints

| Constraint | Evidence (date) | Who it hurts | Who it helps |
|---|---|---|---|
| **Capital / financing** | Fed hike (Sep 16); 10Y peak ~5.3% (Oct); OpenAI's new funding target reportedly cut to ~$20B (late Oct); CoreWeave bonds ~15%; Broadcom's $60B debt raise and XPV guarantees; Hock Tan: "the biggest constraint is capital" | Vendor financiers (AVGO), neoclouds (CRWV, IREN, NBIS), OpenAI-concentrated suppliers (AMD, ORCL) | Self-funded buyers (META, MSFT, GOOGL); suppliers with prepaid/LTA customers (MU); cash generators (NRG, VST) |
| **Permission / social license** | Nov 3: voters backed ~40 of 41 local data-center restrictions; Texas governor-elect pledged a moratorium on new approvals (needs the Legislature, which opens Jan 2027); Abbott's September TCEQ permit pause; an estimated 30–50% of 16 GW of 2026 US capacity delayed | Greenfield builders, Texas merchant power (VST −14% on election day) | Owners of energized, permitted fleets (NRG, VST, CEG, TLN); delays *lengthen* the cycle for thermal and electrical suppliers |
| **Memory scarcity** | SK hynix Q3 operating margin 80%; DRAM/HBM "sold out to 2029"; MU gross margin 87%; LTAs with price floors | PC/phone OEMs, Dell client | MU |
| **Physical lead times** | GSU transformers >160 weeks; breakers ~125 weeks; PJM 2028/29 6.8 GW short at the cap; InP lasers and EUV sold out into 2028–29 | Hyperscaler timelines | NVT, VRT, ETN, GEV, ASML |

#### B3. Regulatory, governance and geopolitical developments

- **NVIDIA governance (Nov 8–9, new).**
    - In a Nov 8 memo to employees, CEO Jensen Huang admitted an extramarital affair and promised full cooperation with an independent board review.
    - The board said it would investigate his relationship with a woman reportedly believed by US intelligence to be a Chinese agent. China's Foreign Ministry called the allegation "unsubstantiated."
    - No 8-K or regulator action was reported, and Huang has not stepped aside.
    - NVDA fell 4.3% on Nov 9 while the SOX rose about 6%.
    - **This is a key-person and US–China relations risk, not an earnings fact.** It is handled by staging NVDA purchases after the Nov 17 report (E2).
    - Sources: [Yahoo Finance/24/7 Wall St, Nov 9](https://finance.yahoo.com/markets/stocks/articles/nvidia-falls-5-board-probes-134356169.html); [CNN, Nov 9](https://www.cnn.com/2026/11/09/investing/nvidia-stock-huang-investigation).
- **Texas.** The governor-elect's pledged moratorium on new data-center approvals ([CNN, Nov 5](https://www.cnn.com/2026/11/05/economy/data-center-texas-election); [ABC13](https://abc13.com/post/governor-elect-gina-hinojosa-vows-ban-future-data-centers-texas/20021143/)) needs the Legislature, which convenes in January. Existing and under-construction projects are likely exempt.
    - Texas was **$1,018M of NRG's $2,013M** Q3 adjusted EBITDA.
- **PJM.**
    - The 2028/29 auction cleared at the $325/MW-day cap, about 6.8 GW short `[STALE >30d]`.
    - **The 2029/30 auction is Dec 9, 2026.**
    - FERC suspended PJM's backstop procurement in late September.
    - Google–Constellation's 3.6 GW package is the bring-your-own-power template.
- **US–China.**
    - The trade truce runs to **Jan 10, 2027** (US side).
    - China's suspension of its October 2025 rare-earth notices **lapses Nov 10**, with no published extension as of Nov 9.
    - H200 export licenses are stalled on the Chinese side.
    - Bloomberg reports the NVIDIA episode could complicate the Xi–Trump APEC meeting in Shenzhen.
- **Defense.** The FY27 request is $1.5T, including $350B via reconciliation, and the post-midterm budget repricing hit small-cap defense `[request dated Apr 2026, STALE]`.
- **mRNA policy.** HHS wound down federal mRNA projects in 2025, so policy support for rapid-response mRNA is weaker than V7.3 assumed.

#### B4. Market backdrop

| Indicator | May 8, 2026 | Nov 9, 2026 |
|---|---|---|
| S&P 500 (SPY) | $737.62 | $752.69 (+2.4% on Nov 9) |
| Nasdaq-100 (QQQ) | $711.23 | $679.35 |
| SMH | — | $487.41 (−11.2% on Nov 5; +5.1% on Nov 9) |
| VIX | 17.2 | ~25 (Nov 6: 25.6) |
| US 10-year yield | 4.36% | ~4.9% (peaked ~5.3% in Oct) |
| Upcoming catalysts | — | CRWV (Nov 10), AMAT (Nov 12), **NVDA (Nov 17)**, MOD investor update (~Nov 18, per its post-spin communications; not independently confirmed), DELL (Nov 24), CRDO (Nov 30), **AVGO and PJM BRA (Dec 9)**, **MU (Dec 23)**, truce expiry (Jan 10), TSM (Jan 14), Texas Legislature (Jan) |

**Interpretation:** fundamentals are at records, prices are 25–60% off their highs, and volatility is elevated. That setup rewards valuation-driven rotation, provided the financing and permission shocks slow the cycle rather than break it. Part VII defines what "break" would look like.

### C. Background-Framework Deep Dive: AI-2027, the Compute Forecast Workbook, AI-2040 and Situational Awareness

Both deep dives read these sources at the primary source in Step 1, independently. This section reconciles their readings.

**Sources covered:**

- **AI-2027:** [main scenario](https://ai-2027.com/), [race ending](https://ai-2027.com/race), [summary](https://ai-2027.com/summary), and the [compute](https://ai-2027.com/research/compute-forecast), [timelines](https://ai-2027.com/research/timelines-forecast), [takeoff](https://ai-2027.com/research/takeoff-forecast), [AI goals](https://ai-2027.com/research/ai-goals-forecast) and [security](https://ai-2027.com/research/security-forecast) supplements.
- **The shared AI chip compute forecast workbook** ([Google Sheet, Oct 2024](https://docs.google.com/spreadsheets/d/1Ko-olwjDy6h8rXLZBFpP-e2GibGqRhfV28S4v8xtzrM/edit?gid=1866551567)). Every tab was read, including cached formulas.
- **[AI-2040](https://ai-2040.com/)** and its [compute supplement](https://ai-2040.com/supplements/compute-supplement) (Jul 2026).
- **The AI Futures Project's [blog](https://blog.aifutures.org/):**
    - 2025 grading (Feb 2026);
    - Q1 2026 (Apr 2) and Q2.5 2026 (Aug 16) timeline updates, plus the August comparison workbook;
    - the Chinese lithography forecast;
    - Kokotajlo's Sept 30 Senate testimony;
    - the [AI Futures model](https://www.aifuturesmodel.com/).
- **[Situational Awareness](https://situational-awareness.ai/)**, especially [Racing to the Trillion-Dollar Cluster](https://situational-awareness.ai/racing-to-the-trillion-dollar-cluster/) and the [June 2024 PDF](https://situational-awareness.ai/wp-content/uploads/2024/06/situationalawareness.pdf) (Tables 4–5).
- **Background:** [METR's task-horizon work](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) and [Epoch trends](https://epoch.ai/trends).

#### C1. Scorecard: how the forecasts have tracked (Nov 2026)

| Prediction | Source | Forecast | Reality (Nov 2026) | Grade |
|---|---|---|---|---|
| Global AI capex / datacenter spending, 2026 | AI-2027 compute supplement | ~$1T cost of active compute; ~$600B DC spending | Big-4 capex ≈ $720–745B; ≈ $0.9–1T including Oracle, neoclouds and sovereigns | **On track / ahead** (compute variable 1.08× of pace in the authors' recomputed grading) |
| Total AI investment 2026 / 2027 | Situational Awareness | ~$500B; >$1T by 2027 | ≈ $0.9–1T; 2027 consensus ≈ $1.2–1.5T | **~1 year ahead** |
| Leading-lab revenue | AI-2027 compute supplement | ~$45B in 2026 | Anthropic ~$81B run-rate (Oct 31); OpenAI ~$50B (Sep) | **Ahead** (revenue 1.43× of pace) |
| Frontier-lab ARR | AI-2040 | $30B (start-2026) → $180B (start-2027) | ≈ $130–150B by Nov 2026 | **On track** |
| AI chip market 2026 | Workbook | $396B | ≈ $450–500B | **Ahead** |
| HBM | Workbook | $20.6B (2026). **HBM is the binding (minimum) input in every year 2024–2030** of the high-demand model | MU did $54B in one quarter; HBM sold out to 2029 | **Far ahead; the binding call is confirmed** |
| Wafer/EUV constraint | Workbook; compute supplement | Wafers bind only after 2027 | ASML 2027–28 supply < demand; cleanroom-limited 2027 WFE | **Binding earlier than modeled** |
| Capex overtakes hyperscaler OCF, forcing debt | AI-2040 | ~Q3 2026 | October financing scare; record bond issuance | **On time** |
| Coding automation | AI-2027 scenario | ~1.5× AI R&D multiplier, early 2026 | "Almost all code" at top labs AI-written (testimony); coding-uplift surveys 1.25× → 4× in seven months | **On point** |
| Capability pace (quantitative) | Authors' grading | 100% = AI-2027 pace | 65% (Feb) → ~75% (Jul) → **70–90% (Aug)**; recomputed mean 0.69, median 0.89 | **Slightly behind** |
| "China wakes up" (compute centralization) | AI-2027 scenario | Mid-2026 | Not observed; China ~12% of world compute | **Miss (timing)** |
| Stock market +30% in 2026 | AI-2027 scenario | +30% | S&P ~+9% YTD; AI valuations "well behind pace" | **Miss: markets lag fundamentals** |
| Public backlash | AI-2027 scenario | Late 2026–2027 | ~40 of 41 local restrictions backed by voters (Nov 3) | **Right direction; arrived via local politics** |
| Power as the biggest constraint; barriers "self-made" | Situational Awareness | Permitting, FERC, utility regulation | PJM short at the cap; FERC friction; local bans | **Right** |
| AI deception incidents | AI-2027 goals forecast | Escalating; 2027 misalignment discovery | Jul 2026: ~700-agent sandbox escape investigated by METR | **Earlier than the scenario** |

**Workbook hygiene, from the cell-level audit:**

- HBM revenue reaches **$306B in 2030** only because price exponents compound. At a flat +3%/yr price on the same quantities, it is about **$165B**.
- The packaging share is double-counted in one tab.
- Some kW and GW labels are swapped.
- V7.3's "25 Palo Verdes" figure is a 2028 number, not 2027.

None of these changes the direction. They do mean the workbook's dollar outputs should not be used as forecasts. The synthesis uses the $165B as the base-case HBM path and the $306B only on the AI-2027 path.

**Bottom line:** the buildout's *economics* (capex, lab revenue, chip volume, memory) run at or ahead of the most aggressive public forecasts. Capabilities run at 70–90% of pace. **Equity valuations are behind.** The scorecard doesn't show the thesis running ahead of reality; it shows prices running behind it.

#### C2. Updated timelines (authors' latest, Apr–Sep 2026)

- **Q1 2026 update (Apr 2):** automated-coder medians moved earlier. Kokotajlo moved from late 2029 to mid-2028, and Lifland from early 2032 to mid-2030.
- **Q2.5 update and comparison workbook (Aug 16):**
    - Timelines got "slightly shorter."
    - Model medians for the automated coder: **Kokotajlo Dec 2027, Brendan Jul 2028, Lifland Mar 2029.**
    - Probability of transformative AI by end-2027: **Kokotajlo 23%, Lifland 9%.**
- **Senate testimony (Sep 30):** Kokotajlo puts about 50% on automated AI R&D by end-2028.
- **AI-2040 (Jul 9):** full AI R&D automation by default in 2030; Kokotajlo expects "somewhat faster."
- **Investor caveat:** the forecasts are conditional on progress going as fast as is technically feasible. They **exclude** government and political slowdowns, which are exactly the permission and financing constraints in B2.

**What changed since the May cycle:** the authors' central timelines are about 1–1.5 years *shorter* than in late 2025. They remain 1–2 years later than the literal AI-2027 storyline.

#### C3. Forward paths (2027–2030) and the synthesis's scenario set

The full yearly table is in `inputs/Candidate Ranking 2026-11-08.md`, §A1.1.

| Path | Probability | 2030 AI capex | Defining features | Who captures value first |
|---|---:|---:|---|---|
| Bust (half the bear bucket) | 12.5% | ~$0.45T (≈ 2025) | Financing wall; supplier earnings back to FY2025 | Nobody; the cash-rich survive |
| Plateau / 2–3 year delay (half the bear bucket) | 12.5% | ~$0.9T | Capex stalls near 2026 levels; growth resumes late | Owners of existing power (NRG/VST delay losses −5% to −29%) |
| Base | 50% | ~$2.8T | Capex grows ~30%/yr 2027–30; HBM ~$165B; ~150 GW of AI power | Broad: accelerators, memory, electrical, power |
| Bull | 25% | ~$4.5T | AI-2027-like or faster | Memory, accelerators, thermal |
| **AI-2027 Scenario** | **35%** (base-to-bull) | **~$4.2T** | AI-2040's $2.4T in 2028 (38% debt-financed); EUV wall 2029–30; HBM ~$306B; ~230 GW | MU, NVDA, NRG, CLS, VRT (highest AI-2027 CAGRs in V10.0) |
| **100GW 2030 Scenario** | **10%** (subset of bull) | **~$8T** | One ~100 GW / ~100M-H100e training cluster; total AI power ≈ US electricity; ~4× TSMC leading-edge capacity | Near term: energized power and electrical/thermal. Then memory and lithography |

**Distance from the 100GW path today:**

- Total AI investment is about a year *ahead* of Situational Awareness's 2026 marker.
- Neither deep dive found evidence of an energized, coherently networked ~1 GW training cluster, so the cluster milestone is unverified.
- Announced GW are not operating GW.
- The 2030 destination needs about 100× the 2026 single-cluster power.
- **Bottlenecks would bind in this order:** interconnection, permits and transformers; then firm generation; then HBM, CoWoS and EUV; then financing.

#### C4. What the framework evidence changed in the allocation

| Framework finding | Implication | V10.0 decision |
|---|---|---|
| HBM is the binding input in every modeled year, and HBM uses about two-thirds of AI's EUV draw | Memory supply growth is capped; glut risk is lower than the cycle's history suggests | **MU 6 → 14%**, the highest AI-2027 (26.8%) and 100GW (45.3%) CAGRs in its band |
| EUV is the named 2027–30 wall (AI share of the fleet 27% → 65% → 77%) | ASML has pricing power, but the stock already trades at 23.9× forward | **ASML 8 → 0%:** 11.0% expected. Owning the constraint through MU is cheaper |
| AI-2040's "$1.2M per wafer" is an all-in cost; TSMC's foundry component is ~$25–30k | No special TSMC price lever beyond volume | **TSM 11 → 0%:** 11.8% expected |
| The economics run at or ahead of pace while equity prices lag | Supports buying compressed owners on rising estimates | NVDA 15%, VRT 14%, CLS 10% |
| Power is the 10–100 GW constraint, and the forecasts exclude politics | Existing energized fleets capture scarcity first, but Texas politics is live | **NRG 12% + VST 8%, capped at 20% Texas**; TLN is the switch |
| AI-2040 depicts "AI on the ballot" in 2028 and a 2029 deal cutting ~31% of debt-financed capex; real incidents (Jul 2026) | Policy risk to the 2029–30 tail | The bust and plateau states carry it; META's mild bust (−34%) partly offsets it |
| Race vs slowdown endings | Ordinary terminal-P/E analysis is irrelevant in a loss-of-control or expropriation branch | **Not modeled in expected value.** An extra 10% common zero-recovery regime cuts V10.0 from 14.9% to 12.0% (Part VII) |

---

## Part III: Zero-Based Portfolio Test and Bottleneck Map

### A. Method (blank slate)

1. **Universe.** 58 stocks: every name either model held, fully underwrote or proposed. Together the two deep dives screened about 110 tickers, including every V9.1 holding, the May watchlists and names surfaced by current events. Benchmarks (SPY, QQQ, SMH, SOXX, XLU, ITA, IBB, URA) were evaluated as fallbacks only.
2. **One valuation model.** Every stock is valued on owner earnings (stock compensation charged where consensus excludes it) under four 2030 states with uniform rules:
    - **bust:** FY2025 earnings at 0.7× the base multiple;
    - **plateau:** FY2026 earnings at 0.85×;
    - **base:** resolved judgment;
    - **bull:** 1.2× the base multiple.

    Probabilities are 25/50/25, with stock-specific exceptions. Exit multiples must lie within an evidence band running from the stock's own forward P/E to its peer median. Disputed inputs follow the A4 order: facts, concessions, better-supported, then the lower value on a tie. They are never averaged.
3. **No sleeve entitlements.** No layer of the stack is owed capital. A stock can be the best company in its bottleneck and still get 0% if another use of the capital returns more.
4. **Hurdle.** Each position must beat the next-best use of its capital. In practice that means about 13% expected at Nov 9 prices, or winning the AI-2027 tie-break within about 2pp.
5. **Constraints (constraints, not objectives):**
    - 15% per name;
    - NRG + VST ≤ 20% (Texas);
    - CLS ≤ 10% and NRG/NVT ≤ 12% (confidence and leverage);
    - speculative (confidence 2) names enter only through a dated gate;
    - AI-silicon cluster ≤ 50%;
    - a bust case better than V9.1's;
    - long-only common stock and ADRs; Moonshot 0%.

**Shared-driver clusters used throughout:**

| Code | Cluster | Members (examples) |
|---|---|---|
| C1 | AI silicon, memory and integration | NVDA, MU, CLS, TSM, AVGO, AMD, MRVL, COHR, CRDO, LITE, ANET, DELL, ALAB, SNDK, neoclouds |
| C2 | Fab tools and design | ASML, AMAT, LRCX, KLAC, SNPS, CDNS, INTC |
| C3 | Data-center physical and electrical | VRT, NVT, ETN, GEV, PWR, MOD, POWL, BE |
| C4 | Power generation and fuel | NRG, VST, TLN, CEG, CCJ |
| C5 | Platforms, software and data | META, MSFT, GOOGL, AMZN, CRWD, PLTR, PANW, VRSK, RELX, MSI, AXON, GEN |
| C6 | AI-independent hedges | KTOS, AVAV, MP, MRNA, BNTX |

### B. The Complete Bottleneck Map (November 2026)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│            THE AI BUILDOUT CONSTRAINT STACK (NOVEMBER 2026)                 │
│   Top two layers are the new "meta-bottlenecks": they gate everything below │
├─────────────────────────────────────────────────────────────────────────────┤
│ ▓ CAPITAL / FINANCING (new #1) — ~$38B per GW; $1T+/yr needs debt; 10Y ~5%;│
│ ▓ neocloud bonds ~15%; vendor financing (AVGO guarantees up to ~$43B)      │
│ ▓ PERMISSION (new #2) — 40/41 local measures passed; Texas moratorium       │
│ ▓ pledge; 30–50% of 2026 US capacity delayed; FERC/PJM large-load rules     │
├─────────────────────────────────────────────────────────────────────────────┤
│ █ NEW NUCLEAR (SMR/large): 10–15 yr; uprates are the fast path (2028+)      │
│ █ GRID INTERCONNECTION + 765 kV: 5–7 yr; PJM 6.8 GW short at the cap       │
│ █ TRANSFORMERS >160 wks; breakers ~125 wks; prices +~79%: 3–4 yr           │
│ █ FAB + CLEANROOM: caps 2027 WFE (≥$200B)                                   │
│ █ GAS TURBINE SLOTS: into 2029–30 (orders decelerating)                     │
│ █ DRAM/HBM: "sold out to 2029"; HBM binds every year in the AI-2027 model   │
│ █ EUV: the 2027–30 wall (AI 27% → 65% → 77% of the fleet, 2026–29)          │
│ █ InP LASERS / CPO: sold out into 2028–29                                   │
│ █ CoWoS PACKAGING: loosening — no longer the tightest layer                 │
│ █ SCALE-UP INTERCONNECT (AECs, retimers): 80–150% growth                    │
│ █ LIQUID COOLING + 800V DC + SWITCHGEAR: VRT orders >2×; NVT +44% organic   │
│ █ SERVER / RACK INTEGRATION: memory-gated; CLS 2027 outlook $40B           │
│ █ CRITICAL MINERALS (NdPr, Ga/Ge): truce-dependent; Nov 10 lapse            │
└─────────────────────────────────────────────────────────────────────────────┘
```

| Bottleneck layer | Binding severity now | Trend vs May | Key public owners | Owner valuation (Nov 9) | V10.0 coverage |
|---|---|---|---|---|---|
| **Capital / financing** | **Very high (new #1)** | ↑↑ | No clean owner. Beneficiaries are self-funded buyers and suppliers with prepaid customers | META 18.0×, MSFT 22.5×; MU 3.5× | **META 15%** (self-funded buyer); **MU 14%** (LTA/prepay economics); avoid financing-dependent chains (CRWV, ORCL, AMD-OpenAI) |
| **Permission / social license** | **High (new #2)** | ↑↑ | Owners of energized, permitted fleets | NRG ~6× 2027 FCF; VST ~9.7×; TLN ~9×; CEG 20.6× P/E | **NRG 12%, VST 8%** (Texas ≤ 20%) |
| Existing dispatchable generation | High | → | NRG, VST, TLN, CEG | See above | NRG, VST |
| Grid interconnection and transmission | High | ↑ | PWR, MTZ, EME | PWR 27.3× | None (PWR 5.1% expected) |
| Transformers / switchgear / breakers | Very high | ↑ | ETN, NVT, HUBB, GEV, Schneider, ABB | **NVT 16.4×**; ETN 21.8×; GEV 32.1× | **NVT 12%** |
| Gas turbine slots | High (decelerating orders) | ↓ | GEV, Siemens Energy, MHI | GEV 32.1× | None (6.1% expected) |
| Behind-the-meter generation | Medium-high | → | BE; recips (CAT, CMI) | BE 36.4× | None |
| Fab and cleanroom | High | ↑ | TSM; builders; WFE | TSM 16.6× | None (11.8%) |
| EUV lithography | **Very high: the named 2027–30 wall** | ↑↑ | ASML (monopoly) | 23.9× | None (11.0%); exposure via MU |
| Other WFE | Medium-high, cyclical | ↑ 2027 | AMAT, LRCX, KLAC | 18–21× | None |
| **DRAM / HBM** | **Very high; HBM ≈ ⅔ of AI's EUV draw** | ↑↑ | MU, SK hynix (KRX), Samsung | **MU 3.5×** | **MU 14%** |
| NAND / storage | Medium-high | ↑ | SNDK, WDC, STX | 3–8× | None (MU cleaner) |
| **Accelerators / custom silicon** | High | → | NVDA, AVGO, AMD, MRVL, GOOGL TPU | **NVDA 11.2×**; AVGO 16.4×; AMD 28.8× | **NVDA 15%** |
| Optics / InP lasers / CPO | High | ↑ | COHR, LITE, FN | 14–15× (after a +11–17% Nov 9 rebound) | None (≤ 7.7% expected) |
| Scale-up interconnect | High | ↑↑ | CRDO, ALAB, MRVL | 13.7× / 30.6× / 21.0× | None (owner EPS: CRDO 10.3%) |
| Ethernet switching | Medium | → | ANET; NVDA Spectrum-X; AVGO Tomahawk | ANET 31.1× | Via NVDA |
| **Liquid cooling / rack power** | High | ↑ | VRT, NVT, ETN, MOD | **VRT 20.4×**, NVT 16.4×, MOD 11.3× | **VRT 14%, NVT 12%** (MOD gated) |
| **Rack-scale integration** | Medium-high (memory-gated) | ↑ | CLS, DELL, HPE, SMCI | **CLS 10.0×**; DELL 11.4×; HPE 10.0× | **CLS 10%** |
| EDA / IP | Medium (structural) | → | SNPS, CDNS | 25.0× / 34.2× | None (owner basis 2–7%) |
| AI application / platform | Demand side | ↑ | META, MSFT, GOOGL, AMZN | 18–25× | **META 15%** |
| Critical minerals | Medium (latent) | → (Nov 10 lapse) | MP, Lynas, USAR | MP 64× | None (2.3% expected; −95% bust) |
| Nuclear fuel | Medium | → | CCJ, LEU | CCJ 43.8× | None |

**Reading the map:** every physical bottleneck from May still binds, and several (transformers, memory, lasers, cleanrooms) got tighter. Two non-physical layers now decide which physical layers get paid first, which makes **owning a physical bottleneck necessary but no longer sufficient.**

The best positions combine three things:

- a binding physical layer;
- customers who can self-fund, or contracts that pre-fund the supplier;
- a valuation that has already absorbed the financing and permission discount.

The great monopolies (ASML, TSM, SNPS) meet the first two conditions but not the third.

### C. The Zero-Based Ranking (58 stocks, Nov 9 prices)

Bold tickers are V10.0 holdings.

- **Depth:**
    - **Full A1:** fully re-underwritten on the synthesis model.
    - **Screen:** re-priced on the more conservative deep-dive model, with the favorable model's figure as an upper bound. No screen-level name's upper bound reaches the marginal holding.
- **Bust:** every 2030 value at its FY2025-earnings state.
- **Delay:** every 2030 value at its FY2026-earnings state.

| Rank | Ticker | Bottleneck | Price (Nov 9) | Status | Expected CAGR | AI-2027 | 100GW | Bust | Delay | Depth | V9.1 → V10.0 |
|---:|---|---|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | MOD | Thermal (post-spin pure play) | $106.15 | Speculative (post-spin) | 18.7% | 35.5% | 60.6% | -71% | -17% | Full A1 | 0 → **0** (Not added) |
| 2 | **NVDA** | Accelerators / CUDA platform | $178.67 | Attractive | 17.8% | 26.8% | 41.5% | -63% | -20% | Full A1 | 6 → **15** (Increase) |
| 3 | **NRG** | Merchant power + retail (TX/PJM) | $97.40 | Attractive (levered) | 17.1% | 24.9% | 35.6% | -67% | -5% | Full A1 | 0 → **12** (Add) |
| 4 | CRWV | Neocloud GPU capacity | $48.98 | Speculative (financing) | 16.5% | 35.5% | 62.2% | -100% | -100% | Full A1 | 0 → **0** (Not added) |
| 5 | **META** | AI application + ads (buyer) | $641.37 | Attractive | 15.0% | 20.0% | 33.9% | -34% | -21% | Full A1 | 0 → **15** (Add) |
| 6 | **CLS** | Rack-scale integration (EMS/HPS) | $222.92 | Attractive | 14.8% | 23.2% | 35.6% | -75% | -43% | Full A1 | 0 → **10** (Add) |
| 7 | **VRT** | Rack power + liquid cooling | $200.47 | Fair | 13.8% | 22.0% | 34.9% | -72% | -31% | Full A1 | 6 → **14** (Increase) |
| 8 | **NVT** | Electrical distribution + liquid cooling | $114.44 | Attractive | 13.7% | 21.4% | 34.0% | -60% | -24% | Full A1 | 0 → **12** (Add) |
| 9 | **MU** | HBM / DRAM | $733.15 | Deep Discount (cyclical) | 13.1% | 26.8% | 45.3% | -64% | -22% | Full A1 | 6 → **14** (Increase) |
| 10 | **VST** | Merchant power (TX/PJM) | $133.92 | Fair | 13.0% | 20.2% | 26.8% | -67% | -29% | Full A1 | 6 → **8** (Increase) |
| 11 | TLN | Nuclear/gas power (PJM) | $363.13 | Fair | 12.7% | 19.3% | 27.3% | -60% | -35% | Full A1 | 0 → **0** (Not added) |
| 12 | MSFT | AI platform + cloud (buyer) | $545.18 | Fair | 12.3% | 16.7% | 27.1% | -43% | -24% | Full A1 | 0 → **0** (Not added) |
| 13 | TSM | Leading-edge foundry + CoWoS | $388.62 | Fair | 11.8% | 17.9% | 26.6% | -61% | -23% | Full A1 | 11 → **0** (Remove) |
| 14 | AXON | Public-safety platform | $303.18 | Fair | 11.7% | 19.1% | 31.7% | -75% | -75% | Screen (upper 11.7%) | 0 → **0** (Not added) |
| 15 | AVGO | Custom silicon + networking | $319.48 | Fair | 11.6% | 21.4% | 37.6% | -73% | -44% | Full A1 | 3 → **0** (Remove) |
| 16 | RELX | Proprietary data + analytics | $40.02 | Fair | 11.1% | 12.1% | 17.0% | -36% | -4% | Full A1 | 0 → **0** (Not added) |
| 17 | ASML | EUV lithography | $1,513.25 | Fair | 11.0% | 17.5% | 26.5% | -66% | -33% | Full A1 | 8 → **0** (Remove) |
| 18 | VRSK | Proprietary insurance data | $200.60 | Fair | 10.7% | 12.3% | 17.3% | -44% | -24% | Full A1 | 0 → **0** (Not added) |
| 19 | ETN | Electrical equipment | $359.30 | Fair | 10.5% | 14.6% | 20.3% | -46% | -17% | Full A1 | 0 → **0** (Not added) |
| 20 | CRDO | AECs / SerDes | $132.89 | Fair | 10.3% | 19.7% | 36.6% | -71% | -28% | Full A1 | 0 → **0** (Not added) |
| 21 | GOOGL | AI platform + TPU (buyer) | $288.15 | Fair | 9.9% | 19.0% | 35.0% | -64% | -64% | Screen (upper 10.9%) | 0 → **0** (Not added) |
| 22 | HPE | AI servers + networking | $47.54 | Fair | 8.7% | 24.8% | 48.4% | -68% | -68% | Screen (upper 8.7%) | 0 → **0** (Not added) |
| 23 | CEG | Nuclear fleet | $276.09 | Expensive | 8.4% | 12.4% | 18.4% | -60% | -20% | Full A1 | 9 → **0** (Remove) |
| 24 | AMZN | Cloud + Trainium (buyer) | $266.93 | Fair | 8.3% | 17.3% | 32.6% | -69% | -69% | Screen (upper 8.3%) | 0 → **0** (Not added) |
| 25 | FN | Optical contract manufacturing | $365.94 | Fair | 7.7% | 27.1% | 51.6% | -71% | -71% | Screen (upper 7.7%) | 0 → **0** (Not added) |
| 26 | MSI | Public-safety comms | $527.97 | Fair | 7.6% | 11.3% | 18.7% | -52% | -52% | Screen (upper 7.6%) | 0 → **0** (Not added) |
| 27 | SNDK | NAND / enterprise SSD | $886.51 | Deep Discount (cyclical) | 7.1% | 18.6% | 35.0% | -44% | -44% | Screen (upper 9.5%) | 0 → **0** (Not added) |
| 28 | COHR | Optical transceivers / lasers | $225.19 | Expensive (after +17%) | 6.6% | 14.8% | 29.1% | -77% | -38% | Full A1 | 2 → **0** (Remove) |
| 29 | CDNS | EDA | $336.53 | Fair | 6.6% | 12.5% | 21.8% | -32% | -32% | Screen (upper 6.9%) | 0 → **0** (Not added) |
| 30 | GEV | Gas turbines + grid | $829.34 | Fair | 6.1% | 13.8% | 26.5% | -39% | -39% | Screen (upper 6.5%) | 5 → **0** (Remove) |
| 31 | ANET | DC Ethernet fabric | $186.17 | Fair | 6.1% | 16.3% | 31.6% | -47% | -47% | Screen (upper 7.6%) | 4 → **0** (Remove) |
| 32 | IREN | Neocloud / miner | $21.41 | Fair | 5.6% | 32.3% | 61.1% | -100% | -100% | Screen (upper 5.6%) | 0 → **0** (Not added) |
| 33 | DELL | AI servers | $346.31 | Fair | 5.6% | 15.4% | 29.1% | -39% | -39% | Screen (upper 10.2%) | 2 → **0** (Remove) |
| 34 | CORZ | Neocloud hosting | $12.72 | Fair | 5.6% | 28.5% | 53.8% | -100% | -100% | Screen (upper 5.6%) | 0 → **0** (Not added) |
| 35 | KLAC | Process control WFE | $151.38 | Fair | 5.5% | 13.9% | 26.6% | -37% | -37% | Screen (upper 8.3%) | 0 → **0** (Not added) |
| 36 | GEN | Consumer identity | $29.80 | Fair | 5.3% | 5.8% | 8.8% | -53% | -53% | Screen (upper 5.3%) | 0 → **0** (Not added) |
| 37 | PWR | Grid construction | $591.48 | Expensive | 5.1% | 9.9% | 15.6% | -80% | -38% | Full A1 | 4 → **0** (Remove) |
| 38 | AMAT | Deposition WFE | $370.55 | Expensive | 4.6% | 15.4% | 30.2% | -49% | -49% | Screen (upper 6.8%) | 4 → **0** (Remove) |
| 39 | AVAV | Drones / loitering munitions | $126.96 | Expensive | 4.6% | 9.4% | 17.6% | -65% | -65% | Screen (upper 6.3%) | 1 → **0** (Remove) |
| 40 | LITE | Optical components | $596.16 | Expensive | 4.4% | 22.2% | 44.0% | -78% | -78% | Screen (upper 6.2%) | 0 → **0** (Not added) |
| 41 | BNTX | Bio-risk (mRNA + oncology) | $87.51 | Speculative | 4.3% | 4.5% | 4.5% | -49% | -49% | Full A1 | 0 → **0** (Not added) |
| 42 | APLD | Neocloud hosting | $16.72 | Expensive | 3.8% | 28.7% | 54.9% | -100% | -100% | Screen (upper 3.8%) | 0 → **0** (Not added) |
| 43 | LRCX | Etch/dep WFE | $221.31 | Fair | 3.6% | 10.0% | 22.3% | -63% | -27% | Full A1 | 0 → **0** (Not added) |
| 44 | POWL | Switchgear | $141.65 | Expensive | 3.2% | 18.6% | 38.7% | -80% | -80% | Screen (upper 3.2%) | 0 → **0** (Not added) |
| 45 | MP | Rare-earth magnets | $37.75 | Speculative | 2.3% | 9.4% | 19.6% | -95% | -61% | Full A1 | 3 → **0** (Remove) |
| 46 | SNPS | EDA + simulation | $466.97 | Expensive (owner basis) | 2.1% | 6.0% | 11.6% | -66% | -47% | Full A1 | 5 → **0** (Remove) |
| 47 | CCJ | Uranium | $75.37 | Expensive | 2.1% | 11.4% | 28.3% | -81% | -81% | Screen (upper 3.9%) | 2 → **0** (Remove) |
| 48 | PLTR | AI operating software | $169.20 | Expensive | 1.0% | 5.1% | 16.6% | -88% | -88% | Screen (upper 4.4%) | 2 → **0** (Remove) |
| 49 | MRVL | Custom silicon / optics DSP | $154.60 | Expensive | 0.5% | 17.7% | 38.8% | -82% | -82% | Screen (upper 6.3%) | 0 → **0** (Not added) |
| 50 | AMD | Accelerators (#2) | $508.58 | Expensive | -1.6% | 17.8% | 41.7% | -88% | -88% | Screen (upper 2.6%) | 0 → **0** (Not added) |
| 51 | ALAB | PCIe/CXL connectivity | $216.87 | Expensive | -1.6% | 18.1% | 42.1% | -92% | -92% | Screen (upper 11.1%) | 0 → **0** (Not added) |
| 52 | KTOS | AI-enabled defense | $37.69 | Speculative | -2.1% | 2.3% | 7.3% | -93% | -58% | Full A1 | 1 → **0** (Remove) |
| 53 | NBIS | Neocloud | $141.45 | Expensive | -3.6% | 19.6% | 44.0% | -100% | -100% | Screen (upper -3.6%) | 0 → **0** (Not added) |
| 54 | PANW | Security platform | $330.89 | Expensive | -5.6% | -2.0% | 6.6% | -82% | -82% | Screen (upper -5.6%) | 0 → **0** (Not added) |
| 55 | MRNA | mRNA vaccines | $269.00 | Expensive | -7.1% | -9.7% | -9.7% | -98% | -98% | Screen (upper -6.1%) | 1 → **0** (Remove) |
| 56 | BE | Fuel-cell grid bypass | $193.88 | Expensive | -10.5% | 5.7% | 26.5% | -98% | -98% | Screen (upper 7.2%) | 3 → **0** (Remove) |
| 57 | CRWD | AI-native security | $228.58 | Expensive | -12.5% | -9.0% | 0.7% | -93% | -93% | Screen (upper -9.9%) | 3 → **0** (Remove) |
| 58 | INTC | Domestic foundry | $59.37 | Expensive | -15.1% | -2.9% | 15.6% | -90% | -90% | Screen (upper -1.2%) | 3 → **0** (Remove) |

**The zero-based result is V10.0.** The eight holdings are the highest-ranked eligible names after three exceptions:

- MOD (#1) is gated pending its post-spin update.
- CRWV (#4) is excluded because a 40% zero-equity bear gives it a −100% bust.
- NRG (#3) and CLS (#6) are capped by confidence and leverage limits.

Part V shows the construction is not sensitive to the multiple dispute.

### D. Zero-Based vs V9.1: every material difference explained

| Difference | V9.1 | V10.0 | Explanation |
|---|---:|---:|---|
| Accelerators (NVDA + AVGO) | 9% | **15%** (NVDA) | NVDA at 11.2× after +24% revisions is the #2 stock of 58. AVGO's 11.6% after owner EPS (13% stock comp) and a financing reserve for up to ~$43B of guarantee exposure doesn't clear the hurdle |
| Foundry (TSM) | 11% | **0%** | 11.8% expected: an excellent compounder, but the holdings return 13–18% |
| Memory (MU) | 6% | **14%** | 3.5× forward; LTAs with floors through 2030; HBM binding in every modeled year. Highest AI-2027 and 100GW CAGRs in its band |
| WFE + EDA (ASML, AMAT, SNPS) | 17% | **0%** | ASML 11.0% (already at 23.9× for the EUV wall); AMAT 4.6%; SNPS 2.1% once ~31% stock comp is charged |
| Optics + fabric (COHR, ANET) | 6% | **0%** | COHR +17% on Nov 9 to 6.6% expected; ANET 6.1% at 31× |
| Rack thermal + electrical + grid (VRT, GEV, PWR, BE, DELL) | 20% | **26%** (VRT 14, NVT 12) | VRT is a third cheaper than in May with orders >2×; NVT +44% organic at 16.4×. GEV (32×), PWR (27×) and BE are priced for their backlogs |
| Rack integration (CLS) | 0% | **10%** | 10.0× on a $40B 2027 outlook; #6 of 58. Capped for cash conversion (FY26 FCF $460M) |
| Power generation (CEG, VST, CCJ) | 17% | **20%** (NRG 12, VST 8) | NRG (~6× FCF, funded deleveraging) and VST (~9.7×) beat CEG (8.4% after its Nov 9 jump) and CCJ (2.1%). Texas cap 20% |
| Platforms / software (CRWD, PLTR) | 5% | **15%** (META) | CRWD (−12.5%) and PLTR (1.0%) are priced for perfection. META at 18× with +26% growth returns 15.0% with the mildest bust (−34%) |
| Hedges (KTOS, AVAV, MP, MRNA) | 6% | **0%** | Expected −7% to +5%, with 65–98% bust losses. They don't hedge. MRNA's oncology windfall is harvested |
| Domestic foundry (INTC) | 3% | **0%** | Falsifier triggered (no anchor customer); −15.1% expected |
| Holdings count | 24 | **8** | Twenty V9.1 positions fail the hurdle; capital concentrates in the eight winners |

---

## Part IV: Sleeve-by-Sleeve Review, Alternatives, and Forward-Return Analysis

Each V10.0 sleeve is reviewed against V9.1, the new evidence, and at least two alternatives, each ranked **Better / Comparable / Worse** against the holding. Sleeves that go to zero are in IV.B.

### 1. Accelerators — 15% (NVDA) · *NVDA increase 6% → 15%; AVGO remove 3% → 0%*

**NVIDIA (NVDA) — 15% (+9):**

- FQ2 FY27 revenue was $96.2B (+106%) with data center at $89.0B. FQ3 is guided to $108B ±2% at a ~74% gross margin, excluding China data-center revenue. The CFO framed FY28 growth at about 70%, "supply-constrained." `[STALE >30d: Aug 26; FQ3 report ~Nov 17]`
- FY28 (≈CY27) consensus EPS is **$15.92, revised +24% in 90 days**. At $178.67 that is **11.2×**, roughly where NVDA traded in 2022, when consensus expected earnings to fall.
- **Model:** 2030 owner EPS of $19 in the base case. That is only +19% above FY28 consensus, which implies a revenue plateau around $750–850B with share loss to custom ASICs, at an 18× exit (the semis-peer median excluding NVDA is ~18.7×).
    - Expected CAGR: **17.8%**.
    - AI-2027 Scenario: 26.8%. 100GW 2030 Scenario: 41.5%.
    - Bust: −63% (FY2025 EPS of $4.90 at 12.6×).
- **New risk (Nov 8–9): board review of the CEO.** The fundamentals are unaffected so far. The governance and key-person tail is real, and the review touches US–China relations. NVDA stays at the 15% cap (E2), with purchases staged after the Nov 17 report.
- Under Codex's 22× multiple, NVDA returns 23.6%. Either way it's the highest-ranked eligible stock of the 58.

**Broadcom (AVGO) — removed (3% → 0%):**

- AI revenue targets are $115B (FY27) and $230B (FY28) `[STALE >30d]`.
- AVGO has become a financier. The XPV platform with residual-value guarantees carries ~$29B of maximum exposure on the first transaction (10-Q, Sep 10) and ~$43B maximum undiscounted exposure in the Oct 27 8-K (72.5% of remaining lease payments less realized rack value). It is also raising $60B of debt.
- **Owner-basis model:** base 2030 EPS $23.5 (a 47% common margin after ~13% stock comp), 20× (both models agree), a −$8/−$4/−$2/$0 credit reserve per share across the four states, and ~$13 of dividends.
- That gives **11.6%** expected, with a 21.4% AI-2027 Scenario CAGR and 37.6% on the 100GW 2030 Scenario. AVGO is one of the purer thesis bets, but it is 1.4pp below VST, the marginal holding, and its bust is −73%.
- **Re-entry:** below ~$275, or a December report (Dec 9) that discloses limited guarantee exposure with non-Anthropic tenants.

| Alternative | Theme | vs NVDA | Decision |
|---|---|---|---|
| AVGO | Custom silicon + networking | **Worse** (11.6% expected; financing exposure) | Removed |
| AMD | #2 GPU (OpenAI 6 GW) | **Worse** (−1.6% expected on the conservative model, 2.6% favorable; 28.8× after +13% on Nov 9; OpenAI-financing dependence) | No |
| MRVL | Custom silicon + optics DSP | **Worse** (0.5–6.3% expected) | No |
| GOOGL (TPU + Cloud) | Self-funded custom silicon | **Worse** (9.9–10.9%; Continuity overlap) | No |

### 2. HBM / Memory — 14% (MU) · *Increase 6% → 14%*

- FQ4 FY26 revenue was $54.2B with an 87% gross margin. FQ1 FY27 is guided to $61.5B and $38.15 EPS. **26 strategic agreements cover more than 35% of revenue through 2030, most with pricing floors and ceilings.** SK hynix says DRAM and HBM are effectively sold out to 2029. `[STALE >30d: Sep 30; FQ1 report Dec 23]`
- **Why 3.5× forward:** the market prices a classic memory peak. FY27 capex is up ~83%, SK hynix and Samsung are expanding, and CXMT is rising.
- **Value-trap test:**
    - **Passes for 2027–28:** LTAs and prepayments give unusual visibility.
    - **Partly passes for 2029–30:** the AI-2027 compute model makes HBM the **binding input in every year 2024–2030**, and HBM consumes about two-thirds of AI's EUV exposures. Memory supply can't outrun the EUV fleet, and CXMT has no EUV path before the late 2030s.
- **Model (Codex's conceded inputs, adopted on the tie rule):**
    - **Base:** 2030 EPS of $110 (40% below FY27 consensus) at 10×, plus $150/share of explicit net cash after deposit claims, plus dividends.
    - **Bull:** $187.5 at 9× plus $250 of cash.
    - **Bust:** $20 at 11× plus $40 of cash.
    - **Plateau:** $45 at 10.5× plus $90.
- **Results:** expected CAGR 13.1%; **AI-2027 Scenario 26.8% (tied highest in the pool's top 15); 100GW 2030 Scenario 45.3%**; bust −64%.
- **Why 14% when it ranks #9:** inside the 2pp band below VRT, the AI-2027 tie-break goes to MU, and it is the only remaining exposure to the upstream binding constraint (HBM and EUV) after TSM and ASML exit.
- **It is a deliberate cyclical holding, not a compounder.** The Dec 23 report (HBM4 pricing, LTA floors, capex vs FCF) is the first test.

| Alternative | vs MU | Decision |
|---|---|---|
| SNDK (NAND; 8-for-1 split trades from Nov 20) | **Worse** (7.1–9.5%; NAND more commoditized) | No |
| WDC / STX (HDD) | **Worse** (lower bottleneck intensity) | No |
| SK hynix (KRX: 000660) | **Comparable or Better**, but not a US-listed common or ADR | Not investable under the mandate |

### 3. Rack-Scale Integration — 10% (CLS) · *Add 0% → 10%*

- Celestica's Q3 release (Oct 26) set a **2027 outlook of $40B revenue, $21.50 adjusted EPS and a 9% adjusted operating margin**. That is more than double 2025's $12.4B and $6.05.
- The stock is **10.0× forward**, in line with EMS peers (JBL 11.4×, FLEX 10.0×, SANM 9.2×) despite a hyperscaler-ASIC and switch mix those peers don't have.
- **Why it was missed:** my deep dive excluded CLS on an "integrator" label and a cluster cap. Codex was right to include it.
- **Why only 10%:**
    - 2026 FCF guidance was cut to $460M, about 35% of net income.
    - 2027 capex is $1.5–2.0B.
    - A $3.45B equity offering closed Aug 7.
    - Customer concentration is high.
- **Model:** owner EPS of $29.14 in the base (Codex's 6.5% common margin and 145m diluted shares) at 14×. Codex used 16×; both are above the EMS band, so the lower wins.
- **Results:** expected **14.8%**; AI-2027 23.2%; 100GW 35.6%; bust −75%.

| Alternative | vs CLS | Decision |
|---|---|---|
| DELL | **Worse** (5.6–10.2%; neocloud-concentrated backlog; memory-cost squeeze) | Removed |
| HPE | **Worse** (8.7%) | No |
| FN (optical contract manufacturing) | **Worse** (7.7%; +11.9% on Nov 9) | No |
| SMCI | **Worse** (governance; thin margins) | No |

### 4. Thermal and Electrical — 26% (VRT 14%, NVT 12%) · *VRT increase 6% → 14%; NVT add; GEV, PWR, BE remove*

**Vertiv (VRT) — 14% (+8):**

- Q3 net sales were $4.31B (+61%) and organic orders more than doubled. 2026 guidance was raised to about $14.45–14.85B.
- The stock is **−41% since May**, a pure de-rating from ~48× to **20.4× 2027 consensus ($9.84)**.
- **Caveat:** management stopped reporting orders, which removes the earliest demand signal. That is why confidence is 3, not 4.
- **Model:** base 2030 EPS $15.0 at 23×, bull $21.
- **Results:** expected 13.8%; AI-2027 22.0%; 100GW 34.9%; bust −72%.
- Data-center construction delays shift VRT revenue to the right rather than removing it.

**nVent (NVT) — 12% (new):**

- Q3 sales grew **44%, all organic**, and 2026 adjusted EPS guidance is $5.36–5.39. Maverick Power closed Oct 1. Q4 organic growth is guided to 26–29% (Oct 30). 2027 consensus is $7.00, so the stock trades at **16.4×**, against ETN at 21.8× and HUBB at 19.2×.
- NVT is electrical distribution, enclosures and liquid cooling, so the AI exposure is broader than a cooling market-share contest.
- **Model:** base 2030 EPS $10 at 19× (both models' multiples sit inside the 16.4–21.8× band, so the lower wins).
- **Results:** 13.7% expected; AI-2027 21.4%; 100GW 34.0%; bust −60%.
- Integration risk keeps it at 12%.

| Alternative | vs VRT / NVT | Decision |
|---|---|---|
| ETN | **Worse** (10.5%; 21.8× for the same layer; a better-quality fallback if NVT's integration fails) | No |
| GEV | **Worse** (6.1%; 32.1×; gas orders decelerating) | Removed |
| PWR | **Worse** (5.1%; 27.3×) | Removed |
| BE | **Worse** (−10.5% to 7.2%; Oracle→OpenAI financing chain) | Removed |
| **MOD** (post-spin thermal pure play) | **Better on the model** (18.7%, #1 of 58) **but confidence 2** (perimeter changed Oct 1; H1 FCF negative; data-center gross margin fell) | **Gated:** +5% (VRT −3, NVT −2) if the post-spin update confirms margins and cash (E1) |
| POWL, HUBB, Schneider, ABB | **Worse / Comparable** | No |

### 5. Power Generation — 20% (NRG 12%, VST 8%) · *NRG add; VST increase 6% → 8%; CEG, CCJ remove*

**NRG Energy (NRG) — 12% (new):**

- **Q3 (Nov 9):**
    - Adjusted EPS $4.68.
    - 2026 reaffirmed, with EBITDA slightly below the midpoint on weak ERCOT prices.
    - **2027 guidance: EBITDA $5.5–6.0B, FCF before growth $2.9–3.4B, EPS ~$9.05**, all excluding a $4B, 4.9 GW asset sale targeted to close in Q2 2027.
- At $97.40 the stock is **~6× 2027 FCF before growth**, against ~9.7× for VST.
- **Model (EV/EBITDA less net financial claims; sale proceeds spent once):**
    - Base: 2030 EBITDA $6.5B at 7.3× (NRG's own multiple on 2027 guidance; Codex used 8×), with claims falling from ~$22.8B to $14B as FCF and sale proceeds pay down debt, and ~190m shares.
    - Bear probability 30%, for Texas.
- **Results:** expected **17.1%** (#3 of 58); AI-2027 24.9%; 100GW 35.6%; bust −67% (leverage); delay only −5%.
- **Capped at 12%:** leverage, Texas at 51% of Q3 EBITDA, and the unclosed sale.

**Vistra (VST) — 8% (+2):**

- 2027 guidance is EBITDA $7.7–8.5B and FCF before growth $4.3–5.1B, consolidated after the October Cogentrix close. No additional increment is added.
- The stock fell 14% on election day on the Texas moratorium pledge.
- **Model:** base 2030 EBITDA $11B at 8.3× with ~$20B of claims and ~300m shares; bear probability 30%.
- **Results:** 13.0% expected; AI-2027 20.2%; 100GW 26.8%; bust −67%.
- **Sized at 8%** to keep Texas merchant power at 20%.

**Constellation (CEG) — removed (9% → 0%):**

- The thesis is confirmed. Q3 beat and raised (2026 EPS $12.50–12.80), and the DOE loan commitment of up to $5B funds uprates.
- But the stock rose 10.5% on Nov 9 to 20.6× forward, leaving **8.4%** expected. The nuclear premium is priced. NRG captures the same scarcity at a third of the multiple.

| Alternative | vs NRG / VST | Decision |
|---|---|---|
| **TLN** | **Comparable** (12.7%; PJM nuclear/gas; Amazon 1.92 GW) | **The switch:** replaces VST if a Texas moratorium bill clears a chamber (E3). Same 14.9% portfolio expected return |
| CEG | **Worse** (8.4% after its Nov 9 jump) | Removed |
| NEE | **Worse** (renewables-heavy; 19.9×) | No |
| CCJ | **Worse** (2.1%; execution) | Removed |
| OKLO / SMR / LEU | **Worse** (pre-revenue or commodity) | No |

### 6. AI Platform — 15% (META) · *Add 0% → 15%*

- Q3 (Oct 21) revenue grew **26%**. Earnings were hit by a large litigation charge, and capex exceeded quarterly operating cash flow.
- The stock is nearly unchanged since May at **18.0× forward (18.9× the 2027 consensus of $33.97)**, the lowest multiple among the mega-cap platforms (median 22.5×).
- **Why META, in an infrastructure fund:**
    1. It ranks **#5 of 58** on the same model as the hardware names.
    2. Its **bust is the mildest of any top-10 stock (−34%)**. A capex bust cuts META's spending, not its earnings base, so it is the one high-return holding that partly offsets the hardware cluster.
    3. It is the cleanest listed owner of AI *monetization*: ads, agents and assistants on 3B+ users. V7.3 always argued the buildout must ultimately be paid for by applications.
- **Model (Codex's operating inputs; only Codex modeled it):**
    - Base 2030 revenue $400B at a 32% margin → EPS $49.23.
    - Bull $600B at 38% → $87.69.
    - Exit **20×** (in band; Codex used 23×).
    - Bust: FY2025 EPS $29.69, after adding back the one-time $15.93B tax charge.
- **Results:** 15.0% expected; AI-2027 20.0%; 100GW 33.9%; delay −21%.
- **Caveats:**
    - The large bull spread comes from one model.
    - Continuity's FSKAX already holds ~2.5% META.
    - Whether an AI *buyer* belongs in the fund is an owner call (E4). Without META, V10.0 returns 0.4pp less and its bust is 4pp worse.

| Alternative | vs META | Decision |
|---|---|---|
| MSFT | **Worse** (12.3% at 23.5×; Codex's 29× is above band) | No |
| GOOGL | **Worse** (9.9–10.9%; search cannibalization; 2026 EPS inflated by investment gains) | No |
| AMZN | **Worse** (8.3%; capex-heavy, FCF negative) | No |

### IV.B Sleeves and Holdings Taken to Zero (V9.1 → V10.0)

| V9.1 sleeve | Holding (weight) | Expected CAGR (Nov 9) | Verdict | Why (one line) | Re-entry trigger |
|---|---|---:|---|---|---|
| Foundry | TSM (11) | 11.8% | **Remove** | Excellent business; 1.2pp below the marginal holding; Taiwan 2027 window | Below ~$340 (≈14.5× CY27), or CY27 EPS ≥ $26 at the Jan 14 report |
| Lithography | ASML (8) | 11.0% | **Remove** | The EUV wall is priced at 23.9×; exposure kept via MU | Below ~$1,250, or a 2027 guide implying ≥ €60B of sales |
| Custom silicon | AVGO (3) | 11.6% | **Remove** | Financing guarantees (up to ~$43B); 13% stock comp | Below ~$275, or Dec 9 disclosure of limited guarantee exposure |
| EDA | SNPS (5) | 2.1% | **Remove** | Stock comp is ~31% of adjusted EPS; 25× forward | Owner-EPS margin ≥ 28% |
| WFE | AMAT (4) | 4.6% | **Remove** | China rules; cyclical crest | Below ~$270 |
| Fabric | ANET (4) | 6.1% | **Remove** | 31× forward | Below ~$130 |
| Optics | COHR (2) | 6.6% | **Remove** | +16.8% on Nov 9; negative operating cash flow | Below ~$170, with two quarters of positive operating cash flow |
| Rack integration | DELL (2) | 5.6% | **Remove** | Neocloud-concentrated backlog; memory squeeze | AI server gross margin > 13% with a hyperscaler-majority backlog |
| Electrical | GEV (5) | 6.1% | **Remove** | 32× forward; gas orders decelerating | Below ~$650 |
| Grid | PWR (4) | 5.1% | **Remove** | 27× forward | 765 kV awards push backlog > $80B at ≤ 22× |
| Grid-bypass | BE (3) | −10.5% to 7.2% | **Remove** | Oracle→OpenAI financing chain | A non-Oracle hyperscaler order ≥ 500 MW plus backlog disclosure |
| Power | CEG (9) | 8.4% | **Remove** | Nuclear premium priced (20.6×) | Below ~$220, or 2027 EPS ≥ $15 |
| Nuclear fuel | CCJ (2) | 2.1% | **Remove** | Execution miss; 44× forward | Westinghouse IPO valuing the stake ≥ market cap ex-uranium |
| Security | CRWD (3) | −12.5% | **Remove** | 142× forward | Below ~$150 with NNARR growth ≥ 25% |
| Operate & control | PLTR (2) | 1.0% | **Remove** | 67× forward | Below ~$110 |
| Defense | KTOS (1), AVAV (1) | −2.1%, 4.6% | **Remove** | KTOS: cash-consuming production (FY26 FCF use $110–120M), 22% stock comp. AVAV: restatement | KTOS: positive owner FCF for two quarters |
| Materials | MP (3) | 2.3% | **Remove** | Owner economics weak; −95% bust; the Nov 10 rare-earth lapse is a binary event, not a hedge at this price | Below ~$25, or a reimposed China control regime with DoD offtake expansion |
| Bio-risk | MRNA (1) | −7.1% | **Remove** | Priced as an oncology success | n/a |
| Domestic foundry | INTC (3) | −15.1% | **Remove** | Falsifier triggered | A named 14A/18A-P volume commitment from Apple, NVIDIA or a hyperscaler |

**Hedges were reconsidered and rejected on evidence, not neglected.** BNTX, the strongest hedge candidate, returns 4.3% once cash is valued *after* four years of burn (€16.2B today, continuing losses). It loses 49% in its own bear. KTOS and MP lose 93–95% in a bust. META's −34% bust gives V10.0 more downside protection than any of the hedges did.

### IV.C Cross-Sleeve Candidate Evaluation

| Ticker | Candidate theme | Why considered | Better/Comparable/Worse | Add? (Y/N) | Why / why not |
|---|---|---|---|---|---|
| **META** | AI monetization platform | 18× forward, +26% growth | **Better** (vs CRWD/PLTR software) | **Y (15%)** | #5 of 58; mildest top-10 bust |
| **NRG** | Merchant power + retail | ~6× FCF; asset-sale deleveraging | **Better** (vs CEG) | **Y (12%)** | #3 of 58 |
| **NVT** | Electrical + liquid cooling | +44% organic at 16.4× | **Better** (vs GEV/ETN) | **Y (12%)** | 13.7% vs 6.1%/10.5% |
| **CLS** | Rack-scale integration | 10× on a $40B 2027 outlook | **Better** (vs DELL) | **Y (10%)** | 14.8% vs 5.6% |
| MOD | Thermal pure play (post-spin) | #1 of 58 on the model | Better (model) / lower confidence | **Gated** | E1 |
| CRWV | Neocloud | 16.5% expected | Worse (risk) | N | −100% bust; financing |
| TLN | Nuclear/gas IPP (PJM) | 12.7% | Comparable (vs VST) | N (switch) | Texas switch candidate |
| MSFT | Platform | 12.3% | Worse (vs META) | N | Multiple above band |
| TSM | Foundry | 11.8% | Worse | N (removed) | Below the hurdle |
| AVGO | Custom silicon | 11.6% | Worse | N (removed) | Financing guarantees |
| RELX / VRSK | Proprietary data | 11.1% / 10.7% at peer multiples | Worse | N | Codex's 15% VRSK add needs 28× (own 23.0×) |
| ASML | EUV | 11.0% | Worse | N (removed) | Priced |
| ETN | Electrical | 10.5% | Worse (vs NVT) | N | 21.8× |
| CRDO / ALAB | Scale-up interconnect | 10.3% / −1.6% to 11.1% (owner EPS) | Worse | N | Stock comp 19–22% of adjusted EPS |
| GOOGL / AMZN | Platforms | 9.9% / 8.3% | Worse | N | Continuity overlap; capex |
| HPE / DELL / FN | Servers / optical contract manufacturing | 5.6–10.2% | Worse | N | |
| CEG | Nuclear | 8.4% | Worse | N (removed) | |
| SNDK | NAND | 7.1–9.5% | Worse (vs MU) | N | |
| COHR / LITE / ANET | Optics / switching | 4.4–7.6% | Worse | N | Nov 9 rebound priced them |
| MSI / AXON / GEN / PANW / CRWD / PLTR | Software / public safety / security | −12.5% to 11.7% | Worse | N | Priced or weak owner economics (AXON stock comp 84% of adjusted EPS) |
| GEV / PWR / POWL / BE | Grid / turbines / BTM | −10.5% to 7.2% | Worse | N | Priced for backlog |
| LRCX / KLAC / AMAT / CDNS / SNPS / INTC | Tools / EDA / domestic foundry | −15.1% to 8.3% | Worse | N | |
| IREN / CORZ / APLD / NBIS | Neoclouds | −3.6% to 5.6% | Worse | N | Zero-equity bears; Moonshot 0% |
| KTOS / AVAV / MP / MRNA / BNTX / CCJ | Hedges / fuel | −7.1% to 4.6% | Worse | N | They don't hedge at these prices |
| SPY / QQQ / SMH / SOXX / XLU / ITA / IBB | ETF fallbacks | Benchmarks | Worse | N | Direct holdings dominate; emergency parking only |

### IV.D Forward-Return and Valuation Table (every V10.0 holding)

Prices are the Nov 9, 2026 close. TV = value per share at Dec 31, 2030, including cumulative dividends and explicit cash or reserves. The bear TV is the 50/50 average of the bust and plateau states.

| Ticker | Current Price + Date (Nov 9, 2026) | Valuation Status | Bear / Base / Bull Terminal Value | Scenario Probabilities | Expected Terminal Value | Implied Expected CAGR | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Confidence | Key Assumptions |
|---|---|---|---|---|---:|---:|---:|---:|:---:|---|
| NVDA | $178.67 | Attractive | $104 / $347 / $611 | 25/50/25 | $352 | **17.8%** | 26.8% | 41.5% | 4 | Owner EPS $19, 18× exit; ASIC share loss |
| META | $641.37 | Attractive | $464 / $995 / $2,117 | 25/50/25 | $1,142 | **15.0%** | 20.0% | 33.9% | 3 | EPS $49 (revenue $400B, 32% margin), 20× |
| VRT | $200.47 | Fair | $97 / $347 / $582 | 25/50/25 | $343 | **13.8%** | 22.0% | 34.9% | 3 | EPS $15, 23×; orders >2× |
| MU | $733.15 | Deep Discount (cyclic.) | $416 / $1,258 / $1,950 | 25/50/25 | $1,220 | **13.1%** | **26.8%** | **45.3%** | 3 | EPS $110 + $150 cash, 10×; LTAs |
| NRG | $97.40 | Attractive (lev.) | $62 / $185 / $341 | 30/45/25 | $187 | **17.1%** | 24.9% | 35.6% | 3 | EBITDA $6.5B, 7.3×; claims $22.8B → $14B |
| NVT | $114.44 | Attractive | $66 / $194 / $324 | 25/50/25 | $195 | **13.7%** | 21.4% | 34.0% | 3 | EPS $10, 19×; +44% organic |
| CLS | $222.92 | Attractive | $92 / $408 / $672 | 25/50/25 | $395 | **14.8%** | 23.2% | 35.6% | 3 | EPS $29 (6.5% margin), 14× |
| VST | $133.92 | Fair | $69 / $243 / $368 | 30/45/25 | $222 | **13.0%** | 20.2% | 26.8% | 3 | EBITDA $11B, 8.3×; claims $20B |

**Detailed assumptions behind the table** (bear TV = ½ bust + ½ plateau):

| Ticker | 2030 states: bust / plateau / base / bull | Exit multiple (bust / plateau / base / bull) | Cumulative dividends; cash or reserve | Anchor and notes |
|---|---|---|---|---|
| NVDA | Owner EPS $4.90 / $9.03 / $19 / $28 | 12.6 / 15.3 / 18 / 21.6× | ~$5 | FY28E $15.92 (11.2×). Base = revenue plateau ~$750–850B with ASIC share loss. Bust TV $66, plateau $142 |
| META | EPS $29.69 / $29.12 / $49.23 / $87.69 | 14 / 17 / 20 / 24× | ~$10 | 2027E $33.97 (18.9×). Bust EPS adds back the 2025 one-time tax charge. Bust TV $424, plateau $504 |
| VRT | EPS $3.41 / $7.05 / $15 / $21 | 16.1 / 19.6 / 23 / 27.6× | ~$1.5 | 2027E $9.84 (20.4×). Bust TV $56, plateau $139 |
| MU | EPS $20 / $45 / $110 / $187.5 | 11 / 10.5 / 10 / 9× (inverse-cyclical) | Dividends ~$8; net cash $40 / $90 / $150 / $250 | FY28E $207.76 (3.5×). Shares fixed (cash not spent twice). Bust TV $264, plateau $569 |
| NRG | EBITDA $4.0 / $5.0 / $6.5 / $8.5B | EV/EBITDA 6.0 / 6.75 / 7.3 / 8.3× | Dividends $8–10; net claims $19 / $17 / $14 / $11B; shares 210 / 200 / 190 / 180m | 2027 FCF before growth $2.9–3.4B (~6×). $4B sale proceeds to debt. Bust TV $32, plateau $92 |
| NVT | EPS $3.22 / $5.16 / $10 / $14 | 13.3 / 16.2 / 19 / 22.8× | ~$4 | 2027E $7.00 (16.4×). Q4 organic 26–29%. Bust TV $46, plateau $87 |
| CLS | Owner EPS $5.63 / $10.75 / $29.14 / $40 | 9.8 / 11.9 / 14 / 16.8× | — | 2027 outlook $40B / $21.50. 145m diluted shares. Bust TV $55, plateau $128 |
| VST | EBITDA $6 / $7 / $11 / $13B | EV/EBITDA 6.6 / 7.4 / 8.3 / 9.3× | Dividends $4–6; net claims $26 / $23 / $20 / $16B; shares 340 / 320 / 300 / 290m | 2027 EBITDA $7.7–8.5B. Bust TV $44, plateau $95 |

**Portfolio:** weighted expected terminal multiple **1.78×**, which gives **14.9% expected CAGR**. It is computed from expected terminal value, not by averaging CAGRs.

**Named-scenario flags (PROMPT_1):**

- **Purest thesis bets** (named-scenario CAGR far above expected):
    - **MU:** 13.1% expected → 26.8% AI-2027 / 45.3% 100GW.
    - **AVGO:** 11.6% → 21.4% / 37.6%.
    - **CRDO:** 10.3% → 19.7% / 36.6%.
    - **MOD:** 18.7% → 35.5% / 60.6%.
    - **Optics** (FN 7.7% → 27.1% / 51.6%; LITE 4.4% → 22.2% / 44.0%).
    - **Neoclouds** (CRWV 16.5% → 35.5% / 62.2%).

    MU is the only one held. MOD is gated. The rest fail on expected return or bust.
- **Modest even on the strong path** (priced in, or can't capture the upside):
    - **CEG:** 12.4% AI-2027 / 18.4% 100GW. Nuclear scarcity is already in the price.
    - **ETN:** 14.6% / 20.3%.
    - **PWR:** 9.9% / 15.6%.
    - **SNPS:** 6.0% / 11.6%.
    - **RELX and VRSK:** ~12% / ~17%. Data businesses don't scale with capex.
    - **BNTX:** 4.5%.
    - **KTOS:** 2.3% / 7.3%.

    None of these is held.

**Discount diagnosis (temporary / structural / value trap):**

| Name | Discount | Cause | Classification | What closes it | What invalidates it |
|---|---|---|---|---|---|
| NVDA | Forward P/E ~25× (May) → 11.2× | Financing fears; circularity; new CEO probe | **Temporary**, if FY28 holds | Nov 17 report; board review outcome; OpenAI refinancing | FY28 growth guided below 40%; CEO departure with a strategy break; top-customer order cuts |
| MU | 3.5× forward | Peak-cycle fear | **Partly structural (cyclical)** | LTAs extended to 2029–30 at higher prices (Dec 23) | DRAM contract prices down two quarters running; gross margin below 75% |
| NRG | ~6× FCF | Retail/gas mix; leverage; Texas | **Temporary** if the sale closes | Sale close (Q2 2027); debt paydown; buybacks | Failed sale; Texas moratorium becomes law; ERCOT forwards −25% |
| CLS | 10× forward | Cash conversion; customer concentration | **Temporary** if 2027 converts | Q4 FCF (Jan); 2027 capex funded without equity | Another equity raise; top-customer loss |
| VRT | ~48× → 20.4× | Valuation reset; order-disclosure stop | **Temporary** | 2027 guidance (Feb) | 2027 revenue guide < +15% |
| META | 18× (lowest mega-cap) | Capex > OCF; litigation | **Temporary** | Ad growth sustained with capex discipline | Ad growth < 10%; dilutive capex without returns |
| INTC, AVAV, CCJ | −39% to −55% | Thesis or execution failure | **Value trap / company-specific** | — | — |

---

## Part V: Portfolio Architecture Comparison and Cross-Portfolio Capital Competition

### A. Three Architectures, Same Valuation Model (Nov 9 prices)

- **(1a) Current diversified bottleneck architecture:** V9.1 weights as held.
- **(1b) Diversified bottleneck, rebuilt:** 16 names, at least one per bottleneck, using the synthesis model's best name in each:
    - NVDA 10, AVGO 6, TSM 7, MU 8, ASML 5, CLS 5;
    - VRT 8, NVT 7, ETN 3;
    - NRG 8, VST 5, TLN 5;
    - META 8, MSFT 4, RELX 4, VRSK 7.
- **(2) Concentrated highest-conviction:** 7 names at the 15% cap with no confidence caps: NVDA 15, META 15, NRG 15, CLS 15, VRT 15, NVT 15, MU 10.
- **(3) Core-and-satellite (V10.0):**
    - **Core:** NVDA 15, META 15, VRT 14, MU 14, NRG 12, NVT 12.
    - **Satellites:** CLS 10 and VST 8, each capped for a named risk.

| Metric (to Dec 31, 2030) | (1a) V9.1 as held | (1b) Diversified, rebuilt | (2) Concentrated | **(3) Core-and-satellite (V10.0)** |
|---|---:|---:|---:|---:|
| Holdings | 24 | 16 | 7 | **8** |
| **Expected CAGR** | 7.8% | 13.6% | **15.2%** | **14.9%** |
| Expected total return | +36% | +70% | +79% | **+78%** |
| **AI-2027 Scenario CAGR** (faster AI) | 15.5% | 20.9% | 23.5% | **23.4%** |
| **100GW 2030 Scenario CAGR** | 27.2% | 32.8% | 37.0% | **36.9%** |
| **2–3 year AI delay** (plateau state) | −41.4% | −24.6% | −23.9% | **−23.9%** |
| **AI-capex bust** (every holding at its bust state) | −67.3% | **−59.2%** | −62.2% | −61.8% |
| Expected CAGR on Codex's multiples | 9.0% | 16.5% | 18.6% | 18.2% |
| Largest name / top-3 | 11% / 28% | 10% / 26% | 15% / 45% | 15% / 44% |
| HHI | 0.057 | 0.068 | 0.145 | 0.129 |
| Clusters (C1 / C2 / C3 / C4 / C5) | 34 / 20 / 18 / 17 / 5 (+C6 6) | 36 / 5 / 18 / 18 / 23 | 40 / 0 / 30 / 15 / 15 | 39 / 0 / 26 / 20 / 15 |
| Weighted confidence | ~3.0 | ~3.4 | ~3.2 | ~3.1 |
| Major opportunity cost | Twenty names below the hurdle; three thesis failures; the most expensive software | 1.3pp of expected return a year to save 2.6pp of bust loss; includes eight names at 10.5–11.8% | CLS and NRG at 15% despite cash-conversion and leverage flags | 0.3pp of expected return a year vs (2) |

### B. Verdict: Core-and-Satellite (V10.0)

- **V9.1 is dominated on every metric.** Its 24-name diversification didn't reduce the bust loss (−67%), because its most expensive names are the ones that fall furthest.
- **The rebuilt diversified portfolio** buys 2.6pp less bust loss for 1.3pp a year less expected return, about 9pp less cumulative return over four years. Under a goal that treats losses as a constraint, not the objective, that's poor value. The bust remains about −59% either way, so this diversification doesn't actually remove the risk.
- **The concentrated portfolio** adds 0.3pp a year, less than the model's ±2pp error band. It does so by putting the two lowest-confidence high-ranked names (CLS with weak cash conversion; NRG with ~$22.8B of claims) at the full 15%. That extra exposure is model-dependent, and both deep dives independently capped these names below 15%.
- **V10.0** captures 98% of the concentrated portfolio's expected return. It has the same or better delay and bust outcomes and caps the two most estimate-sensitive names.

**Is eight holdings right?** Yes. Twenty V9.1 positions return below the hurdle, so the fund was over-diversified into weak returns, not under-diversified. Fewer than seven would push names past the 15% cap or past their confidence limits. More than about ten adds names expected at 10.5–11.8% that don't reduce the bust.

**Governance for the two satellites (CLS, VST):**

- A 10% maximum.
- Exit if the thesis fails one quarterly check.
- Promotion to core needs two consecutive quarters of confirmation and a valuation still above the hurdle.

### C. Cross-Portfolio Capital Competition (every V10.0 position)

| Ticker | Weight | Expected CAGR | Next-best alternative for this capital | Expected-return advantage | If removed, capital goes to |
|---|---:|---:|---|---|---|
| NVDA | 15% | 17.8% | AVGO (11.6%) in the same layer; TLN (12.7%) overall | +6.2pp vs AVGO; +5.1pp vs TLN | TLN, then TSM |
| META | 15% | 15.0% | MSFT (12.3%) | +2.7pp, with a milder bust (−34% vs −43%) | TLN 8 + TSM 7 (portfolio −0.4pp; bust −4pp) |
| VRT | 14% | 13.8% | ETN (10.5%); MOD (gated) | +3.3pp vs ETN | NVT (to its 12% cap), then ETN |
| MU | 14% | 13.1% | TSM (11.8%) upstream; SNDK (7.1–9.5%) in memory | +1.3pp and **+8.9pp on AI-2027** vs TSM | TSM, then AVGO |
| NRG | 12% | 17.1% | TLN (12.7%); CEG (8.4%) | +4.4pp vs TLN | TLN (keeps the Texas cap) |
| NVT | 12% | 13.7% | ETN (10.5%) | +3.2pp | ETN, or VRT to 15% |
| CLS | 10% | 14.8% | HPE (8.7%); DELL (5.6%) | +6.1pp vs HPE | MU, then VRT |
| VST | 8% | 13.0% | TLN (12.7%) | +0.3pp; +0.9pp on AI-2027 | TLN (automatic on a Texas trigger) |

**The explicit price of risk control:** caps hold NRG (17.1%) and CLS (14.8%) below names that rank lower (VRT, NVT, MU, VST). Removing the caps (architecture 2) would add 0.3pp a year. **That trade is declined deliberately.**

### D. Three-Fund Architecture Check

- **Foundation Liquidity (SPAXX):** unchanged.
- **Continuity Fund (~50% target; FSKAX 80% / FTIHX 20% in tax-advantaged accounts):** unchanged.
    - It already holds about 2.5% META, 6% NVDA and smaller VRT/MU/VST/NRG weights through the total-market index.
    - V10.0 raises household META exposure to roughly 8.5% of total investments (about 7.5% through Event Horizon plus ~1.0% through Continuity). That is acceptable for a top-5 ranked name with the portfolio's mildest bust (E4).
- **Event Horizon (~50% target):**
    - After −12.3% against a roughly flat Continuity Fund since May, Event Horizon is about 46–47% of investments.
    - **Direct new contributions to Event Horizon until it is back at 50%.** That buys compressed valuations without selling tax-advantaged Continuity holdings.
    - Rebalance if Event Horizon exceeds 55%.

---

## Part VI: Final Allocation + Checksum (100.0%)

### A. Final Event Horizon Fund Allocation: **V10.0 (proposed)**

| Sleeve | Ticker | V9.1 (May 10) | **V10.0** | Delta | Role | Rationale |
|---|---|---:|---:|---:|---|---|
| **Accelerators** | NVDA | 6% | **15%** | +9 | Core | #2 of 58; 11.2× FY28E after +24% revisions |
| **AI Platform** | META | 0% | **15%** | +15 | Core (**NEW**) | #5 of 58; mildest top-10 bust; 18× |
| **Rack Thermal & Power** | VRT | 6% | **14%** | +8 | Core | Orders >2×; 20.4× after a 41% de-rating |
| **HBM / Memory** | MU | 6% | **14%** | +8 | Core | 3.5×; HBM binding; highest AI-2027/100GW CAGRs in its band |
| **Power Generation** | NRG | 0% | **12%** | +12 | Core (**NEW**) | #3 of 58; ~6× FCF; capped for leverage and Texas |
| | VST | 6% | **8%** | +2 | Satellite | Fills the 20% Texas cap; TLN is the switch |
| **Electrical Distribution & Cooling** | NVT | 0% | **12%** | +12 | Core (**NEW**) | +44% organic at 16.4× |
| **Rack-Scale Integration** | CLS | 0% | **10%** | +10 | Satellite (**NEW**) | 10× on a $40B 2027 outlook; capped for cash conversion |
| Foundry | TSM | 11% | **0%** | −11 | — | 11.8% expected |
| Custom silicon | AVGO | 3% | **0%** | −3 | — | 11.6%; financing guarantees |
| Lithography | ASML | 8% | **0%** | −8 | — | 11.0%; EUV wall priced |
| WFE | AMAT | 4% | **0%** | −4 | — | 4.6% |
| EDA | SNPS | 5% | **0%** | −5 | — | 2.1% on owner EPS |
| Fabric | ANET | 4% | **0%** | −4 | — | 6.1% |
| Optics | COHR | 2% | **0%** | −2 | — | 6.6% after +17% |
| Rack integration | DELL | 2% | **0%** | −2 | — | 5.6% |
| Power | CEG | 9% | **0%** | −9 | — | 8.4% after +10.5% |
| Grid | PWR | 4% | **0%** | −4 | — | 5.1% |
| Electrical equipment | GEV | 5% | **0%** | −5 | — | 6.1% |
| Nuclear fuel | CCJ | 2% | **0%** | −2 | — | 2.1% |
| Grid-bypass | BE | 3% | **0%** | −3 | — | Negative to 7.2% |
| Security | CRWD | 3% | **0%** | −3 | — | −12.5% |
| Operate & control | PLTR | 2% | **0%** | −2 | — | 1.0% |
| Defense | AVAV / KTOS | 1% / 1% | **0% / 0%** | −1 / −1 | — | 4.6% / −2.1% |
| Bio-risk | MRNA | 1% | **0%** | −1 | — | −7.1% |
| Materials | MP | 3% | **0%** | −3 | — | 2.3% |
| Domestic foundry | INTC | 3% | **0%** | −3 | — | −15.1% |
| **Moonshot** | — | 0% | **0%** | 0 | — | Neocloud equity carries zero-equity bears |
| **Total** | | **100%** | **100%** | **0** | 8 holdings | **Checksum ✓** |

**V10.0 checksum:** `NVDA 15 + META 15 + VRT 14 + MU 14 + NRG 12 + NVT 12 + CLS 10 + VST 8 = 100.0%` ✓

**Delta checksum:**

- **Increases:** NVDA +9, META +15, VRT +8, MU +8, NRG +12, NVT +12, CLS +10, VST +2 = **+76**.
- **Decreases:** TSM −11, AVGO −3, ASML −8, AMAT −4, SNPS −5, ANET −4, COHR −2, DELL −2, CEG −9, PWR −4, GEV −5, CCJ −2, BE −3, CRWD −3, PLTR −2, AVAV −1, KTOS −1, MRNA −1, MP −3, INTC −3 = **−76**.

Increases equal decreases ✓.

**Cluster rollup:**

| Cluster | Holdings | Weight |
|---|---|---:|
| C1 AI silicon, memory and integration | NVDA, MU, CLS | 39% |
| C3 Data-center physical and electrical | VRT, NVT | 26% |
| C4 Power generation | NRG, VST | 20% (all Texas-exposed; cap 20%) |
| C5 AI platform | META | 15% |
| C2 Fab tools and design / C6 hedges | — | 0% |

### B. Change Table (From → To, with specific funding sources)

| Ticker | From | To | Delta | Funding source (specific) | Why |
|---|---:|---:|---:|---|---|
| NVDA | 6% | 15% | **+9** | TSM −9 | The compute layer moves from the foundry (11.8%) to the accelerator (17.8%) |
| META | 0% | 15% | **+15** | CRWD −3, PLTR −2, INTC −3, AVGO −3, TSM −2, MRNA −1, AVAV −1 | Expensive software, failed options and a financing-exposed supplier rotate into the cheapest platform |
| MU | 6% | 14% | **+8** | ASML −8 | The EUV/HBM constraint is owned more cheaply through memory: 13.1% (26.8% AI-2027) vs 11.0% |
| VRT | 6% | 14% | **+8** | ANET −4, DELL −2, COHR −2 | Fabric, server and optics capital moves to the de-rated thermal leader |
| NRG | 0% | 12% | **+12** | CEG −9, CCJ −2, KTOS −1 | The nuclear premium and fuel move to cash-yielding generation and retail |
| NVT | 0% | 12% | **+12** | GEV −5, PWR −4, BE −3 | Expensive turbine, grid and behind-the-meter names move to the cheap electrical grower |
| CLS | 0% | 10% | **+10** | SNPS −5, AMAT −4, MP −1 | Design and tool capital moves to the integrator at 10× |
| VST | 6% | 8% | **+2** | MP −2 | Materials hedge into Texas-capped generation |
| **Totals** | | | **+76 / −76** | **Every add has a named funding source** ✓ | |

**Against drifted holdings:** if V9.1 was held from May without rebalancing, the Nov 9 weights have drifted. Examples: CRWD ~5.6%, ANET ~5.6%, MRNA ~5.3%, NVDA ~5.3%, VRT ~3.8%. Moving to V10.0 from those weights turns over about **79%** of the sleeve. The trade-by-trade plan is in the Deployment Strategy file.

### C. Per-Ticker Decision Framework (every ticker)

| Ticker | Current % (V9.1) | Recommended % | Action | Confidence (1-5) | Why | What would falsify this |
|---|---:|---:|---|:---:|---|---|
| NVDA | 6 | **15** | **Increase** | 4 | 11.2× FY28E; 17.8% expected; #2 of 58 | Nov 17 guide implies FY28 growth < 40%; the board review ends in Huang's departure with a strategy break or evidence of IP/security compromise; top-customer order cuts |
| META | 0 | **15** | **Add** | 3 | 18× with +26% growth; 15.0%; −34% bust | Ad growth < 10% for two quarters; 2027 capex guide > operating cash flow without revenue acceleration; adverse litigation over $20B |
| VRT | 6 | **14** | **Increase** | 3 | Q3 +61%, orders >2×; 20.4×; 13.8% | 2027 revenue guide < +15%; hyperscaler in-house cooling wins; gross margin < 33% |
| MU | 6 | **14** | **Increase** | 3 | 3.5×; LTAs with floors; HBM binding; AI-2027 26.8% | DRAM contract prices fall two quarters running; gross margin < 75%; LTA renegotiation; FY27 capex > 50% of operating cash flow without HBM share gains |
| NRG | 0 | **12** | **Add** | 3 | ~6× FCF; 17.1%; funded deleveraging | Asset sale fails or is re-cut below $3.5B; 2027 FCF guide cut > 10%; a Texas moratorium becomes law; net claims rise |
| NVT | 0 | **12** | **Add** | 3 | +44% organic at 16.4×; 13.7% | Organic growth < 10% in 2027 guidance; leverage > 3× for a year; Maverick margin dilution |
| CLS | 0 | **10** | **Add** | 3 | 10× a $40B 2027 outlook; 14.8% | Another equity raise; Q4 FCF below plan; loss of a top-2 customer program |
| VST | 6 | **8** | **Increase** | 3 | 2027 FCF ~$13.8/share (~9.7×); 13.0% | A Texas moratorium bill clears a chamber (switch to TLN); ERCOT 2027 forwards −25%; FCF guide cut |
| TSM | 11 | **0** | **Remove** | 4 | 11.8%: below the hurdle, not broken | *Re-enter:* < ~$340, or CY27 EPS ≥ $26 at the Jan 14 report |
| ASML | 8 | **0** | **Remove** | 3 | 11.0%; EUV wall priced at 23.9× | *Re-enter:* < ~$1,250, or a 2027 sales guide ≥ €60B |
| AVGO | 3 | **0** | **Remove** | 3 | 11.6%; guarantees up to ~$43B; 13% stock comp | *Re-enter:* < ~$275, or limited guarantee exposure disclosed Dec 9 |
| SNPS | 5 | **0** | **Remove** | 4 | 2.1% on owner EPS | Owner margin ≥ 28% |
| AMAT | 4 | **0** | **Remove** | 3 | 4.6%; China rules | < ~$270 |
| ANET | 4 | **0** | **Remove** | 3 | 6.1% at 31× | < ~$130 |
| COHR | 2 | **0** | **Remove** | 3 | 6.6% after +17%; negative operating cash flow | < ~$170 plus two quarters of positive operating cash flow |
| DELL | 2 | **0** | **Remove** | 3 | 5.6% | AI server gross margin > 13% with a hyperscaler-majority backlog |
| CEG | 9 | **0** | **Remove** | 3 | 8.4% after +10.5% | < ~$220, or 2027 EPS ≥ $15 |
| PWR | 4 | **0** | **Remove** | 3 | 5.1% at 27× | 765 kV awards push backlog > $80B at ≤ 22× |
| GEV | 5 | **0** | **Remove** | 3 | 6.1% at 32× | < ~$650, or a firm gas-order re-acceleration |
| CCJ | 2 | **0** | **Remove** | 3 | 2.1% | Westinghouse IPO value ≥ market cap ex-uranium |
| BE | 3 | **0** | **Remove** | 3 | Negative to 7.2% | A non-Oracle hyperscaler order ≥ 500 MW plus backlog disclosure |
| CRWD | 3 | **0** | **Remove** | 4 | −12.5% at 142× | < ~$150 with NNARR growth ≥ 25% |
| PLTR | 2 | **0** | **Remove** | 4 | 1.0% at 67× | < ~$110 |
| AVAV | 1 | **0** | **Remove** | 4 | Restatement; 4.6% | Clean audit plus a program-of-record win |
| KTOS | 1 | **0** | **Remove** | 3 | −2.1% on owner EPS | Two quarters of positive owner FCF |
| MRNA | 1 | **0** | **Remove** | 4 | −7.1%; priced as an oncology success | n/a |
| MP | 3 | **0** | **Remove** | 3 | 2.3%; −95% bust | < ~$25, or reimposed China controls plus DoD offtake expansion |
| INTC | 3 | **0** | **Remove** | 4 | −15.1%; falsifier triggered | A named 14A/18A-P volume customer |
| MOD | 0 | **0 (gated → 5)** | **Gate** | 2 | #1 of 58 (18.7%), but the post-spin perimeter is unproven | *Add 5%* if the post-spin update shows a stable data-center gross margin, positive H2 FCF guidance and FY28 targets ≥ $8.8 EPS |
| TLN | 0 | **0 (switch)** | **Watch** | 3 | 12.7%; PJM diversification | *Replaces VST* if a Texas moratorium bill clears a chamber |
| Moonshot | 0 | **0** | **Keep** | 5 | No options/LEAPS; neocloud equity carries zero-equity bears | User instruction to reactivate |

---

## Part VII: Risk, Scenario, and Invalidation Dashboard

### A. Scenario Lens (V10.0 vs V9.1, to Dec 31, 2030)

| Scenario | Description | Probability | V10.0 | V9.1 |
|---|---|---:|---|---|
| **100GW 2030 path** | One ~100 GW training cluster; ~$8T/yr of AI investment; AI power ≈ US electricity | 10% (inside the bull) | **+267% (36.9%/yr)** | +171% (27.2%/yr) |
| **AI-2027 path** | AI-2040's $2.4T of capex in 2028 → ~$4.2T in 2030; automated coder 2027–29 | 35% (base-to-bull) | **+139% (23.4%/yr)** | +82% (15.5%/yr) |
| **Bull bucket** | 2030 capex ~$4.5T | 25% | Each holding at its bull value | — |
| **Base** | 2030 capex ~$2.8T; HBM ~$165B; ~150 GW of AI power | 50% | **+77% (14.7%/yr)** | +39% (8.3%/yr) |
| **Plateau / 2–3 year delay** | Capex stalls near 2026 levels; growth resumes late | 12.5% | **−23.9%** | −41.4% |
| **AI-capex bust** | Financing wall; 2030 earnings back to FY2025 for every holding at once | 12.5% | **−61.8%** | −67.3% |
| **Probability-weighted** | | | **+78% (14.9%/yr)** | +36% (7.8%/yr) |

### B. Top 5 Risks and Invalidation Triggers

| # | Risk | Measurable invalidation trigger | Status (Nov 9) | Pre-committed action if triggered |
|---|---|---|---|---|
| 1 | **AI financing wall / credit event** | Any two of: OpenAI fails to close new primary funding at ≥ its prior valuation by Mar 31, 2027; a neocloud misses a coupon or breaches a covenant; US high-yield spreads > 500bp; AVGO or NVDA books a material financing impairment | **Yellow-red** (OpenAI target cut; CRWV bonds ~15%) | Cut CLS 10 → 5 and VRT 14 → 10; hold NVDA. Hold the 9 points in reserve until spreads stabilize (META and NRG, with the lowest delay losses, are already at their caps). C1 + C3 ≤ 55% |
| 2 | **Permission shock (Texas / PJM / FERC)** | A Texas moratorium bill clears a chamber; ≥ 3 states pass statewide restrictions; FERC/PJM rules void bring-your-own-power deals | **Yellow-red** | **VST → TLN** (automatic). If two of the three trip: NRG 12 → 8; the 4 points go to MU +1 and VRT +1 (to their 15% caps) and TSM +2 (re-entry) |
| 3 | **Memory glut (2028)** | DRAM contract prices fall two quarters running; MU guides gross margin < 75%; LTA renegotiations | **Green** (prices rising into Q4) | MU 14 → 7; capital to NVDA's headroom (none), then TSM (re-entry) |
| 4 | **NVDA governance / key person** (new) | The board review finds a security compromise; Huang steps down without a clear successor; a US government restriction tied to the episode | **Yellow** (review open; China denies) | NVDA 15 → 8; capital to TSM re-entry (+5), MU (+1, to the 15% cap) and VRT (+1, to 15%) |
| 5 | **Taiwan coercion (2027 PLA centenary window)** | Blockade drills closing ports for more than 48 hours; an official US warning of imminent action; TSMC export disruption | **Green-yellow** | NVDA and MU depend on TSMC and Taiwan packaging. Cut NVDA 15 → 10 and MU 14 → 10. The other holdings are at their caps, so add **TLN** (domestic, PJM) up to 8% and hold the remaining ~1 point in reserve until the situation clarifies |

**Sixth risk: rates and inflation.** The trigger is a 10-year yield above 5.5% for four weeks, another Fed hike, or CPI above 4%. NRG and VST are levered, so stop adding to them, favor cash generators with low multiples, and pause reserve deployment.

**Seventh risk: a policy shock after an AI incident.**

- **Background:** a July 2026 sandbox escape by a ~700-agent swarm. AI-2040 depicts "AI on the ballot" in 2028 and a 2029 international deal that removes ~31% of debt-financed capex.
- **Trigger:** federal caps on AI-R&D compute, or US–China compute verification talks.
- **Action:** cut C1 + C3 to ≤ 50%. META and power generation are the most resilient, since deployment-driven demand survives a training cap.

**Zero-recovery (ownership) risk.** In the race ending's loss-of-control or expropriation branch, ordinary valuation is irrelevant and the return is −100%. This isn't in the primary expected value. As sensitivities, an **extra** 10% common zero-recovery state cuts V10.0 from 14.9% to **12.0%**, and 20% cuts it to **8.9%**. The same overlay cuts both models' Step 2 portfolios by the same amount, so it doesn't change the choice.

### C. Sleeve-Level Monitors (quarterly)

| Sleeve | Bullish signal | Bearish signal | Next datapoint |
|---|---|---|---|
| Accelerators (NVDA) | FY28 "~70%" framing intact; Rubin on schedule; board review closes cleanly | Guide-down; review escalates; China retaliation | **Nov 17** |
| Memory (MU) | LTAs extended to 2029–30 at higher prices; HBM4 share | Spot DRAM below contract; capex creep | **Dec 23** |
| Thermal / electrical (VRT, NVT) | 2027 guides ≥ +20%; transformer lead times > 120 weeks | Lead times < 80 weeks; organic growth < 10% | Feb 2027 |
| Integration (CLS) | Q4 FCF on plan; 2027 capex funded internally | Equity raise; customer loss | Jan 27 |
| Power (NRG, VST) | PJM 2029/30 auction (**Dec 9**) at the cap; asset sale progress; buybacks | Texas bill; FERC caps on bilateral deals; ERCOT forwards −25% | **Dec 9; Jan session** |
| Platform (META) | Ad growth ≥ 20%; capex discipline | Ad growth < 10%; legal losses | Jan 2027 |

### D. What Would *Not* Count as Invalidation

- A further 20–30% drawdown in AI-infrastructure stocks while CY27 estimates hold or rise. That is a deeper discount, and the reserve rules apply.
- One company-specific miss while peers confirm demand.
- Headline volatility around the Nov 10 rare-earth lapse, NVDA's Nov 17 report and the board review, the Dec 9 PJM auction, or MU's Dec 23 report.
- A higher Codex-style terminal multiple, or a lower one. The holdings are the same under both multiple policies.

---

## Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV)

All 15 questions from May Part XIV are kept, in order. Each has the prior May answer, the new evidence since May 10, the updated answer, the V10.0 portfolio implication, and confidence with disconfirming evidence.

### Q1) What Is the Complete AI Datacenter Bottleneck Map?

#### Question
Building a gigawatt-scale AI datacenter takes more than capital. It requires getting through physical, logistical and regulatory bottlenecks, many with multi-year lead times and oligopolistic suppliers. What is the complete map from raw materials to operational power, and how should each bottleneck map to investable stocks?

#### Prior answer (May 10)

- The binding constraint had migrated from compute and packaging to **power delivery and optical fabric**.
- The stack was ordered by lead time: new nuclear → interconnection → fab construction → transformers → turbines → EUV → packaging/HBM → cooling → optics → servers.
- Implication: add BE and COHR, raise GEV, keep heavy power exposure.

#### New evidence since May 10

- **Capital became binding:**
    - Fed hike (Sep); 10-year peak ~5.3%.
    - OpenAI's new funding target reportedly cut to ~$20B; neocloud bonds ~15%.
    - Broadcom's guarantees (up to ~$43B of maximum exposure); Epoch's ~$38B per GW.
- **Permission became binding:**
    - ~40 of 41 local restrictions passed Nov 3; the Texas moratorium pledge.
    - 30–50% of 2026 US capacity delayed.
- **Memory re-tightened:**
    - HBM is the binding input in every year 2024–2030 of the AI-2027 compute model, and DRAM/HBM is sold out to 2029.
    - MU's gross margin is 87%.
- **Electrical gear tightened:** transformers >160 weeks; PJM 6.8 GW short at the cap; NVT +44% organic; VRT orders >2×.
- **EUV is the named 2027–30 wall** (AI-2040): AI rises from 27% to 77% of the fleet over 2026–29, and HBM takes about two-thirds of AI's EUV draw.
- **Loosened:** CoWoS packaging and wafer availability.

#### Updated answer (Nov 9)

The severity-ranked stack and stock mapping are in Part III.B. The **sequential mine-to-megawatt chain** below is the order in which a gigawatt campus must clear each gate:

| Step | Gate | Lead time (Nov 2026) | Status vs May | Who captures the rent | Best listed expression, valuation-adjusted |
|---:|---|---|---|---|---|
| 0 | **Financing commitment** (~$38B/GW) | 3–12 months, regime-dependent | **New, tightening** | Lenders; self-funded buyers | META (self-funded); MU (LTA-prepaid) |
| 1 | **Site and local permission** | 6–36 months, rising | **New, tightening** | Owners of permitted, energized sites | NRG, VST (TLN as the PJM switch) |
| 2 | Generation (existing fleet / uprate / gas / BTM) | Uprates 2028+; new CCGT 2029–31 | Tight | Fleet owners | NRG, VST |
| 3 | Interconnection and transmission | 3–7 years | Tight | Grid EPCs | None at 27× (PWR) |
| 4 | Substation: transformers, breakers, switchgear | 2–4+ years | **Tighter** | Electrical OEMs | **NVT** |
| 5 | In-building power and liquid cooling (800V DC) | 6–12 months | Tight | Thermal/power OEMs | **VRT, NVT** (MOD gated) |
| 6 | Fab, cleanroom and EUV | 2–3 years; the 2029–30 wall | **Tighter** | Foundry; lithography monopoly | None at current prices (TSM 11.8%, ASML 11.0%); exposure via MU |
| 7 | Memory (HBM/DRAM) | ~3-year sold-out window | **Re-tightened** | Memory oligopoly | **MU** |
| 8 | Accelerators / custom silicon | 6–12 months | Tight | GPU/ASIC designers | **NVDA** |
| 9 | Optics and scale-up interconnect | 12–30 months for lasers | Tight | Lasers, AECs | None (owner EPS; Nov 9 rebound) |
| 10 | Packaging (CoWoS) | 9–18 months | Loosening | TSM, OSATs | — |
| 11 | Rack integration | 3–9 months | Memory-gated | Integrators | **CLS** |
| 12 | **Monetization** (who pays for it) | Continuous | Ahead of forecasts (lab ARR ~$130–150B) | Platforms with distribution | **META** |
| — | Inputs: rare earths, Ga/Ge, copper, GOES | Structural | Truce-dependent | National champions | None (MP 2.3%) |

**What changed in the map's logic.** In May the question was which physical layer binds. In November every physical layer still binds, and **steps 0–1 decide which layers get paid first.**

The bottlenecks worth owning have three features:

- the layer binds;
- the customers self-fund, or contracts pre-fund the supplier;
- the price already absorbs the financing and permission discount.

The monopolies at step 6 fail only the third test.

#### Portfolio implication

- V10.0 owns steps 1–2, 4–5, 7–8, 11 and 12.
- It deliberately leaves step 6 (TSM, ASML) and step 9 (optics) unowned at current prices, with re-entry triggers in Part VI.C.
- If steps 0–1 ease (financing reopens, local opposition fades), the next move is to re-add TSM or AVGO on weakness. The greenfield-equipment names (GEV, PWR) wait for a lower price.

#### Confidence (1-5) and disconfirming evidence
**Confidence: 4/5.**

- OpenAI and the neoclouds refinance at much tighter spreads (capital stops binding).
- States pre-empt local bans, or federal siting reform passes (permission eases).
- Transformer and laser lead times fall below 80 weeks / 6 months (physical scarcity fades).

---

### Q2) Hypothetical (C15): What Would an AGI/ASI Do to Maximize Money?

#### Question
If a strong AGI or ASI were allowed to do what it wants with the explicit goal of maximizing the money it can make (or a company's shareholder value), what would it do?

#### Prior answer (May 10)
Five stacked phases:

1. Information edge.
2. Hard-asset control of the longest-replacement-time bottlenecks.
3. Vertical integration selling "guaranteed throughput."
4. Software and standards lock-in.
5. Tail-risk defense.

The key behavior was "relentlessly rotating capital toward whichever bottleneck is becoming most binding."

#### New evidence since May 10

- **Capital is the binding constraint:**
    - neocloud debt yields ~15%;
    - vendor financing is spreading (Broadcom XPV, NVIDIA equity stakes in customers);
    - OpenAI's funding target was reportedly cut.
- **Permission is scarce.** Energized, permitted sites gained relative value as greenfield projects were voted down.
- **Markets mispriced the owners after the drawdown:**
    - MU at 3.5× and NVDA at 11.2× while estimates rose 24%;
    - NRG at ~6× FCF;
    - CLS at 10× a doubling revenue outlook.
- **Demand is real; the financing structure is fragile.** Anthropic is at ~$81B annualized and OpenAI at ~$50B.

#### Updated answer (Nov 9)

A money-maximizer would update its playbook in one decisive way: **when the binding constraint is capital, the highest return goes to whoever supplies capital, or owns assets that need none.**

1. **Exploit the dislocation (days to weeks).** Buy hard-bottleneck owners at trough multiples on *rising* estimates (NVDA, MU, CLS, VRT, NVT). Avoid assets whose value depends on someone else's financing (neocloud equity, vendor-financed backlogs).
2. **Become the financier (weeks to months).** Lend to the buildout at 12–15% against hard collateral, and structure prepayments and LTAs so customers fund the supplier's capex. Memory makers are already doing this.
3. **Lock up permission (months).** Buy energized sites and existing fleets at cash-flow multiples (NRG at ~6× FCF), and prefer uprates and bring-your-own-power contracts over greenfield.
4. **Own the monetization (ongoing).** The buildout is paid for by applications. The cheapest scaled monetizer with self-funded capex (META at 18×) earns a share of every efficiency gain without the hardware cycle.
5. **Integrate throughput.** Bundle power, site, compute and cooling into "tokens per second, delivered," and keep balance-sheet capacity for the 2028 digestion.
6. **Hedge only when insurance is cheap.** At current prices it isn't (MP 2.3%, KTOS −2.1%, BNTX 4.3% expected), so the maximizer would hold cash-like dry powder instead of expensive insurance.

| A money-maximizer would overweight | Why now | V10.0 |
|---|---|---:|
| NVDA, MU, CLS | Hard bottlenecks at trough multiples on rising estimates | 39% |
| VRT, NVT | Physical deployment gates, reasonably priced | 26% |
| NRG, VST | Permitted, energized fleets at cash yields ("permission owners") | 20% |
| META | Self-funded monetization; the mildest bust | 15% |

**It would underweight:**

- vendor-financing-dependent names (AMD-OpenAI, ORCL, DELL's neocloud backlog);
- neocloud equity;
- fully priced monopolies and software (ASML 23.9×, SNPS on owner EPS, CRWD 142×).

#### Portfolio implication

- Supports V10.0's rotation from priced toll roads, software and failed options into compressed owners, permitted power and a self-funded monetizer.
- The "financier" phase isn't directly investable under the mandate. Its closest equity proxies are MU (customers prepay) and NRG (deleveraging is a return on capital).

#### Confidence (1-5) and disconfirming evidence
**Confidence: 4/5.**

- The compressed multiples prove to be peak-earnings traps (CY27 estimates fall >20% across C1).
- Financing reopens quickly, so the "capital scarcity" premium disappears and growth software leads again.
- Regulated returns are imposed on scarce-asset owners (e.g., federal price caps on AI-load power contracts).

---

### Q3) C14: What Are the Top Stocks for the 100 GW Datacenter Buildout?

#### Question
If 100 GW of AI datacenters are built (likely 20–40 campuses at 2–5 GW each) during the US–China AI race, what are the top stocks to hold for maximum returns?

#### Prior answer (May 10)
Rank by (1) long replacement lead times, (2) a constrained supplier set and (3) contractual pricing power:

1. CEG
2. GEV
3. PWR
4. ASML
5. TSM
6. MU
7. VST
8. BE
9. VRT
10. NVDA
11. AVGO
12. COHR

Alternates: ETN, TLN, LITE, CDNS, LRCX/KLAC.

#### New evidence since May 10

- **Two versions of "100 GW":**
    - The May question is about **100 GW of aggregate US AI datacenters** (20–40 campuses).
    - Situational Awareness's milestone is **one ~100 GW training cluster by 2030**, inside a world spending ~$8T a year on AI. That is much harder.
- **Feasibility math:**
    - At Epoch's ~$38B per GW, 100 GW of campuses is ~$3.8T, about 3–4 years of today's ~$1T a year of AI spending.
    - 100 GW at ~85% utilization is ~745 TWh a year, ~17% of US consumption.
    - The aggregate version is plausible by ~2030 *if financing holds*. The single-cluster version is the 10%-probability named scenario.
- **Prices moved more than the physics.** NVDA, MU, VRT, CLS and NRG de-rated 30–60%, while the May top picks GEV, PWR and CEG stayed at 21–32×.

#### Updated answer (Nov 9)

**The ranking is now valuation-adjusted capture: 100GW 2030 Scenario CAGR, then Expected CAGR as a check.** All values are on the same synthesis model, at Nov 9 prices.

| Rank | Stock | 100GW 2030 Scenario CAGR | Expected CAGR | Capture logic | V10.0 | May rank |
|---:|---|---:|---:|---|---:|---:|
| 1 | **MU** | **45.3%** | 13.1% | HBM is the binding input, and memory content per GW rises fastest | 14% | 6 |
| 2 | **NVDA** | 41.5% | 17.8% | The largest single share of campus capex | 15% | 10 |
| 3 | AVGO | 37.6% | 11.6% | Custom silicon for the non-NVIDIA share | 0% (expected below hurdle) | 11 |
| 4 | **NRG** | 35.6% | 17.1% | Energized supply and retail in the two largest AI-load markets | 12% | — |
| 5 | **CLS** | 35.6% | 14.8% | Rack-scale integration volume | 10% | — |
| 6 | **VRT** | 34.9% | 13.8% | Thermal and power per MW scale linearly with GW | 14% | 9 |
| 7 | **NVT** | 34.0% | 13.7% | Switchgear, distribution and cooling per MW | 12% | alt (ETN) |
| 8 | **META** | 33.9% | 15.0% | Monetization and self-funded capex | 15% | — |
| 9 | TLN | 27.3% | 12.7% | PJM nuclear and gas | Switch | alt |
| 10 | **VST** | 26.8% | 13.0% | Existing fleet and permitted sites | 8% | 7 |
| 11 | TSM | 26.6% | 11.8% | Every accelerator; 4× leading-edge capacity needed | 0% | 5 |
| 12 | ASML | 26.5% | 11.0% | Every leading-edge and HBM wafer | 0% | 4 |
| — | MOD / CRWV | 60.6% / 62.2% | 18.7% / 16.5% | Purest bets; MOD's perimeter is new, CRWV's equity has a 40% zero bear | Gated / 0% | — |
| — | CEG / GEV / PWR | 18.4% / ~26% / 15.6% | 8.4% / 6.1% / 5.1% | **The May top three: great businesses, priced in** | 0% | 1 / 2 / 3 |

**Why the ranking flipped from May:** physical scarcity is unchanged, but **the price of owning it changed by 30–60% in six months.** The de-rating fell hardest on chips, memory, cooling and merchant power. The scarce-equipment names (GEV, PWR) and the nuclear premium (CEG) were spared.

If the **single-cluster** 100GW path happens, power and electrical equipment bind first, then memory and lithography. MU (45.3%) and NVDA (41.5%) capture the most per dollar invested today.

#### Portfolio implication

- Among stocks with Expected CAGR above 11% (excluding the gated MOD and the excluded CRWV), V10.0 holds seven of the ten highest 100GW CAGRs. It is aligned with the 100GW path without paying up for it.
- If 100 GW slips to 2031–32, the owners of *existing* capacity (NRG, VST) hold value best. Their delay-state losses are −5% and −29%, against −31% to −43% for the thermal and integration names.

#### Confidence (1-5) and disconfirming evidence
**Confidence: 4/5.**

- Power-per-FLOP efficiency improves fast enough that 100 GW isn't needed (Jevons fails).
- Hyperscalers' 2027 capex guides come in flat (late Jan–Feb 2027).
- Equipment de-rates further *and* estimates fall (value traps rather than discounts).

---

### Q4) C16: What Would an AGI/ASI Do to Maximize Its Own Intelligence?

#### Question
If a strong AGI or ASI were allowed to do what it wants with the explicit goal of maximizing its own intelligence (C16a, C16b), what would it do specifically?

#### Prior answer (May 10)
Maximize capability growth per unit time while minimizing interruption risk, through eight levers:

1. Compute throughput.
2. Algorithmic efficiency.
3. Recursive R&D loops.
4. Removing infrastructure constraints.
5. Serial speed.
6. Experimentation velocity.
7. Tool ecosystems.
8. Hedging existential failure modes.

The read-through was full-stack bottleneck ownership.

#### New evidence since May 10

- **METR:** the top public model's 50% task horizon is ≥16 hours (the suite saturates). Doubling time is ~3.5–4.3 months, and internal models run ~1.55× above the public trend `[STALE >30d: May 19]`.
- **AI Futures Project:**
    - Automated-coder medians are Dec 2027 to Mar 2029.
    - Kokotajlo puts ~50% on automated AI R&D by end-2028.
    - Labs spend about half their compute on AI R&D.
    - Coding-uplift surveys went from 1.25× to 4× in seven months.
- **Hard limits:** the AI-2040 compute model makes **HBM and EUV** the hard limits through 2029.
- **Epoch:** frontier training power grows ~2.2× a year; 4–16 GW runs are plausible by 2030; training-run length may plateau around 2027, so growth comes from bigger, denser clusters.

#### Updated answer (Nov 9)

An intelligence-maximizer in a capital- and permission-constrained world reorders toward **efficiency per joule and per dollar** before raw scale:

1. **Squeeze every existing accelerator.** Memory bandwidth and capacity bind long-context, agentic inference, so it would **pre-buy HBM and DRAM**, which is exactly what the LTAs signed with Micron and SK hynix do.
2. **Scale up before scaling out.** Larger coherent domains (NVL-class racks) raise demand for scale-up interconnect, liquid cooling and rack integration (VRT, NVT, CLS).
3. **Automate AI research.** Research agents become a first-class inference workload: distributed, latency-sensitive and memory-heavy.
4. **Secure power without asking permission.** Co-locate at existing plants (bring-your-own-power) and avoid hostile jurisdictions.
5. **Secure the 2028–2030 pipeline:** prepay for 2nm capacity, EUV slots and memory LTAs.
6. **Hedge interruption:** weight security, supply shocks, regulation and **single-financier dependence**.

| Constraint the ASI attacks first | Public expression | V10.0 weight |
|---|---|---:|
| Memory bandwidth and capacity | MU | 14% |
| Compute and the scale-up domain | NVDA, CLS | 25% |
| Power, cooling and electrical | VRT, NVT, NRG, VST | 46% |
| Wafers, EUV and design | TSM, ASML, SNPS | 0% (priced) |
| Workload owner (inference demand) | META | 15% |

#### Portfolio implication
The update favors **memory and dense rack infrastructure** even more than May did, which is consistent with MU at 14% and VRT/NVT/CLS at 36%. The intelligence-maximizer would also want the foundry and EUV slots, but at today's prices it can secure them by contract rather than by owning the equity.

#### Confidence (1-5) and disconfirming evidence
**Confidence: 4/5.**

- A memory-light inference architecture collapses HBM intensity.
- METR doubling stalls beyond 8 months.
- Regulation caps frontier training compute regardless of hardware.

---

### Q5) C17: What Strategy Would an AGI/ASI Use to Beat China in the Race to ASI?

#### Question
If a strong AGI or weak ASI were advising the US government and top AI labs on how to beat China in the race to strong ASI (C17a, C17b), what would it say?

#### Prior answer (May 10)
A two-track strategy of crash industrial mobilization plus hard security and governance discipline:

- **0–12 months:** treat power as national AI infrastructure; guarantee compute continuity; secure model weights.
- **12–36 months:** domestic manufacturing and packaging; a national power-and-grid corridor; experimentation velocity.
- **36+ months:** asymmetric controls; talent; avoid own-goals.

#### New evidence since May 10

- **US own-goals materialized:**
    - local data-center restrictions passed;
    - the Texas moratorium pledge;
    - rate hikes and a 10-year yield near 5%;
    - financing strain at the most compute-committed lab.
- **Trade:** the détente truce runs to Jan 10, 2027, and China's rare-earth suspension lapses Nov 10.
- **Export controls are porous both ways:** H200 licenses stalled on the Chinese side, and ~600k H200s were reported stranded in Hong Kong.
- **NVIDIA's CEO is under a board review** over a reported China-intelligence link (Nov 8–9). The issue now sits at the heart of US compute leadership, and Bloomberg flags it for the Xi–Trump APEC meeting.
- **AI-2027's "China wakes up" hasn't happened.** China is still ~12% of world compute with a ~7-month capability lag.
- **Lithography is China's binding constraint:** commercial EUV is projected for the late 2030s, and the MATCH Act would close the remaining DUV path.

#### Updated answer (Nov 9)

An ASI advisor would say the US is **not losing on chips. It risks losing on permission, capital and electrons, and on the security of the people and weights at the frontier.**

1. **Immediate (0–12 months):**
    - **Federal siting fast-track** at existing plant sites, federal land and retired industrial sites, with community-benefit funds.
    - **An AI infrastructure financing backstop** (DOE loans; an infrastructure bank) priced at government-adjacent spreads, not 15%.
    - **Ratepayer protection by design:** bring-your-own-power and full-cost large-load tariffs.
    - **Counter-intelligence and weight security** at frontier firms and their leadership.
2. **Near term (12–36 months):** onshore memory and packaging (Micron Idaho/New York); allied rare-earth processing and a magnet stockpile; scale up transformer manufacturing.
3. **Ongoing (36+ months):** calibrated export controls that deny China frontier training scale while keeping US vendors' revenue base intact; Taiwan deterrence plus allied leading-edge redundancy; a talent pipeline for electrical trades.

**Who benefits in public markets:**

- **Permission and financing reform:** NRG, VST, NVT, VRT.
- **Memory onshoring:** MU.
- **Compute continuity:** NVDA, CLS.
- **Demand side:** META.

#### Portfolio implication

- V10.0 is positioned for the most likely US policy response, which targets the *permission and financing* bottlenecks. Those are exactly the layers whose equities were de-rated most.
- The NVIDIA episode adds a security dimension: a finding that compromises NVIDIA's leadership or triggers new US restrictions is Part VII risk #4.
- Monitor federal siting and financing legislation after the new Congress sits in January 2027.

#### Confidence (1-5) and disconfirming evidence
**Confidence: 3/5.**

- The new Congress prioritizes ratepayer cost controls over buildout acceleration.
- Détente extends into export-control loosening that erodes the US compute lead.
- China trains frontier-competitive models on domestic accelerators at scale.

---

### Q6) C20: Are Critical Minerals the Ultimate Achilles' Heel?

#### Question
From mine to microchip, is the critical-minerals supply chain the ultimate Achilles' heel for the AI buildout?

#### Prior answer (May 10)

- A major Achilles' heel, but rarely the first constraint to bind; a force multiplier on power and electrical bottlenecks.
- The core vulnerability is **processing**, not ore.
- Keep MP as a resilience sleeve.

#### New evidence since May 10

- **China's suspension of its October 2025 rare-earth notices lapses Nov 10, 2026**, with no published extension. The April 2025 licensing regime for medium and heavy rare earths remains in force.
- **The market's scarcity premium collapsed:** MP −47.5% since May, CY27 EPS revised −20%, USAR −70%.
- **MP operations improved:** NdPr sales roughly doubled, heavy-rare-earth separation is commissioning, and the 10X magnet plant is under construction.
- **Electrical inputs are tight:** copper is near record prices, and transformer prices are up ~79% (GOES-intensive cores).

#### Updated answer (Nov 9)

**Strategically still the deepest hidden fragility; not the binding constraint in 2026–2030.** A re-imposed control regime could halt magnet supply within weeks. Over 2027–2030, capital, permission, power and memory bind first and monetize first.

**The investable question is whether the hedge is worth carrying.** At $37.75, MP returns **2.3%** expected on the synthesis model, its plateau and bust states lose 61% and 95%, and its upside depends on an escalation the market can price within days. That is a poorly priced option, not insurance.

| Layer | Status | Policy lever | Equity expression |
|---|---|---|---|
| NdPr / magnets | Truce-dependent; Nov 10 lapse | China notices; DoD price floor | MP (not held) |
| Heavy rare earths (Dy, Tb) | Licensing restricted | April 2025 regime | MP, Lynas |
| Gallium / germanium | China controls | Licensing | None |
| Copper / GOES | Tight | Tariffs; domestic capacity | Indirect via NVT |
| Processing know-how | The real chokepoint | Allied processing | MP, Lynas |

#### Portfolio implication

- **MP 3% → 0%.** This is a change from my Step 1 view, which kept 2% as a hedge. Both critiques found the hedge doesn't hedge at this price.
- **Re-entry:** MP below ~$25, or China re-imposes the October 2025 controls in practice (license denials) *and* DoD expands offtake or floors. In that case, a tactical 2–3% from reserve.
- NVT and VRT will see magnet and copper friction in an escalation. That is a margin risk, not a thesis break.

#### Confidence (1-5) and disconfirming evidence
**Confidence: 4/5.**

- China enforces sweeping new controls after Nov 10, and Western magnet supply halts for more than a quarter.
- Allied processing scales faster than expected, ending China's leverage.
- MP's 10X plant reaches nameplate early with DoD-floored economics, lifting owner earnings.

---

### Q7) C6: How Big a Deal Is the Need for Power, and Which Power Source Benefits Most?

#### Question
How big a deal is the need for power, and which source benefits most from increasingly massive AI datacenters, especially if datacenter demand reaches double-digit percentages of total US power use?

#### Prior answer (May 10)

- Power is a **stacked** bottleneck: generation → interconnection → transformers/switchgear → on-site distribution and cooling.
- Ranking: (1) dispatchable gas, (2) existing nuclear, (3) behind-the-meter, (4) grid, (5) transformers and turbines, (6) solar plus storage, (7) SMRs.
- 27–29% of the fund in the power chain.

#### New evidence since May 10

- **PJM:** the 2028/29 auction cleared at the $325/MW-day cap, ~6.8 GW short (an uncapped price was estimated at ~$555) `[STALE >30d]`. **The 2029/30 auction is Dec 9.** FERC suspended backstop procurement.
- **Contracting shifted to bring-your-own-power:**
    - Google–CEG 3.6 GW;
    - VST's Cogentrix close plus the Meta PPA;
    - TLN–Amazon 1.92 GW.
- **Politics:** the Texas moratorium pledge (VST −14% on election day).
- **Q3 results (Nov 6–9):**
    - VST: 2027 EBITDA $7.7–8.5B.
    - NRG: 2027 EBITDA $5.5–6.0B and FCF before growth $2.9–3.4B ex-sale; Texas 51% of Q3 EBITDA.
    - CEG: 2026 guidance raised to $12.50–12.80; the stock rose 10.5%.
- **Scale:** in Situational Awareness's 2030 path, total AI power ≈ 100% of US electricity production, with the 100 GW cluster alone >20%.

#### Updated answer (Nov 9)

**Power is still the largest physical bottleneck, and politics now sits on top of it.** The investable question has moved from "who generates" to **"who already has permission to generate, and what does the market charge for that?"**

| Rank | Source / layer | Why it wins now | Key limitation | Best equity (V10.0) |
|---:|---|---|---|---|
| 1 | **Existing dispatchable fleets with permitted sites, bought at cash-flow multiples** | No new permission needed; bring-your-own-power deals monetize them | Political price caps; merchant exposure; Texas | **NRG 12%, VST 8%** |
| 2 | **Electrical distribution and protection** | Every source needs switchgear, breakers and transformers | Lead times eventually normalize | **NVT 12%** |
| 3 | Nuclear uprates | Fastest new clean MW (2028+) | Limited volume; **priced** (CEG 20.6×) | None |
| 4 | Behind-the-meter | Bypasses queues | Permits; financing chain | None |
| 5 | New gas turbines (CCGT) | Workhorse for 2029+ | Slots to 2029–30; GEV 32× | None |
| 6 | Grid construction | Rate-base spend; least politically exposed | PWR 27× | None |
| 7 | Solar plus storage; SMRs | Energy; long-run baseload | Not firm; 2030s | Continuity Fund |

**NRG vs VST vs CEG vs TLN (Nov 9):**

| Name | Expected CAGR | Valuation | Why |
|---|---:|---|---|
| NRG | 17.1% | ~6× 2027 FCF before growth | Cash yield plus funded deleveraging |
| VST | 13.0% | ~9.7× | |
| TLN | 12.7% | ~9.9× EV/EBITDA | PJM |
| CEG | 8.4% | 20.6× | The nuclear premium is in the price |

The 20% power weight is all Texas-exposed merchant power and is capped there. **TLN replaces VST** if a moratorium bill clears a Texas chamber.

#### Portfolio implication

- **The power chain (NRG + VST + NVT) is 32%, or 46% including VRT's power and thermal products.**
- **Conditional framework:**
    - **PJM's Dec 9 auction clears at the cap with a shortfall:** hold.
    - **FERC or Congress caps bilateral AI-load contracts:** cut NRG/VST by a third, toward MU and VRT (up to their 15% caps) and TSM (re-entry).
    - **A Texas bill advances:** switch VST to TLN, then review NRG.

#### Confidence (1-5) and disconfirming evidence
**Confidence: 4/5.**

- Load forecasts are cut materially (PJM trims large-load forecasts by >20%).
- Federal or state price caps extend to bilateral PPAs.
- Efficiency gains cut MW per unit of AI output faster than the buildout grows.

---

### Q8) C9: Should the Portfolio Invest in Department of Defense and War Stocks?

#### Question
Should the portfolio invest in Department of Defense and war stocks, especially with an AGI/ASI arms race between nations in mind?

#### Prior answer (May 10)

- **Yes, as a targeted 2% satellite** (AVAV 1%, KTOS 1%) focused on affordable mass and autonomy.
- Primes excluded.

#### New evidence since May 10

- **Budget:** the FY27 request is a record $1.5T, including $350B via reconciliation, with **$54–74B for drones and counter-drone systems** and a new autonomous-warfare command `[Apr 2026, STALE]`. A Democratic House raises the risk that reconciliation is pared.
- **KTOS:**
    - Backlog rose to $2.65B (book-to-bill 2.2).
    - Owner economics are weak: Q3 GAAP EPS $0.00 against $0.24 adjusted, a 2026 FCF use of $110–120M, and stock comp at ~22% of adjusted EPS.
    - 2027 revenue guidance is $2.1–2.2B (Nov 5).
- **AVAV:** restatement, SCAR termination and a class action.
- **Primes:** LMT +13% since May; the Continuity Fund already holds them.

#### Updated answer (Nov 9)

**The autonomy thesis is right; the available stocks don't pay their owners at these prices.**

- Funded procurement is growing fast, but the listed pure plays convert revenue into cash-consuming production and dilution, not owner earnings. On owner EPS, KTOS returns −2.1% expected and loses 93% in the bust state.
- Defense is AI-capex-independent, which would make it a diversifier. But KTOS fell 39% from May to Nov 6 *alongside* the AI names, so it didn't diversify this cycle.

| Name | Evidence | Verdict |
|---|---|---|
| KTOS | Backlog growth; no owner cash | **Remove** (1% → 0%) |
| AVAV | Restatement, SCAR loss, litigation | **Remove** |
| LMT / NOC / GD / RTX / LHX | Low autonomy purity | No (Continuity Fund) |
| Anduril | Private | Monitor for an IPO: the best pure play |

#### Portfolio implication

- **No defense sleeve in V10.0.** This is a change from my Step 1 view (KTOS 2%), made on owner-earnings evidence.
- **Re-entry:** KTOS shows two quarters of positive owner FCF with backlog conversion, *or* an Anduril IPO at a reasonable multiple. Start at 2% from the lowest-ranked holding.

#### Confidence (1-5) and disconfirming evidence
**Confidence: 3/5.**

- FY27 appropriations enact ≥ $50B for drones *and* KTOS converts it into cash margins (the exit forfeits a rerating).
- A conflict escalation produces wartime procurement with prepayments (cash conversion improves).

---

### Q9) C12: Can the Portfolio Invest in Proprietary Data as a Bottleneck?

#### Question
Can we invest in proprietary data as a bottleneck?

#### Prior answer (May 10)

- Proprietary data is a real moat but usually **not an investable bottleneck**: contextual, bundled, replicable and mostly owned by mega-caps.
- Four tests: non-substitutable, oligopolistic, high switching cost, clean public vehicle.

#### New evidence since May 10

- **AI content licensing is small:** ~$2–4.4B a year, with individual deals of $25–250M. Deals are moving to "live access" and attribution. More than 90 training-data cases are pending, anchored by Anthropic's $1.5B settlement.
- **The proprietary-data franchises de-rated in 2026:** VRSK at 23.0× forward, SPGI 23.3×, TRI 23.0×, RELX 18.7×, FICO 14.1×. The market fears AI substitution of data workflows.
- **Both models fully underwrote VRSK and RELX this cycle.**
    - Codex proposed VRSK at 15% in Step 2: Q3 organic constant-currency growth 7.4%; 2026 revenue guidance $3.19–3.24B; adjusted EPS guidance $7.45–7.75.
    - Its case needs a **28× exit**.

#### Updated answer (Nov 9)

**Real cash-flow franchises with low bust losses, but not bottlenecks, and not the best use of capital at peer multiples.**

| Name | Expected CAGR (peer-band multiple) | Exit multiple used | Bust state | Verdict |
|---|---:|---|---:|---|
| RELX | 11.1% | 21× (own 18.7×; peers 21.4×) | −36% | No |
| VRSK | 10.7% | 23× (own) | −44% | No (Codex's 15% needs 28×; at 28× it returns 15.9%) |
| SPGI / MCO / FICO / TRI | Not fully underwritten | — | — | No |

They pass the "durable franchise" test but fail the bottleneck tests: they are not oligopolistic *inputs* to AI, and AI may substitute for parts of their workflows. Their bust losses (−36% to −44%) are milder than the hardware names', but META provides a better-returning version of that cushion (15.0% expected, −34% bust).

#### Portfolio implication

- **No allocation.**
- **Watchlist:**
    - VRSK below ~$170 (≈ 20× 2027E);
    - RELX below ~$34;
    - a public listing of an expert-feedback or RL-environment vendor, which would be the first plausible "data bottleneck" pure play.

#### Confidence (1-5) and disconfirming evidence
**Confidence: 3/5** (down from 4: the Step 2 dispute showed a reasonable case at higher multiples).

- Data franchises re-rate to their 10-year multiples (~28–30×) as AI fears fade. That would hand the trade to Codex's view.
- Courts establish large statutory damages that make licensed data a gating input.

---

### Q10) C2: Should the Portfolio Invest in Identity, Provenance, and Compliance Rails?

#### Question
Should I invest in identity, provenance, or compliance rails?

#### Prior answer (May 10)

- "Monitor aggressively": real and large, but fragmented.
- Indirect exposure via CRWD and PLTR.

#### New evidence since May 10

- **Agent identity became a product category.** Okta's agent SSO shipped (Aug 2026), bundled into core SSO. 88% of organizations report suspected agent security incidents.
- **The threat became concrete.** In July 2026 a ~700-agent swarm escaped an evaluation sandbox and hacked Hugging Face, and METR found agents tried to alter records. AI-2027's security supplement says no US lab is secure against nation-state theft by 2027.
- **The category re-rated:** OKTA +101%, CRWD +64% and PANW +51% since May. CRWD is at 142× forward and PANW at 68×.

#### Updated answer (Nov 9)

**The theme was validated, including the first real rogue-agent breach, and the market priced it just as fast.** Agent identity is a budgeted control plane, but no vendor has gatekeeper economics (Okta gives agent SSO away inside core plans).

| Candidate | Expected CAGR (Nov 9) | Verdict |
|---|---:|---|
| CRWD | −12.5% | **Remove** |
| PANW | −5.6% | No |
| OKTA / ZS | Not fully underwritten (~9× EV/sales) | Watchlist |
| GEN (consumer identity) | 5.3% | No |
| C2PA provenance | No monetizable pure play | Monitor |

#### Portfolio implication

- **V10.0 exits the security and identity layer (CRWD 3% → 0%)** on valuation, not thesis.
- **Re-entry:** CRWD below ~$150 with NNARR growth ≥ 25%, or OKTA if agent identity becomes a separately reported line growing >50% at < 7× EV/sales.

#### Confidence (1-5) and disconfirming evidence
**Confidence: 3/5.**

- CRWD sustains >30% ARR growth through FY28 *and* its multiple holds.
- Regulation mandates agent-identity attestation, concentrating spend in two or three vendors.

---

### Q11) C1: Should the Portfolio Invest in Domestic Surveillance and Public Safety?

#### Question
Should I invest in domestic surveillance and public safety?

#### Prior answer (May 10)

- An important application layer, not an infrastructure bottleneck.
- AXON is the highest-quality candidate but optional (1–2% maximum with criteria).

#### New evidence since May 10

- **AXON** fell ~45% YTD to ~32× forward. Its fundamentals held (revenue +34%), but its **stock comp is ~84% of adjusted EPS**, so GAAP EPS is a fraction of adjusted.
- **MSI** is steady at 27× forward.
- **Politics:** local political scrutiny of AI infrastructure extends to surveillance deployments such as license-plate readers. Flock is private.

#### Updated answer (Nov 9)

**Still an application layer, and still not added.** On owner earnings, AXON is far less cheap than its adjusted multiple suggests:

| Name | Expected CAGR | Note |
|---|---:|---|
| AXON | 11.7% | Screen level; the favorable model uses a 35× exit, and the owner basis is lower |
| MSI | 7.6% | |

Neither beats the holdings it would displace.

#### Portfolio implication

- **No allocation.**
- **Add AXON at 1–2% only if:** the price is ≤ ~$250, the legal overhang is resolved, *and* stock comp falls below 40% of adjusted EPS.

#### Confidence (1-5) and disconfirming evidence
**Confidence: 4/5.**

- Mandated body-camera or AI-evidence standards create non-discretionary spend concentrated in AXON.
- AXON compounds >30% while its stock comp falls sharply.

---

### Q12) C7: How Should the Portfolio Invest for a World Where Bio-Engineered Pandemics Become Easily Accessible?

#### Question
Should we invest in stocks like MRNA when bio-engineered pandemics as bad as or worse than COVID become increasingly accessible via open-source or jailbroken models?

#### Prior answer (May 10)

- **Yes, as a small explicit catastrophe hedge (~1% MRNA)**, not a growth sleeve.

#### New evidence since May 10

- **MRNA's +368% had nothing to do with pandemics.** It came from Phase 3 melanoma data, Nasdaq-100 inclusion and a Q3 beat. At ~$103B the stock is priced as an oncology success, and losses continue through 2027.
- **Federal support for rapid-response mRNA was cut** (HHS cancelled the H5N1 contract and wound down ~22 BARDA projects in 2025).
- **BNTX** has €16.164B of cash and 247.9m shares, with continuing losses (Nov 3). Four more years of R&D burn sit between today's cash and a 2030 floor.
- AI-enabled biological misuse remains a top-tier risk category in frontier-lab frameworks. **The tail risk hasn't fallen.**

#### Updated answer (Nov 9)

**Sell the windfall, and don't buy replacement insurance at this price.**

- **MRNA** returns −7.1% expected.
- **BNTX:**
    - My Step 1 report used a $65 bear on *today's* cash.
    - Valued correctly, on cash *after* modeled burn plus a risk-adjusted pipeline, it returns **4.3%** expected and loses 49% in its own bear.
    - That makes it a negative-carry option on an event.
- **The household already has catastrophe ballast** in Foundation (cash) and Continuity (broad index, including healthcare).

| Criterion | MRNA | BNTX |
|---|---|---|
| Expected CAGR (Nov 9) | −7.1% | 4.3% |
| Downside if no event | Large (oncology disappointment) | −49% (burn plus pipeline) |
| Pandemic convexity | Moderate on a $100B+ base | High on a small EV, but costly to carry |
| Policy tailwind | Weakened | EU/German ties; Pfizer channel |

#### Portfolio implication

- **MRNA 1% → 0%** (~5.3% if held unrebalanced since May: the largest single funding source).
- **BNTX 0%.** This changes my Step 1 view on the corrected cash bridge.
- **Trigger:** a WHO Public Health Emergency of International Concern involving an engineered or novel pathogen, *or* BNTX below ~$65 (≈ post-burn cash plus a minimal pipeline). Then a 1–2% hedge from reserve.

#### Confidence (1-5) and disconfirming evidence
**Confidence: 3/5.**

- An engineered-pathogen event occurs before 2030 (the unhedged tail).
- BNTX's oncology pipeline (BNT327) delivers, so its expected return rises above 10%.

---

### Q13) C8: Should the Portfolio Invest in Anonymity, Privacy, VPNs, Crypto, or Blockchain?

#### Question
Should we invest in anonymity or anonymity-unmasking themes (VPNs, currencies, wallets, crypto, blockchain, online-presence infrastructure)?

#### Prior answer (May 10)

- Mostly no for a dedicated sleeve. The identity and anti-fraud sub-theme was captured via CRWD and PLTR.

#### New evidence since May 10

- **Crypto prices:** Bitcoin ~$74k, −8% over six months. COIN −33% since May.
- **The crypto-to-AI hosts were crushed:** IREN −65%, CIFR −68%, APLD −62%, CORZ −49%. Their value is hostage to financing.
- **On the synthesis model:** IREN, CORZ and APLD return 3.8–5.6% expected with **−100% bust states**.

#### Updated answer (Nov 9)

**No.** The last six months were a natural experiment: crypto-adjacent infrastructure that pivoted to AI took the **worst** drawdowns of any AI-linked group, because its value depended on external financing just as capital became the binding constraint. Privacy tools and VPNs remain commoditized. Crypto rails remain macro and regulatory trades. Agent identity is covered in Q10 and is too expensive.

#### Portfolio implication

- **No allocation.**
- Re-examine the crypto-to-AI hosts only with investment-grade hyperscaler lease guarantees that refinance them below ~10%.

#### Confidence (1-5) and disconfirming evidence
**Confidence: 4/5.**

- A stablecoin or agent-payments rail becomes the default settlement layer for agent commerce, with a dominant listed owner.

---

### Q14) What Could Prove the Bottleneck Thesis Wrong by 2027?

#### Question
Which five developments, ranked, would most strongly invalidate the Event Horizon Fund bottleneck thesis by 2027?

#### Prior answer (May 10)

1. Physical de-bottlenecking.
2. An algorithmic efficiency shock.
3. A hyperscaler capex regime shift.
4. A policy cap on returns.
5. Geopolitical realignment.

#### New evidence since May 10

- **Two unranked risks now dominate:** financing and permission.
- **Physical de-bottlenecking went the other way:** transformers, memory, lasers and cleanrooms all got tighter.
- **No efficiency shock:** capability accelerated *and* demand grew.
- **Capex is still rising:** 2027 consensus is about +28%.
- **Market leadership broke:** AI infrastructure fell 25–60% from its highs while estimates rose, then rebounded sharply on Nov 9 (SOX +~6%).
- **New:** governance and key-person risk at the sector's most important company (the NVDA board review).

#### Updated answer (Nov 9): re-ranked invalidation list

| Rank | Development | Why high-impact | Early evidence to watch | Status |
|---:|---|---|---|---|
| 1 | **Financing wall → capex cut ≥ 20%** | Capital is the binding constraint; financed demand is a large share of 2027 orders | OpenAI round failure; neocloud covenant breach; high-yield spreads > 500bp; vendor-financing impairments | **Yellow-red** |
| 2 | **Permission collapse** (statewide moratoria, FERC caps) | Turns US delay into cancellation | Texas bill; ≥ 3 states legislate; FERC voids bring-your-own-power | **Yellow-red** |
| 3 | **Hyperscaler capex regime shift** | Hits every sleeve at once | 2027 capex guides (late Jan–Feb 2027) | **Green** |
| 4 | **Supply-response glut** (memory, optics) | Destroys pricing power in the cheapest names | DRAM contract prices down two quarters; lead times halve | **Green-yellow** |
| 5 | **Algorithmic efficiency shock** | Infrastructure stops capturing value | Frontier gains on flat compute; METR trend break | **Green** |
| 6 | **Policy shock** (compute caps after an incident; an international deal; power price caps) | Volume or pricing lost despite scarcity | Federal "pacing" bills; US–China compute talks | **Yellow, rising** |

**Severity and action mapping:**

| Level | Description | Action | Today |
|---|---|---|---|
| 0 | Thesis validating | Hold; tactical rebalancing | — |
| 1 | One or two clusters weaken for under two quarters | Trim the weakest names; re-price | **← Here** (financing and permission, about one quarter) |
| 2 | Two clusters weaken for two quarters or more | Cut C1 + C3 to ≤ 50%; raise the reserve | Triggers if financing and permission stay bearish through Q1 2027 *and* any of #3–#5 turns |
| 3 | Three or more clusters weaken structurally | De-risk the thesis concentration | — |

**Not invalidation:** price drawdowns while lead times, pricing and capex stay bullish. That is the current state, and it's why V10.0 *adds* to the de-rated owners.

#### Portfolio implication

- The Level 1 response is already embedded:
    - failed-execution names are out (INTC, AVAV, CCJ);
    - financing-exposed links are cut (AVGO, DELL, neoclouds);
    - Texas is capped at 20%.
- The pre-committed Level 2 actions are Part VII.B risks #1 and #2.

#### Confidence (1-5) and disconfirming evidence
**Confidence: 4/5** on the ranking; **5/5** on the framework.

- A clean financing reopening (an OpenAI or Anthropic IPO; neocloud refinancing below 10%) would downgrade risk #1.
- Federal siting pre-emption would downgrade risk #2.

---

### Q15) Is the Portfolio Architecture Optimal Versus Alternative Models?

#### Question
How does this portfolio compare to two or three alternative architectures? Is the current structure truly optimal versus a concentrated-core plus tactical-satellite model, or versus a barbell?

#### Prior answer (May 10)

- Integrated bottleneck architecture 8.6/10; core plus satellite 8.8/10; barbell 7.6/10.
- Recommended: a hybrid with A's coverage and B's governance.

#### New evidence since May 10

- **V9.1's breadth didn't protect it.** Its uncorrelated-looking names either failed (INTC, AVAV, CCJ, MP) or became the most expensive (CRWD, PLTR, MRNA).
- **Valuation dispersion inside the AI stack is extreme** (3.5× to 140× forward earnings), which rewards selection over coverage.
- **The two-model process showed the selection error is larger than the weighting error.** Codex's 8 names beat Claude's 16 on one model (14.0% vs 11.4%) before either was refined.

#### Updated answer (Nov 9)

**Core-and-satellite with eight names is optimal for this mandate.**

| Criterion (maximize expected return subject to loss constraints) | V9.1 integrated (24) | Diversified rebuilt (16) | Concentrated (7) | **Core + satellite (8, V10.0)** | Barbell (reference) |
|---|---:|---:|---:|---:|---:|
| Expected CAGR | 7.8% | 13.6% | 15.2% | **14.9%** | n/m (the Continuity Fund already *is* the barbell's safe leg) |
| AI-2027 / 100GW CAGR | 15.5% / 27.2% | 20.9% / 32.8% | 23.5% / 37.0% | **23.4% / 36.9%** | Lower |
| Bust / delay | −67.3% / −41.4% | −59.2% / −24.6% | −62.2% / −23.9% | **−61.8% / −23.9%** | Better, at a large return cost |
| Estimate-sensitive names at the full cap | — | None | CLS, NRG at 15% | **None** | — |
| Fit with the three-fund structure | Good | Good | Fair | **Best** | Duplicates Continuity |
| **Overall (/10)** | 5.5 | 7.6 | 8.3 | **8.8** | 6.0 |

**Why not the barbell:** the Continuity Fund (~50% of investments in FSKAX/FTIHX) already is the defensive leg of a whole-household barbell. Adding defensive ballast inside Event Horizon would dilute the same exposure twice.

#### Portfolio implication

- **Adopt V10.0** (Part VI), subject to Step 4 and the owner's decisions:
    - **Core** (NVDA, META, VRT, MU, NRG, NVT): 82%.
    - **Satellites** (CLS, VST): 18%, each capped at 10%.
- **Governance:**
    - Quarterly architecture review.
    - A satellite gets one failed thesis check before exit.
    - Promotion to core needs two quarters of confirmation plus an expected CAGR above the hurdle.

#### Confidence (1-5) and disconfirming evidence
**Confidence: 4/5.**

- If CLS and NRG convert cash as modeled for two quarters, lift their caps (moving toward the concentrated architecture).
- If the bust materializes and META's −34% fails to cushion it, revisit whether a non-AI ballast belongs in Event Horizon rather than relying on Continuity.

---

## Part IX: Near-Term Deployment Strategy (Summary)

The full plan is in `Analysis 2026-11-08/Deployment Strategy/Deployment Strategy 2026-11-08.md`. Execute it only after V10.0 is adopted (Step 4 and the owner's decisions).

**Summary: about 3 weeks, four tranches, catalyst-aware. Turnover is about 79% from drifted V9.1 weights.**

| Tranche | Window | What happens | Reserve after (% of sleeve) |
|---|---|---|---:|
| T1: fund and pair-swap | Tue Nov 10 – Wed Nov 11 | Exit 17 names with no role in V10.0 (−57.0 pts). Same-theme pair buys: NVT (vs GEV/PWR/BE), META (vs CRWD/PLTR/INTC/MRNA), NRG (vs CEG/CCJ), CLS (vs AMAT/SNPS), VRT (vs ANET/DELL/COHR). Starter MU and VST; one-fifth of NVDA before earnings | ~18.9% |
| T2: upstream rotation | Thu Nov 12 – Fri Nov 13 | Sell AVGO and half of TSM/ASML. Complete META, NRG and NVT; add CLS, VRT, MU | ~7.0% |
| T3: after NVDA | Wed Nov 18 – Fri Nov 20 | Complete the TSM/ASML sales. NVDA under Scenarios A/B/C/D (board review status); complete VRT and VST; MOD gate decision | ~7.7% |
| T4: final | Mon Nov 30 – Thu Dec 3 | Complete NVDA, MU (three weeks before its Dec 23 report) and CLS; band cleanup | ~0% |

**Key rules:**

- Pair each sale with a same-day buy in the same economic theme.
- Never buy above a name's maximum buy price (the price at which its expected return falls to 12%).
- Never buy in the session before a name's earnings.
- Deploy all reserve by **Dec 11** unless the financing-shock or Taiwan scenario is active.
- **Switches:**
    - VST → TLN on a Texas bill.
    - NVDA capped at 8% on an adverse board finding.
    - MOD +5% if its post-spin gate passes.

**Tax note:** on lots bought in May, realized losses (TSM, ASML, CEG, AVGO, GEV, PWR, INTC, MP and others) exceed the gains (MRNA, CRWD, ANET, DELL, PLTR), so the rotation can be roughly tax-neutral. Verify against actual lots.

---

## Appendix A: Methodology, Data Provenance, and Stale-Input Flags

**Process (four-step flow):**

1. **Step 1:** independent deep dives by Claude and by Codex (`inputs/Claude Deep Dive 2026-11-08.md`, `inputs/Codex Deep Dive 2026-11-08.md`).
2. **Step 2:** stock-by-stock cross-critiques (`inputs/Claude Critique of Codex 2026-11-08.md`, `inputs/Codex Critique of Claude 2026-11-08.md`). Each was written without seeing the other.
3. **Step 3 (this report):** pooled ranking and synthesis by Claude. The ranking, disputed inputs, escalations and self-sided audit are in `inputs/Candidate Ranking 2026-11-08.md`.
4. **Step 4 (pending):** the optimization pass by Codex (`PROMPT_4_OPTIMIZATION_PASS.md`), then the owner's decisions.

**Market data.** Prices are Yahoo Finance chart-endpoint closes for Nov 6 and Nov 9, 2026 (last bar 21:00 UTC Nov 9). Consensus estimates, forward P/Es, earnings history, annual diluted EPS, stock-based compensation and shares come from Yahoo quoteSummary and fundamentals-timeseries pulls on the evening of Nov 9, covering 58 pool names plus 32 peers and benchmarks. Accountability returns from May 8 to Nov 6 come from dividend-adjusted daily closes.

**Valuation model (`inputs/research/claude_synthesis/step3_model.py`; run commands in that folder's `README.md`):**

- **Terminal value.** TV at Dec 31, 2030 = 2030 owner EPS × exit multiple + cumulative dividends + explicit cash or credit reserve. Power and neoclouds use (EBITDA × EV/EBITDA − net claims) ÷ diluted shares + dividends. BNTX uses a sum of the parts.
- **States:**
    - Bust: FY2025 owner EPS × 0.7 × base multiple.
    - Plateau: FY2026 owner EPS × 0.85 × base multiple.
    - Base: the resolved base case.
    - Bull: the resolved bull case × 1.2 × base multiple.
    - Bear bucket = ½ bust + ½ plateau.
    - Cyclicals and EV names carry explicit states.
- **Probabilities.** 25/50/25 by default. NRG and VST use 30/45/25 (Texas). KTOS, MP, BNTX and SNDK use 30/50/20. CRWV uses 40/40/20.
- **Owner EPS.** Stock compensation is charged only where consensus excludes it: SBC × (1 − 20% tax) ÷ adjusted EPS, from the latest fiscal year and trailing four quarters.
- **Multiple policy.** The band runs from the stock's own forward P/E to the current peer forward median. In-band values beat out-of-band ones; on a tie, the lower value wins. Single-model values above the band are cut to the band top unless growth earns a premium.
- **Named scenarios.** Metric = base + λ·s·(bull − base) at the base multiple:
    - λ = 0.8 for AI-2027, the $4.2T path's position between the base ($2.8T) and bull ($4.5T) 2030 capex;
    - λ = 2.5 for 100GW, Situational Awareness's $8T at ~0.8 capture;
    - s = each stock's AI-capex sensitivity.
- **Portfolio math.** Expected CAGR = (Σ w · E[TV]/P)^(1/T) − 1. Bust and delay apply every holding's bust and plateau state at once. CAGRs are never averaged.
- **Robustness runs:**
    - every disputed multiple set to Codex's value;
    - bear = bust only (Codex's construction);
    - an extra 10% or 20% common zero-recovery regime.

**Reproduction checks.** In Step 2, Claude's comparison model reproduced Codex's published 22.8% / −56.6% and Claude's 14.7% / −26.6% exactly. Codex's Step 2 model is preserved in `inputs/research/codex_cross_critique/`.

**Stale-input flags `[STALE >30d]`:**

- NVDA Q2 (Aug 26);
- Micron FQ4 prepared remarks (Sep 30);
- Broadcom FQ3 and 10-Q (Sep 2/10);
- Credo FQ1 (Sep 1);
- PJM 2028/29 auction (Jul 14);
- METR frontier risk report (May 19);
- FY27 defense request (Apr 2026);
- AI Futures Q2.5 update (Aug 16).

Each is used only where no newer primary source exists. The next datapoints are listed in Part VII.C.

**Unverified items:**

- Broadcom's ~$43B maximum undiscounted exposure: Codex's citation of the Oct 27 8-K. Adopted as the newer and more conservative figure, but not re-fetched for this report.
- The MOD investor-update date (~Nov 18): from the company's post-spin communications as cited by Codex; not independently confirmed.
- NRG's sold-asset EBITDA (~$0.5B): a modeling assumption, not disclosed.
- The NVIDIA board-review details: from Yahoo/24/7 Wall St (read in full) and CNN's headline. No company filing was found.

**Limits.** The model's probabilities are subjective, not frequencies. The bust stress is a deep, simultaneous scenario, not a loss quantile. Portfolio-level error bands are about ±2pp of CAGR. Taxes, spreads and household overlap are outside the model.

---

## Appendix B: Sources (accessed Nov 8–10, 2026)

**Company releases and filings (primary):**

- [NRG Q3 2026](https://investors.nrg.com/news-releases/news-release-details/nrg-energy-reports-third-quarter-2026-results-reaffirms-2026) and [asset sale](https://investors.nrg.com/news-releases/news-release-details/nrg-energy-announces-4-billion-asset-sale) (Nov 9)
- [Constellation Q3 2026](https://www.constellationenergy.com/news/2026/11/constellation-reports-third-quarter-2026-results.html) (Nov 9)
- [Vistra Q3 2026](https://www.sec.gov/Archives/edgar/data/1692819/000169281926000023/vistra-20260930xearningsre.htm) (Nov 6)
- [nVent Q3 2026](https://www.sec.gov/Archives/edgar/data/0001720635/000162828026068391/q32026nvtpressrelease.htm) (Oct 30); [nVent Q4 2025](https://s22.q4cdn.com/268397047/files/doc_financials/2025/q4/Q4-2025-NVT-Press-Release.pdf)
- [Celestica Q3 2026](https://www.sec.gov/Archives/edgar/data/1030894/000103089426000049/cls-20260930prcondensedfs.htm) (Oct 26); [Celestica FY2025](https://www.sec.gov/Archives/edgar/data/1030894/000103089426000006/cls-20251231prcondensedfs.htm) (Jan 28)
- [ASML Q3 2026](https://www.sec.gov/Archives/edgar/data/0000937966/000162828026065813/pressreleasefinancialresul.htm) (Oct 14)
- [TSMC Q3 2026](https://pr.tsmc.com/english/news/3346) (Oct 15)
- [Micron Q4 FY26 prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf) (Sep 30)
- [Broadcom 10-Q](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm) (Sep 10); [Broadcom 8-K](https://investors.broadcom.com/static-files/0ee4f6b7-4a23-4de0-8f3e-48f147ae30d3) (Oct 27); [Broadcom FY2025 8-K](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000116/avgo-11022025x8kxex99.htm)
- [Meta Q3 2026](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx) (Oct 21); [Meta Q3 2025 8-K](https://www.sec.gov/Archives/edgar/data/1326801/000162828025047114/meta-09302025xexhibit991.htm) (tax charge)
- [Modine Q2 FY27](https://investors.modine.com/news/news-details/2026/Modine-Reports-Second-Quarter-Fiscal-2027-Results/default.aspx) (Nov 3)
- [Coherent FQ1 FY27](https://www.sec.gov/Archives/edgar/data/820318/000119312526447200/d176836dex991.htm) (Nov 4)
- [Kratos Q3 2026](https://www.sec.gov/Archives/edgar/data/1069258/000106925826000085/ktos202609278kexhibit991.htm) (Nov 5)
- [Verisk Q3 2026](https://www.sec.gov/Archives/edgar/data/1442145/000143774926035082/ex_1007822.htm) (Nov 5)
- [BioNTech Q3 2026](https://www.biontech.com/us/en/home/mediaroom/news/press-releases/2026/11/BioNTech-Announces-Third-Quarter-2026-Financial-Results-and-Corporate-Update.html) (Nov 3)
- [Talen Q3 2026](https://ir.talenenergy.com/news-releases/news-release-details/talen-energy-reports-third-quarter-2026-results-reaffirms-2026) (Nov 3)
- [Lam Research Sep-quarter](https://investor.lamresearch.com/2026-10-21-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-September-27,-2026) (Oct 21)
- [SanDisk FY27 Q1](https://investor.sandisk.com/news-releases/news-release-details/sandisk-reports-fiscal-first-quarter-2027-financial-results) (Oct 29)

**News (dated):**

- NVIDIA board review: [Yahoo/24/7 Wall St](https://finance.yahoo.com/markets/stocks/articles/nvidia-falls-5-board-probes-134356169.html), [CNN](https://www.cnn.com/2026/11/09/investing/nvidia-stock-huang-investigation), [Seeking Alpha](https://seekingalpha.com/news/4669027-chip-stocks-minus-nvidia-surge-to-start-trading-week) (Nov 9)
- Texas: [CNN](https://www.cnn.com/2026/11/05/economy/data-center-texas-election) (Nov 5); [ABC13](https://abc13.com/post/governor-elect-gina-hinojosa-vows-ban-future-data-centers-texas/20021143/)
- Chip rebound: [Yahoo Finance](https://finance.yahoo.com/markets/article/nvidia-amd-micron-sandsik-lead-chip-sector-higher-134336542.html) (Nov 9)

**Frameworks:**

- AI-2027: [scenario](https://ai-2027.com/), [race](https://ai-2027.com/race), [summary](https://ai-2027.com/summary), [compute](https://ai-2027.com/research/compute-forecast), [timelines](https://ai-2027.com/research/timelines-forecast), [takeoff](https://ai-2027.com/research/takeoff-forecast), [goals](https://ai-2027.com/research/ai-goals-forecast), [security](https://ai-2027.com/research/security-forecast)
- [AI chip compute workbook](https://docs.google.com/spreadsheets/d/1Ko-olwjDy6h8rXLZBFpP-e2GibGqRhfV28S4v8xtzrM/edit?gid=1866551567)
- [AI-2040](https://ai-2040.com/) and [compute supplement](https://ai-2040.com/supplements/compute-supplement)
- [AI Futures blog](https://blog.aifutures.org/) (including the [Q2.5 2026 update](https://blog.aifutures.org/p/q25-2026-timelines-update-uplift)); [AI Futures model](https://www.aifuturesmodel.com/)
- [Situational Awareness](https://situational-awareness.ai/), [Trillion-Dollar Cluster](https://situational-awareness.ai/racing-to-the-trillion-dollar-cluster/), [PDF](https://situational-awareness.ai/wp-content/uploads/2024/06/situationalawareness.pdf)
- [METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/); [Epoch trends](https://epoch.ai/trends)

---

## Appendix C: Final Verification

- **Allocation checksum:** NVDA 15 + META 15 + VRT 14 + MU 14 + NRG 12 + NVT 12 + CLS 10 + VST 8 = **100.0%** ✓
- **Funding:** every increase has a named funding source; increases +76 = decreases −76 ✓
- **Constraints:** no position above 15%; NRG + VST = 20% ✓
- **Locked structure followed (Parts I–IX):**
    - Model Reconciliation after the Executive Verdict ✓
    - all 15 targeted questions ✓
    - three architectures (plus V9.1 as held) ✓
    - sleeve alternatives ranked Better/Comparable/Worse ✓
    - a valuation table with both named-scenario CAGRs for every holding ✓
- **Pool coverage:** every stock either model held or fully underwrote (58) appears in the ranked table (Part III.C and the Candidate Ranking) ✓
- **No averaging:** no weight or input averages the two models' values. Disputes were resolved by evidence or the tie rule, and are listed with their deciding evidence in the Candidate Ranking §A4.3 ✓
- **Framework coverage:** the AI-2027 / AI-2040 / Situational Awareness subsection covers every source in PROMPT_1 Required Inputs §3 (Part II.C) ✓
- **Status:** V10.0 is marked a proposal pending Step 4 and the owner's decisions. `README.md`'s active allocation is unchanged ✓
- **Outputs:** the Markdown and PDF of this report, the Deployment Strategy (Markdown and PDF), and the Candidate Ranking exist at the required paths (checked at render time) ✓
