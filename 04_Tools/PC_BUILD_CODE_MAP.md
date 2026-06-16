# PC Build App Code Map

Date: 2026-06-16

Purpose: quick editing notes for the Marimo PC build planner.

## Files

- `04_Tools/pc_build_marimo.py`: local working app. Reads live CSV files from `02_PC_Builds/`.
- `04_Tools/pc_build_marimo_WASM_SAFE.py`: browser/GitHub Pages app. Embeds CSV text near the top.
- `docs/planner.html`: exported hosted page. Do not edit by hand; regenerate from the WASM-safe file.

## Main Data Flow

1. `parts` comes from `parts_options_seed.csv` locally, or `PARTS_CSV_DATA` in the WASM file.
2. `eu_lowest` comes from `eu_lowest_price_seed.csv` locally, or `EU_LOWEST_CSV_DATA` in the WASM file.
3. `builds` maps build names to selected row IDs.
4. `compare_ids` maps Poland rows to Hungary reference rows for savings.
5. `build_table()` converts selected row IDs into the display table with HUF, UAH, savings, raw currency, and store data.
6. UI cells render in order: title, build selector, part dropdowns, selected build table, summary cards, purchase baskets, FX logic, EU check, raw database.

## Common Edit Points

- Add or change a part: edit `02_PC_Builds/parts_options_seed.csv`, then sync the WASM embedded `PARTS_CSV_DATA`.
- Add a build preset: edit the `builds` dictionary. Every ID in a build must exist in the active parts data.
- Change default build: edit the `value=` in the `build_choice = mo.ui.dropdown(...)` cell.
- Change savings logic: edit `compare_ids` and `build_table()`.
- Change FX logic: edit `load_rates()` and the `FX logic` display cell.
- Change hosted layout: edit `pc_build_marimo_WASM_SAFE.py`, export, then verify `docs/planner.html` in browser.

## WASM Safety Rules

- Browser export cannot read local CSV files, so the WASM file must embed current CSV snapshots.
- `marimo.App(width="wide")` breaks WASM export at runtime. Use `width="full"`.
- If the hosted page shows only independent sections, check for:
  - dropdown default not present in `builds`
  - build IDs missing from embedded `PARTS_CSV_DATA`
  - unsupported app config in browser logs
- After CSV changes, run:

```bash
.venv_marimo/bin/marimo export html-wasm 04_Tools/pc_build_marimo_WASM_SAFE.py -o docs/planner.html
```

## Last Fix

The hosted page was missing the main builder because `pc_build_marimo_WASM_SAFE.py` had stale embedded data and an invalid default build name. Some build presets referenced case/cooler IDs that existed in the live CSV but not in `PARTS_CSV_DATA`. The app width was also changed from invalid WASM value `wide` to `full`.
