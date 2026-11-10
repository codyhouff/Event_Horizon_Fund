# Event Horizon Fund — Step 5: Final Assembly

Step 5 of 5 in the analysis flow (see `README.md` → Analysis Flow):

1. `PROMPT_1_DEEP_DIVE.md`: Claude and Codex each produce an independent deep dive
2. `PROMPT_2_CROSS_CRITIQUE.md`: each model critiques the other's picks head-to-head
3. `PROMPT_3_SYNTHESIS.md`: one model ranks every candidate from both models and writes the final analysis
4. `PROMPT_4_OPTIMIZATION_PASS.md`: both models, independently, look for better stocks and weights
5. **`PROMPT_5_FINAL_ASSEMBLY.md`** ← this file: run by the **Step 3 synthesis model** in one pass. It decides every open item on the evidence and produces the adopted final

---

## Cycle Settings (update each cycle)

- Cycle date: `2026-11-08`
- Cycle folder: `Analysis 2026-11-08/`
- Synthesis model (you): **`Claude`**
- Proposed version from Step 3: `V10.0`

## Goal (shared by all five prompts)

Pick the stocks and weights with the **highest expected return at current prices** over 2027–2030, with an AI-2027-like path as the most likely scenario. For every stock, compare **Expected CAGR** (probability-weighted, the primary metric), **AI-2027 Scenario CAGR**, and **100GW 2030 Scenario CAGR**, as defined in `PROMPT_1_DEEP_DIVE.md` → Named Scenario Returns. Losses in the delay and bust scenarios are a constraint, not the objective.

## Your Job in This Step

Turn the Step 3 proposal into the **adopted** allocation in a single pass:

1. Merge every open item: both Step 4 Optimization Passes and the Step 3 escalations.
2. **Decide each item yourself**, choosing whatever produces the most optimal portfolio under the Goal and the constraints. Don't stop for owner input.
3. Apply the decisions to the final analysis and Deployment Strategy **with minimal edits**.

This is not a new analysis. Don't re-rank the pool or rewrite unaffected sections.

## Files to Read

1. Final: `Analysis 2026-11-08/Event Horizon Fund Analysis 2026-11-08.md`
2. `Analysis 2026-11-08/Deployment Strategy/Deployment Strategy 2026-11-08.md`
3. `Analysis 2026-11-08/inputs/Candidate Ranking 2026-11-08.md`, especially A6 (escalations)
4. Both Step 4 passes:
    - `Analysis 2026-11-08/inputs/Claude Optimization Pass 2026-11-08.md`
    - `Analysis 2026-11-08/inputs/Codex Optimization Pass 2026-11-08.md`
5. `PROMPT_1_DEEP_DIVE.md`: constraints and required deliverables
6. The synthesis valuation scripts, if published (this cycle: `Analysis 2026-11-08/inputs/research/claude_synthesis/`)

## 1. Merge the Open Items

Collect every item from:

- Claude's Owner Decision Sheet (`C1`, `C2`, …);
- Codex's Owner Decision Sheet (`X1`, `X2`, …; assign IDs in order if the sheet has none);
- the Step 3 escalations (`E1`, `E2`, …);
- any sanity-check flag in either pass.

Combine items that propose the same change, keeping all their source IDs. Mark each one:

- **Agree:** both passes propose it;
- **Conflict:** the passes disagree;
- **One model only.**

## 2. Re-check, then Decide

**Re-check before deciding:**

- **Same model:** recompute every proposed change on the same valuation model and prices as the final. Use the synthesis scripts where they exist. Where a Step 4 pass used different inputs, state the difference and decide which inputs are better supported, using the A4 order from `PROMPT_3_SYNTHESIS.md`: facts, then concessions, then the better-supported judgment; on a tie, the lower value. Never average.
- **Facts:** verify every new fact that drives a decision at the primary source.
- **Prices:** if a held or proposed stock has moved more than 10% since the final's price date, re-price it and check whether the decision changes.

**Decision rules, applied in order:**

1. **Constraints first.** Reject any change that breaks a `PROMPT_1_DEEP_DIVE.md` constraint (15% single-name cap, long-only common stock, Moonshot 0%) or a stated cluster or confidence cap. A change may move a cap only with explicit evidence.
2. **Accept a change only if it improves the portfolio by more than noise.** It must raise portfolio Expected CAGR by **at least 0.25pp**, or by at least 0.1pp while also improving the AI-2027 Scenario CAGR and not worsening the bust case by more than 1pp. Smaller gains are cosmetic: reject them and put the name on the bench or watchlist.
3. **Agreement is strong evidence, not proof.** An Agree item still has to pass rule 2 on the same model. A Conflict item goes to the better-supported side, with the deciding evidence stated.
4. **Escalated judgment calls** (risk appetite, concentration, mandate scope). Decide them the way the Goal ranks them: highest expected return first, with losses as a constraint. If two options are within noise on expected return, choose the one with the better bust case.
5. **Input corrections with no weight effect** (for example, a corrected valuation input): apply them to the record.

**Self-sided note.** You wrote the Step 3 final and one of the Step 4 passes. For every decision that sides with your own earlier work, give the deciding evidence. Count how many decisions went to each model's pass.

## 3. Apply the Decisions (minimal edits)

### 3a. Before editing

Copy the Step 3 proposal files to `Analysis 2026-11-08/inputs/superseded/`, so the record of what changed is kept:

- the final analysis (`.md` and `.pdf`), with " (Step 3 proposal)" added to the file name;
- the Deployment Strategy (`.md` and `.pdf`), to `inputs/superseded/Deployment Strategy/`.

### 3b. Update only what the decisions change

| Where | Update |
|---|---|
| Header | Version label and status: **adopted** on `<date>`, after Steps 4 and 5. Keep the label (for example `V10.0`) unless weights changed materially; in that case use the next minor version (for example `V10.1`) |
| Part I: Executive Verdict | The allocation table, portfolio results and decisive changes. Replace "Decisions escalated to the owner" with **"Final decisions"**: each merged item, the decision, its effect and its deciding evidence |
| Model Reconciliation | Add columns for **Claude Step 4 %**, **Codex Step 4 %** and **Adopted %**. Add a row for any new name. Update the portfolio comparison table and the self-sided audit |
| **New section: "Selection Rationale: Chosen vs Considered"** (right after Model Reconciliation) | See 3c below. This is the one new section Step 5 adds |
| Part III.C ranking | Only if a new name enters: add it, fully underwritten on the same model, at its ranked position |
| Part IV | The sleeve text for every holding added, removed or resized; the IV.D valuation table; and the cross-sleeve table if new names were assessed |
| Part V | The architecture table and capital-competition rows the changes affect |
| Part VI | The final allocation, checksum, change table with funding sources, and per-ticker decision table |
| Part VII | Risk actions and monitors that name a changed holding; the bench and trigger rules from accepted items |
| Part VIII | Only the answers whose portfolio implication changes. Edit the implication line; don't rewrite the answer |
| Part IX and the Deployment Strategy | Recompute trades, tranche amounts, cash path and buy-price limits for the adopted weights. Update every trigger rule that names a changed holding |
| Candidate Ranking | Don't rewrite it. Append an **"Addendum: Step 4 and Step 5 decisions"** listing each merged item, its decision, and any new names' rows |

### 3c. Selection Rationale: Chosen vs Considered

One section that explains, in one place, why the adopted portfolio holds what it holds at the weights it does, and why the strongest alternatives aren't in it. Build it from the final ranking, both Step 4 passes and the Step 5 decisions. Don't introduce new analysis.

1. **Funnel summary** (one short table):
    - the number of stocks screened by each model;
    - the number fully valued in Step 1;
    - the pooled candidates in Step 3;
    - the number of new names each Step 4 pass added;
    - the final holdings.
2. **Chosen:** one row per adopted holding.

    `Ticker | Adopted % | Rank | Expected CAGR | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Bust | Why chosen (the edge, in one line) | Why this weight (cap, tie-break, confidence, cluster limit) | Next-best alternative it beat, and by how much`
3. **Considered, not chosen:** the 15–20 strongest names not held. Include:
    - every stock ranked above the lowest-ranked holding;
    - the best Step 4 alternatives from both passes;
    - every name a Step 5 decision rejected.

    `Ticker | Rank / source | Expected CAGR | AI-2027 Scenario CAGR | 100GW 2030 Scenario CAGR | Why not chosen (valuation, bust, confidence, cluster, Step 5 decision) | What would bring it in (price or trigger)`
4. **Removed from the prior version:** one line per prior-version holding that went to 0%, with its main reason and its re-entry trigger. Refer to Part VI.C rather than repeating it.

Keep the section to about two pages. It summarizes and points to the detailed parts.

### 3d. Don't change

- unaffected sections, or the 15 question answers beyond their implication lines;
- the report's price date of record (keep it, and add a note for any stock re-priced in section 2);
- any input or weight that no decision touches.

### 3e. Regenerate and record

- **Recompute:** re-run the synthesis scripts with the adopted weights and use the generated tables. Don't copy numbers by hand.
- **Decision Log:** save the merged items and decisions to `Analysis 2026-11-08/inputs/Step 5 Decision Log 2026-11-08.md`:

    `ID (sources) | Item | Agreement | Claude's view | Codex's view | Decision | Deciding evidence | Effect on portfolio (Expected / AI-2027 / 100GW / bust)`

    End it with the self-sided count and the before/after portfolio.
- **PDFs:** regenerate with `python md_to_pdf.py "<path to .md>"`. On Windows set `$env:WEASYPRINT_DLL_DIRECTORIES = 'C:\msys64\mingw64\bin'` first.
- **README:** update
    - the active allocation version and snapshot;
    - the sleeve rollup;
    - the Synthesis Log (Step 4 models and the adopted version);
    - the file tree.
- **Commit:** commit and push only when the owner asks.

## Final Verification

- The Decision Log exists, and every merged item has a decision with its deciding evidence.
- Every accepted change passed rule 2 on the same model. Every rejected change is on the bench or watchlist with a trigger.
- Allocation checksum = 100.0%. Every change from the Step 3 proposal and from the prior version has a funding source.
- Constraints hold: 15% single-name cap; cluster and Texas caps; bust case better than the baseline's.
- Weights match across the final's tables, the Deployment Strategy, and the README.
- The Selection Rationale section exists. It covers every adopted holding and every name ranked above the lowest-ranked holding.
- Unaffected sections are unchanged. Compare against the superseded Step 3 proposal and list every section you edited.
- Both PDFs are regenerated.
