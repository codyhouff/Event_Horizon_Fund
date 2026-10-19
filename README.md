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



## Workflow


| Path                                                                                           | Purpose                                                                                                                      |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `Analysis YYYY-MM-DD/`                                                                         | Repeatable cycle folder. Each cycle contains the dated thesis, allocation updates, and execution materials for that refresh. |
| `Analysis YYYY-MM-DD/Inputs/`                                                                  | Cycle inputs and supporting source material used to produce that cycle's analysis (create/use this folder each cycle).       |
| `Analysis YYYY-MM-DD/Deployment Strategy/`                                                     | Cycle-specific deployment planning (tranches, timing windows, trigger rules, and position tracking artifacts).               |
| `Followup Gemini & GPT Prompt.md` and `Cursor Followup Prompt.md`                              | Follow-up prompt templates used for reanalysis and iterative updates between major cycle refreshes.                          |
| `Analysis 2025-09-14/`, `Analysis 2026-01-20/`, `Analysis 2026-03-31/`, `Analysis 2026-05-10/` | Historical cycle snapshots so thesis and allocation changes remain auditable over time.                                      |
| `Original Large Thesis Writeup 2025-09-10/`                                                    | Initial long-form foundation thesis and early framing used before the recurring cycle structure.                             |
| `Archive/`                                                                                     | Older or superseded research/support materials retained for reference.                                                       |




## File Structure

```text
Event_Horizon_Fund/
├── README.md
├── ANALYSIS_PROMPT_TEMPLATE.md
├── Followup Gemini & GPT Prompt.md
├── Cursor Followup Prompt.md
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

- [AI-2027](https://ai-2027.com/)
- [SITUATIONAL AWARENESS](https://situational-awareness.ai/)
- [METR Long Horizon Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)
- [Epoch Trends](https://epoch.ai/trends)



## Notes

- This repository is a research and process workspace, not financial advice.
- Keep `README.md` synced when active allocation version or sleeve weights change.

