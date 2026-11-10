# Event Horizon Fund — Step 2: Cross-Critique

Step 2 of 4 in the analysis flow (see `README.md` → Analysis Flow):

1. `PROMPT_1_DEEP_DIVE.md`: Claude and Codex each produce an independent deep dive
2. **`PROMPT_2_CROSS_CRITIQUE.md`** ← this file: run by **both** models in parallel; each critiques the *other's* deep dive
3. `PROMPT_3_SYNTHESIS.md`: one model builds the disagreement ledger and writes the final analysis
4. `PROMPT_4_RED_TEAM.md`: the other model audits the final

---

## Cycle Settings (update each cycle)

- Cycle date: `2026-11-08`
- Cycle folder: `Analysis 2026-11-08/`
- Baseline allocation: `V9.1` (from `Analysis 2026-05-10/Event Horizon Fund Analysis 2026-05-10.md`)
- You are: **`<Claude or Codex>`**. The other model is the remaining one.

## Your Role

You wrote one of the two independent deep dives. Now read the other model's deep dive closely and critique it, and re-examine your own work against it.

This is **not** a merge. Do not write a combined report or a blended allocation. The goal is to surface every material disagreement, settle the factual ones, and argue the judgment calls with evidence so Step 3 can resolve them.

## Files to Read

1. Your own deep dive: `Analysis 2026-11-08/inputs/<Your Model> Deep Dive 2026-11-08.md`
2. The other model's deep dive: `Analysis 2026-11-08/inputs/<Other Model> Deep Dive 2026-11-08.md`
3. `PROMPT_1_DEEP_DIVE.md`, for the rules both deep dives had to follow (constraints, valuation framework, required outputs)

Do not read the other model's Step 2 critique if it already exists. Both critiques must be written independently.

## Rules

- **Evidence beats confidence.** Change your view only for specific evidence, data, or a better argument, never because the other model stated a different number or sounded certain.
- **No diplomatic concessions.** Don't concede points to look balanced, and don't defend a position just because it's yours. When the other model is right, say so plainly.
- **Settle facts, don't argue them.** When the two reports state different facts (prices, guidance, capex figures, dates, events, framework numbers), check the primary source and record the result with source and date. If it can't be verified, say so.
- **Same-date comparisons.** If the two reports used different market-data dates, note the gap. Don't count price moves between those dates as analytical disagreements.
- **Compare underwriting on equal terms.** For every name both reports underwrote, compare the inputs (2030 metric, exit multiple, scenario probabilities, dividends), not just the resulting CAGR. Identify the specific assumption that drives each gap.
- **No averaging.** Any change to your allocation must come from a specific concession in this critique. Splitting the difference is not a reason.
- Fresh web research is allowed, but only to settle conflicts or check claims. This is not a new deep dive.
- Prefer tables to prose. Target length: roughly 300–700 lines.

## Required Output

Save to `Analysis 2026-11-08/inputs/<Your Model> Critique of <Other Model> 2026-11-08.md`. A PDF is optional (`python md_to_pdf.py "<path>"`).

### 1. Verdict (max 10 bullets)

- The most important thing the other model got right that you missed or got wrong.
- The most important thing the other model got wrong.
- Net: how much your allocation changes after this critique, and in which direction.

### 2. Allocation Diff

Cover every ticker held by either report, plus any name either one fully underwrote but excluded:

`Ticker | Mine % | Other % | Delta (pp) | Driver of the gap (assumption / fact / thesis) | Better call | Why (evidence)`

Then add the same comparison at the sleeve and shared-driver cluster level: AI silicon and interconnect, fab tools and design, data-center physical and electrical, power generation, software, and AI-independent hedges.

### 3. Factual Conflicts

`# | Claim | Mine says | Other says | Primary-source check (source + date) | Resolved value | Who was right`

Include framework numbers from AI-2027, AI-2040, and Situational Awareness when the two reports cite them differently.

### 4. Valuation Assumption Comparison

For every name both reports underwrote:

`Ticker | Price/date (mine vs other) | Bear/Base/Bull TV (mine vs other) | Probabilities (mine vs other) | E[CAGR] (mine vs other) | Key input driving the gap | Which input is better supported`

Also check the other report's math: whether E[TV] was computed before the CAGR, whether scenario CAGRs were averaged, whether probabilities sum to 100%, and whether CAGR exponents are consistent with the horizon.

### 5. Concessions: Where the Other Model Is Right

`# | Topic | My original view | Their view | Evidence that convinced me | Change to my allocation or analysis`

### 6. Rebuttals: Where the Other Model Is Wrong

`# | Topic | Their view | Why it's wrong (evidence + source/date) | Severity (High/Med/Low) | Weight at stake (pp)`

### 7. Coverage Gaps

- Evidence, risks, candidates, or bottlenecks the other report found that yours missed. State whether each matters.
- Evidence, risks, candidates, or bottlenecks yours found that the other missed.
- Differences in how the AI-2027 / AI-2040 / Situational Awareness framework material was read and applied: scorecard grades, timelines, forward paths.

### 8. Rule-Compliance Check of the Other Report

Check against `PROMPT_1_DEEP_DIVE.md`: 100.0% checksum; 15% single-name cap; long-only universe; funding sources for every change; at least 2 alternatives per sleeve; full underwriting of the top 10 challengers; three architectures; all 15 targeted questions; stale-data flags; a deployment plan with triggers, no-trade conditions, and reserve rules.

`Requirement | Met? | Note`

### 9. Revised Allocation (Yours, After Critique)

`Ticker | Original % | Revised % | Delta | Concession # that justifies it`

- Must sum to exactly 100.0%, with a checksum line.
- Every change must cite a concession from §5. If nothing changes, say so and explain why.

### 10. Expected Open Disagreements for Step 3

Rank the disagreements still standing after this critique by portfolio impact (weight at stake × gap in expected CAGR, or a holding-in/out decision):

`Rank | Issue | My position | Their position | Weight at stake | What evidence would settle it`

## Final Verification

- The critique file exists at the required path.
- §2 covers every ticker in both reports.
- §9 sums to 100.0%, and every change cites a concession.
- Every factual conflict in §3 has a primary-source check or is marked unverified.
