# Followup Gemini & GPT Prompt

Use this exact prompt for both Gemini Pro Research and GPT5.5 Research.

You are reviewing an existing portfolio analysis and must challenge it rigorously.

## Primary file to review
- `Analysis 2026-05-10/Event Horizon Fund Analysis 2026-05-10.md`

## Goal
Determine whether the current allocation is truly optimal for maximizing returns from AI infrastructure bottlenecks (2026-2030), or whether a superior allocation exists.

## Requirements

1) **Red-team first**
- List the top 10 weaknesses in the current allocation/framework.
- For each weakness, quantify likely impact (`low` / `medium` / `high`) and confidence.

2) **Propose an improved allocation**
- Provide a full revised allocation table summing to **100.0%**.
- Include only high-conviction changes (no cosmetic edits).
- For each change, include: `old %`, `new %`, `reason`, and expected benefit.

3) **Alternatives challenge**
- For each sleeve, evaluate at least 3 alternatives (including cross-sleeve contenders).
- Explicitly rank each alternative: `Better` / `Comparable` / `Worse` vs current holding.

4) **Invalidation test**
- Give the top 5 developments that would invalidate your revised allocation by 2027.
- Provide measurable indicators for each invalidation condition.

5) **Scenario robustness**
- Stress test under 3 scenarios:
  - Faster AI acceleration
  - 2-3 year AI delay
  - Capex slowdown + policy/regulatory constraints
- Show which names are most fragile and most resilient in each scenario.

6) **BE and COHR valuation check (required)**
- Are `BE` and `COHR` currently overpriced, fairly valued, or still attractive?
- Provide a range-based decision framework with add/hold/trim zones.

7) **Output format**
- Executive verdict (max 10 bullets)
- Revised allocation table (100.0% checksum)
- Sleeve-by-sleeve change log
- Top 5 adds, top 5 trims/removals
- Risk/invalidation dashboard
- Final recommendation: Keep current allocation vs adopt revised (with confidence 1-5)
- Machine-readable final table:
  - `Ticker | Old % | New % | Delta | Action | One-line rationale`

## Constraints
- Be decisive; do not hedge with generic language.
- If recommending no changes, prove why with explicit evidence.
- Focus on bottleneck economics (scarcity, lead times, pricing power, substitution risk), not broad market commentary.
- Use up-to-date evidence and clearly label assumptions if any data is stale.
- For each major factual claim, include source + date.
- Flag any evidence older than 30 days as stale.

## Usage note (for request efficiency)
- Run this prompt as a one-pass complete output.
- Use the exact same prompt for both Gemini Pro and GPT5.5.
- After both outputs are complete, do a reconciliation pass:
  - Where they agree
  - Where they conflict
  - Final merged best-of allocation
