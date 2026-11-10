# Event Horizon Fund — Step 4: Optimization Pass

Step 4 of 4 in the analysis flow (see `README.md` → Analysis Flow):

1. `PROMPT_1_DEEP_DIVE.md`: Claude and Codex each produce an independent deep dive
2. `PROMPT_2_CROSS_CRITIQUE.md`: each model critiques the other's picks head-to-head
3. `PROMPT_3_SYNTHESIS.md`: one model ranks every candidate from both models and writes the final analysis
4. **`PROMPT_4_OPTIMIZATION_PASS.md`** ← this file: run by the model that did **not** write Step 3

---

## Cycle Settings (update each cycle)

- Cycle date: `2026-11-08`
- Cycle folder: `Analysis 2026-11-08/`
- You are: **`Codex`** (the model that did not write the Step 3 final; 2026-11-08 cycle)

## Goal (shared by all four prompts)

Pick the stocks and weights with the **highest expected return at current prices** over 2027–2030, with an AI-2027-like path as the most likely scenario. For every stock, compare **Expected CAGR** (probability-weighted, the primary metric), **AI-2027 Scenario CAGR**, and **100GW 2030 Scenario CAGR**, as defined in `PROMPT_1_DEEP_DIVE.md` → Named Scenario Returns. Losses in the delay and bust scenarios are a constraint, not the objective.

## Your Job in This Step

Take a fresh pass at the final allocation and answer one question: **is there a better portfolio?** That means better stocks and better weights. Steps 1–3 already compared everything both models found. Your edge is to look **outside that pool** and to challenge the weights.

Don't rewrite the final analysis. Propose specific, justified changes, or show why none are warranted.

## Files to Read

1. Final: `Analysis 2026-11-08/Event Horizon Fund Analysis 2026-11-08.md`
2. `Analysis 2026-11-08/inputs/Candidate Ranking 2026-11-08.md`: the ranked pool and the scenario assumptions it used
3. Both deep dives in `Analysis 2026-11-08/inputs/`, to see which candidates were already considered and why they were rejected
4. `PROMPT_1_DEEP_DIVE.md`: constraints, valuation framework, and named scenarios

Do fresh research with current prices. If a candidate was already rejected in an input, address that rejection directly. Don't just repeat the name.

## 1. Top 20 Alternatives

List the 20 most credible stocks **not** in the final allocation that could improve it. Include:

- **at least 10 names that are not in the Step 3 candidate pool**: new bottlenecks, new developments, overlooked suppliers;
- the strongest excluded names from the candidate ranking, but only where you think the ranking got them wrong;
- any category leader, cheaper peer, or second-order beneficiary of the same bottleneck the portfolio holds.

`Rank | Ticker | Bottleneck / theme | Competes with (held ticker) | Price + date | Valuation status | Expected CAGR vs the held ticker's | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Verdict (Add / Replace X / Watchlist / Reject) | Why or why not`

Use the candidate ranking's scenario assumptions (A1) so your numbers compare with the final's. If you think those assumptions are wrong, say so in §3.

For every **Add** or **Replace** verdict, include full underwriting per `PROMPT_1_DEEP_DIVE.md`: bear/base/bull terminal values, probabilities, E[TV], implied CAGR, key assumptions, and what would falsify it. Also explain why it beats what it would displace, considering valuation, bottleneck strength, and how much it shares the same drivers as the rest of the portfolio.

## 2. Weakest Current Holdings

Rank all current holdings by valuation-adjusted expected return and conviction. For the bottom 5:

`Ticker | Final % | Expected CAGR | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Main weakness | Best replacement (from §1 or another holding) | Keep / Trim / Replace | Why`

## 3. Allocation Optimization

Check whether the weights themselves are right, given the names:

- holdings whose weight is out of line with their expected return or confidence;
- concentration in shared drivers that's too high, or diversification that's paying for too little protection;
- whether the number of holdings is right.

Then give the result:

- **Proposed allocation:** up to 8 changes, high conviction only, no cosmetic tweaks.
  `Ticker | Final % | Proposed % | Delta | Funding source | Reason`
  Must sum to exactly 100.0%, with a checksum line. Show Expected CAGR, AI-2027 Scenario CAGR, 100GW 2030 Scenario CAGR, and bust-case return, before and after.
- Or **no changes**, with the evidence that the final is already the better portfolio.

## 4. Sanity Check (brief)

Only flag problems. Don't write up a full audit:

- Final allocation sums to 100.0%, and weights match across the final's tables and the Deployment Strategy.
- Spot-recompute Expected CAGR for the 5 largest holdings from the report's stated inputs.
- Any stock either model held or fully underwrote that's missing from the candidate ranking.
- Any top-ranked stock that was left out, or low-ranked stock that was included, without an explanation.
- Any final weight that is just the average of the two models' weights without its own justification.

## Output

Save to `Analysis 2026-11-08/inputs/Optimization Pass 2026-11-08.md`. A PDF is optional.

Start the file with an **Owner Decision Sheet**, one page:

- each proposed change from §3, and each escalated item from the candidate ranking;
- for each one: the question, the case for and against in 1–2 sentences, your recommendation, and the weight at stake.

Then write §1–§4.

## After This Step (Step 5: Owner Decision, no prompt file)

1. The owner accepts or rejects each item on the Owner Decision Sheet.
2. The **synthesis model** applies the accepted changes and any sanity-check fixes to the final analysis and Deployment Strategy, regenerates the PDFs, and marks the version as adopted.
3. Update `README.md`: active allocation version, snapshot, sleeve rollup, and synthesis log. Then commit.
