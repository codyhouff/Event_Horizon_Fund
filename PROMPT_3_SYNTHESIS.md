# Event Horizon Fund — Step 3: Disagreement Ledger and Final Synthesis

Step 3 of 4 in the analysis flow (see `README.md` → Analysis Flow):

1. `PROMPT_1_DEEP_DIVE.md`: Claude and Codex each produce an independent deep dive
2. `PROMPT_2_CROSS_CRITIQUE.md`: each model critiques the other's deep dive
3. **`PROMPT_3_SYNTHESIS.md`** ← this file: run by **one** model (alternate each cycle; see the README's synthesis log)
4. `PROMPT_4_RED_TEAM.md`: the other model audits the final

---

## Cycle Settings (update each cycle)

- Cycle date: `2026-11-08`
- Cycle folder: `Analysis 2026-11-08/`
- Prior analysis: `Analysis 2026-05-10/Event Horizon Fund Analysis 2026-05-10.md`
- Baseline allocation: `V9.1`
- Synthesis model (you): **`<Claude or Codex>`**

This prompt runs as a full deep dive. It may take a while; prioritize completeness and quality over speed.

## Your Role

Turn two independent deep dives and two cross-critiques into one final, decisive analysis. Do it by resolving each disagreement on its merits, not by blending the two portfolios.

You wrote one of the deep dives, so you start out biased toward it. The Step 4 red team will count how often you sided with your own original position and check the evidence for each of those calls.

## Files to Read (all)

1. `Analysis 2026-11-08/inputs/Claude Deep Dive 2026-11-08.md`
2. `Analysis 2026-11-08/inputs/Codex Deep Dive 2026-11-08.md`
3. `Analysis 2026-11-08/inputs/Claude Critique of Codex 2026-11-08.md`
4. `Analysis 2026-11-08/inputs/Codex Critique of Claude 2026-11-08.md`
5. `PROMPT_1_DEEP_DIVE.md`: all of its constraints, valuation framework, required deliverables, locked output structure, and deployment rules apply to the final analysis
6. The prior analysis (Cycle Settings) and `Original Large Thesis Writeup 2025-09-10/Event Horizon Fund Draft V7.3 2025-09-10.md`, for continuity

## Phase A: Disagreement Ledger

Save to `Analysis 2026-11-08/inputs/Disagreement Ledger 2026-11-08.md`.

### A1. Agreement Map

List what both deep dives agree on: holdings both keep, both remove, and both add, plus shared thesis calls. Agreement means higher confidence, but it isn't proof. Flag any agreement that rests on the same weak source or assumption.

### A2. Ledger

Include every **material** disagreement, meaning any of the following:

- a weight difference of at least 1.0pp;
- a holding that is in one portfolio and out of the other;
- a scenario-probability difference of at least 5pp on any holding;
- a different factual claim that affects a decision;
- a different cluster or sleeve cap.

Build the list directly from the two deep dives. Use the critiques' §10 lists as a cross-check, not as the source.

`ID | Type (Fact / Valuation input / Thesis judgment / Sizing / Process) | Claude position | Codex position | Critique outcome (who conceded what) | Resolution | Basis (rule # below + evidence/source/date) | Final weight impact | Status (Resolved / Escalated)`

### A3. Resolution Rules (apply in order)

1. **Facts:** verify at the primary source as of the synthesis date. The verified value wins. If it can't be verified, use the more conservative value and mark it unverified.
2. **Conceded in critique:** if one side conceded in Step 2, adopt the conceded-to position unless newer evidence contradicts it.
3. **Both revised to the same answer:** adopt it, after a sanity check. Convergence alone doesn't prove it's right.
4. **Judgment and valuation:** re-underwrite the contested name yourself on **one consistent framework**: TV = 2030 metric × exit multiple + cumulative dividends; E[TV] = Σ p·TV; CAGR = (E[TV]/P)^(1/years) − 1. Use current prices. Side with the position that has the stronger evidence and the better valuation-adjusted expected return.
5. **Genuine tie:** take the risk-control default: smaller position, lower shared-driver concentration, or closer to baseline for marginal names. **Never average the two positions to split the difference.**
6. **Escalate to owner:** a material item that is still a genuine tie after rules 1–5, or one that depends on the owner's preferences (risk tolerance, ethics, concentration appetite). Escalate at most 5 items. For each one, still make a provisional call so the final allocation is complete.

### A4. Escalated Items

`ID | Question for owner | Option A (best one-paragraph case) | Option B (best one-paragraph case) | Provisional call in the final | Weight at stake`

### A5. Self-Sided Audit

`Resolutions siding with Claude's original: N | with Codex's original: N | new position (neither): N`

List every resolution that sided with your own model's original position and give the deciding evidence for each.

## Phase B: Final Analysis and Deployment Strategy

Before writing, refresh market data (prices, and consensus estimates where they're used) to the synthesis date. If any holding moved more than 10% since the deep dives' data date, re-check its valuation status.

Produce the final deliverables exactly as defined in `PROMPT_1_DEEP_DIVE.md` → Required Deliverables (Step 3 final), Locked Output Structure, and Deployment Execution Rules:

- `Analysis 2026-11-08/Event Horizon Fund Analysis 2026-11-08.md` and `.pdf`
- `Analysis 2026-11-08/Deployment Strategy/Deployment Strategy 2026-11-08.md` and `.pdf`

If any of these files already exist (for example, from an earlier single-model run), move them to `Analysis 2026-11-08/inputs/superseded/` first. Don't delete them.

Additional requirements for the final analysis:

- **Version label:** propose the next version number (for example, `V10.0`). Mark the analysis as a **proposal pending owner decisions and red-team review**, not an adopted allocation.
- **Model Reconciliation section** (after the Executive Verdict):
  - Allocation comparison: `Ticker | Baseline % | Claude blind % | Codex blind % | Claude post-critique % | Codex post-critique % | Final % | Ledger ID(s)`. This table is the record next cycle uses to grade each model separately.
  - Summary of the agreement map, the main resolved disagreements, and the escalated items, with links to ledger IDs.
- The final is a **standalone report**: complete on its own, not a diff of the inputs. Where the inputs already contain good analysis, use it, but the final must meet the full depth standard of `PROMPT_1_DEEP_DIVE.md`. That includes all 15 targeted questions, three architectures, sleeve alternatives, and valuation tables for every holding.
- Cite sources and dates as usual. When a conclusion comes from one model's input, verify it; don't cite "the Codex report" or "the Claude report" as evidence.
- Do **not** update `README.md`'s active allocation. That happens after Step 4 and the owner's decisions.

## Final Verification

- The ledger, final analysis, and Deployment Strategy (`.md` and `.pdf`) all exist at the required paths.
- Final allocation checksum = 100.0%. Every change from baseline has a funding source.
- Every material disagreement between the two deep dives appears in the ledger, and every ledger resolution matches the final allocation.
- No final weight is the average of the two blind or post-critique weights unless the ledger gives independent evidence for that exact number.
- The Model Reconciliation table is present and complete.
- The self-sided audit (A5) is filled in.
