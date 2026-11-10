# Event Horizon Fund

Concentrated AI infrastructure portfolio focused on physical and economic bottlenecks across power, semis, memory, networking, optical, and grid buildout.

Current active allocation version: **V10.1** (adopted 2026-11-10, after Steps 4 and 5 of the 2026-11-08 cycle). Supersedes V9.1 (2026-05-10).  
Primary source doc: `Analysis 2026-11-08/Event Horizon Fund Analysis 2026-11-08.md`.

## Read This First

- Core thesis, full framework and the adopted allocation: `Analysis 2026-11-08/Event Horizon Fund Analysis 2026-11-08.md`
- Current execution plan: `Analysis 2026-11-08/Deployment Strategy/Deployment Strategy 2026-11-08.md` (local only; the `Deployment Strategy/` folders are gitignored)
- How the final decisions were made: `Analysis 2026-11-08/inputs/Step 5 Decision Log 2026-11-08.md`
- Prior cycle: `Analysis 2026-05-10/Event Horizon Fund Analysis 2026-05-10.md` (V9.1)

## Current Allocation Snapshot (V10.1)

**Accelerators (15%):** NVDA (15%)  
**AI Platform (15%):** META (15%)  
**Rack Thermal & Power (15%):** VRT (15%)  
**HBM / Memory (15%):** MU (15%)  
**Power Generation (12%):** NRG (12%)  
**Electrical Distribution & Cooling (12%):** NVT (12%)  
**Rack-Scale Integration (10%):** CLS (10%)  
**Site Development & Electrical Installation (6%):** STRL (6%)  
**Moonshot (0%)**  
Total: 100%

On the synthesis model at Nov 9, 2026 prices: Expected CAGR 15.4% to 2030 (AI-2027 Scenario 24.0%; 100GW 2030 Scenario 38.1%), bust −61.5%, 2–3 year delay −22.3%. V9.1 on the same model: 7.9% expected, bust −67.3%.

### Sleeve Rollup


| Sleeve                                               | Weight |
| ---------------------------------------------------- | ------ |
| Accelerators (NVDA)                                  | 15%    |
| HBM / Memory (MU)                                    | 15%    |
| Rack-Scale Integration (CLS)                         | 10%    |
| Thermal, Electrical & Site Work (VRT + NVT + STRL)   | 33%    |
| Power Generation (NRG)                               | 12%    |
| AI Platform (META)                                   | 15%    |
| Moonshot                                             | 0%     |




## Thesis (Quick Summary)

- AI capex remains elevated and has moved higher, not lower.
- Best risk-adjusted exposure is in **bottleneck owners**, not broad integrators.
- Portfolio concentrates on the most constrained layers:
  - power delivery and generation
  - foundry and wafer-fab equipment
  - memory (HBM), cooling, and optical throughput
  - grid buildout and electrical equipment
- Core risk controls: position sizing discipline, sleeve diversification, and explicit invalidation triggers.



## Analysis Flow

Each cycle runs two models (Claude Code and Codex) through five prompts, plus an optional sixth review step. Every prompt has the same goal: **pick the stocks and weights with the highest expected return at current prices, with an AI-2027-like path as the most likely scenario.** Every stock reports three returns:

- **Expected CAGR**: probability-weighted, the primary ranking metric;
- **AI-2027 Scenario CAGR**;
- **100GW 2030 Scenario CAGR**, from Situational Awareness's path to a trillion-dollar cluster.

Each step looks for better stocks in a different place, so the steps work like a funnel rather than repeating each other:

| Step | Main purpose | Where it looks for better stocks |
| ---- | ------------ | -------------------------------- |
| 1. Deep dive | Build the best portfolio independently | The whole universe, from scratch |
| 2. Cross-critique | Head-to-head: for every stock where the two portfolios differ, which pick is better priced with the higher expected return? | The other model's picks versus mine |
| 3. Synthesis | Value every candidate from both models on one valuation model, rank them, and build the portfolio from the ranking | Everything both models found, combined |
| 4. Optimization pass | Each model independently: top 20 alternatives (at least 10 that neither model considered), the weakest holdings, and better weights | Outside what both models found |
| 5. Final assembly | Merge both optimization passes and the open Step 3 calls; decide each item on the evidence (an accepted change must beat noise on the same model); apply the decisions with minimal edits and adopt | Nowhere new: chooses among the proposals |
| 6. Final review (optional) | The other model audits the adopted final: reproduces the tables, checks each Step 5 decision and the document's consistency, and fixes errors in place. A weight change must pass the same Step 5 bar | Nowhere new: checks what was decided |

```text
1. Deep dive      Claude Deep Dive              Codex Deep Dive            (blind, parallel)
                         │      ╲            ╱      │
2. Cross-critique  Claude Critique of Codex    Codex Critique of Claude   (parallel)
                         └───────────┬──────────────┘
3. Synthesis       one model:  Candidate Ranking → Final Analysis + Deployment Strategy
                                     │
4. Optimization   Claude Optimization Pass       Codex Optimization Pass    (independent, parallel)
                         └───────────┬──────────────┘
5. Final assembly  synthesis model: merge items → decide on evidence → apply + adopt + update README
                                     │
6. Final review    other model: reproduce → audit decisions + document → fix in place (optional)
```

| Step | Prompt | Who runs it | Output (in `Analysis YYYY-MM-DD/`) |
| ---- | ------ | ----------- | ---------------------------------- |
| 0 | — | Owner | Update the cycle settings in all five prompts: cycle date, prior analysis, baseline version and allocation. Create `Analysis YYYY-MM-DD/inputs/`. |
| 1 | `PROMPT_1_DEEP_DIVE.md` | Claude **and** Codex, separately. Neither may open the other's files. | `inputs/Claude Deep Dive YYYY-MM-DD.md/.pdf`, `inputs/Codex Deep Dive YYYY-MM-DD.md/.pdf` |
| 2 | `PROMPT_2_CROSS_CRITIQUE.md` | Claude **and** Codex, in parallel. Each compares the *other's* picks with its own, head-to-head. | `inputs/Claude Critique of Codex YYYY-MM-DD.md`, `inputs/Codex Critique of Claude YYYY-MM-DD.md` |
| 3 | `PROMPT_3_SYNTHESIS.md` | **One** model, alternating each cycle (see log below) | `inputs/Candidate Ranking YYYY-MM-DD.md`, `Event Horizon Fund Analysis YYYY-MM-DD.md/.pdf`, `Deployment Strategy/Deployment Strategy YYYY-MM-DD.md/.pdf` |
| 4 | `PROMPT_4_OPTIMIZATION_PASS.md` | Claude **and** Codex, independently. Neither reads the other's pass. Each looks for better stocks (top 20 alternatives), the weakest holdings, and better weights, and proposes up to 8 changes. | `inputs/Claude Optimization Pass YYYY-MM-DD.md`, `inputs/Codex Optimization Pass YYYY-MM-DD.md`, each starting with an Owner Decision Sheet |
| 5 | `PROMPT_5_FINAL_ASSEMBLY.md` | The **synthesis model**, in one pass. It merges both decision sheets and the Step 3 open calls, decides every item on the evidence, applies the decisions with minimal edits (adding a "Selection Rationale: Chosen vs Considered" section), regenerates the PDFs, marks the version adopted, and updates this README. | `inputs/Step 5 Decision Log YYYY-MM-DD.md`; the adopted final analysis and Deployment Strategy; the Step 3 proposal kept in `inputs/superseded/` |
| 6 | `PROMPT_6_FINAL_REVIEW.md` (optional) | The **other model** (not the synthesis model), in one pass. It reproduces the Step 5 tables, audits every Step 5 decision and the final's numbers and consistency, fixes errors in place, and changes weights only if a change passes the Step 5 bar. | `inputs/Step 6 Review Log YYYY-MM-DD.md`; the reviewed final (and Deployment Strategy if changed); the pre-review copy kept in `inputs/superseded/` |

**How to run a step:** open the repo in Claude Code or Codex and say: `Read and execute PROMPT_N_....md. You are <Claude/Codex>.`

**Rules that make the flow work:**

- Step 1 must stay blind. Don't give either model the other's deep dive until Step 2.
- Never average the two portfolios or their inputs. Facts are settled at the primary source, and disputed inputs go to the better-supported value. A genuine tie takes the more conservative value.
- Keep every intermediate file. Next cycle's accountability section grades the Claude blind, Codex blind, and final allocations separately (the Model Reconciliation table in the final analysis). Over a few cycles this shows which model to trust on which kinds of calls.
- PDFs: `python md_to_pdf.py "<path to .md>"`. On Windows this needs `$env:WEASYPRINT_DLL_DIRECTORIES = 'C:\msys64\mingw64\bin'` first. Python-Markdown needs a blank line before every list.

### Synthesis Log (alternate the Step 3 model each cycle)

| Cycle | Step 3 + Step 5 (synthesis model) | Step 4 optimization (both models) | Step 6 review (other model) | Adopted version |
| ----- | ---------------- | --------------- | --------------- | --------------- |
| 2026-11-08 | Claude (V10.0 proposed Nov 9–10; Step 5 Nov 10) | Codex (done); Claude (done, Nov 10) | Codex (pending) | **V10.1** (adopted Nov 10, 2026) |

## Repository Layout


| Path                                                                                           | Purpose                                                                                                                      |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `PROMPT_1_DEEP_DIVE.md` … `PROMPT_6_FINAL_REVIEW.md`                                            | The prompts of the analysis flow, in order; Step 6 is optional (see Analysis Flow above).                                    |
| `Analysis YYYY-MM-DD/`                                                                         | Repeatable cycle folder. Each cycle contains the dated thesis, allocation updates, and execution materials for that refresh. |
| `Analysis YYYY-MM-DD/inputs/`                                                                  | Steps 1–6 working files: both deep dives, both critiques, the candidate ranking, both optimization passes, the Step 5 decision log, the Step 6 review log, superseded drafts, and research data. |
| `Analysis YYYY-MM-DD/Deployment Strategy/`                                                     | Cycle-specific deployment planning (tranches, timing windows, trigger rules, and position tracking artifacts).               |
| `Followup Gemini & GPT Prompt.md` and `Cursor Followup Prompt.md`                              | Legacy follow-up prompts from the 2026-05-10 cycle and earlier, replaced by Steps 2–4. Kept for reference.                  |
| `Analysis 2025-09-14/`, `Analysis 2026-01-20/`, `Analysis 2026-03-31/`, `Analysis 2026-05-10/` | Historical cycle snapshots so thesis and allocation changes remain auditable over time.                                      |
| `Original Large Thesis Writeup 2025-09-10/`                                                    | Initial long-form foundation thesis and early framing used before the recurring cycle structure.                             |
| `Archive/`                                                                                     | Older or superseded research/support materials retained for reference.                                                       |




## File Structure

```text
Event_Horizon_Fund/
├── README.md
├── PROMPT_1_DEEP_DIVE.md
├── PROMPT_2_CROSS_CRITIQUE.md
├── PROMPT_3_SYNTHESIS.md
├── PROMPT_4_OPTIMIZATION_PASS.md
├── PROMPT_5_FINAL_ASSEMBLY.md
├── PROMPT_6_FINAL_REVIEW.md          (optional)
├── Followup Gemini & GPT Prompt.md   (legacy)
├── Cursor Followup Prompt.md         (legacy)
├── md_to_pdf.py
├── Analysis 2025-09-14/
│   └── inputs/
│       ├── GPT5 Pro Research 2025-09-14.md
│       ├── Gemini 2.5 Pro Research 2025-09-14.md
│       └── GPT5 and Gemini Combined Research 2025-09-14.md
├── Analysis 2026-01-20/
│   └── inputs/
│       ├── GPT5.2 Pro Research 2026-01-20.md
│       ├── Gemini Pro Research 2026-01-20.md
│       └── GPT5.2 and Gemini Combined Research 2026-01-20.md
├── Analysis 2026-03-31/
│   ├── Event Horizon Fund Analysis 2026-03-31.md
│   └── Deployment Strategy/
│       └── Deployment Strategy 2026-03-31.md
├── Analysis 2026-05-10/
│   ├── Event Horizon Fund Analysis 2026-05-10.md
│   ├── inputs/
│   │   ├── GPT5.5 Pro Research 2026-05-05.md
│   │   └── Gemini Pro Research 2026-05-05.md
│   ├── Follow Up/
│   │   ├── Followup Cursor Results 5-10-2026.md
│   │   ├── GPT Followup 5-10-2026.md
│   │   └── Gemini Followup 5-10-2026.md
│   └── Deployment Strategy/
│       ├── Deployment Strategy 2026-05-10.md
│       └── Portfolio_Positions_2026-05-11.xlsx
├── Analysis 2026-11-08/
│   ├── Event Horizon Fund Analysis 2026-11-08.md / .pdf      (adopted V10.1)
│   ├── Deployment Strategy/                                  (local only, gitignored)
│   │   └── Deployment Strategy 2026-11-08.md / .pdf
│   └── inputs/
│       ├── Claude Deep Dive 2026-11-08.md / .pdf             (Step 1)
│       ├── Codex Deep Dive 2026-11-08.md / .pdf              (Step 1)
│       ├── Claude Critique of Codex 2026-11-08.md / .pdf     (Step 2)
│       ├── Codex Critique of Claude 2026-11-08.md / .pdf     (Step 2)
│       ├── Candidate Ranking 2026-11-08.md / .pdf            (Step 3, with a Step 4–5 addendum)
│       ├── Claude Optimization Pass 2026-11-08.md / .pdf     (Step 4)
│       ├── Codex Optimization Pass 2026-11-08.md / .pdf      (Step 4)
│       ├── Step 5 Decision Log 2026-11-08.md / .pdf          (Step 5)
│       ├── superseded/                                       (Step 3 proposal; Codex single-model run)
│       └── research/
│           ├── claude_synthesis/                             (Steps 2–5 model, data and tables)
│           ├── codex_initial_deep_dive/
│           ├── codex_cross_critique/
│           └── forecast_audit/
├── Original Large Thesis Writeup 2025-09-10/
│   └── Event Horizon Fund Draft V7.3 2025-09-10.md
└── Archive/
    └── backups/
        └── (historical backups)
```



## Top Background Reading

- [AI-2027](https://ai-2027.com/): also the [race ending](https://ai-2027.com/race), [summary](https://ai-2027.com/summary), and research supplements on [compute](https://ai-2027.com/research/compute-forecast), [timelines](https://ai-2027.com/research/timelines-forecast), [takeoff](https://ai-2027.com/research/takeoff-forecast), [AI goals](https://ai-2027.com/research/ai-goals-forecast), and [security](https://ai-2027.com/research/security-forecast)
- [AI chip compute forecast (Google Sheet)](https://docs.google.com/spreadsheets/d/1Ko-olwjDy6h8rXLZBFpP-e2GibGqRhfV28S4v8xtzrM/edit?gid=1866551567#gid=1866551567): the data behind the AI-2027 compute forecast
- [AI-2040](https://ai-2040.com/) and [AI Futures Project updates](https://blog.aifutures.org/)
- [SITUATIONAL AWARENESS](https://situational-awareness.ai/), especially [Racing to the Trillion-Dollar Cluster](https://situational-awareness.ai/racing-to-the-trillion-dollar-cluster/)
- [METR Long Horizon Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)
- [Epoch Trends](https://epoch.ai/trends)



## Notes

- This repository is a research and process workspace, not financial advice.
- Keep `README.md` synced when active allocation version or sleeve weights change.

