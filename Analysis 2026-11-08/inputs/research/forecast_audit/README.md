# Forecast audit — November 9, 2026

This research supplements `../../Codex Deep Dive 2026-11-08.md`. It revises the treatment of rapid AI progress, compute constraints, valuation uncertainty and shareholder-regime risk. It does not change the report's November 6 price snapshot, its eight recommended weights, any actual account, or the active house allocation. Earlier report and deployment deliverables are preserved in `pre_revision/`.

## What was examined

All ten user-specified inputs were covered: AI 2027's race, summary, compute, timelines, takeoff, goals and security pages; the shared chip-compute workbook; AI 2040; and Situational Awareness's trillion-dollar-cluster chapter. Material follow-through included:

- AI Futures' original and updated forecast distributions, February grading, April update and August 16 model/forecast update.
- Native Google Sheets values, formulas and notes for the compute model and the grading/forecast comparison workbooks.
- AI 2040's compute and economics supplements and its full 90-page PDF. The main HTML alone did not contain the entire chosen narrative branch.
- METR's time-horizon methods, raw measurements, dashboard caveats, productivity follow-up and May 2026 survey.
- Epoch's company-revenue and compute-spending records and its chip-sales series/definitions.
- The linked software-intelligence-explosion argument, and issuer evidence on EUV supply and HBM market/contracts.

This is a targeted, investment-relevant audit, not an independent reproduction of the complete AI Futures simulator, an exhaustive verification of every hyperlink, or an independently calibrated probability forecast for every narrative event. The report distinguishes those limitations explicitly.

## Source files and provenance

`source_manifest.json` records URLs, retrieval times, response sizes and retrieval failures. For HTML sources, `.html` is the raw response, `.txt` is an extracted reading view, and `_links.json` lists links found. The fetcher's `.html` suffix also holds raw CSV/YAML responses; use the raw file, not the BeautifulSoup text view, to parse those datasets. PDF sources have a `.pdf` plus an extracted `.txt`.

Publication-safety exception: embedded third-party Mapbox tokens are redacted from archived responses. GitHub push protection identified two occurrences in the downloaded LessWrong page (`old_track_record.html`); they were removed before publication, without changing the research text. `sanitize_snapshots.py` performs the bounded mechanical redaction without printing tokens, and `fetch_sources.py` now applies it before saving future HTML responses. The manifest retains the original response byte count and separately records the sanitized archive size and redaction count.

Direct downloads of the two ASML pages returned HTTP 403. Both were separately opened and reviewed through the web research tool; their direct archive failures remain visible rather than being represented as successful snapshots. `model_app.html` is client-rendered and its extracted text is empty. The model's readable about/changelog page, authors' explanatory posts and native forecast tables support the cited updates; the model was not executed. Public web pages may change after this snapshot.

Native connected-application responses are preserved without modifying the online documents:

| Snapshot | Read scope / purpose |
| --- | --- |
| `filemeta.json`, `sheetmeta.json` | Shared compute workbook identity, exposed tab, dimensions and modification timestamp |
| `sheet_values_1.json`, `sheet_values_2.json`, `sheet_headers.json` | Bounded displayed-value and header reads through row 120; the inspected populated model ends at row 78 |
| `sheet_formula_cells.json` | `Clean version!B5:O78`, formulas, cached values, notes and links |
| `scorecard_cells.json` | Earlier grading workbook for original pace comparison and methodology |
| `forecast_history_cells.json` | Earlier forecast comparison for historical revisions |
| `august_scorecard_cells.json` | `Aug 2026 grades!A1:K35`; populated grade table through row 27 |
| `august_forecasts.json` | `Aug 2026!A1:N20`; original/current forecaster comparison and linked sources |

The workbook title's 2024 date is not treated as an immutable version stamp: Drive metadata reports modification in April 2025. All findings apply to the inspected snapshot, not necessarily to an unseen original revision. Cached values and formulas were read and cross-checked; a general-purpose spreadsheet recalculation engine was not run.

## Reproducible calculations

From the project root:

```text
python "Analysis 2026-11-08/inputs/research/forecast_audit/audit_calculations.py"
python "Analysis 2026-11-08/inputs/research/forecast_audit/verify_audit.py"
```

The calculations import the saved original valuation model, not a fresh market-data feed. They write `audit_results.json` and `audit_verification.json` locally. They neither edit the source workbooks nor adopt the counterfactual assumptions into `valuation_model.py`.

The audit reproduces source chip production, market size, compute stock and power; identifies the binding supply constraint; calculates cohort-versus-current-efficiency power; and tests HBM wafer growth and price compounding. The flat-3% price sensitivity retains an obsolete 2024 TAM anchor and must not be read as a new market forecast. Micron's December 2024 and September 2026 primary evidence is used to contextualize that limitation.

The scorecard audit recomputes category mean/median and isolates two apparent formula inconsistencies. Its counterfactual is an analyst consistency check, not an author-confirmed correction. The authors' roughly 70–90% pace summary is not an accuracy percentage, a probability of AGI or a probability of the race ending.

The portfolio audit specifies the 11-stock upstream challenge and exact funding, a common 50%-bull reweighting, stronger upstream operating assumptions, three separate 5-point COHR-to-upstream swaps, relative-value replacement thresholds and a zero-recovery regime overlay. All four full architectures and the marginal substitutions are evaluated with expected terminal wealth before CAGR. The TSM-only swap narrowly beats the selected eight under the stronger operating counterfactual; the report discloses that reversal. Scenarios remain subjective and conditional. A common regime overlay cannot measure differential company exposure or prove robustness to loss of enforceable ownership.

## Main changes to interpretation

The original treatment of the forecasting work as stale background was insufficient. Updated distributions keep serious rapid coding/research automation inside the investment horizon. Physical constraints do not refute a software-led takeoff on an existing hardware base. Conversely, forecast success does not establish profitable infrastructure utilization, sustained scarcity margins or enforceable shareholder claims.

The recommended allocation remains unchanged after the additional tests, with moderate confidence rather than a claim of mathematical optimality. Sections 3.3–3.7, 5.6, 7.2–7.3 and the targeted questions contain the substantive revisions. Price and issuer-event checks are still required before any implementation.
