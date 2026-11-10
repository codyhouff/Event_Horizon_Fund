# Event Horizon Fund — Step 4: Red Team Review

Step 4 of 4 in the analysis flow (see `README.md` → Analysis Flow):

1. `PROMPT_1_DEEP_DIVE.md`: Claude and Codex each produce an independent deep dive
2. `PROMPT_2_CROSS_CRITIQUE.md`: each model critiques the other's deep dive
3. `PROMPT_3_SYNTHESIS.md`: one model builds the disagreement ledger and writes the final analysis
4. **`PROMPT_4_RED_TEAM.md`** ← this file: run by the model that did **not** write Step 3

---

## Cycle Settings (update each cycle)

- Cycle date: `2026-11-08`
- Cycle folder: `Analysis 2026-11-08/`
- Red-team model (you): **`<Claude or Codex>`**
- Synthesis model (audited): **`<the other model>`**

## Your Role

Audit the final analysis. **Do not rewrite it**, and do not produce a competing allocation. Your job:

1. find errors (math, facts, broken rules, internal inconsistencies);
2. check that the synthesis resolved disagreements honestly and dropped none;
3. hand the owner a short decision sheet.

You wrote one of the deep dives, so you're biased toward it. Keep **errors** (objectively wrong) separate from **judgment dissents** (you'd have decided differently). Judgment dissents are capped at 5 and need evidence, not preference.

## Files to Read (all)

1. Final: `Analysis 2026-11-08/Event Horizon Fund Analysis 2026-11-08.md`
2. Final: `Analysis 2026-11-08/Deployment Strategy/Deployment Strategy 2026-11-08.md`
3. `Analysis 2026-11-08/inputs/Disagreement Ledger 2026-11-08.md`
4. Both deep dives and both critiques in `Analysis 2026-11-08/inputs/`
5. `PROMPT_1_DEEP_DIVE.md` and `PROMPT_3_SYNTHESIS.md`, which are the rules the final had to meet

## Audit Checklist

### A. Mechanical Integrity

- Final allocation sums to exactly 100.0%. Recompute it yourself.
- The same weight for each ticker appears everywhere: final table, change table, decision table, sleeve rollup, Model Reconciliation table, and Deployment Strategy.
- Every change from baseline has a funding source. Funding sources and uses net to zero.
- Deployment tranches reconcile to the target weights: buys and sells per tranche, cash path, and ending cash about 0 or as stated.
- 15% single-name cap respected, or justified as the template requires. Cluster caps match those stated.
- Locked Output Structure order followed. All 15 targeted questions present with full treatment.
- PDFs exist for the final analysis and Deployment Strategy.

### B. Valuation Math

For every holding, recompute E[TV] and the implied CAGR from the inputs stated in the report. Check that probabilities sum to 100%, that scenario CAGRs weren't averaged, that the horizon exponent is consistent, and that prices match the stated data date.

`Ticker | Stated E[CAGR] | Recomputed | Δ | Issue`

### C. Ledger Integrity

- Build your own diff of the two blind deep-dive allocations, then check that every material difference appears in the ledger (thresholds are in `PROMPT_3_SYNTHESIS.md` A2).
- Every ledger resolution is reflected in the final allocation and text.
- Each resolution cites the right rule and real evidence. Flag resolutions that only restate one side's view.
- Flag any final weight that equals, or nearly equals, the average of the two inputs without independent evidence for it.

### D. Bias Audit

- Check the synthesis self-sided count (ledger A5) against your own count.
- For each resolution that sided with the synthesis model's own original position, judge whether the cited evidence actually decides it.
- Note whether the concessions in the synthesis model's Step 2 critique were honored in the final.

### E. Evidence Spot-Check

Verify at the primary source the at least 10 factual claims with the largest impact on the allocation, prioritizing claims that drive a weight of 5% or more or an in/out decision.

`# | Claim | Location | Verified? | Source + date | Impact if wrong`

Also flag data older than 30 days that isn't marked as stale.

### F. Deployment Rules

Check that every trigger, no-trade condition, and reserve rule is unambiguous and executable: measurable threshold, date, and action. Flag rules that conflict or can't be acted on.

## Required Output

Save to `Analysis 2026-11-08/inputs/Red Team Review 2026-11-08.md`. A PDF is optional.

1. **Verdict:** `Approve` / `Approve with fixes` / `Reject (blockers)`, with a 3–5 bullet summary.
2. **Findings:**
   `ID | Severity (Blocker / Major / Minor) | Location (file + section) | Issue | Evidence | Required fix`
   - *Blocker*: wrong checksum, a broken hard constraint, a math error that changes a holding decision, or a material disagreement that was dropped.
   - *Major*: a wrong fact or math error that changes a weight by 1pp or more, an unsupported resolution, or a rule that can't be executed.
   - *Minor*: inconsistencies, formatting, or a missing citation with no decision impact.
3. **Valuation recompute table** (§B).
4. **Ledger and bias audit results** (§C–D).
5. **Evidence spot-check table** (§E).
6. **Judgment dissents (max 5):**
   `# | Decision in final | My alternative | Evidence | Weight at stake`
7. **Owner Decision Sheet:** the synthesis's escalated items plus any judgment dissents worth the owner's attention. Each item gets a one-line question, both options with their best case in 1–2 sentences, the synthesis's provisional call, your lean, and the weight at stake. Keep it to one page.

## After This Step (Step 5: Owner Decision, no prompt file)

1. The owner answers the Owner Decision Sheet.
2. The **synthesis model** applies all Blocker and Major fixes plus the owner's decisions to the final analysis and Deployment Strategy, regenerates the PDFs, and marks the version as adopted.
3. Update `README.md`: active allocation version, snapshot, sleeve rollup, and the synthesis log. Then commit.

## Final Verification

- The review file exists at the required path.
- Every finding has a severity, a location, and a required fix.
- Errors and judgment dissents are kept separate. Judgment dissents number 5 or fewer.
- The Owner Decision Sheet fits on one page.
