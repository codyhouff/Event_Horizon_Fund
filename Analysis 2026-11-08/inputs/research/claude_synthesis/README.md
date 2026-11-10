# Claude Step 2 / Step 3 model files (2026-11-08 cycle)

These are the reproducible inputs and scripts behind:

- `inputs/Claude Critique of Codex 2026-11-08.md` (Step 2), in `step2/`
- `inputs/Candidate Ranking 2026-11-08.md` and the Step 3 final `Event Horizon Fund Analysis 2026-11-08.md` / `Deployment Strategy 2026-11-08.md`, in this folder

All prices are the **Nov 9, 2026 close**. The terminal date is **Dec 31, 2030** (T = 4.1424 years).

## Files

| File | What it is |
|---|---|
| `fetch_step3.py` | Pulls the data snapshot from Yahoo: quoteSummary for consensus and valuation, fundamentals-timeseries for annual EPS, stock comp and shares, and recent daily closes |
| `data/step3_snap.json` | The snapshot used: 58 pool names plus 32 peers and benchmarks, pulled the evening of Nov 9 |
| `step3_model.py` | The single synthesis model: A1 states (bust, plateau, base, bull), owner EPS, the multiple evidence band, named scenarios and portfolio math. Every input carries a tag (C / X / B / A) for whose value was adopted |
| `data/ports.json` | The portfolios compared (V9.1, both blind and both post-critique portfolios, the architectures, V10.0 and its variants) |
| `data/step3_out.json` | Model output |
| `data/step3_out_cxmult.json` | Robustness run with every disputed multiple set to Codex's value |
| `data/disputes.json` | The 53 disputed inputs and how each was resolved (Candidate Ranking §A4.3) |
| `step3_tables.py` | Writes `tables/ranked.md`, `detail.md`, `portfolios.md` and `sensitivity.md` |
| `extra_tables.py` | Writes `tables/reconciliation.md`, `pool.md`, `disputes.md` and `trades.md`, plus `data/drift_nov9.json`. It also prints the tranche cash path and the buy-price limits |
| `tables/` | The generated tables pasted into the reports |
| `step2/` | Step 2 critique model (`step2_model.py`), the Nov 9 fundamentals (`fund_step2.json`) and its output (`step2_out.json`) |

The Codex deep-dive ledger the model reads is `../valuation_outputs.json`, one folder up. Codex's own Step 2 model is in `../codex_cross_critique/`.

## Reproduce (run from this folder)

```bash
python -I step3_model.py data/step3_snap.json ../valuation_outputs.json data/step3_out.json "$(cat data/ports.json)"
python -I step3_model.py data/step3_snap.json ../valuation_outputs.json data/step3_out_cxmult.json "$(cat data/ports.json)" codexmult
python -I step3_tables.py data/step3_out.json data/step3_out_cxmult.json tables
python -I extra_tables.py data/step3_out.json data/step3_snap.json data/disputes.json tables data
```

Re-running reproduces every file in `tables/` and `data/` byte for byte (verified Nov 10, 2026).

To refresh prices for a later date, re-run:

```bash
python -I fetch_step3.py data/step3_snap.json <comma-separated tickers>
```

Then change the `"2026-11-09"` date keys in `step3_model.py` and `extra_tables.py`. Treat the result as a new run, not as an update of this cycle's record.

**Step 2 model:**

```bash
python -I step2/step2_model.py step2/step2_out.json '{"NVDA":15,"MU":12,"AVGO":11,"CLS":7,"TSM":5,"VRT":14,"NVT":11,"NRG":11,"VST":9,"ASML":4,"BNTX":1}'
```
