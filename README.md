# Event Horizon Fund

Concentrated AI infrastructure portfolio focused on physical and economic bottlenecks across power, semis, memory, networking, optical, and grid buildout.

Current active allocation version: **V9.1** (as of 2026-05-10).  
Primary source doc: `Analysis 2026-05-10/Event Horizon Fund Analysis 2026-05-10.md`.

## Read This First

- Core thesis and full framework: `Analysis 2026-05-10/Event Horizon Fund Analysis 2026-05-10.md`
- Current execution plan: `Analysis 2026-05-10/Deployment Strategy/Deployment Strategy 2026-05-10.md`
- Reconciliation notes: `Analysis 2026-05-10/Follow Up/Followup Cursor Results 5-10-2026.md`

## Current Allocation Snapshot (V9.1)

**Foundry (11%):** TSM (11%)  
**Accelerators & Custom Silicon (9%):** NVDA (6%), AVGO (3%)  
**HBM / Memory (6%):** MU (6%)  
**WFE / Semi Capital Equipment (12%):** ASML (8%), AMAT (4%)  
**Electronic Design Automation (5%):** SNPS (5%)  
**AI Data Center Fabric (4%):** ANET (4%)  
**Rack-Scale Integration & Liquid Cooling (8%):** VRT (6%), DELL (2%)  
**Energy / Power Generation (19%):** CEG (9%), VST (6%), PWR (4%)  
**AI-Native Security (3%):** CRWD (3%)  
**AI-Native Operate & Control (2%):** PLTR (2%)  
**AI-Enabled Military (2%):** AVAV (1%), KTOS (1%)  
**Bio-Risk Insurance (1%):** MRNA (1%)  
**Strategic Materials (3%):** MP (3%)  
**Domestic Foundry (3%):** INTC (3%)  
**Electrical Equipment (5%):** GEV (5%)  
**Nuclear Fuel (2%):** CCJ (2%)  
**Grid-Bypass Power (3%):** BE (3%)  
**Optical Fabric (2%):** COHR (2%)  
Total: 100%

### Sleeve Rollup


| Sleeve                             | Weight |
| ---------------------------------- | ------ |
| Power Generation (CEG + VST + PWR) | 19%    |
| Foundry + WFE (TSM + ASML + AMAT)  | 23%    |
| Rack-Scale & Cooling (VRT + DELL)  | 8%     |
| Accelerators (NVDA + AVGO)         | 9%     |
| Memory (MU)                        | 6%     |
| EDA (SNPS)                         | 5%     |
| Networking (ANET)                  | 4%     |
| Security (CRWD)                    | 3%     |
| Operations (PLTR)                  | 2%     |
| Defense (AVAV + KTOS)              | 2%     |
| Bio-Risk Hedge (MRNA)              | 1%     |
| Materials (MP)                     | 3%     |
| Domestic Foundry (INTC)            | 3%     |
| Electrical Equipment (GEV)         | 5%     |
| Nuclear Fuel (CCJ)                 | 2%     |
| Grid-Bypass (BE)                   | 3%     |
| Optical Fabric (COHR)              | 2%     |
| Moonshot                           | 0%     |




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

Each cycle runs two models (Claude Code and Codex) through five prompts. Every prompt has the same goal: **pick the stocks and weights with the highest expected return at current prices, with an AI-2027-like path as the most likely scenario.** Every stock reports three returns:

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
| 5. Final assembly | Merge both optimization passes into one Owner Decision Sheet; the owner decides; apply the decisions to the final with minimal edits | Nowhere new: the owner chooses among the proposals |

```text
1. Deep dive      Claude Deep Dive              Codex Deep Dive            (blind, parallel)
                         │      ╲            ╱      │
2. Cross-critique  Claude Critique of Codex    Codex Critique of Claude   (parallel)
                         └───────────┬──────────────┘
3. Synthesis       one model:  Candidate Ranking → Final Analysis + Deployment Strategy
                                     │
4. Optimization   Claude Optimization Pass       Codex Optimization Pass    (independent, parallel)
                         └───────────┬──────────────┘
5. Final assembly  synthesis model: merged Owner Decision Sheet → owner decides → apply + adopt + update README
```

| Step | Prompt | Who runs it | Output (in `Analysis YYYY-MM-DD/`) |
| ---- | ------ | ----------- | ---------------------------------- |
| 0 | — | Owner | Update the cycle settings in all five prompts: cycle date, prior analysis, baseline version and allocation. Create `Analysis YYYY-MM-DD/inputs/`. |
| 1 | `PROMPT_1_DEEP_DIVE.md` | Claude **and** Codex, separately. Neither may open the other's files. | `inputs/Claude Deep Dive YYYY-MM-DD.md/.pdf`, `inputs/Codex Deep Dive YYYY-MM-DD.md/.pdf` |
| 2 | `PROMPT_2_CROSS_CRITIQUE.md` | Claude **and** Codex, in parallel. Each compares the *other's* picks with its own, head-to-head. | `inputs/Claude Critique of Codex YYYY-MM-DD.md`, `inputs/Codex Critique of Claude YYYY-MM-DD.md` |
| 3 | `PROMPT_3_SYNTHESIS.md` | **One** model, alternating each cycle (see log below) | `inputs/Candidate Ranking YYYY-MM-DD.md`, `Event Horizon Fund Analysis YYYY-MM-DD.md/.pdf`, `Deployment Strategy/Deployment Strategy YYYY-MM-DD.md/.pdf` |
| 4 | `PROMPT_4_OPTIMIZATION_PASS.md` | Claude **and** Codex, independently. Neither reads the other's pass. Each looks for better stocks (top 20 alternatives), the weakest holdings, and better weights, and proposes up to 8 changes. | `inputs/Claude Optimization Pass YYYY-MM-DD.md`, `inputs/Codex Optimization Pass YYYY-MM-DD.md`, each starting with an Owner Decision Sheet |
| 5 | `PROMPT_5_FINAL_ASSEMBLY.md` | The **synthesis model**, in two phases. **A:** merges both decision sheets and the Step 3 escalations into one sheet, then stops. The **owner** answers each item. **B:** the synthesis model applies the decisions with minimal edits, regenerates the PDFs, marks the version adopted, and updates this README. | `inputs/Owner Decision Sheet YYYY-MM-DD.md`; updated final analysis and Deployment Strategy; Step 3 proposal kept in `inputs/superseded/` |

**How to run a step:** open the repo in Claude Code or Codex and say: `Read and execute PROMPT_N_....md. You are <Claude/Codex>.`

**Rules that make the flow work:**

- Step 1 must stay blind. Don't give either model the other's deep dive until Step 2.
- Never average the two portfolios or their inputs. Facts are settled at the primary source, and disputed inputs go to the better-supported value. A genuine tie takes the more conservative value or goes to the owner.
- Keep every intermediate file. Next cycle's accountability section grades the Claude blind, Codex blind, and final allocations separately (the Model Reconciliation table in the final analysis). Over a few cycles this shows which model to trust on which kinds of calls.
- PDFs: `python md_to_pdf.py "<path to .md>"`. On Windows this needs `$env:WEASYPRINT_DLL_DIRECTORIES = 'C:\msys64\mingw64\bin'` first. Python-Markdown needs a blank line before every list.

### Synthesis Log (alternate the Step 3 model each cycle)

| Cycle | Step 3 + Step 5 (synthesis model) | Step 4 optimization (both models) | Adopted version |
| ----- | ---------------- | --------------- | --------------- |
| 2026-11-08 | Claude (V10.0 proposed, Nov 9–10) | Codex (done); Claude (pending) | pending (Step 5 owner decisions) |

## Repository Layout


| Path                                                                                           | Purpose                                                                                                                      |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `PROMPT_1_DEEP_DIVE.md` … `PROMPT_5_FINAL_ASSEMBLY.md`                                          | The five prompts of the analysis flow, in order (see Analysis Flow above).                                                   |
| `Analysis YYYY-MM-DD/`                                                                         | Repeatable cycle folder. Each cycle contains the dated thesis, allocation updates, and execution materials for that refresh. |
| `Analysis YYYY-MM-DD/inputs/`                                                                  | Steps 1–5 working files: both deep dives, both critiques, the candidate ranking, both optimization passes, the owner decision sheet, superseded drafts, and research data. |
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

