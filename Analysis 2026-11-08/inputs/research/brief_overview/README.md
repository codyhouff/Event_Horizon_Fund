# Brief Overview scripts (Nov 11, 2026)

These scripts support `Analysis 2026-11-08/Analysis 2026-11-08 Brief Overview.md`. They read the adopted model output and never modify it.

- **`owner2.py`:** re-weights every stock's existing terminal values to the owner view (AI-2027 ±1 year) and evaluates the portfolio variants in Sections 4, 9 and 11.

  ```text
  python owner2.py "../codex_final_review/data/step6_out.json"
  ```

- **`wb_implied.py`:** recomputes the workbook-implied figures in Section 8: the binding input each year, HBM and chip volumes, and installed chip power. Its values are transcribed from the workbook's "Clean version" tab.
- **`dump2.py`:** reads every tab of the workbook's xlsx export, with values and formulas, using only the standard library.

  ```text
  python dump2.py compute.xlsx
  ```

  The export URL is `https://docs.google.com/spreadsheets/d/1Ko-olwjDy6h8rXLZBFpP-e2GibGqRhfV28S4v8xtzrM/export?format=xlsx`.

- **`agi_robust.py`:** a side check that the overview doesn't cite. It asks whether the holdings still pay off if AI-2027 lands within about two years but the gains go elsewhere. It applies stock-specific failure modes to the model's terminal values: rates, value shifting to labs and platforms, supply catching up, power politics, and a Taiwan tail. The weights are judgment parameters set out in the script. Run it from this folder, because it loads `owner2.py`:

  ```text
  python agi_robust.py "../codex_final_review/data/step6_out.json"
  ```
