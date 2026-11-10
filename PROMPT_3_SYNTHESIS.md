# Event Horizon Fund — Step 3: Candidate Ranking and Final Synthesis

Step 3 of 5 in the analysis flow (see `README.md` → Analysis Flow):

1. `PROMPT_1_DEEP_DIVE.md`: Claude and Codex each produce an independent deep dive
2. `PROMPT_2_CROSS_CRITIQUE.md`: each model critiques the other's picks head-to-head
3. **`PROMPT_3_SYNTHESIS.md`** ← this file: run by **one** model (alternate each cycle; see the README's synthesis log)
4. `PROMPT_4_OPTIMIZATION_PASS.md`: both models, independently, look for better stocks and weights
5. `PROMPT_5_FINAL_ASSEMBLY.md`: the synthesis model merges both optimization passes into one decision sheet, then applies the owner's decisions to the final

---

## Cycle Settings (update each cycle)

- Cycle date: `2026-11-08`
- Cycle folder: `Analysis 2026-11-08/`
- Prior analysis: `Analysis 2026-05-10/Event Horizon Fund Analysis 2026-05-10.md`
- Baseline allocation: `V9.1`
- Synthesis model (you): **`Claude`** (2026-11-08 cycle; next cycle: Codex)

This prompt runs as a full deep dive. It may take a while; prioritize completeness and quality over speed.

## Goal (shared by all five prompts)

Pick the stocks and weights with the **highest expected return at current prices** over 2027–2030, with an AI-2027-like path as the most likely scenario. For every stock, compare **Expected CAGR** (probability-weighted, the primary metric), **AI-2027 Scenario CAGR**, and **100GW 2030 Scenario CAGR**, as defined in `PROMPT_1_DEEP_DIVE.md` → Named Scenario Returns. Losses in the delay and bust scenarios are a constraint, not the objective.

## Your Job in This Step

Combine every candidate either model found into one pool and value them all on **one consistent model** at current prices. Rank the pool, then build the best portfolio from that ranking. Don't blend the two portfolios or split differences between them.

You wrote one of the deep dives, so you start out biased toward it. The self-sided audit (A6) makes that bias visible to the owner.

## Files to Read (all)

1. `Analysis 2026-11-08/inputs/Claude Deep Dive 2026-11-08.md`
2. `Analysis 2026-11-08/inputs/Codex Deep Dive 2026-11-08.md`
3. `Analysis 2026-11-08/inputs/Claude Critique of Codex 2026-11-08.md`
4. `Analysis 2026-11-08/inputs/Codex Critique of Claude 2026-11-08.md`
5. `PROMPT_1_DEEP_DIVE.md`: its constraints, valuation framework, named scenarios, required deliverables, locked output structure, and deployment rules all apply to the final analysis
6. The prior analysis (Cycle Settings) and `Original Large Thesis Writeup 2025-09-10/Event Horizon Fund Draft V7.3 2025-09-10.md`, for continuity

## Phase A: Candidate Ranking

Save to `Analysis 2026-11-08/inputs/Candidate Ranking 2026-11-08.md`.

### A1. One Set of Scenario Assumptions

Before valuing anything, reconcile how the two models defined the scenarios. Set one yearly path for each of the following, checked against the primary sources:

- the bear, base, and bull cases;
- the AI-2027 Scenario;
- the 100GW 2030 Scenario.

For each path, give compute, AI capex, chip/HBM/EUV volumes, power, and financing, plus the probability of each scenario. Where the two models' assumptions differed, state which one you adopted and why.

### A2. Candidate Pool

The pool includes every stock that was:

- held by either model, before or after its critique;
- fully underwritten by either model;
- raised in either critique as a better alternative.

### A3. Ranked Table

Re-underwrite every stock in the pool at current prices, using the A1 assumptions. If the deep dives or critiques don't report AI-2027 Scenario or 100GW 2030 Scenario CAGRs (true of the 2026-11-08 deep dives, which predate these scenarios), calculate them yourself for every stock in the pool. Then rank by Expected CAGR:

`Rank | Ticker | Bottleneck | Price + date | Valuation status | Expected CAGR | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Bust-case return | Claude % (blind / post-critique) | Codex % (blind / post-critique) | Disputed inputs and how they were resolved`

Before writing the final, refresh prices to the synthesis date. Re-check any stock that moved more than 10% since the deep dives' data date.

### A4. Resolving Disputed Inputs (apply in order)

1. **Facts:** verify at the primary source. The verified value wins. If it can't be verified, use the more conservative value and mark it unverified.
2. **Conceded in critique:** if one model conceded an input in Step 2, adopt the conceded-to value unless newer evidence contradicts it.
3. **Judgment inputs** (2030 metric, exit multiple, probabilities): use the better-supported value. On a genuine tie, use the more conservative value. **Never average the two models' inputs.**

### A5. From Ranking to Portfolio

Build the final weights from the ranking under the constraints in `PROMPT_1_DEEP_DIVE.md`: the 15% single-name cap, shared-driver cluster limits, and an acceptable bust-case loss. Then explain the exceptions:

- each top-ranked stock that was **left out** or capped: why, for example concentration, an overlapping driver, or the bust case;
- each lower-ranked stock that was **included**: what it does for the portfolio that a higher-ranked stock can't, for example a hedge or a different bottleneck.

Show the portfolio's Expected CAGR, AI-2027 Scenario CAGR, 100GW 2030 Scenario CAGR, and bust-case return. Also show these four numbers for the Claude blind, Codex blind, and both post-critique portfolios, all on the same A1 assumptions.

### A6. Escalated Items and Self-Sided Audit

- **Escalate to owner** (max 5): calls that depend on owner preferences (risk tolerance, concentration appetite, ethics) or that are still genuine ties.
  `ID | Question for owner | Option A (best case) | Option B (best case) | Provisional call in the final | Weight at stake`
- **Self-sided audit:** count the disputed inputs and weight calls that went to Claude's original view, to Codex's original view, and to neither. For each one decided in favor of your own model, state the deciding evidence.

## Phase B: Final Analysis and Deployment Strategy

Produce the final deliverables exactly as defined in `PROMPT_1_DEEP_DIVE.md` → Required Deliverables (Step 3 final), Locked Output Structure, and Deployment Execution Rules:

- `Analysis 2026-11-08/Event Horizon Fund Analysis 2026-11-08.md` and `.pdf`
- `Analysis 2026-11-08/Deployment Strategy/Deployment Strategy 2026-11-08.md` and `.pdf`

If any of these files already exist (for example, from an earlier single-model run), move them to `Analysis 2026-11-08/inputs/superseded/` first. Don't delete them.

Additional requirements for the final analysis:

- **Version label:** propose the next version number (for example, `V10.0`). Mark the analysis as a **proposal pending the Step 4 optimization passes and the Step 5 owner decisions**, not an adopted allocation.
- **Model Reconciliation section** (after the Executive Verdict):
  - `Ticker | Rank | Baseline % | Claude blind % | Codex blind % | Claude post-critique % | Codex post-critique % | Final %`. This table is the record next cycle uses to grade each model separately.
  - The A5 portfolio comparison: Expected CAGR, both named-scenario CAGRs, and bust case for each portfolio.
  - The main disputed inputs and escalated items.
- The final is a **standalone report**: complete on its own, not a diff of the inputs. It must meet the full depth standard of `PROMPT_1_DEEP_DIVE.md`, including all 15 targeted questions, three architectures, sleeve alternatives, and valuation tables with both named-scenario CAGRs for every holding.
- Cite sources and dates. When a conclusion comes from one model's input, verify it; don't cite "the Codex report" or "the Claude report" as evidence.
- Do **not** update `README.md`'s active allocation. That happens after Step 4 and the owner's decisions.

## Final Verification

- The candidate ranking, final analysis, and Deployment Strategy (`.md` and `.pdf`) all exist at the required paths.
- Every stock either model held or fully underwrote appears in the ranked table.
- Final allocation checksum = 100.0%. Every change from baseline has a funding source.
- Every exception between rank and weight is explained in A5.
- No final weight or input is the average of the two models' values without its own justification.
- The Model Reconciliation table and the self-sided audit are complete.
