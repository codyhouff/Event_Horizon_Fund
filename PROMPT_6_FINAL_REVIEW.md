# Event Horizon Fund — Step 6: Final Review

Step 6 of the analysis flow, run after the final is adopted (see `README.md` → Analysis Flow):

1. `PROMPT_1_DEEP_DIVE.md`: Claude and Codex each produce an independent deep dive
2. `PROMPT_2_CROSS_CRITIQUE.md`: each model critiques the other's picks head-to-head
3. `PROMPT_3_SYNTHESIS.md`: one model ranks every candidate from both models and writes the final analysis
4. `PROMPT_4_OPTIMIZATION_PASS.md`: both models, independently, look for better stocks and weights
5. `PROMPT_5_FINAL_ASSEMBLY.md`: the synthesis model decides every open item and produces the adopted final
6. **`PROMPT_6_FINAL_REVIEW.md`** ← this file: run by the **other model** (not the synthesis model). It audits the adopted final against the Step 5 record and corrects it where needed

---

## Cycle Settings (update each cycle)

- Cycle date: `2026-11-08`
- Cycle folder: `Analysis 2026-11-08/`
- Synthesis model (wrote Steps 3 and 5): `Claude`
- Reviewer (you): **`Codex`**
- Adopted version under review: `V10.1`
- Price date of record: `2026-11-09` (close)

## Goal (shared by all prompts)

Pick the stocks and weights with the **highest expected return at current prices** over 2027–2030, with an AI-2027-like path as the most likely scenario. For every stock, compare **Expected CAGR** (probability-weighted, the primary metric), **AI-2027 Scenario CAGR**, and **100GW 2030 Scenario CAGR**, as defined in `PROMPT_1_DEEP_DIVE.md` → Named Scenario Returns. Losses in the delay and bust scenarios are a constraint, not the objective.

## Your Job in This Step

The final is already adopted. **Don't rebuild it.** Check it and fix it:

1. **Audit the Step 5 decisions:** did each one follow from the evidence and the PROMPT_5 decision rules?
2. **Audit the final document:** does every number, weight and claim match the Step 5 record and the generated tables, and is the document internally consistent?
3. **Edit the final in place** where something is wrong, and record every finding (including the ones you reject) in a Review Log.

You're a second pair of eyes on another model's work, not a third synthesis. Prefer leaving a defensible call alone over replacing it with an equally defensible one.

## Files to Read

1. The adopted final: `Analysis 2026-11-08/Event Horizon Fund Analysis 2026-11-08.md`
2. `Analysis 2026-11-08/inputs/Step 5 Decision Log 2026-11-08.md`
3. `Analysis 2026-11-08/Deployment Strategy/Deployment Strategy 2026-11-08.md` (local only, gitignored)
4. `Analysis 2026-11-08/inputs/Candidate Ranking 2026-11-08.md`, including the "Addendum: Step 4 and Step 5 decisions"
5. Both Step 4 passes:
    - `Analysis 2026-11-08/inputs/Claude Optimization Pass 2026-11-08.md`
    - `Analysis 2026-11-08/inputs/Codex Optimization Pass 2026-11-08.md`
6. The Step 3 proposal, for comparison: `Analysis 2026-11-08/inputs/superseded/`
7. The synthesis model, scripts and tables: `Analysis 2026-11-08/inputs/research/claude_synthesis/` (`step5_model.py`, `step5_tables.py`, `data/step5_*.json`, `data/ports5.json`, `tables5/`; the README there has the run commands)
8. `PROMPT_5_FINAL_ASSEMBLY.md`: the rules the final was supposed to follow
9. `PROMPT_1_DEEP_DIVE.md`: constraints and required deliverables

## 1. Reproduce First

Before judging anything, re-run the Step 5 commands from `claude_synthesis/README.md` into a scratch location, not over the committed files. Run them from inside `claude_synthesis/`, since they use relative paths. The commands are written for bash; in PowerShell, replace `"$(cat data/ports5.json)"` with `(Get-Content data/ports5.json -Raw)`. Confirm that the outputs match `data/step5_out.json`, `data/step5_out_cxmult.json` and `tables5/` byte for byte.

If they don't match, that is finding #1. Stop and report it before reviewing anything else, because every later check depends on these tables.

## 2. Audit the Step 5 Decisions

For each Decision Log item (D1, D2, …), check:

- **Rule compliance:** was the PROMPT_5 decision rule applied correctly? An accepted change must raise portfolio Expected CAGR by at least 0.25pp, or by at least 0.1pp while improving AI-2027 and not worsening the bust by more than 1pp. Were constraints and caps respected?
- **Inputs:** where the passes disagreed, was the better-supported input chosen (facts, then concessions, then better-supported judgment; on a tie, the lower value)? Spot-check every fact that drives a decision at its primary source.
- **Self-siding:** the synthesis model also wrote one of the Step 4 passes. For every decision that sided with its own pass, is the stated deciding evidence actually sufficient?
- **Your own self-siding:** you also wrote one of the Step 4 passes. Treat your own rejected proposals with extra skepticism. To overturn a decision in favor of your own pass, you need evidence that wasn't in front of the synthesis model, or a demonstrable error in how it applied the rules. Disagreeing with its judgment isn't enough. Count your verdicts that favor each model's pass and report them in the Review Log summary.
- **Omissions:** is any item from either Step 4 Owner Decision Sheet, any Step 3 escalation or any sanity-check flag missing from the Decision Log?

**Verdict for each item:** **Upheld**, **Upheld with correction** (the decision stands but its numbers or wording were wrong), or **Overturned**.

## 3. Audit the Final Document

Check the adopted final for:

1. **Numbers:** every table and every quoted figure matches `tables5/` and `data/step5_out.json`. This includes the per-stock returns, the portfolio Expected / AI-2027 / 100GW / bust / delay, and the ranks. Pay special attention to numbers that were hand-written in prose rather than pasted from a generated table.
2. **Weights:** the same weights appear in Part I, Model Reconciliation, Selection Rationale, Parts IV, V, VI and IX, the Deployment Strategy, and `README.md`. The checksum is 100.0%.
3. **Internal consistency:**
    - no section still describes V10.0 weights or holdings as current;
    - every name that left (for example VST) has its re-entry trigger;
    - every name that entered (for example STRL) is fully underwritten in III.C and IV;
    - the trigger rules (Texas, MOD gate, NVDA review) agree everywhere they appear.
4. **Required content:** everything PROMPT_5 3b–3c requires is present, including the Selection Rationale section. It must cover every holding and every name ranked above the lowest-ranked holding.
5. **Stale or wrong claims:** dates, event calendars (earnings dates, investor days, board reviews), and any fact that has changed since the price date. Verify these at the primary source. If a held or bench name has moved more than 10% since the price date, note it. Don't re-price the report; that belongs to the next cycle or to a trigger rule.
6. **Clarity:** wording that is ambiguous or misleading about what the owner should do. Fix only what could cause a wrong action. Don't restyle.

## 4. What You May Change

| Kind of finding | What you do |
|---|---|
| **Fix:** a wrong number, a stale weight, a contradiction, a missing trigger, a broken cross-reference, misleading wording | Edit the final (and the Deployment Strategy or README if the same error is there) directly, with the smallest change that fixes it |
| **Input correction with no weight effect** | Apply it to the record, as PROMPT_5 rule 5 allows. If it changes a generated table, re-run the scripts (see 5b) rather than editing the table by hand |
| **Overturned decision or a new weight/holding change** | Allowed **only** if it passes PROMPT_5 rule 2 on the same model, the same Nov 9 prices and the same constraints. Show the before/after portfolio. Anything that doesn't clear the bar goes in the Review Log as a **Recommendation for next cycle**, not into the final |
| **A judgment call you'd have made differently** that is within noise | Don't change it. Log it as **Noted, no change** with your reasoning |

Hard limits:

- Don't add new candidates to the pool, re-rank the pool, or change valuation inputs the Decision Log didn't touch, unless the change fixes a demonstrable error (a wrong fact, a formula bug, a double count).
- Don't edit the Step 1–4 files, the Decision Log, the Candidate Ranking, or anything in `inputs/superseded/`. They're the record. Your findings go in the Review Log.
- Don't change the price date of record.

## 5. Apply and Record

### 5a. Before editing

Copy the adopted final (`.md` and `.pdf`) to `Analysis 2026-11-08/inputs/superseded/`, adding " (V10.1 before Step 6)" to the file name. If you'll change the Deployment Strategy, copy it the same way to `inputs/superseded/Deployment Strategy/`.

### 5b. If weights change

- Use the next minor version (for example `V10.1` → `V10.2`) and update the header status: adopted after Step 6 review on `<date>`.
- Add the new portfolio to the synthesis model's portfolio set. Put any new script or data in `Analysis 2026-11-08/inputs/research/codex_final_review/`, and never overwrite the `step5_*` files. Re-run, and use the generated tables. Don't copy numbers by hand.
- Update everything PROMPT_5 3b lists for a weight change: Part I, Model Reconciliation (add a **Step 6 %** column), Selection Rationale, Parts IV–VII and IX, the Deployment Strategy (trades, tranches, cash path, limits), and `README.md` (version, snapshot, sleeve rollup, Synthesis Log).

If no weights change, keep the version label and add one header line: "Reviewed in Step 6 by `<model>` on `<date>`: N fixes, no weight changes."

### 5c. Review Log

Save to `Analysis 2026-11-08/inputs/Step 6 Review Log 2026-11-08.md`:

1. **Summary:** the reproduction result; the self-siding count; counts of Upheld / Upheld with correction / Overturned; the number of fixes; whether weights changed; the before/after portfolio, if they did.
2. **Decision audit:**

    `ID | Step 5 decision | Verdict | Evidence | Effect (Expected / AI-2027 / 100GW / bust), if changed`
3. **Document findings:**

    `# | Location (part / section / line) | Finding | Severity (wrong action possible / wrong number / cosmetic) | Action (fixed / noted / recommendation for next cycle)`
4. **Recommendations for next cycle:** findings that didn't clear the bar or that belong to the process (for example a PROMPT change).
5. **Sections edited:** the list of every section of the final you changed, from a diff against the copy in `inputs/superseded/`.

### 5d. Regenerate

- **PDFs:** regenerate every `.md` you edited, plus the Review Log, with `python md_to_pdf.py "<path to .md>"`. On Windows set `$env:WEASYPRINT_DLL_DIRECTORIES = 'C:\msys64\mingw64\bin'` first. Python-Markdown needs a blank line before every list.
- **README:** add the Step 6 reviewer and outcome to the Synthesis Log, and add the Review Log to the file tree.
- **Commit:** commit and push only when the owner asks.

## Final Verification

- The reproduction check ran, and its result is in the Review Log.
- Every Decision Log item has a verdict with evidence.
- Every change to weights passed PROMPT_5 rule 2 on the same model. Everything else is logged as a fix, a "noted, no change" or a recommendation.
- Weights match across the final, the Deployment Strategy and the README. The checksum is 100.0%.
- No Step 1–5 record file was edited.
- The pre-review copy is in `inputs/superseded/`, and the Review Log lists every section you edited.
- The PDFs are regenerated.
