# Event Horizon Fund Prompt Template

Use this prompt to run each full analysis cycle.

---

Read this file and execute it as a **full deep dive**.  
This may take a while; prioritize completeness and quality over speed.

You are doing a full-cycle Event Horizon Fund review.

## Objective
Re-evaluate the Event Horizon Fund thesis and allocations for maximum risk-adjusted upside from AGI/ASI infrastructure bottlenecks, using all provided sources.

## Required Inputs (read all)
1) Foundation and prior house view:
- `Original Large Thesis Writeup 2025-09-10/Event Horizon Fund Draft V7.3 2025-09-10.md`
- `Analysis 2026-03-31/Event Horizon Fund Analysis 2026-03-31.md`

2) New model inputs:
- `Analysis 2026-05-10/inputs/GPT5.5 Pro Research 2026-05-05.md`
- `Analysis 2026-05-10/inputs/Gemini Pro Research 2026-05-05.md`

3) Background web context:
- <https://ai-2027.com/>
- <https://situational-awareness.ai/>
- <https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/>
- <https://epoch.ai/trends>

## Portfolio Constraints
- Event Horizon Fund remains ~50% of total net investments.
- Foundation + Continuity structure stays unchanged unless explicitly justified.
- Moonshot sleeve currently 0% unless strongly justified otherwise.

## Current Event Horizon Allocation Baseline (V8.3)
Paste the latest allocation table here before running.

## Required Research Standards
- Perform fresh, up-to-date research for **every currently allocated ticker** (not just a subset).
- For each holding, verify whether it remains the optimal choice under the current thesis and market conditions.
- Explicitly evaluate **credible alternatives/contenders** for each sleeve and explain why they should or should not replace or complement current picks.
- For each sleeve, evaluate at least 2 alternatives and explicitly rank each as: `Better / Comparable / Worse` vs current holding.
- Evaluate **all credible stock alternatives** surfaced by:
  - GPT/Gemini input documents
  - prior analysis watchlists
  - current market developments
  even if they do not fit neatly into existing sleeves.
- Include a dedicated cross-sleeve candidate section:
  - `Ticker | Candidate Theme | Why Considered | Better/Comparable/Worse | Add? (Y/N) | Why/Why not`
- Identify any thesis drift, valuation dislocations, execution risks, or new bottlenecks since the last cycle.
- Include a market-data timestamp and source date for any time-sensitive claim (price, valuation, consensus estimates, macro data).
- Flag stale inputs explicitly when data is older than 30 days.

## Formatting Requirement
- Follow a very similar structure and formatting style as:
  - `Analysis 2026-03-31/Event Horizon Fund Analysis 2026-03-31.md`
- Keep headings/tables style consistent so versions are easy to compare.
- You may propose an improved section layout if it increases clarity, but preserve overall comparability with the reference format.

## Hard Allocation Constraints
- Final Event Horizon allocation must sum to **exactly 100.0%**.
- Include explicit checksum validation.
- If a new stock is added, specify exact funding source(s) from existing positions.
- Avoid tiny/immaterial allocations unless explicitly justified as hedges.
- Keep Moonshot at 0% unless explicitly instructed otherwise.

## Required Deliverables
1) New analysis file:
- `Analysis 2026-05-10/Event Horizon Fund Analysis 2026-05-10.md`
- `Analysis 2026-05-10/Event Horizon Fund Analysis 2026-05-10.pdf`

2) Allocation decision outputs (required):
- Final allocation table (must sum to 100.0%)
- Change table (`From`, `To`, `Delta`, `Why`)
- `Keep / Increase / Reduce / Remove / Add` decision for every ticker
- Per-ticker decision framework table:
  - `Ticker | Current % | Recommended % | Action | Confidence (1-5) | Why | What would falsify this`
- Top 5 risks and invalidation triggers
- What changed vs `2026-03-31` (new evidence only)

3) Near-term execution plan (separate file):
- `Analysis 2026-05-10/Deployment Strategy/Deployment Strategy 2026-05-10.md`
- `Analysis 2026-05-10/Deployment Strategy/Deployment Strategy 2026-05-10.pdf`
- Include a 2-4 tranche buy plan for next ~3 weeks based on:
  - current allocation gaps
  - market conditions
  - scenario probabilities
  - reserve logic

## Locked Output Structure (in this order)
1. Executive verdict
2. What changed since last cycle
3. Sleeve-by-sleeve review
4. Final allocation + checksum (100.0%)
5. Risk and invalidation dashboard
6. Near-term deployment strategy

## Deployment Execution Rules (explicit)
- Include explicit trigger rules:
  - `If Scenario A -> do X`
  - `If Scenario B -> do Y`
- Include no-trade conditions.
- Include reserve deployment rules.

## Analysis Standards
- Be explicit, evidence-based, and internally consistent.
- No duplicate sections.
- Be decisive; avoid vague language.
- If uncertain, state uncertainty and provide conditional plan branches.
- Focus on bottleneck economics:
  - scarcity
  - lead times
  - pricing power
  - substitutability

## Final Verification (required)
- Verify all required markdown and PDF outputs were generated.
- Verify allocation checksum = 100.0%.
- Verify every allocation change has a funding source.
