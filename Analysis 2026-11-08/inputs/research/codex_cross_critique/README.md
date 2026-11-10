# Codex cross-critique supporting calculations

Cycle: 2026-11-08. Market cutoff: 2026-11-09 regular-session close. Terminal date: 2030-12-31.

The report is `../../Codex Critique of Claude 2026-11-08.md`; the optional PDF is beside it. This folder does not contain a synthesis or edits to either original deep dive.

## Reproduce

From the repository root, run:

```powershell
python 'Analysis 2026-11-08/inputs/research/codex_cross_critique/critique_model.py'
python 'Analysis 2026-11-08/inputs/research/codex_cross_critique/sync_tables.py'
python 'Analysis 2026-11-08/inputs/research/codex_cross_critique/render_critique.py'
python 'Analysis 2026-11-08/inputs/research/codex_cross_critique/verify_critique.py'
```

Rendering and PDF inspection reuse the existing temporary dependency installation selected by `EHF_REPORT_DEPS`, or `TEMP/ehf_report_deps_20261108`. They also require the Windows Arial fonts used by the existing renderer. The shared renderer is imported, not modified. These dependencies may require sandbox read approval. Model calculations and Markdown table synchronization use only the Python standard library.

Do not refresh prices when reproducing this dated comparison. `quotes.json` and the raw chart responses preserve the actual inputs and retrieval timestamps. `fetch_quotes.py` is retained for provenance, not as an instruction to overwrite a historical cutoff. ALAB was fetched as a preliminary comparison candidate but is not included in the final 25-name underwriting or allocation.

## Files and checks

- `critique_model.py`: original weights/endpoints; new company and named-scenario inputs; explicit missing-model proxies; portfolio calculations.
- `critique_results.json`: full-precision outputs.
- `sync_tables.py` and `generated_tables.md`: ten mechanically synchronized report tables; operating share-count precision is preserved to three decimals of a billion.
- `verify_critique.py` and `verification.json`: 19 required disagreements plus one extra row, 25 modeled names, all scenario calculations, original Claude table transcription, 100% funding, split invariance and original-file preservation.
- `source_links.json`: cited public source URLs. Primary-source research is summarized and distinguished from assumptions in the report's evidence ledger.
- `preview_*.png`: PDF inspection pages. The head-to-head, named-input and primary-evidence pages were visually reviewed; the PDF has no detected text outside page bounds or footer-only pages.

The verifier reads the original Claude deep dive, never Claude's separate Step 2 critique. It confirms both original deep dives match HEAD at verification time. Existing unrelated work is not staged, committed, pushed or changed.

## Interpretation limits

Scenario probabilities, normalized margins, valuation multiples and future cash allocations are analyst judgments, not statistically validated estimates. Named reconstructions marked with a dagger are proxies where original operating bridges are absent. The report's revised portfolio is the Step 2 head-to-head result; the remaining non-contested universe still needs uniform comparison in Step 3. A modest multiple change can reverse the allocation advantage, and the modeled bust loss remains substantial.
