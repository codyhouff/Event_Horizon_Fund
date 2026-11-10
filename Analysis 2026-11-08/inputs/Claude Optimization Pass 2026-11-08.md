# Event Horizon Fund — Step 4: Claude Optimization Pass (2026-11-08 cycle)

**Step 4 of 5** (`PROMPT_4_OPTIMIZATION_PASS.md`). **Author:** Claude (Opus 5.5). **Written:** November 10, 2026.

**Independence.** Both models run this step separately. I did not open or use `inputs/Codex Optimization Pass 2026-11-08.md` or its PDF. Their file names appeared in directory listings, and that is the only exposure.

**Self-review warning.** I wrote the Step 3 final under review here. Following the prompt:

- Most of the effort went into the search outside the 58-stock pool.
- Every Step 3 call I keep is flagged in §2–§3 with its evidence.
- The file ends with a self-review disclosure.

**Valuation basis.** Every number uses the **same A1 rules and the same Nov 9, 2026 close** as the final, so the CAGRs compare directly. No Nov 10 bar was available at the time of writing.

- **Shared model:** the Step 3 scripts in `inputs/research/claude_synthesis/`.
- **New candidates:** `step4_model.py` values them on identical rules:
    - bust: FY2025 owner EPS at 0.7× the base multiple;
    - plateau: FY2026 owner EPS at 0.85×;
    - base and bull, with the bull at 1.2× the base multiple;
    - probabilities 25/50/25;
    - named-scenario loadings 0.8 / 2.5;
    - the multiple evidence band.

Each new name's base multiple sits inside its own band, as the holdings' did.

---

## Owner Decision Sheet

**Verdict: no high-conviction change to the V10.0 weights.** I searched about 70 stocks outside the pool and valued 19 carefully on the final's rules. The best of them would add **+0.04 to +0.12pp a year** to the portfolio, well inside the ±2pp error band. Each one would also add either Texas, financing or multiple risk. The pass does find **one input error in the final (AVGO)** and two refinements to the trigger rules.

| ID | Question | Case for | Case against | Recommendation | Weight at stake |
|---|---|---|---|---|---|
| **C1** | **Correct AVGO's base 2030 EPS in the record** ($23.5 → $27.0 owner EPS)? | The final's base sits *below* management's own FY28 target of adjusted EPS "exceeding $30" (Sep 2, reaffirmed Sep 14). It implies earnings decline after FY28, which contradicts the A1 base path. Corrected, AVGO returns **13.5%** expected (not 11.6%), with 21.9% AI-2027 and 34.6% 100GW | Management targets aren't owner earnings. The correction leaves a 13% stock-comp haircut and roughly a two-year slip. Even corrected, AVGO doesn't beat any holding by a meaningful margin | **Accept** (record only; no weight change). AVGO becomes the first name on the bench (C3) | 0 now |
| **C2** | **Swap VST 8% → STRL 8%** (Sterling Infrastructure, data-center site work)? | STRL beats VST on every stock metric: expected 14.6% vs 13.0%, AI-2027 21.6% vs 20.2%, 100GW 33.6% vs 26.8%, delay −13% vs −29%. The portfolio's expected CAGR rises 0.12pp | Three problems: **(a)** STRL's lead depends entirely on a 14× exit (the evidence band runs from its own 10.3× to peers at 15.5×); at 12× it returns 10.4%, at its own 10.3× 6.4%. **(b)** Its growth is concentrated in **Texas** (the CEC acquisition), so the swap doesn't cut the Texas risk VST carries. **(c)** It adds an eighth AI-capex construction exposure | **Reject now; watchlist.** Revisit if STRL's Q4 (Feb 2027) shows signed book-to-burn ≥ 1.1 and stable margins | 8 |
| **C3** | **Name a bench**, so capital freed by any trigger has a pre-agreed destination? | Today several triggers (Parts VII and IX) send capital to TSM, TLN or the reserve on an ad hoc basis. A ranked bench makes them consistent | Adds a rule to maintain | **Accept.** Bench in order: **AVGO** (13.5%, after C1); **STRL** (14.6%, multiple-sensitive); **AEIS** (13.4%, rack power); **TLN** (12.7%, for power and the Texas switch); **TSM** (11.8%, for a Taiwan-safe scenario reversal) | 0 now |
| **C4** | **Keep TLN as the Texas-switch target** (E3), not STRL? | TLN is PJM-based, so it actually reduces Texas exposure | TLN's expected return (12.7%) is below STRL's (14.6%) | **Accept:** keep TLN. STRL is Texas-concentrated | 8 (conditional) |
| E1 | **MOD:** add now or after the post-spin update? (Step 3) | Ranks #1 of 58 (18.7%) | Five-week-old perimeter; H1 FCF negative | **Gate (unchanged).** No new evidence | 5 |
| E2 | **NVDA 15% or 12%** during the CEO board review? (Step 3) | 17.8% expected, #2 of 58 | Unresolved key-person and China-relations risk | **15%, deployed after Nov 17 (unchanged)** | 3 |
| E3 | **Texas power:** keep VST, or switch now? (Step 3) | VST beats TLN by 0.3pp expected and 0.9pp on AI-2027 | A Texas moratorium is pledged | **Keep VST; automatic switch to TLN on a Texas bill (unchanged; see C4)** | 8 |
| E4 | **META at 15%** (an AI buyer in an infrastructure fund)? (Step 3) | #5 of 58; −34% bust, the mildest of the top names | Continuity overlap; mandate scope | **15% (unchanged).** The outside search found no infrastructure name with comparable expected return and bust | 15 |
| E5 | **8 names or 16?** (Step 3) | 8: 14.9% expected | 16: −59.2% bust (vs −61.8%) | **8 (unchanged).** Adding the best outside names doesn't improve the bust either | All |

**Portfolio after accepting everything recommended:** unchanged from V10.0: **14.9% Expected / 23.4% AI-2027 / 36.9% 100GW / −61.8% bust / −23.9% delay.** Checksum 100.0%.

---

## 1. Top 20 Alternatives

**Search scope:** about 70 US-listed stocks and liquid ADRs outside the 58-stock pool, in four steps:

1. Pull Nov 9 consensus, multiples, earnings history and stock-comp data.
2. Run a mechanical A1 screen with holdings-consistent treatment: peer-median exit multiples and a bull case about 1.4× base.
3. Research the strongest 15 at their latest primary releases (Q3 2026).
4. Value 19 carefully, plus a re-underwrite of one pool name (AVGO) where I think the ranking got it wrong.

**All 19 outside names are new to the Step 3 pool.**

- **Screened in Step 1 and rejected there:** GNRC, SBGSY, CMI, FIX, EME, ASX, WDC, STX, ORCL, ONTO and others. Those rejections are re-examined below.
- **New to this cycle:** STRL, AEIS, AAON, DY, MKSI, WCC, ON, APH, Infineon (IFNNY) and KLIC.

| Rank | Ticker | Bottleneck / theme | Competes with | Price (Nov 9) | Valuation status | Expected CAGR vs held ticker's | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Verdict | Why or why not (detail in note) |
|---:|---|---|---|---:|---|---|---:|---:|---|---|
| 1 | **STRL** | Data-center site work | VST (8%) / NVT | $290.67 | Attractive, if 14× holds | **14.6% vs VST 13.0%** | 21.6% | 33.6% | **Watchlist (C2)** | Wins only at 14×; Texas-heavy [1] |
| 2 | **ORCL** | OCI cloud capacity | META (15%) | $119.79 | Speculative (financing) | 13.6% vs META 15.0% | 21.3% | 33.8% | **Reject** | Financing chain; FCF −$45.9B [2] |
| 3 | **AVGO*** | Custom silicon | VST / MU | $319.48 | Fair | **13.5% vs VST 13.0%, MU 13.1%** | 21.9% | 34.6% | **Watchlist, bench #1 (C1, C3)** | Ranking erred; still ≈ bottom holdings [3] |
| 4 | **AEIS** | Rack power supplies | VRT (14%) / NVT | $219.30 | Attractive, if 17× holds | 13.4% vs VRT 13.8%, NVT 13.7% | 21.6% | 34.4% | **Watchlist, bench #3** | Below VRT/NVT; 10.1% at 15× [4] |
| 5 | **MKSI** | Semi subsystems | MU (14%) | $211.59 | Fair (cyclical) | 12.1% vs MU 13.1% | 19.7% | 32.2% | **Reject** | Cyclical; MU wins all three [5] |
| 6 | **SBGSY** | Electrical + cooling | NVT (12%) | $52.71 | Fair | 10.7% vs NVT 13.7% | 15.1% | 22.5% | **Reject** | 3pp below NVT [6] |
| 7 | **GNRC** | Data-center gensets | NVT / VST | $188.75 | Fair | 10.4% vs NVT 13.7% | 15.6% | 24.1% | **Reject** | Residential cycle; −84% bust [7] |
| 8 | **DY** | Fiber construction | NVT | $219.93 | Fair | 9.9% vs NVT 13.7% | 13.8% | 20.5% | **Reject** | Telecom-weighted [8] |
| 9 | **ASX** | Packaging / test | MU / CLS | $34.36 | Fair | 9.6% vs MU 13.1% | 17.4% | 29.5% | **Reject** | Not the tight layer [9] |
| 10 | **CMI** | Gensets (diversified) | VST / NVT | $466.47 | Fair | 9.2% vs VST 13.0% | 11.4% | 15.9% | **Reject** | Low AI purity [10] |
| 11 | **ON** | SiC power semis | MU | $69.11 | Fair | 8.8% vs MU 13.1% | 12.8% | 20.0% | **Reject** | Auto-weighted [11] |
| 12 | **AAON** | Liquid cooling | VRT (14%) | $62.87 | Fair | 8.8% vs VRT 13.8% | 15.6% | 26.8% | **Reject** | Backlog fell q/q [12] |
| 13 | **WDC** | HDD storage | MU (14%) | $289.78 | Deep Discount on consensus, but cyclical | 8.0% vs MU 13.1% | 17.7% | 30.6% | **Reject** | Cyclical; 8% normalized [13] |
| 14 | **APH** | Interconnect | CLS / NVT | $80.71 | Expensive | 7.8% vs CLS 14.8% | 13.6% | 23.7% | **Reject** | 22.3× priced [14] |
| 15 | **FIX** | MEP contractor | NVT / VRT | $1,113.23 | Fair-to-Expensive | 7.7% vs NVT 13.7% | 13.5% | 23.7% | **Reject** | Backlog priced at 16.6× [15] |
| 16 | **WCC** | Electrical distribution | NVT | $316.47 | Fair | 6.9% vs NVT 13.7% | 10.4% | 16.8% | **Reject** | Mid-single-digit 2027 [16] |
| 17 | **KLIC** | TCB bonding | MU | $68.97 | Speculative (cyclical) | 6.6% vs MU 13.1% | 14.4% | 26.1% | **Reject** | −95% bust [17] |
| 18 | **EME** | E&M contractor | NVT | $652.89 | Fair | 6.2% vs NVT 13.7% | 10.0% | 17.3% | **Reject** | Low growth [18] |
| 19 | **STX** | HDD storage | MU | $506.14 | Fair (cyclical) | 5.6% vs MU 13.1% | 15.1% | 27.8% | **Reject** | As WDC, less upside [19] |
| 20 | **IFNNY** | Power semis | MU | $55.80 | Expensive | 5.6% vs MU 13.1% | 9.7% | 15.1% | **Reject** | Auto-heavy; priced [20] |

**Notes by rank (the full reasoning behind each verdict):**

1. ****STRL**** (Data-center site development (E-Infrastructure); Q3 revenue +127%, combined backlog $6.14B (+78%)): Wins on every metric at 14×; 10.4% at 12×, 6.4% at its own 10.3×. Texas-concentrated. Signed book-to-burn was 0.9 in Q3; mix-driven margin pressure
2. ****ORCL**** (OCI capacity; backlog $638B (Jun), more than half OpenAI): Trailing FCF −$45.9B; debt $169B; the backlog rests on the financing chain the portfolio deliberately avoids. Bust −67%. Step 1 rejected it for "OpenAI-financing dependence," and nothing has changed
3. ****AVGO** (re-underwritten; pool)** (Custom silicon + networking): The ranking got it wrong: base EPS $23.5 → $27 owner, consistent with management's FY28 adjusted EPS > $30. Still within 0.4pp of the bottom holdings, with a worse bust (−73%) and delay (−44%) than VST. Up to ~$43B of guarantee exposure
4. ****AEIS**** (AI rack power supplies + semi plasma power; Q3 revenue +50%, data center +49%): Below both thermal and electrical holdings. 10.1% at 15×. Stock comp ~13% of adjusted EPS; FCF roughly zero in the trailing twelve months
5. ****MKSI**** (Semi subsystems + advanced packaging chemistry; semi sales +54%): WFE-cyclical, and $1.4B of convertibles are convertible this quarter. MU wins on all three returns
6. ****SBGSY**** (Schneider: electrical + cooling (Motivair)): Step 1: "comparable, overlaps." That still holds: −53% bust, but 3pp less expected
7. ****GNRC**** (Data-center backup gensets; data-center backlog $1.6B → ~$4.5B (Amazon)): Step 1 rejected the "residential mix." The new backlog is real, but residential cyclicality and lower data-center margins hold it to 10.4%, with a −84% bust
8. ****DY**** (Fiber and data-center connectivity construction; backlog $12.2B (+53%)): Telecom-weighted; 9%/yr base growth
9. ****ASX** (ASE)** (OSAT / advanced packaging + test): Step 1: "CoWoS loosened." Packaging is no longer the tightest layer
10. ****CMI**** (Gensets / power systems (diversified)): Low AI purity (s = 0.4); bust −46% is mild, but the expected return is too low
11. ****ON**** (SiC / power semis for 800V DC racks): Auto-weighted; AI power is a small share
12. ****AAON**** (Data-center liquid cooling (BASX sales +218%)): Backlog fell about $100M sequentially in Q3; gross margin fell to 26.7%; 2027 consensus already assumes +46% EPS
13. ****WDC**** (HDD duopoly; nearline storage for AI; revenue per EB +28%): 7.2× FY28E looks cheap, but with MU-consistent normalization (FY28 EPS −21% by 2030, milder than MU's −47%) it returns 8%. Step 1: "lower bottleneck intensity than HBM"
14. ****APH**** (Interconnect (AI racks, power)): High quality, but 22.3× forward
15. ****FIX**** (MEP contractor; backlog $17.8B (+90%)): Step 1: "permission-exposed; priced." The backlog surge is real, but 16.6× on 2027 E +32% already prices it; margin dilution started in Q3
16. ****WCC**** (Electrical/datacom distribution; data-center sales +55%): 2027 sales guided to mid-to-high single digits; leverage 2.8×
17. ****KLIC**** (Thermocompression bonding (advanced packaging)): FY25 EPS ~0 makes its bust −95%
18. ****EME**** (Electrical/mechanical contractor): Lower growth than FIX
19. ****STX**** (HDD duopoly): Same normalization as WDC; less upside
20. ****IFNNY** (Infineon)** (Power semis (AI DC, auto)): Auto-heavy; 2027 consensus +72% already priced

\* AVGO is a pool name re-underwritten here because the ranking got its base EPS wrong (C1).

**Also screened, below ~10% on holdings-consistent rules, not shown:**

- HUBB, TT, JCI, CARR, SPXC, LII, CAT, BKR, PRIM, MTZ, IESC;
- CIEN, GLW, AAOI, CSCO, QCOM, ARM, MPWR, VICR;
- TER, ONTO, CAMT, ENTG, AMKR, TSEM, UMC, COHU, BELFB, NVTS, SMCI;
- EQT, WMB, KMI, NEE, PEG, LEU, BWXT, OKLO;
- EQIX, DLR, FCX;
- LMT, NOC, GD, LHX, KRMN;
- NOW, APP, ADBE, CRM.

**What the search shows:**

- **The market prices the obvious second-order AI-infrastructure winners fully.** Electrical, thermal and construction leaders trade at 16–24× forward on 2027 consensus that already includes 20–45% growth.
- **The cheap-looking names are cyclical,** including storage (WDC, STX) and equipment (MKSI, KLIC). Under the same normalization the final applied to MU, they fall below MU.
- **Only names whose cheapness is a contested multiple come close** (STRL, AEIS), and they land within ±1.6pp of the weakest holdings.

**Full underwriting for the names closest to the portfolio.** No candidate earned an Add or Replace verdict. The five that come within about 1.6pp of the weakest holding, in either direction, are shown on the same rules as the final's IV.D table:

| Ticker | Bear / Base / Bull TV (bust / plateau inside bear) | Probabilities | E[TV] | Implied Expected CAGR | Key assumptions | What would falsify it |
|---|---|---|---:|---:|---|---|
| STRL | $172 ($92 / $252) / $508 / $853 | 25/50/25 | $510 | 14.6% | Owner EPS FY25 $9.38 / FY26 $21.18 / 2030 base $36.28 (2027E $28.10 +10%/yr) / bull $50.79. Exit 14× (band 10.3–15.5×). No dividend | Signed book-to-burn < 1.0 for two quarters; E-Infrastructure margin compression; a Texas moratorium hitting campus starts |
| AVGO (revised) | $133 ($86 / $180) / $551 / $921 | 25/50/25 | $539 | 13.5% | Owner EPS $5.93 / $10.15 / **$27.0** / $37.7. 20×. ~$13 dividends; −$2 credit reserve in the base. FY28 target > $30 adjusted (Sep 2026) | FY28 AI target cut; guarantee impairments; Anthropic or OpenAI program delays (Dec 9 report) |
| ORCL | $68 ($40 / $96) / $204 / $337 | 25/50/25 | $203 | 13.6% | Owner EPS bust $3.0 (OpenAI-failure state) / FY27E $6.85 / 2030 base $13.05 / bull $18.27. 15× (band 10.8–22.5×, financing discount) | OpenAI funding failure; debt beyond ~$290B; a credit-rating cut |
| AEIS | $102 ($47 / $158) / $374 / $628 | 25/50/25 | $370 | 13.4% | Owner EPS $3.84 / $10.80 / $21.92 / $30.68. 17× (band 12.2–~20×). Stock comp 13% | 2027 growth below the ~30% indicated; data-center share loss to in-house power designs |
| MKSI | $117 ($50 / $184) / $339 / $566 | 25/50/25 | $340 | 12.1% | Owner EPS $4.37 / $14.09 / $22.30 / $31.22. 15×. Convertibles dilutive | WFE downturn in 2028; packaging-chemistry share loss |

Every other name's inputs (bust, plateau, base and bull EPS, multiples, dividends, AI sensitivity, band) are in `inputs/research/claude_synthesis/step4_model.py` and `data/step4_out.json`.

---

## 2. Weakest Current Holdings

**All eight holdings ranked** by expected CAGR, with conviction as the tie-break (confidence 1–5):

| Rank | Ticker | Final % | Expected CAGR | AI-2027 | 100GW | Bust | Confidence |
|---:|---|---:|---:|---:|---:|---:|:---:|
| 1 | NVDA | 15 | 17.8% | 26.8% | 41.5% | −63% | 4 |
| 2 | NRG | 12 | 17.1% | 24.9% | 35.6% | −67% | 3 |
| 3 | META | 15 | 15.0% | 20.0% | 33.9% | −34% | 3 |
| 4 | CLS | 10 | 14.8% | 23.2% | 35.6% | −75% | 3 |
| 5 | VRT | 14 | 13.8% | 22.0% | 34.9% | −72% | 3 |
| 6 | NVT | 12 | 13.7% | 21.4% | 34.0% | −60% | 3 |
| 7 | MU | 14 | 13.1% | 26.8% | 45.3% | −64% | 3 |
| 8 | VST | 8 | 13.0% | 20.2% | 26.8% | −67% | 3 |

**Bottom five:**

| Ticker | Final % | Expected CAGR | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Main weakness | Best replacement (from §1 or another holding) | Keep / Trim / Replace | Why |
|---|---:|---:|---:|---:|---|---|---|---|
| VST | 8 | 13.0% | 20.2% | 26.8% | Lowest expected and AI-2027 return in the portfolio; Texas moratorium risk | STRL (14.6%), AVGO (13.5%), TLN (12.7%) | **Keep** | The best swap adds only 0.04–0.12pp. STRL shares the Texas risk; AVGO worsens bust and delay; TLN lowers expected return. The E3 switch to TLN stays as the defined trigger |
| MU | 14 | 13.1% | **26.8%** | **45.3%** | Cyclical; the base is 47% below FY28 consensus | AVGO (13.5%) | **Keep** (own Step 3 call, flagged) | Inside the 2pp band, MU has the highest AI-2027 and 100GW CAGRs of any candidate, in or outside the pool. That is PROMPT_1's tie-break. MU 14 → 10 with AVGO +4 changes expected return by +0.01pp and lowers AI-2027 by 0.2pp |
| NVT | 12 | 13.7% | 21.4% | 34.0% | Maverick integration; Q4 organic growth slowing to 26–29% | STRL (14.6%, multiple-sensitive), SBGSY (10.7%) | **Keep** | No outside electrical name comes within 1pp except STRL, at a contested multiple |
| VRT | 14 | 13.8% | 22.0% | 34.9% | Order disclosure discontinued | AEIS (13.4%), AAON (8.8%) | **Keep** | AEIS is close but below, with weaker FCF |
| CLS | 10 | 14.8% | 23.2% | 35.6% | Cash conversion (FY26 FCF $460M) | AEIS / STRL | **Keep at the 10% cap** (own Step 3 call, flagged) | Its expected return ranks #4 of the holdings. The cap is about estimate risk, not return |

---

## 3. Allocation Optimization

**Weights against expected return and confidence:**

- **Capped below their rank:** NRG (#2, 12%) and CLS (#4, 10%) sit below names that rank lower.
    - **Own call, kept.** Both caps rest on evidence that a return estimate can't capture:
        - NRG: ~$22.8B of net claims against ~$19.5B of equity; the asset sale isn't closed; Texas was 51% of Q3 EBITDA.
        - CLS: FCF is ~35% of net income; an equity raise closed Aug 7.
    - Lifting both to 15% (the concentrated architecture) adds 0.3pp, inside the error band.
- **Above its rank: MU** (#7 of 8, 14%).
    - **Own call, kept.** The evidence is PROMPT_1's tie-break: MU leads every candidate on AI-2027 (26.8%) and 100GW (45.3%), and it is the portfolio's only exposure to the HBM/EUV constraint.
- **At the cap: NVDA and META.** No outside name offers comparable expected return with comparable conviction.

**Concentration:**

| Cluster | Weight | Holdings |
|---|---:|---|
| C1 AI silicon, memory and integration | 39% | NVDA, MU, CLS |
| C3 Data-center physical and electrical | 26% | VRT, NVT |
| C4 Power generation | 20% | NRG, VST; all Texas-exposed (cap 20%) |
| C5 AI platform | 15% | META |

Every outside alternative that comes close (STRL, AEIS, AVGO, ORCL) would *add* to C1 or C3, or bring in Texas or financing exposure. None would diversify a driver. **Eight holdings remains the right count.**

**Tested variants** (same model, Nov 9 prices):

| Portfolio | Expected CAGR | AI-2027 | 100GW | Bust | Delay |
|---|---:|---:|---:|---:|---:|
| **V10.0 final (Step 3)** | **14.93%** | **23.43%** | **36.88%** | **−61.8%** | **−23.9%** |
| VST 8 → STRL 8 | 15.05% | 23.54% | 37.35% | −61.9% | −22.6% |
| VST 8 → AVGO 8 (revised) | 14.97% | 23.56% | 37.42% | −62.3% | −25.0% |
| VST 8 → AEIS 8 | 14.97% | 23.54% | 37.41% | −62.7% | −23.8% |
| VST 8 → AVGO 4 + STRL 4 | 15.01% | 23.55% | 37.38% | −62.1% | −23.8% |
| VST 8 → TLN 8 | 14.91% | 23.37% | 36.91% | −61.2% | −24.3% |
| MU 14 → 10, AVGO +4 | 14.94% | 23.23% | 36.42% | −62.2% | −24.7% |

**Result: no changes.**

- The best variant (VST → STRL) adds 0.12pp a year. That is 1/16th of the model's error band, and it rests on a contested 14× multiple for a Texas-concentrated contractor. It is a cosmetic change.
- No variant improves the bust case except TLN, which lowers expected return.
- **The final is already the better portfolio on the evidence available at Nov 9.**

**Proposed allocation (unchanged):** NVDA 15, META 15, VRT 14, MU 14, NRG 12, NVT 12, CLS 10, VST 8.

**Checksum: 100.0%.** Before = after: 14.9% Expected / 23.4% AI-2027 / 36.9% 100GW / −61.8% bust.

---

## 4. Sanity Check (flags only)

| # | Check | Result |
|---:|---|---|
| 1 | Allocation sums to 100.0%; weights match across the final's tables and the Deployment Strategy | **OK.** The final's Part I.B and Part VI and the Deployment Strategy's destination table all show 15/15/14/14/12/12/10/8 |
| 2 | Spot-recompute expected CAGR for the 5 largest holdings from stated inputs | **OK.** NVDA 17.80, META 14.95, VRT 13.84, MU 13.09, NRG 17.07 reproduce exactly from the bust/plateau/base/bull values and probabilities |
| 3 | Any stock either model held or fully underwrote that's missing from the ranking | **OK.** All 58 are present |
| 4 | Top-ranked stocks left out, or low-ranked included, without explanation | **OK.** MOD (#1), CRWV (#4), the NRG/CLS caps and MU's tie-break are all explained in A5 and Part III.C |
| 5 | Any weight that is just an average | **OK, with one note.** CLS 10% lies between Claude's 7% and Codex's 12%. It's justified by a stated cap (cash conversion), not by averaging, but the cap value is a judgment |
| 6 | **AVGO base EPS** | **Flag (C1):** below management's FY28 target, which contradicts the A1 base path. Corrected value 13.5% |
| 7 | TSM base EPS ($33) vs TSMC's target | **OK.** TSMC raised its 2024–29 USD revenue CAGR target to "approaching 25%" (Jan 2026). With 2026 already ~$178B, that implies ~15–16%/yr to 2029 and 2030 EPS near ~$35, close to the final's $33 |
| 8 | Texas-switch target (E3) | **OK, with a note (C4):** keep TLN. STRL, which scores higher, shares the Texas exposure |
| 9 | Price staleness | No Nov 10 close yet. Re-check any holding that moves more than 10% before Step 5 Phase A, as PROMPT_5 requires |

---

## Self-Review Disclosure

I wrote the Step 3 final.

**Changed in my own work:** one input. AVGO's base 2030 EPS ($23.5 → $27.0 owner EPS). In Step 3 I adopted Codex's owner-basis value ($23.5) without checking it against management's FY28 target, which was already public (Sep 2). The correction raises AVGO from 11.6% to 13.5% expected. That is still not enough to change a weight, but the record should carry the corrected figure.

**Kept from my own Step 3 work, with the deciding evidence:**

1. **No change to the eight weights:** the best alternative adds 0.04–0.12pp (§3 table).
2. **MU at 14% above its rank:** it has the highest AI-2027 and 100GW CAGRs of any candidate inside or outside the pool, and it is the only HBM/EUV exposure.
3. **NRG and CLS caps:** NRG's leverage and unclosed sale; CLS's FCF at ~35% of net income and its Aug equity raise.
4. **TLN as the Texas switch:** STRL is Texas-concentrated (company and Zacks commentary on CEC's Texas presence).
5. **Holding the multiple policy fixed for new names:** each new name's multiple was placed inside its own band, as the holdings' were. STRL's and AEIS's sensitivities are shown explicitly, because their ranking depends on that choice.

**Where a reviewer without my stake might disagree:**

- **STRL:** a reviewer who accepts the 14× multiple and discounts the Texas overlap could reasonably swap VST → STRL. The cost of being wrong either way is about 0.1pp a year.
- **MU vs AVGO** at the margin.

Both are listed on the Owner Decision Sheet so you can decide.

---

**Sources** (accessed Nov 10, 2026):

- Advanced Energy Q3 2026: [8-K](https://www.sec.gov/Archives/edgar/data/0000927003/000092700326000037/aeis-ex99d1.htm); [call summary](https://www.mitrade.com/insights/news/live-news/article-8-2224538-20261103)
- Sterling Q3 2026: [8-K](https://www.sec.gov/Archives/edgar/data/0000874238/000087423826000122/a20261028ex991earningsrele.htm); [StockStory](https://stockstory.org/us/stocks/nasdaq/strl/news/earnings-call/strl-q3-deep-dive-infrastructure-demand-drives-growth-margin-mix-shifts-prompt-scrutiny); [Texas concentration, Zacks via finanzen.net](https://www.finanzen.net/nachricht/aktien/sterling-s-e-infrastructure-boom-continues-can-data-centers-keep-up-15555300); [Simply Wall St](https://simplywall.st/stocks/us/capital-goods/nasdaq-strl/sterling-infrastructure/news/sterling-infrastructure-puts-e-infrastructure-and-data-cente)
- Generac Q3 2026: [8-K](https://www.sec.gov/Archives/edgar/data/0001474735/000143774926033685/ex_1032565.htm); [24/7 Wall St](https://247wallst.com/cards/generac-q3-2026-earnings-gnrc-01m60ztbceak40kt17w5zvbg6m)
- Western Digital / Seagate: [Blocks & Files, Oct 23](https://www.blocksandfiles.com/disk/2026/10/23/wd-knocks-earnings-out-of-the-park-again/5304988); [Zacks](https://www.zacks.com/stock/news/3015774/wdc-s-fiscal-q2-forecast-improves-what-s-fueling-the-momentum)
- Broadcom FY28 targets: [TIKR](https://www.tikr.com/blog/broadcom-stock-has-gone-nowhere-in-2026-despite-doubling-ai-revenue-heres-what-tan-said-next); [DCD](https://www.datacenterdynamics.com/en/news/broadcom-slams-ai-silicon-fueled-q3-promises-double-double-on-the-way/); [Crypto Briefing (reaffirmation)](https://cryptobriefing.com/broadcom-ceo-reaffirms-ai-revenue-targets/)
- Oracle: [SiliconANGLE, Jun 10](https://siliconangle.com/2026/06/10/oracles-ai-investments-spook-investors-despite-another-impressive-earnings-revenue-beat/); [Yahoo Finance](https://finance.yahoo.com/news/analysts-slash-oracle-orcl-price-105755728.html)
- Comfort Systems Q3 2026: [8-K](https://www.sec.gov/Archives/edgar/data/0001035983/000110465926118156/fix-ex99d1.htm); [Finviz](https://finviz.com/news/407457/comfort-systems-posts-a-record-178-billion-backlog-and-raises-guidance-again-as-margins-slip-and-shares-sit-near-30-lower)
- Wesco Q3 2026: [8-K](https://www.sec.gov/Archives/edgar/data/0000929008/000092900826000029/wcc-3q2026earnings.htm); [Distribution Strategy](https://distributionstrategy.com/2026/10/wesco-q3-sales-rise-16-6-earnings-climb-42-8-as-data-center-demand-grows/)
- MKS Q3 2026: [8-K](https://www.sec.gov/Archives/edgar/data/0001049502/000119312526447410/mksi-ex99_1.htm)
- Dycom Q2 FY27: [release](https://dycomind.gcs-web.com/node/20776/html)
- AAON Q3 2026: [8-K](https://www.sec.gov/Archives/edgar/data/0000824142/000082414226000083/liveaaonpressreleaseexs.htm); [10-Q](https://www.sec.gov/Archives/edgar/data/0000824142/000082414226000088/aaon-20260930.htm)
- TSMC long-term targets: [KGI, Jan 2026](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/tsmc_2330-tt_15012026e.pdf); [Design & Reuse](https://www.design-reuse.com/news/202529963)

*Model files:*

- `inputs/research/claude_synthesis/step4_model.py`
- `data/step4_snap.json` (Nov 9 snapshot of ~70 outside names)
- `data/step4_out.json`

*Run:*

```bash
python -I step4_model.py data/step3_out.json data/step4_snap.json data/step4_out.json
```
