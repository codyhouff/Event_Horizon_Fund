# Event Horizon Fund — Step 5 Decision Log (2026-11-08 cycle)

**Step 5 of 5** (`PROMPT_5_FINAL_ASSEMBLY.md`). **Synthesis model:** Claude (Opus 5.5). **Written:** November 10, 2026.

**Inputs:**

- `inputs/Claude Optimization Pass 2026-11-08.md` (items C1–C4)
- `inputs/Codex Optimization Pass 2026-11-08.md` (items O1, O2, E1–E5, and six sanity flags, labeled here X-S1 to X-S6)
- the Step 3 open calls E1–E5 in `inputs/Candidate Ranking 2026-11-08.md`

**Basis.** Every item was re-checked on the **same valuation model and the same Nov 9, 2026 close as the final**: `inputs/research/claude_synthesis/step5_model.py`. Step 5's model is the Step 3 model plus the decided input changes below. No held or proposed stock had a newer close than Nov 9 at the time of writing, so nothing needed re-pricing.

**Decision rules** (PROMPT_5 §2), applied in order:

1. **Constraints first.**
2. **A change must beat noise:** at least +0.25pp portfolio Expected CAGR, or at least +0.1pp while also raising the AI-2027 CAGR and not worsening the bust by more than 1pp.
3. **Agreement still has to pass rule 2.** On a conflict, the better-supported side wins (facts, then concessions, then the better-supported judgment; on a tie, the lower value; never average).
4. **Judgment calls:** the higher expected return wins; if within noise, the better bust case.
5. **Input corrections** are applied to the record.

## Decisions

| ID (sources) | Item | Agreement | Claude's view | Codex's view | Decision | Deciding evidence | Effect on portfolio (Expected / AI-2027 / 100GW / bust) |
|---|---|---|---|---|---|---|---|
| **D1** (C1) | Correct AVGO's base 2030 owner EPS from $23.5 to $27.0 | One model only | Accept | Not raised | **Accept (input correction)** | Management's FY28 adjusted EPS target is above $30 (Sep 2, reaffirmed Sep 14). The old base implied earnings falling after FY28, against the A1 base path. AVGO goes from 11.6% to **13.5%** expected. It isn't held, so it becomes bench #1 | None |
| **D2** (X-S5) | Remove the double stock-comp charge on VRT and NVT anchors | One model only | Not raised | Fix | **Accept (input correction)** | Vertiv's and nVent's adjusted-EPS reconciliations already retain stock comp. VRT plateau EPS $7.05 → $7.19; NVT bust $3.22 → $3.35 and plateau $5.16 → $5.38. VRT 13.8% → 13.9%; NVT 13.7% → 13.8% | +0.02pp (portfolio Expected 14.93% → 14.95% before other changes) |
| **D3** (O1) | Replace VST 8% with WCC 8% | One model only (Codex) | WCC 6.9% in Claude's pass | WCC 18.3% (base 2030 EPS $44) | **Reject** | Codex's bridge needs revenue growth of 11.3%/yr for 2027–30 and owner margin rising from ~3.3% to 5.5%. Wesco itself guides 2027 sales growth to mid-to-high single digits and has a 5–8% long-run revenue aspiration; its 10%+ EBITDA target predates the AI ramp (Q3 2026 release and investor presentation). The consensus-anchored base ($27.3; 2027E $21.94 + 9%/yr) is better supported. On it, WCC returns **7.0%**, and Codex's own −20%-EPS sensitivity erases its advantage. Portfolio with O1: 14.5% (−0.4pp) | Rejected: −0.42 / −0.63 / −0.55 / +1.01pp |
| **D4** (O2, C2) | Add STRL | **Agree on STRL as the best outside name.** Conflict on inputs, funding and size | 14.6% at a formula base (+10%/yr); keep VST | 19.5% at an explicit operating bridge; fund 5% from NVT | **Accept STRL at Codex's inputs; fund from VST, not NVT; size 6%** | **Inputs:** Codex's explicit bridge ($9.0B revenue × 15% owner margin ÷ 31.5m shares; bull $13B / 16% / 33m) is better supported than my growth formula. It implies ~16%/yr owner-EPS growth from 2027, close to what the holdings got (VRT 15%/yr), and no company guidance contradicts it. **Funding:** VST is the weakest holding on both Expected (13.0%) and AI-2027 (20.2%), and Codex's own pass removes it (O1). Funding from VST beats funding from NVT by +0.1pp Expected and +0.2pp AI-2027. **Size:** with VST out, the freed 8 points can go only to names below their caps, so VRT 14 → 15 and MU 14 → 15 (both at the 15% cap). STRL takes the 6% residual, close to Codex's 5% ceiling for Texas and project risk. The 8%-STRL alternative is within noise (+0.1pp) with the same bust, so rule 4 keeps the less-proven name smaller | **+0.41 / +0.61 / +1.22 / +0.09pp** (14.95 → 15.36; 23.43 → 24.04; 36.88 → 38.10; −61.62 → −61.53) |
| **D5** (C3) | Name a bench for capital freed by any trigger | One model only | Accept | — | **Accept** | Makes the trigger rules consistent. **Bench:** 1 AVGO (13.5%); 2 VST (13.0%, re-entry if the Texas risk clears) or TLN (12.7%, PJM); 3 AEIS (13.4%, Step 4 pass); 4 TSM (11.8%) | None |
| **D6** (C4, E3, Codex §3.6) | Texas trigger: automatic VST → TLN switch on a Texas bill? | **Conflict** | Automatic switch | No automatic headline trade; re-underwrite first | **Codex's view.** With VST exited, the rule becomes: **a Texas moratorium bill clearing a chamber triggers a re-underwrite of NRG and STRL within 5 sessions.** If the impact is confirmed: NRG 12 → 8, STRL 6 → 3, TLN +7 | Existing generation, existing PPAs and new data-center approvals are affected differently. Abbott's TCEQ permit pause already exists, so a vote isn't by itself a new fact about cash flows | Conditional: 15.0 / 23.5 / 37.3 / −61.1 if triggered |
| **D7** (E1) | MOD: add now, or gate on its post-spin investor day? | **Agree (gate)** | Gate | Gate; date confirmed | **Keep the gate. Correct its wording** (X-S2) | The investor day is **Nov 18, 2026**, confirmed by Modine's own announcement. The gate is FY28 targets that credibly bridge to **2030** owner EPS of $8.84 (not "FY28 EPS ≥ $8.8"), a stable data-center gross margin, and positive H2 FCF guidance. If it passes: MOD 5, funded VRT −3, NVT −2 | Conditional: 15.6 / 24.8 / 39.7 / −61.7 |
| **D8** (E2, X-S1) | NVDA at 15% during the board review; pre-earnings buy | **Agree on 15%. Conflict on timing** (Step 3 deployment) | 15% | 15%; no buy before Nov 17 | **15%; no NVDA purchase before the Nov 17 report and a review-status check** | Codex is right that the deployment plan's T1 bought 1.93 pts before earnings, contradicting the E2 rule. The NVDA-12% variant also breached NVT's 12% cap (X-S1). Both fixed. New adverse-review action: NVDA 15 → 8, AVGO +7 (bench #1) | Conditional (adverse): 15.1 / 23.7 / 37.6 / −62.2 |
| **D9** (E4) | META at 15% | **Agree** | 15% | 15%; verify household look-through | **Keep 15%** | #6 of 60, with the mildest bust of the top names (−34%). Neither Step 4 pass found a better non-hardware alternative | None |
| **D10** (E5) | Eight holdings or more? | **Conflict** (Claude 8, Codex 9) | 8 | 9 | **8** | Codex's ninth name was WCC, rejected in D3. The adopted set is 8 names because VST's exit is funded by STRL plus the VRT/MU caps | — |
| **D11** (X-S3) | The claim that the holdings are the same under Codex's multiples | One model only | — | Too strong | **Accept: correct the claim** | Under Codex's multiples, MSFT (18.0%) outranks VRT (15.0%) and MU (13.1%) on Expected CAGR. They stay ahead on AI-2027 (MU 26.8%, VRT 23.3% vs MSFT 22.7%), and MSFT's rank there rests on a 29× multiple outside its own band. The final now says: "V10.1 is the best of the tested portfolios under both multiple policies; the constituents are not invariant" | None |
| **D12** (X-S4) | "Upper bound" wording for the screen-level names | One model only | — | Misleading | **Accept** | A screen-level re-price on the other model's terminal values is a favorable-model estimate, not a mathematical upper bound. Relabeled in Part III.C | None |
| **D13** (X-S6) | HBM scorecard compares Micron's total revenue with an HBM-only forecast | One model only | — | Not like-for-like | **Accept** | Part II.C1 is corrected. The binding-HBM claim rests on the workbook's own model plus SK hynix's "sold out to 2029," not on a measured HBM market size | None |
| **D14** (Codex §1) | Other outside names: SANM, PRIM, SPXC, EME, ONTO, IESC, HUBB and others | Partly agree | Reject or watchlist | Watchlist or reject | **Watchlist:** SANM (Codex 16.2% vs CLS 14.8%; earn-out, tariff benefit and new-perimeter margins unreconciled) and ONTO. The rest rejected | Both passes find none clears rule 2 against the holding it would displace once confidence gates apply | None |

## Self-sided count

I wrote the Step 3 final and one of the two Step 4 passes, so this count makes my bias visible.

| Went to | Items |
|---|---|
| Codex's pass | D2, D6, D8 (timing), D11, D12, D13, and D4 on STRL inputs and on removing VST: **7** |
| Claude's pass | D1, D3, D5, D10, and D4 on funding: **4** in substance (D4 is shared) |
| Both agreed | D7, D9, D14 |

**Every decision that went to my side, with its evidence:**

- **D1:** management's FY28 target.
- **D3:** Wesco's own growth guidance and aspiration.
- **D5:** consistency of the trigger rules.
- **D10:** follows from D3.
- **D4 funding:** VST is last on both metrics in both passes, and Codex's own O1 removes it.

**Where I changed my own Step 4 view:**

- I had rejected VST → STRL as cosmetic (+0.12pp at my STRL inputs). With Codex's better-supported STRL bridge, the swap clears the noise bar (+0.41pp).
- I had wanted an automatic Texas switch; I adopted Codex's re-underwrite rule instead.

## Before and after

Same model, Nov 9 prices:

| Portfolio | Expected CAGR | AI-2027 | 100GW | Bust | Delay | Expected CAGR on Codex's multiples |
|---|---:|---:|---:|---:|---:|---:|
| V10.0 Step 3 proposal (after D2 input fixes) | 14.95% | 23.43% | 36.88% | −61.6% | −23.3% | 18.2% |
| Codex's Step 4 proposal (O1 + O2) | 14.83% | 23.19% | 36.84% | −61.0% | −22.7% | 17.6% |
| **V10.1 (adopted)** | **15.36%** | **24.04%** | **38.10%** | **−61.5%** | **−22.3%** | **18.4%** |

**V10.1:** NVDA 15, META 15, VRT 15, MU 15, NRG 12, NVT 12, CLS 10, STRL 6 = **100.0%**. Changes from the Step 3 proposal:

- VST −8
- STRL +6
- VRT +1
- MU +1

Every change is funded by VST's exit.
