# Event Horizon Fund — Step 5: Owner Decisions and Final Assembly

Step 5 of 5 in the analysis flow (see `README.md` → Analysis Flow):

1. `PROMPT_1_DEEP_DIVE.md`: Claude and Codex each produce an independent deep dive
2. `PROMPT_2_CROSS_CRITIQUE.md`: each model critiques the other's picks head-to-head
3. `PROMPT_3_SYNTHESIS.md`: one model ranks every candidate from both models and writes the final analysis
4. `PROMPT_4_OPTIMIZATION_PASS.md`: both models, independently, look for better stocks and weights
5. **`PROMPT_5_FINAL_ASSEMBLY.md`** ← this file: run by the **Step 3 synthesis model**, in two phases with an owner decision in between

---

## Cycle Settings (update each cycle)

- Cycle date: `2026-11-08`
- Cycle folder: `Analysis 2026-11-08/`
- Synthesis model (you): **`Claude`**
- Proposed version from Step 3: `V10.0`

## Goal (shared by all five prompts)

Pick the stocks and weights with the **highest expected return at current prices** over 2027–2030, with an AI-2027-like path as the most likely scenario. For every stock, compare **Expected CAGR** (probability-weighted, the primary metric), **AI-2027 Scenario CAGR**, and **100GW 2030 Scenario CAGR**, as defined in `PROMPT_1_DEEP_DIVE.md` → Named Scenario Returns. Losses in the delay and bust scenarios are a constraint, not the objective.

## Your Job in This Step

Turn the Step 3 proposal into the adopted allocation. **The owner decides; you prepare the decisions and apply them.**

- **Phase A:** merge both Step 4 Optimization Passes and the Step 3 escalations into one Owner Decision Sheet. Then stop.
- **Phase B:** once the owner has answered, apply the accepted decisions to the final analysis and Deployment Strategy **with minimal edits**.

This is not a new analysis. Don't re-rank the pool, rewrite unaffected sections, or reopen decisions the owner has made.

## Files to Read

1. Final: `Analysis 2026-11-08/Event Horizon Fund Analysis 2026-11-08.md`
2. `Analysis 2026-11-08/Deployment Strategy/Deployment Strategy 2026-11-08.md`
3. `Analysis 2026-11-08/inputs/Candidate Ranking 2026-11-08.md`, especially A6 (escalations)
4. Both Step 4 passes: `Analysis 2026-11-08/inputs/Claude Optimization Pass 2026-11-08.md` and `Analysis 2026-11-08/inputs/Codex Optimization Pass 2026-11-08.md`
5. `PROMPT_1_DEEP_DIVE.md`: constraints and required deliverables
6. The synthesis valuation scripts, if published (this cycle: `Analysis 2026-11-08/inputs/research/claude_synthesis/`)

## Phase A: Merged Owner Decision Sheet

Save to `Analysis 2026-11-08/inputs/Owner Decision Sheet 2026-11-08.md`.

### A1. Merge the items

Collect every item from:

- Claude's Owner Decision Sheet (`C1`, `C2`, …);
- Codex's Owner Decision Sheet (`X1`, `X2`, …);
- the Step 3 escalations (`E1`, `E2`, …).

Combine items that propose the same change, and keep all their source IDs.

### A2. Re-check before recommending

- **Same model:** recompute every proposed change on the same valuation model and prices as the final, so each item's effect is comparable. Use the synthesis scripts where they exist. Where a Step 4 pass used different inputs, state the difference.
- **Facts:** verify any new fact that drives a recommendation at the primary source.
- **Prices:** if a held or proposed stock has moved more than 10% since the final's price date, re-price it and say whether the recommendation changes.

### A3. The sheet

`ID (sources) | Question | Claude's view | Codex's view | Agreement (Agree / Conflict / One model only) | Recommendation | Weight at stake | Effect on portfolio (Expected / AI-2027 / 100GW / bust) | Owner decision`

Leave the **Owner decision** column blank.

- **Agree:** both passes propose the same change. This is the strongest signal; say so.
- **Conflict:** give each side's best case in one or two sentences and the evidence that decides it.
- **One model only:** say why the other model didn't raise it, if its file shows why. For example, it considered and rejected the name.
- **Combined portfolio:** below the sheet, show the portfolio if every recommendation is accepted, next to the Step 3 proposal: Expected CAGR, AI-2027 Scenario CAGR, 100GW 2030 Scenario CAGR, bust and delay returns, and the checksum.

**Self-sided note:** you wrote both the Step 3 final and one of the Step 4 passes. Mark each recommendation that sides with your own work, and give the deciding evidence.

### A4. Stop

Ask the owner to fill in the Owner decision column, or to answer each ID in chat: Accept / Reject / Modify (with the change). **Don't apply anything until the owner answers.**

## Phase B: Apply the Owner's Decisions (minimal edits)

### B1. Before editing

Copy the Step 3 proposal files to `Analysis 2026-11-08/inputs/superseded/`, so the record of what changed is kept:

- the final analysis (`.md` and `.pdf`), with " (Step 3 proposal)" added to the file name;
- the Deployment Strategy (`.md` and `.pdf`), to `inputs/superseded/Deployment Strategy/`.

### B2. Update only what the decisions change

| Where | Update |
|---|---|
| Header | Version label and status: **adopted** on `<date>`, after Step 4 and owner decisions. Keep the label (for example `V10.0`) unless the owner chooses a new one |
| Part I: Executive Verdict | The allocation table, portfolio results, and decisive changes. Replace "Decisions escalated to the owner" with **"Owner decisions"**: each ID, the decision taken, and its effect |
| Model Reconciliation | Add columns for **Claude Step 4 %**, **Codex Step 4 %** and **Adopted %**. Add a row for any new name. Update the portfolio comparison table |
| **New section: "Selection Rationale: Chosen vs Considered"** (right after Model Reconciliation) | See B2a below. This is the one new section Step 5 adds |
| Part III.C ranking | Only if a new name enters: add it, fully underwritten on the same model, at its ranked position |
| Part IV | The sleeve text for every holding added, removed or resized; the IV.D valuation table; and the cross-sleeve table if new names were assessed |
| Part V | The architecture table and capital-competition rows that the changes affect |
| Part VI | The final allocation, checksum, change table with funding sources, and per-ticker decision table |
| Part VII | Risk actions and monitors that name a changed holding |
| Part VIII | Only the answers whose portfolio implication changes. Edit the implication line; don't rewrite the answer |
| Part IX and the Deployment Strategy | Recompute trades, tranche amounts, cash path and buy-price limits for the adopted weights. Update every trigger rule that names a changed holding |
| Candidate Ranking | Don't rewrite it. Append an **"Addendum: Step 4 and owner decisions"** listing each decision and any new names' rows |

### B2a. Selection Rationale: Chosen vs Considered

Add one section that explains, in one place, why the adopted portfolio holds what it holds at the weights it does, and why the strongest alternatives aren't in it. Build it from the final ranking, both Step 4 passes and the owner's decisions. Don't introduce new analysis.

1. **Funnel summary** (one short table):
    - the number of stocks screened by each model;
    - the number fully valued in Step 1;
    - the pooled 58 in Step 3;
    - the number of new names each Step 4 pass added;
    - the final holdings.
2. **Chosen:** one row per adopted holding.

    `Ticker | Adopted % | Rank | Expected CAGR | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Bust | Why chosen (the edge, in one line) | Why this weight (cap, tie-break, confidence, cluster limit) | Next-best alternative it beat, and by how much`
3. **Considered, not chosen:** the 15–20 strongest names that aren't held. Include:
    - every stock ranked above the lowest-ranked holding;
    - the best Step 4 alternatives from both passes;
    - every name the owner rejected.

    `Ticker | Rank / source | Expected CAGR | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Why not chosen (valuation, bust, confidence, cluster, owner decision) | What would bring it in (price or trigger)`
4. **Removed from the prior version:** one line per V9.1 holding that went to 0%: the main reason and its re-entry trigger. Refer to Part VI.C rather than repeating it.

Keep the section to about two pages. It summarizes and points to the detailed parts; it doesn't repeat them.

**Don't change:**

- unaffected sections or the 15 question answers, beyond implication lines;
- the report's price date of record (keep it, and add a note for any stock re-priced in A2);
- any input or weight the owner didn't decide.

### B3. Regenerate and record

- Re-run the synthesis scripts with the adopted weights and use the generated tables. Don't copy numbers by hand.
- Regenerate the PDFs: `python md_to_pdf.py "<path to .md>"`. On Windows set `$env:WEASYPRINT_DLL_DIRECTORIES = 'C:\msys64\mingw64\bin'` first.
- Update `README.md`:
    - the active allocation version and snapshot;
    - the sleeve rollup;
    - the Synthesis Log (Step 4 models and the adopted version);
    - the file tree.
- Commit and push only when the owner asks.

## Final Verification

- The Owner Decision Sheet exists, and every item has an owner decision applied exactly as given (Accept, Reject or Modify).
- Allocation checksum = 100.0%. Every change from the Step 3 proposal and from V9.1 has a funding source.
- Constraints hold: 15% single-name cap; cluster and Texas caps; bust case better than the baseline's.
- Weights match across the final's tables, the Deployment Strategy, and the README.
- The Selection Rationale section exists. It covers every adopted holding and every name ranked above the lowest-ranked holding.
- Unaffected sections are unchanged. Compare against the superseded Step 3 proposal and list every section you edited.
- Both PDFs are regenerated.
