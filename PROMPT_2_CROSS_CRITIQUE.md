# Event Horizon Fund — Step 2: Cross-Critique (Head-to-Head Stock Picks)

Step 2 of 5 in the analysis flow (see `README.md` → Analysis Flow):

1. `PROMPT_1_DEEP_DIVE.md`: Claude and Codex each produce an independent deep dive
2. **`PROMPT_2_CROSS_CRITIQUE.md`** ← this file: run by **both** models in parallel; each critiques the *other's* deep dive
3. `PROMPT_3_SYNTHESIS.md`: one model ranks every candidate from both models and writes the final analysis
4. `PROMPT_4_OPTIMIZATION_PASS.md`: both models, independently, look for better stocks and weights
5. `PROMPT_5_FINAL_ASSEMBLY.md`: the synthesis model merges both optimization passes into one decision sheet, then applies the owner's decisions to the final

---

## Cycle Settings (update each cycle)

- Cycle date: `2026-11-08`
- Cycle folder: `Analysis 2026-11-08/`
- You are: **`<Claude or Codex>`**. The other model is the remaining one.

## Goal (shared by all five prompts)

Pick the stocks and weights with the **highest expected return at current prices** over 2027–2030, with an AI-2027-like path as the most likely scenario. For every stock, compare **Expected CAGR** (probability-weighted, the primary metric), **AI-2027 Scenario CAGR**, and **100GW 2030 Scenario CAGR**, as defined in `PROMPT_1_DEEP_DIVE.md` → Named Scenario Returns. Losses in the delay and bust scenarios are a constraint, not the objective.

## Your Job in This Step

Compare your portfolio with the other model's, **stock by stock**. Wherever the two differ, decide which pick is better priced and has the higher expected return, and find what the other model got right that beats your picks.

This is not a merge. Don't write a combined report or a blended allocation.

## Files to Read

1. Your own deep dive: `Analysis 2026-11-08/inputs/<Your Model> Deep Dive 2026-11-08.md`
2. The other model's deep dive: `Analysis 2026-11-08/inputs/<Other Model> Deep Dive 2026-11-08.md`
3. `PROMPT_1_DEEP_DIVE.md`: valuation framework and the named-scenario definitions

Don't read the other model's Step 2 critique if it already exists.

## Rules

- **Evidence beats confidence.** Change a pick or weight only for specific evidence or a better-supported valuation input, never because the other model stated a different number.
- **No diplomatic concessions, no defending turf.** When their pick is better, say so plainly.
- **Same prices.** Re-price every contested stock to one current date, so price moves between the two reports' data dates don't look like analytical disagreements.
- **Missing named-scenario returns.** If either deep dive doesn't report AI-2027 Scenario or 100GW 2030 Scenario CAGRs (true of the 2026-11-08 deep dives, which predate these scenarios), calculate them yourself for every stock in §2–§4, using the definitions in `PROMPT_1_DEEP_DIVE.md`.
- **Compare inputs, not just outputs.** When CAGRs differ, find the specific input driving the gap (2030 metric, exit multiple, probabilities, scenario path) and decide which is better supported.
- **Check facts only where they change a pick.** If the two reports disagree on a fact that drives a weight or an in/out decision, verify it at the primary source.
- **No averaging.** Every change to your allocation must come from a specific head-to-head win in §2 or §3.
- Use fresh research only to settle contested picks. This is not a new deep dive. Prefer tables to prose.

## Required Output

Save to `Analysis 2026-11-08/inputs/<Your Model> Critique of <Other Model> 2026-11-08.md`. A PDF is optional.

### 1. Verdict (max 10 bullets)

- The other model's best pick that you missed or underweighted, and why it's better.
- The other model's weakest pick, and why.
- How your allocation changes after this critique.

### 2. Head-to-Head: Every Stock Where the Portfolios Differ

Cover every ticker that is held by only one model, or held by both with weights at least 1pp apart:

`Ticker | Mine % | Other % | Price + date | Expected CAGR (mine / theirs / re-underwritten) | AI-2027 Scenario CAGR (mine / theirs) | 100GW 2030 Scenario CAGR (mine / theirs) | Input driving the gap | Better call | Why`

Where the two estimates differ by more than 3pp, **re-underwrite the stock yourself** on current prices, with each disputed input set to the better-supported value.

### 3. Their Picks vs Mine (Same Bottleneck)

Where the two models chose different stocks for the same bottleneck or sleeve (for example, different memory, optical, power, or tool names), compare them directly:

`Bottleneck | My pick | Their pick | Expected CAGR each | AI-2027 Scenario CAGR each | 100GW 2030 Scenario CAGR each | Valuation status each | Better stock | Why`

### 4. Candidates Only One of Us Found

- Names the other model underwrote or held that you never considered: your verdict on each (Add / Replace X / Reject), with the reason.
- Names you underwrote that the other model never considered, and why they matter.

### 5. Facts That Change a Pick

`# | Claim | Mine | Theirs | Primary-source check (source + date) | Resolved | Pick affected`

Include framework numbers from AI-2027, AI-2040, and Situational Awareness if the two reports read them differently and it changes a scenario CAGR.

### 6. Revised Allocation (Yours, After Critique)

`Ticker | Original % | Revised % | Delta | Head-to-head row that justifies it`

- Must sum to exactly 100.0%, with a checksum line.
- Show portfolio Expected CAGR, AI-2027 Scenario CAGR, 100GW 2030 Scenario CAGR, and bust-case return, before and after.

### 7. Picks Still Contested

Rank by portfolio impact:

`Rank | Ticker or bottleneck | My position | Their position | Weight at stake | What evidence would settle it`

## Final Verification

- The critique exists at the required path.
- §2 covers every ticker where the portfolios differ.
- §6 sums to 100.0%, and every change cites a head-to-head row.
