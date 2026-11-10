# Claude Step 2–5 model files (2026-11-08 cycle)

These are the reproducible inputs and scripts behind:

- `inputs/Claude Critique of Codex 2026-11-08.md` (Step 2), in `step2/`
- `inputs/Candidate Ranking 2026-11-08.md` and the Step 3 proposal (V10.0, now in `inputs/superseded/`), in this folder
- `inputs/Claude Optimization Pass 2026-11-08.md` (Step 4)
- the adopted final (V10.1) `Event Horizon Fund Analysis 2026-11-08.md`, its `Deployment Strategy 2026-11-08.md` and `inputs/Step 5 Decision Log 2026-11-08.md` (Step 5)

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
| `step4_model.py`, `data/step4_snap.json`, `data/step4_out.json` | Step 4 (Claude Optimization Pass): values ~20 out-of-pool candidates and the re-underwritten AVGO on the same A1 rules, then tests swap variants. Run: `python -I step4_model.py data/step3_out.json data/step4_snap.json data/step4_out.json` |
| `step5_model.py` | Step 5 (final assembly): `step3_model.py` plus the decided input changes (Decision Log D1–D4): AVGO base corrected; VRT/NVT stock-comp double count removed; WCC and STRL added |
| `data/step5_snap.json` | `data/step3_snap.json` plus STRL and WCC, copied unchanged from `data/step4_snap.json` (same Nov 9 close) |
| `data/ports5.json` | Every portfolio compared in Step 5: the Step 3 set plus Codex's O1/O2 proposals, the STRL-8% alternative, the adopted V10.1 and its three conditional variants (MOD gate, Texas hit, NVDA adverse) |
| `data/step5_out.json`, `data/step5_out_cxmult.json` | Step 5 model output, and the robustness run on Codex's multiples |
| `step5_tables.py` | Writes `tables5/pool5.md`, `recon5.md`, `portfolios5.md`, `trades5.md` and `destination5.md`, plus `data/drift_nov9.json`. It prints the tranche cash path |
| `tables5/` | The generated tables used in the adopted final and its Deployment Strategy |
| `step2/` | Step 2 critique model (`step2_model.py`), the Nov 9 fundamentals (`fund_step2.json`) and its output (`step2_out.json`) |

The Codex deep-dive ledger the model reads is `../codex_initial_deep_dive/valuation_outputs.json` (sibling folder). Codex's own Step 2 model is in `../codex_cross_critique/`.

## Reproduce (run from this folder)

```bash
python -I step3_model.py data/step3_snap.json ../codex_initial_deep_dive/valuation_outputs.json data/step3_out.json "$(cat data/ports.json)"
python -I step3_model.py data/step3_snap.json ../codex_initial_deep_dive/valuation_outputs.json data/step3_out_cxmult.json "$(cat data/ports.json)" codexmult
python -I step3_tables.py data/step3_out.json data/step3_out_cxmult.json tables
python -I extra_tables.py data/step3_out.json data/step3_snap.json data/disputes.json tables data
```

Re-running reproduces every file in `tables/` and `data/` byte for byte (verified Nov 10, 2026).

**Step 5 (adopted V10.1):**

```bash
python -I step5_model.py data/step5_snap.json ../codex_initial_deep_dive/valuation_outputs.json data/step5_out.json "$(cat data/ports5.json)"
python -I step5_model.py data/step5_snap.json ../codex_initial_deep_dive/valuation_outputs.json data/step5_out_cxmult.json "$(cat data/ports5.json)" codexmult
python -I step5_tables.py data/step5_out.json data/step5_out_cxmult.json data/step5_snap.json tables5 data
```

To refresh prices for a later date, re-run:

```bash
python -I fetch_step3.py data/step3_snap.json <comma-separated tickers>
```

Then change the `"2026-11-09"` date keys in `step3_model.py` and `extra_tables.py`. Treat the result as a new run, not as an update of this cycle's record.

**Step 2 model:**

```bash
python -I step2/step2_model.py step2/step2_out.json '{"NVDA":15,"MU":12,"AVGO":11,"CLS":7,"TSM":5,"VRT":14,"NVT":11,"NRG":11,"VST":9,"ASML":4,"BNTX":1}'
```
