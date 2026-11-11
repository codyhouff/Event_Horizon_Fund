# Event Horizon Fund — Step 6 Independent Final Review

**Reviewer:** Codex. **Review date:** November 10, 2026. **Cycle:** November 8, 2026. **Synthesis model:** Claude. **Reviewed:** adopted V10.1. **Result:** **V10.2 adopted after Step 6 review.** The price date remains **November 9, 2026 close**; terminal date remains December 31, 2030.

## 1. Summary

**The adopted portfolio needed a small rule-driven correction, not a rebuild.** The already-tested STRL-8 alternative passes the second branch of PROMPT_5 rule 2. D4 incorrectly rounded its advantage to “within noise” and treated the 6% residual as if the other allocation were unavailable. Move **STRL 6 → 8%, VRT 15 → 14%, MU 15 → 14%**. Every other holding and weight stays unchanged.

- **Reproduction: PASS, before judgment or edits.** Both Step 5 output JSON files, all five `tables5/` Markdown files, and `drift_nov9.json` matched byte for byte in scratch. No original output was overwritten.
- **Decisions:** **3 Upheld, 10 Upheld with correction, 1 Overturned (D4 sizing only)**; all D1–D14 audited.
- **Findings:** **31 fixed findings (F02–F32)**, grouped by root cause rather than repeated occurrence; **5 noted/no-change findings (F01, F33–F36)**. Recommendations are separately listed below. Fixes include the sizing correction, not 31 separate investment decisions.
- **Self-siding attribution, mutually exclusive:** **Codex 6** (D2, D6, D8, D11, D12, D13); **Claude 4** (D1, D3, D5, D10); **both 3** (D7, D9, D14); **mixed/neither 1** (D4). Total 14. These counts describe the substantive outcome relative to the passes, not a model accuracy score. D4 retains Codex's inputs and Claude's VST funding, but adopts neither author's proposed size.
- **Own rejected proposals:** WCC remains rejected, including after fixing its duplicate SBC charge; NVT-funded STRL-5 is not restored; neither SANM nor ONTO is added; no higher-multiple policy is imported. The changed size is the exact alternative already in Claude's Step 5 portfolio set, not a newly invented optimization.
- **Records:** Step 1–5 files, Decision Log, Candidate Ranking and existing superseded files were left unchanged. Copies of the final and Deployment Strategy MD/PDF were preserved as **“V10.1 before Step 6”** before edits. New code/data are confined to `inputs/research/codex_final_review/`.
- **Execution:** no orders, account changes, commits or pushes were made. The Deployment Strategy remains local/gitignored.

### Before and after: same model, prices and caps

| Holding | V10.1 | V10.2 | Change |
|---|---:|---:|---:|
| NVDA | 15% | 15% | — |
| META | 15% | 15% | — |
| VRT | 15% | 14% | −1pp |
| MU | 15% | 14% | −1pp |
| NRG | 12% | 12% | — |
| NVT | 12% | 12% | — |
| CLS | 10% | 10% | — |
| STRL | 6% | 8% | +2pp |
| **Total** | **100%** | **100%** | **0** |

| Metric | Step 5 V10.1 | Step 6 V10.2 | Change (pp) |
|---|---:|---:|---:|
| Expected CAGR | 15.3604% | 15.4847% | +0.1243 |
| AI-2027 Scenario CAGR | 24.0352% | 24.1243% | +0.0891 |
| 100GW 2030 Scenario CAGR | 38.1021% | 38.1747% | +0.0726 |
| Bust total return | -61.5326% | -61.4798% | +0.0528 |
| Delay total return | -22.3491% | -22.1233% | +0.2258 |

The unrounded Expected gain is **0.1243311483pp**, AI-2027 **0.0890722351pp**, and the bust **improves 0.0528019562pp**. Rule 2 requires +0.25pp Expected **or** +0.1pp Expected with higher AI-2027 and no more than 1pp worse bust. The second branch passes. The WCC input correction has **zero effect on this test**, since neither portfolio owns WCC; every held-name valuation input is unchanged.

**Constraint proof:** max position 15%; NRG/NVT 12%; CLS 10%; STRL 8% below the adopted 10% satellite limit; NRG + STRL **20%**, exactly the existing Texas limit; C1 **39%** below 50%; eight names; no leverage or options; Moonshot 0%; Foundation and Continuity unchanged. V10.2's bust remains milder than V9.1's −67.3%. D4 explicitly described 6% as a *residual*, not a newly adopted hard cap. Codex's earlier 5% recommendation was not the adopted constraint. No cap was relaxed to obtain this result. If the owner wants a new hard STRL ceiling below 8%, that is a new constraint and needs a new funded allocation.

**Small is not certain:** the formal pass is much smaller than the model's roughly ±2pp error band. It satisfies the owner's stated rule; it is not statistically demonstrated investment superiority. V10.2 has more contractor/Texas exposure, and reaches the Texas cap. A different preference for project risk would be a new owner constraint, not grounds to silently ignore rule 2.

## 2. Reproduction and numerical provenance

The three Step 5 commands in `claude_synthesis/README.md` ran with that directory as working directory, redirecting both model outputs and all table/data destinations into:

`C:/Users/00MrK/AppData/Local/Temp/ehf_step6_eb701102b07a4717b8c1b19391edb9a9`

That scratch folder contains the runner and command outputs. Persistent evidence is `codex_final_review/data/reproduction.json`, including full original/reproduced SHA-256 hashes. All eight comparisons passed:

| Artifact | SHA-256 prefix (full hash in manifest) | Result |
|---|---|---|
| `step5_out.json` | `f32a910c2f79d70f` | Identical |
| `step5_out_cxmult.json` | `f538a694c2d985c9` | Identical |
| `drift_nov9.json` | `104010807ed263d5` | Identical |
| `destination5.md` | `5922728f6126b87d` | Identical |
| `pool5.md` | `cb3cd14b70217490` | Identical |
| `portfolios5.md` | `748bdeaf040d5027` | Identical |
| `recon5.md` | `e40ecad057870573` | Identical |
| `trades5.md` | `3980c30cb6385ca9` | Identical |

`review_model.py` runs the unchanged Step 5 evaluator in memory, asserts that its initial outputs still match, adds V10.2 and three funded conditional portfolios, applies only the WCC duplicate-factor correction, and redirects generated tables to `tables6/`. The portfolio aggregation remains expected terminal wealth followed by annualization; it does not average CAGRs. Price snapshot, horizon, scenario probabilities, sensitivity coefficients, multiple policies and held-name operating bridges remain unchanged. The 60-name pool retains the **Step 5 ordinal order**; WCC's changed return does not cause re-ranking.

Key outputs: `data/rule2_test.json`, `step6_out.json`, `step6_out_cxmult.json`, `ports6.json`, `strl_multiple_sensitivity.json`, `tranche_ledger.json`, `cash_path.json`, and `tables6/`. The independent current-price check is `quote_audit.json`; PJM's public schedule is captured in `pjm_calendar.json`. Source metadata for AVGO/VRT/NVT/STRL is corrected in the overlay, not in historical records.

Re-run from the repository root:

```powershell
python -X utf8 "Analysis 2026-11-08/inputs/research/codex_final_review/review_model.py"
python -X utf8 "Analysis 2026-11-08/inputs/research/codex_final_review/protect_records.py"
python -X utf8 "Analysis 2026-11-08/inputs/research/codex_final_review/verify_review.py"
```

The latter two verify immutable-file hashes and final-document/model consistency. They are not a fresh data pull. The fetch scripts are separate, read-only public-source utilities; rerunning them changes the audit timestamp and should be treated as a later observation.

## 3. Decision audit: D1–D14

Effects below use **Expected / AI-2027 / 100GW / bust**, in percentage points where a delta is given. “No weight effect” does not mean an input was unchanged.

| ID | Step 5 decision | Verdict | Evidence and reasoning | Effect if changed |
|---|---|---|---|---|
| D1 | AVGO base owner EPS $23.50 → $27; remain unheld | **Upheld with correction** | Reported FY28 adjusted target >$30 is corroborated by the call transcript, but the issuer release itself does not state it; claimed Sept 14 reaffirmation not verified. $27/0.87 = $31.03 adjusted EPS: a judgment, not a guaranteed conversion of $30. $23.50 owner EPS versus $30 adjusted did not by itself prove decline. The Oct 27 8-K verifies the contingent ~$43B maximum. Retain the delayed-target judgment and reserve, not a new AVGO purchase. | No held-weight effect; AVGO still 13.5% Expected |
| D2 | Remove VRT/NVT duplicate SBC deductions | **Upheld with correction** | Primary adjusted-EPS reconciliations retain ordinary SBC. Presence of SBC in a CFO bridge does not imply exclusion from adjusted EPS. Stored metadata still described old factors; corrected overlay labels. VRT $7.19 is the adopted consensus anchor, not the $7.15 midpoint of company FY26 guidance. | Step 5 numerical correction retained; no additional held-input change |
| D3 | Reject WCC replacing VST | **Upheld with correction** | Wesco explicitly retains SBC in adjusted EPS; remove the extra 4% charge. Q3's non-DC +7% is historical, not 2027 guidance. The older 5–8% long-term revenue aspiration is not a 2027 ceiling. Claude's lower-growth bridge remains defensible judgment; correcting its rationale does not prove Codex's $44 base. Even after correction, WCC remains far below the marginal holding. | WCC 7.0 → **8.0% Expected**, 10.5 → **11.6% AI**, 16.9 → **18.0% 100GW**; bust unchanged at −54.5%; no holding change |
| D4 | Add STRL, remove VST, size STRL 6 with VRT/MU 15 | **Overturned — sizing only** | Existing Step 5 STRL-8 alternative clears rule 2's lower branch unrounded. Inputs and VST funding stand. No new thesis, price, candidate or cap introduced. Rule 4's better-bust fallback would not support rejecting 8% either. | **+0.1243 / +0.0891 / +0.0726 / +0.0528pp** versus V10.1; STRL 8, VRT/MU 14 |
| D5 | Bench AVGO, VST/TLN, AEIS, TSM | **Upheld with correction** | A bench is useful but cannot supersede the risk-matched replacements in Part V.C or purchase eligibility. AEIS's issuer filing confirms the business/performance premise; it still does not clear the primary-model swap hurdle. No mechanical AVGO purchase during a shared financing/Taiwan shock. | No baseline weight effect |
| D6 | Texas re-underwrite, not an automatic bill-driven trade | **Upheld with correction** | Existing September TCEQ directive is real; project permits, grandfathering and cash-flow effects require review now. Two simultaneous headlines did not justify the final's contradictory bypass of the review. Remove bypass; confirm economic impact before substitution. | New funded conditional weights NRG 8 / STRL 3 / TLN 9; Expected 15.0%, not a baseline recommendation |
| D7 | Gate MOD on Nov 18 investor day | **Upheld** | Issuer confirms Nov 18. Nov 3 continuing-business report shows spin changed the perimeter, negative H1 FCF and weaker DC gross margin. FY28 targets must bridge to **2030** owner EPS $8.84; no demand for FY28 EPS $8.84. | V10.2 conditional MOD 5 / VRT 11 / NVT 10; Expected 15.7% |
| D8 | NVDA 15; buy only after Nov 17 and status check | **Upheld** | Issuer confirms Nov 17; primary Nov 8 board statement confirms an independent review, not a finding of compromise. No verified adverse conclusion found at review cutoff. Retain event gate and adverse NVDA-8/AVGO-7 vector. | V10.2 adverse conditional Expected 15.2%; baseline remains 15% NVDA |
| D9 | META 15 with household check | **Upheld with correction** | Issuer confirms monetization/capex tradeoff, including Q3 negative FCF. No live household balances/index weights were supplied. Illustrative 8.5% household exposure is not a measured result; direct 7.5% assumes Event Horizon exactly 50%. META is not cash ballast. | No weight effect; execution preflight strengthened |
| D10 | Eight holdings rather than Codex's nine | **Upheld** | The ninth name was WCC; corrected WCC still fails. NRG leverage and CLS cash conversion/capex justify existing confidence caps. Eight names remains defensible without claiming an exhaustive optimizer. | No name-count change |
| D11 | Correct multiple-invariant holding claim | **Upheld with correction** | Step 5's replacement “best under both policies” was also too broad: the concentrated architecture has higher Codex-multiple Expected CAGR but breaches caps; MOD is gated. MSFT 18.0% versus VRT 15.0% exceeds the 2pp band, so AI-2027 cannot automatically tie-break it away. | Narrowed claim; no multiple-policy or holding change |
| D12 | Replace screen “upper bounds” | **Upheld with correction** | Retain favorable-model estimates; identify 29 full A1 underwrites versus 31 screens. Screen downside is not the same test as a full FY2025 bust state. All eight holdings are full underwrites. | No re-ranking or input change |
| D13 | Correct HBM forecast scorecard | **Upheld with correction** | Micron total DRAM+NAND revenue cannot validate industry HBM revenue. Primary prepared remarks support contracted HBM tightness, not a quantified “tighter than modeled” error. Workbook constraint result remains a model output, not empirical proof of every forecast. | Qualitative grade only; scenario probabilities retained |
| D14 | Other Step 4 candidates rejected/watchlisted | **Upheld with correction** | SANM's new perimeter and adjustment uncertainty, PRIM execution losses, and ONTO's weaker return versus MU's named-scenario exposure remain defensible reasons. Restore omitted EME/IESC/HUBB comparisons and explicit review conditions. Different authors' Step 4 returns are not new A1 ranks. | No additions; no new candidates or pool re-ranking |

### Primary evidence register and limits

Accessed November 10, 2026. A successful lookup verifies the cited fact, not all forecasts derived from it. Forecast inputs remain analyst judgments unless explicitly labeled company guidance.

1. **AVGO (D1):** [Q3 issuer release](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-third-quarter-fiscal-year-2026-financial) confirms reported results and the SBC-excluding reconciliation; [Oct 27 8-K, Item 2.03](https://investors.broadcom.com/static-files/0ee4f6b7-4a23-4de0-8f3e-48f147ae30d3) confirms the maximum contingent backstop. The >$30 target is in a [third-party call transcript](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/), not independently authenticated issuer audio. That remaining primary-source gap is disclosed; it is not converted into certainty or used to enlarge the holding.
2. **VRT/NVT (D2):** [Vertiv Q3 adjusted EPS reconciliation](https://www.sec.gov/Archives/edgar/data/1674101/000162828026067707/q32026exhibit991vrt10282026.htm) and [nVent Q3 reconciliation](https://www.sec.gov/Archives/edgar/data/1720635/000162828026068391/q32026nvtpressrelease.htm). Ordinary SBC is retained. nVent FY26 $5.36–5.39 supports the $5.38 rounded anchor; VRT company midpoint $7.15 differs from the retained $7.19 consensus snapshot.
3. **WCC (D3):** [Q3 earnings release](https://www.sec.gov/Archives/edgar/data/929008/000092900826000029/wcc-3q2026earnings.htm) and [Q1 investor deck, PDF page 13 adjusted-EPS note](https://investors.wesco.com/static-files/6da5e262-57ff-497d-b112-ff02b3aa1af2). SBC/cloud amortization are retained in adjusted EPS but excluded from adjusted EBITDA. The older long-term aspiration is not a current 2027 sales guide. Apply only `stored EPS / 0.96` to plateau/base/bull: **18.3854167 / 28.4166667 / 36.9375**, retaining bust 13.05, 15×, probabilities, sensitivity and dividends. This reverses a duplicate factor; it does not assume a new growth path or infer unrounded source inputs.
4. **STRL (D4):** [Q3 release](https://www.sec.gov/Archives/edgar/data/874238/000087423826000122/a20261028ex991earningsrele.htm). Signed versus combined backlog and sub-1.0 signed book-to-burn matter; unsigned pipeline is not a firm order. The adopted operating bridge remains unchanged. Sensitivity is regenerated at 14×/12×/10.3×: **19.5159% / 15.1501% / 10.9809%**, not the earlier ~10%/~6% prose from another earnings case. The original bridge already contains explicit owner-EPS/SBC and cash conversion assumptions; these are now summarized in the final without adding retained FCF twice.
5. **Texas (D6):** [Governor's September 21 TCEQ directive](https://gov.texas.gov/news/post/governor-abbott-directs-tceq-to-halt-data-center-permits). Administrative restrictions predate the prospective legislation. The page was searchable but intermittently timed out on direct opening; no project-level legal exemption opinion is claimed. Existing power, contracts and new-campus permissions are distinct exposures.
6. **MOD (D7):** [Nov 18 event announcement](https://investors.modine.com/news/news-details/2026/Modine-to-Host-Analyst-and-Investor-Day-on-November-18-2026/default.aspx); [Nov 3 results](https://investors.modine.com/news/news-details/2026/Modine-Reports-Second-Quarter-Fiscal-2027-Results/default.aspx). H1 FCF −$145.6M and DC gross margin 19.7% support retaining the gate; no claim the gate has passed.
7. **NVDA (D8):** [Nov 8 board statement](https://investor.nvidia.com/news/press-release-details/2026/Statement-from-NVIDIA-Board-of-Directors/default.aspx); [Nov 17 earnings announcement](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx). The statement is primary evidence of a review, not of reported foreign-intelligence allegations or a completed clearance.
8. **META/NRG/CLS (D9–D10):** [Meta Q3](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx), [NRG Q3 and 2027 guidance](https://investors.nrg.com/news-releases/news-release-details/nrg-energy-reports-third-quarter-2026-results-reaffirms-2026), [Celestica Q3](https://www.sec.gov/Archives/edgar/data/1030894/000103089426000049/cls-20260930prcondensedfs.htm). These support the retained business and confidence judgments, not a verified household look-through. CLS's lower FCF guidance and higher planned capex still justify the 10% cap.
9. **HBM (D13):** [Micron September 30 prepared remarks, page 3](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf) `[STALE >30d]`: most CY27 HBM bits contracted with higher year-over-year prices. This corroborates scarcity qualitatively. It does not measure the workbook's global HBM-only revenue series. No forecast probability was raised merely because a different revenue aggregate grew quickly.
10. **Other candidates (D5/D14):** [AEIS Q3](https://www.sec.gov/Archives/edgar/data/927003/000092700326000037/aeis-ex99d1.htm), [Sanmina FY26](https://ir.sanmina.com/news/news-details/2026/Sanmina-Reports-Fourth-Quarter-and-Fiscal-2026-Financial-Results/default.aspx), [Onto Q3](https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Reports-2026-Third-Quarter-Results/default.aspx), [Primoris Q3](https://ir.prim.com/~/media/Files/P/Primoris-IR-v2/press-release/2026/primoris-services-corporation-reports-third-quarter-2026-results.pdf), [EMCOR Q3](https://www.sec.gov/Archives/edgar/data/105634/000010563426000132/eme-ex991_2026930xq3.htm), [IES Q3](https://investors.ies-corporate.com/news-releases/news-release-details/ies-holdings-reports-fiscal-2026-third-quarter-results-and) `[IES STALE >30d]`. Strong reported growth does not itself settle owner cash, acquisition adjustments or equal-model expected return. Hubbell's previously cited page returned 403; its Step 4 comparison is retained as historical model work, not represented as freshly verified.

### Completeness and self-siding checks

The merged Owner Decision Sheets cover Claude C1–C4 through D1/D4/D5/D6; Codex O1/O2 through D3/D4; all Step 3 E1–E5 through D7/D8/D6/D9/D10; and sanity flags X-S1–X-S6 through D8/D7/D11/D12/D2/D13. D14 covers the remaining outside-candidate conclusions. **No decision-sheet item is missing from the Decision Log.** Some final-report summaries were missing (D5 and D11–D14, and EME/IESC/HUBB); those presentation omissions are fixed without editing the historical log or ranking.

The strongest own-side concern was D3: its source attribution was wrong and its accounting had a double charge. Both are corrected, but neither establishes the stronger Codex forecast. The rejection survives. D1's adjustment/target comparison was also overstated; a defensible delayed-target judgment survives with the source limitation explicit. D5's bench order is a useful default only, and D10's eight-name count follows from rejected WCC. D4's explicit-bridge choice and removal of the weakest holding were defensible; its size was not, under the stated rule. This is why the review changes only that size rather than rebuilding around my earlier pass.

## 4. Document findings

Locations use section names rather than unstable line numbers. Each fixed root cause may require edits at several repeated locations; the diff-derived section list below is exhaustive.

| # | Location | Finding | Severity | Action |
|---|---|---|---|---|
| F01 | Step 5 scripts/data/tables | All eight reproduction artifacts identical | Wrong number if failed | **Noted, no change:** prerequisite passed |
| F02 | I.D, Reconciliation, V.C; D4 | +0.1pp rule-2 branch omitted/misapplied; rounded STRL-8 edge wrongly dismissed | Wrong action possible | **Fixed:** D4 sizing overturned with unrounded proof |
| F03 | I, Reconciliation, Selection, III–IX, README | Sizing change requires every current weight/rollup/return to agree | Wrong number | **Fixed:** generated V10.2 tables; 100% checksum; 82/18 core/satellite; C1 39/C3 34; Texas 20 |
| F04 | I.D, VI.C, VII, Deployment triggers | Old conditional funding would not match new baseline | Wrong action possible | **Fixed:** MOD 5 from VRT/NVT; Texas TLN 9; financing reserve 19; Taiwan reserve 1 |
| F05 | IX, Deployment §§3–4 | Trade/tranche/cash path stale after resizing; T1 said it sold every exit | Wrong action possible | **Fixed:** 84.54% turnover; cash 23.78/5.48/8.67/0; 18 of 21 exits in T1 |
| F06 | WCC rows, generated model/table overlay | SBC deducted a second time from adjusted EPS | Wrong number | **Fixed:** reverse 0.96 factor; Expected 8.0210%; no holding change |
| F07 | D3 explanations throughout | Historical/long-run growth described as company 2027 guidance | Wrong action possible | **Fixed:** remove misattribution; preserve lower growth as judgment |
| F08 | IV.1, Appendix A | AVGO adjusted target treated as guaranteed owner-EPS floor; Sept 14 reaffirmation unverified | Wrong action possible | **Fixed:** distinguish measures, judgment and source gap |
| F09 | Model provenance / overlay | AVGO/VRT/NVT/STRL tags did not all describe Step 5 numerical inputs | Wrong number | **Fixed:** overlay tags; no rewrite of historical data |
| F10 | I.E, IV.4 | STRL 12×/10.3× sensitivities used old operating case | Wrong number | **Fixed:** regenerate 15.15%/10.98% |
| F11 | IV.4 | STRL owner-SBC/history and cash bridge too abbreviated for an added holding | Wrong action possible | **Fixed:** summarize already-adopted bridge; distinguish signed/unsigned backlog and forecasts |
| F12 | I.E, Reconciliation, III.C, V, VII.D, Q15 | “Best under both multiple policies” and automatic MSFT tie-break overstate robustness | Wrong action possible | **Fixed:** primary-model comparison only; no global optimum claim |
| F13 | Intro, III.C, Appendix A | All 60 names implied to have equally complete A1/bust models | Wrong number | **Fixed:** 29 full / 31 screen; frozen ordinal ranks; no upper-bound claim |
| F14 | II.C1 | “Tighter than modeled” still claimed quantitative HBM validation | Wrong number | **Fixed:** qualitative scarcity only; HBM-only forecast unverified |
| F15 | V.D, IV.6, Deployment preflight | Household META/FSKAX look-through treated as measured; META implied cash cushion | Wrong action possible | **Fixed:** illustrative assumptions, live verification; negative Q3 FCF acknowledged |
| F16 | V.D, Deployment final checks | Stale 46–47% sleeve estimate could force excess contributions | Wrong action possible | **Fixed:** contribute only after measuring actual sleeve weight below 50% |
| F17 | I.C/E, III, IV.1/2, Selection, V.C, VII, Deployment C | NVDA #1 of 58, MU highest held AI return, cap/top-three statements stale or false; some spreads computed from rounded values; META/NRG incorrectly called the two lowest delay losses | Wrong number | **Fixed:** #3 of 60; STRL highest held AI; MU strongest in its band; two at cap; top-three 44%; spreads use unrounded values; shock preference distinguished from delay ranking |
| F18 | I.D, Selection Rationale | Incomplete decision summary; EME/IESC/HUBB omitted; removed-name count ambiguous | Wrong number | **Fixed:** all D1–D14 summarized; restore three comparisons; 21 V9.1 exits |
| F19 | IV.B, VI.C, Selection | MRNA missing re-entry trigger; grouped AVAV row omitted its trigger; rejected-name conditions incomplete | Wrong action possible | **Fixed:** evidence/valuation conditions, not automatic buys |
| F20 | VII.B, Deployment E/preflight | Two Texas headlines bypassed D6's re-underwrite; existing TCEQ action underweighted | Wrong action possible | **Fixed:** expedite, never bypass confirmation; review operative permits now |
| F21 | IV.1, V.C, VI.C, Deployment bench | Generic bench conflicts with risk-specific destinations and correlated shocks | Wrong action possible | **Fixed:** specific replacement/eligibility overrides generic order; reserve if none qualify |
| F22 | II.B, VII.C/D, Q7, IX, Deployment | Dec 9 PJM opening mistaken for clearing/results | Wrong action possible | **Fixed:** Dec 9 opening, Dec 15 close, Dec 22 results scheduled |
| F23 | Report/Deployment calendars | MU Dec 23, TSM Jan 14 and CLS Jan 27 presented as confirmed without primary confirmation | Wrong action possible | **Fixed:** tentative labels; refresh issuer calendars before orders |
| F24 | II.B3, Appendix A | No primary NVIDIA board source acknowledged; allegations could read as established | Wrong action possible | **Fixed:** cite board statement, distinguish review from findings/allegations |
| F25 | IX, Deployment A/G/R3/R4 | Forced Dec 11 deployment; Jan 8 buy date before Jan 10 hold event; 10% cash limit conflicts with blocked trades | Wrong action possible | **Fixed:** review checkpoints; gates override timetables and acceleration; blocked cash allowed temporarily |
| F26 | Deployment §§6/8/10 | +1pp tolerance/pro-rata purchases can exceed confidence/Texas caps or approved targets | Wrong action possible | **Fixed:** only eligible remaining gaps; no over-target orders; simultaneous-trigger reconciliation |
| F27 | I.E, IX, Deployment preflight/tax | Incomplete wash-sale window; illustrative losses imply account tax neutrality | Wrong action possible | **Fixed:** 30 days before/after and relevant household/IRA purchases; actual-lot/tax review |
| F28 | VII.B | Common zero-recovery overlay said to subtract identical CAGR points | Wrong number | **Fixed:** common wealth factor preserves ordering, not equal pp decrement; V10.2 12.6%/9.4% |
| F29 | IV.2 | Global common-stock mandate incorrectly called US-only for SK hynix | Wrong action possible | **Fixed:** access/liquidity/valuation unverified, not blanket mandate exclusion; next-cycle candidate work only |
| F30 | VII, Q14 | ≤55% immediate financing cut conflated with ≤50% prolonged Level 2 action | Wrong action possible | **Fixed:** separate trigger severity and funded review requirement |
| F31 | Model Reconciliation, Appendix C, README | Historical attribution count mixed D4 categories; current overlap/version/provenance incomplete | Wrong number | **Fixed:** mutually exclusive 6/4/3/1; overlap 71%/92%; Step 6 status/file tree/history |
| F32 | Appendix A, Deployment; audit data | No post-price-date quote check or verification boundary | Wrong action possible | **Fixed:** timestamped 16-name check, no >10% move; no repricing; source gaps explicit |
| F33 | D1/D3/D10 | Alternative reasonable growth/multiple judgments could produce other portfolios | Wrong action possible | **Noted, no change:** not permission to restore rejected proposals |
| F34 | D14 / watchlist | New growth data alone do not resolve SANM/PRIM/ONTO eligibility/cash gates | Wrong action possible | **Noted, no change:** retain watchlist/rejection |
| F35 | Forecast framework | Exact AI timeline, HBM market and loss-of-control probabilities remain uncertain | Wrong number | **Noted, no change:** no new probability estimates or candidate reranking in final review |
| F36 | Historical screens / source gaps | Some screen models, forward-multiple history and calendar/primary-source evidence are incomplete | Wrong action possible | **Noted, no change:** explicitly bounded; recommendations below |

### Event and current-price audit

PJM's [official auction schedule workbook](https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/rpm-auction-schedule.xlsx), first worksheet BRA rows 59–61, contains Excel serial dates **46365 / 46371 / 46378**, decoded against 1899-12-30 as **December 9 / 15 / 22, 2026**. Results are no earlier than 4 p.m. Eastern. A summary worksheet's date differs; the detailed activity rows, corroborated by PJM's description of a December 15 close, govern this calendar correction. Dates must still be refreshed before execution. No trading deadline is conditioned on nonexistent December 9 results.

Issuer-confirmed: NVDA November 17, MOD November 18, and [AVGO December 9](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announce-fourth-quarter-and-fiscal-year-2026). No confirmed December 23 date was found in [Micron's calendar](https://investors.micron.com/events-and-presentations/) or prepared remarks. [TSMC's calendar](https://investor.tsmc.com/english/financial-calendar) did not confirm January 14 earnings; monthly revenue dates are different events. Its dynamic monthly-revenue page did not expose October figures in the accessible text, so no newly reported October number is asserted. Other inherited minor read-through dates are not certified by this review and must be checked at order time. The November 9 geopolitical snapshot is not a claim that legal or trade-policy status cannot change on November 10.

| Name | Nov 10 observed price | Change vs Nov 9 | >10% flag |
|---|---:|---:|---|
| NVDA | $168.22 | -5.85% | No |
| META | $644.90 | +0.55% | No |
| VRT | $193.60 | -3.43% | No |
| MU | $718.36 | -2.02% | No |
| NRG | $97.29 | -0.11% | No |
| NVT | $112.69 | -1.52% | No |
| CLS | $225.28 | +1.06% | No |
| STRL | $292.10 | +0.49% | No |
| AVGO | $332.66 | +4.13% | No |
| VST | $130.92 | -2.24% | No |
| TLN | $361.15 | -0.55% | No |
| AEIS | $221.73 | +1.11% | No |
| TSM | $396.62 | +2.06% | No |
| MOD | $103.75 | -2.26% | No |
| SANM | $156.08 | +4.30% | No |
| ONTO | $196.15 | +1.09% | No |

Quotes were public Yahoo chart observations around **20:27 UTC November 10**, during the session, not closing prices. None crosses the prompt's **absolute 10% move** flag. Saved data include each endpoint, retrieval timestamp, market timestamp and November 9 daily close. The model and buy limits remain on the recorded November 9 snapshot; live trading still requires refreshed eligibility.

## 5. Recommendations for next cycle / no change now

1. **Uniform pool modeling:** upgrade screen-only candidates to full owner-cash, balance-sheet, dilution and comparable downside models before claiming a universal optimum. Do not re-rank in this review; a corrected WCC return is displayed at its frozen Step 5 ordinal reference.
2. **WCC growth:** test Codex's stronger DC mix and margin bridge against fresh guidance. The incorrect 2027-guide claim is removed, but proving the high case requires evidence, not reversal by default. Retain the 9% judgment for now after removing double SBC.
3. **AVGO:** obtain/authenticate issuer call audio for the FY28 EPS target and any reaffirmation; update actual funded guarantees, customer credit, cash/dilution and the owner-EPS bridge at the December report. No automatic use of the ~$43B maximum as a booked loss.
4. **STRL:** obtain a consistent multi-year *forward*-multiple history and Texas/project/customer exposure breakdown. The ex-post P/E comparison in Step 4 is not equivalent. Track signed order conversion, CEC execution, SBC and cash conversion. A new hard ceiling below 8% requires explicit owner preference and funded re-optimization; the review cannot invent it.
5. **SANM/ONTO/PRIM and omitted comparisons:** preserve watchlists; reconcile Sanmina earn-out, tariff and continuing-perimeter cash; require PRIM clean execution/cash quarters; compare ONTO against live MU returns after identical owner adjustments. Revisit EME/IESC/HUBB with current financials and better-priced alternatives. No qualifying new swap was demonstrated here.
6. **Higher-multiple policy:** run a separately identified constrained optimization with MSFT and the conditional names if the owner wants that policy. Do not claim primary-A1 invariance or use an AI tie-break outside its 2pp band.
7. **Household and tax data:** obtain actual positions, lot basis, relevant household/IRA transactions and current index constituent weights before deployment. Build one combined risk-target vector if multiple triggers fire. No account tax or look-through result can be certified from this repository alone.
8. **Calendar/process:** record event opening, closing and result dates separately; distinguish confirmed versus estimated earnings dates; make gate/cap precedence explicit in future prompt templates. Do not edit those templates during this final review.
9. **Forecast calibration:** compare like-for-like global HBM revenue, annual capex versus installed-compute cost, and coding automation versus autonomous research capability. AI-2027 remains the central scenario; apparent directional success is not enough to change numerical probabilities without a fresh calibration exercise.
10. **Global investability:** the common-stock mandate is not US-only. Check broker access, liquidity, foreign market/ADR tax treatment and owner valuation for SK hynix next cycle; no new candidate is added now.

These are not instructions to trade, change prompts, collect private account data or expand the mandate automatically. Defensible Step 5 judgments that failed the review's overturn standard remain intact.

## 6. Sections edited (diff against V10.1 before Step 6)

### Final analysis

- Header / process / market-data convention
- Part I: Executive Verdict → B. Allocation: V10.2, eight positions
- Part I: Executive Verdict → C. The decisive changes
- Part I: Executive Verdict → D. Final decisions (Step 5, reviewed in Step 6)
- Part I: Executive Verdict → E. Additional risks accepted in pursuing maximum expected return
- Model Reconciliation → Weights by source
- Model Reconciliation → Every portfolio on the same assumptions (Nov 9 prices)
- Model Reconciliation → How the two models' disagreements were resolved
- Selection Rationale: Chosen vs Considered → Chosen
- Selection Rationale: Chosen vs Considered → Considered, not chosen
- Selection Rationale: Chosen vs Considered → Removed from V9.1
- Part II: Prior-Cycle Accountability and What Changed Since May 10, 2026 → B. What Changed Since May 10 (new evidence only) → B3. Regulatory, governance and geopolitical developments
- Part II: Prior-Cycle Accountability and What Changed Since May 10, 2026 → B. What Changed Since May 10 (new evidence only) → B4. Market backdrop
- Part II: Prior-Cycle Accountability and What Changed Since May 10, 2026 → C. Background-Framework Deep Dive: AI-2027, the Compute Forecast Workbook, AI-2040 and Situational Awareness → C1. Scorecard: how the forecasts have tracked (Nov 2026)
- Part II: Prior-Cycle Accountability and What Changed Since May 10, 2026 → C. Background-Framework Deep Dive: AI-2027, the Compute Forecast Workbook, AI-2040 and Situational Awareness → C3. Forward paths (2027–2030) and the synthesis's scenario set
- Part II: Prior-Cycle Accountability and What Changed Since May 10, 2026 → C. Background-Framework Deep Dive: AI-2027, the Compute Forecast Workbook, AI-2040 and Situational Awareness → C4. What the framework evidence changed in the allocation
- Part III: Zero-Based Portfolio Test and Bottleneck Map → B. The Complete Bottleneck Map (November 2026)
- Part III: Zero-Based Portfolio Test and Bottleneck Map → C. The Zero-Based Ranking (60 stocks after Step 5, Nov 9 prices)
- Part III: Zero-Based Portfolio Test and Bottleneck Map → D. Zero-Based vs V9.1: every material difference explained
- Part IV: Sleeve-by-Sleeve Review, Alternatives, and Forward-Return Analysis
- Part IV: Sleeve-by-Sleeve Review, Alternatives, and Forward-Return Analysis → 1. Accelerators — 15% (NVDA) · *NVDA increase 6% → 15%; AVGO remove 3% → 0%*
- Part IV: Sleeve-by-Sleeve Review, Alternatives, and Forward-Return Analysis → 2. HBM / Memory — 14% (MU) · *Increase 6% → 14%*
- Part IV: Sleeve-by-Sleeve Review, Alternatives, and Forward-Return Analysis → 4. Thermal, Electrical and Site Work — 34% (VRT 14%, NVT 12%, STRL 8%) · *VRT increase 6% → 14%; NVT add; STRL add (Step 5); GEV, PWR, BE remove*
- Part IV: Sleeve-by-Sleeve Review, Alternatives, and Forward-Return Analysis → 5. Power Generation — 12% (NRG) · *NRG add; VST 6% → 0% (Step 5); CEG, CCJ remove*
- Part IV: Sleeve-by-Sleeve Review, Alternatives, and Forward-Return Analysis → 6. AI Platform — 15% (META) · *Add 0% → 15%*
- Part IV: Sleeve-by-Sleeve Review, Alternatives, and Forward-Return Analysis → IV.B Sleeves and Holdings Taken to Zero (V9.1 → V10.2)
- Part IV: Sleeve-by-Sleeve Review, Alternatives, and Forward-Return Analysis → IV.C Cross-Sleeve Candidate Evaluation
- Part IV: Sleeve-by-Sleeve Review, Alternatives, and Forward-Return Analysis → IV.D Forward-Return and Valuation Table (every V10.2 holding)
- Part V: Portfolio Architecture Comparison and Cross-Portfolio Capital Competition → A. Three Architectures, Same Valuation Model (Nov 9 prices)
- Part V: Portfolio Architecture Comparison and Cross-Portfolio Capital Competition → B. Verdict: Core-and-Satellite (V10.2)
- Part V: Portfolio Architecture Comparison and Cross-Portfolio Capital Competition → C. Cross-Portfolio Capital Competition (every V10.2 position)
- Part V: Portfolio Architecture Comparison and Cross-Portfolio Capital Competition → D. Three-Fund Architecture Check
- Part VI: Final Allocation + Checksum (100.0%) → A. Final Event Horizon Fund Allocation: **V10.2 (adopted November 10, 2026)**
- Part VI: Final Allocation + Checksum (100.0%) → B. Change Table (From → To, with specific funding sources)
- Part VI: Final Allocation + Checksum (100.0%) → C. Per-Ticker Decision Framework (every ticker)
- Part VII: Risk, Scenario, and Invalidation Dashboard → A. Scenario Lens (V10.2 vs V9.1, to Dec 31, 2030)
- Part VII: Risk, Scenario, and Invalidation Dashboard → B. Top 5 Risks and Invalidation Triggers
- Part VII: Risk, Scenario, and Invalidation Dashboard → C. Sleeve-Level Monitors (quarterly)
- Part VII: Risk, Scenario, and Invalidation Dashboard → D. What Would *Not* Count as Invalidation
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV)
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q1) What Is the Complete AI Datacenter Bottleneck Map? → Portfolio implication
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q2) Hypothetical (C15): What Would an AGI/ASI Do to Maximize Money? → Updated answer (Nov 9)
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q2) Hypothetical (C15): What Would an AGI/ASI Do to Maximize Money? → Portfolio implication
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q3) C14: What Are the Top Stocks for the 100 GW Datacenter Buildout? → Updated answer (Nov 9)
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q3) C14: What Are the Top Stocks for the 100 GW Datacenter Buildout? → Portfolio implication
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q4) C16: What Would an AGI/ASI Do to Maximize Its Own Intelligence? → Updated answer (Nov 9)
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q4) C16: What Would an AGI/ASI Do to Maximize Its Own Intelligence? → Portfolio implication
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q5) C17: What Strategy Would an AGI/ASI Use to Beat China in the Race to ASI? → Portfolio implication
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q7) C6: How Big a Deal Is the Need for Power, and Which Power Source Benefits Most? → New evidence since May 10
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q7) C6: How Big a Deal Is the Need for Power, and Which Power Source Benefits Most? → Updated answer (Nov 9)
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q7) C6: How Big a Deal Is the Need for Power, and Which Power Source Benefits Most? → Portfolio implication
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q8) C9: Should the Portfolio Invest in Department of Defense and War Stocks? → Portfolio implication
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q10) C2: Should the Portfolio Invest in Identity, Provenance, and Compliance Rails? → Portfolio implication
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q14) What Could Prove the Bottleneck Thesis Wrong by 2027? → Updated answer (Nov 9): re-ranked invalidation list
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q14) What Could Prove the Bottleneck Thesis Wrong by 2027? → Portfolio implication
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q15) Is the Portfolio Architecture Optimal Versus Alternative Models? → New evidence since May 10
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q15) Is the Portfolio Architecture Optimal Versus Alternative Models? → Updated answer (Nov 9)
- Part VIII: Targeted Question Reanalysis (November 2026 Update of May Part XIV) → Q15) Is the Portfolio Architecture Optimal Versus Alternative Models? → Portfolio implication
- Part IX: Near-Term Deployment Strategy (Summary)
- Appendix A: Methodology, Data Provenance, and Stale-Input Flags
- Appendix C: Final Verification

### Deployment Strategy

- Header / process / market-data convention
- 1. Destination
- 2. Preflight (before any order)
- 3. Trade List (drift basis, % of sleeve)
- 4. Tranche Plan (four tranches, ~3 weeks, catalyst-aware)
- 5. Explicit Trigger Rules (If Scenario X → do Y)
- 6. Price Discipline
- 8. Reserve Deployment Rules
- 9. Calendar
- 10. Final Checks After T4

### README

- Active version / Read This First; Current Allocation Snapshot; Sleeve Rollup; Synthesis Log; File Structure. The analysis-flow instructions and background-reading links are unchanged.

The edits are confined to correctness, required missing content, adoption/version synchronization and operational ambiguity. Unchanged source inputs and historical decisions are not silently rewritten. The Step 3 proposal was also compared with the adopted final to distinguish historical VST/NVDA/MOD decisions from current instructions.

## 7. Final verification

- Exact reproduction passed before review; persistent eight-artifact hash evidence exists.
- All fourteen decisions have a verdict and an evidence-based explanation; the complete Owner Decision Sheet/escalation/flag map is above.
- The only weight change passes rule 2 at unchanged prices, held-name inputs and adopted caps; no new candidate or rank order was introduced.
- Every current target is NVDA 15 / META 15 / VRT 14 / MU 14 / NRG 12 / NVT 12 / CLS 10 / STRL 8 = **100.0%**. Generated table and tranche checks are recorded by `verify_review.py`.
- V10.1 final and Deployment Strategy MD/PDF backups exist. Immutable-file hashes verify no Step 1–5 record was edited.
- The final analysis, Deployment Strategy, README and this Review Log have regenerated PDFs using the repository's `md_to_pdf.py`; PDF text/layout checks are recorded with the validation artifacts.
- No orders, commits or pushes were made. The Deployment Strategy and its backup remain gitignored/local.

This review improves consistency and applies the stated decision rule. It does not certify future returns, every inherited news claim, a complete real-time event feed, or an executable account-specific trade list without the preflight checks.
