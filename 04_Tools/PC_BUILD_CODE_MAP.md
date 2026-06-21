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
6. The local `Change Parts` UI is two-stage: first country dropdowns, then part dropdowns filtered to that country.
7. UI cells render in order: title, build selector, country/part dropdowns, selected build table, summary cards, purchase baskets, FX logic, EU check, raw database.

## Common Edit Points

- Add or change a part: edit `02_PC_Builds/parts_options_seed.csv`, then sync the WASM embedded `PARTS_CSV_DATA`.
- Add a build preset: edit the `builds` dictionary. Every ID in a build must exist in the active parts data.
- Change default build: edit the `value=` in the `build_choice = mo.ui.dropdown(...)` cell.
- Change the country-first part picker: edit the cells around `markets_for()`, `options_for(part, market)`, and `part_row(...)` in `pc_build_marimo.py`.
- Change savings logic: edit `compare_ids` and `build_table()`.
- Change FX logic: edit `load_rates()` and the `FX logic` display cell.
- Change hosted layout: edit `pc_build_marimo_WASM_SAFE.py`, export, then verify `docs/planner.html` in browser.

## Fast Price Refresh Loop

Use this when prices change next week and the goal is a quick surgical update:

1. Update or add rows in the dated snapshot/review CSVs under `02_PC_Builds/01_Price_Refresh/<date>/`.
2. Run `python3 04_Tools/audit_parts_seed_against_refresh.py` from the project root.
3. Review the printed queue. Add only planner-worthy rows to `02_PC_Builds/parts_options_seed.csv`.
4. Keep suspicious rows as `Watch`/`High` risk. Do not overwrite known protected rows, such as the cleaner `MB_01_UA` 12,989 UAH row, with suspicious lower rows.
5. Run:

```bash
python3 -m py_compile 04_Tools/pc_build_marimo.py
marimo check 04_Tools/pc_build_marimo.py
```

6. Only after the local app looks correct, sync `PARTS_CSV_DATA` in `pc_build_marimo_WASM_SAFE.py` and export `docs/planner.html`.

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

## Current Hosted Sync Rule

The local app and hosted app must stay visually matched. The safe update flow is:

1. Edit `02_PC_Builds/parts_options_seed.csv`.
2. Mirror the CSV text into `PARTS_CSV_DATA` in `pc_build_marimo_WASM_SAFE.py`.
3. If layout changes were made in `pc_build_marimo.py`, copy the matching UI/rendering cells into `pc_build_marimo_WASM_SAFE.py`.
4. Export `docs/planner.html`.
5. Verify the exported HTML, not only the Python notebook.

GitHub Pages is static. It cannot save a named build back into the repo by itself. A future "Name build and save" button can save in browser storage for that device, but real GitHub persistence would need manual export/commit or a backend/GitHub-auth flow.

## Last Fix

The hosted page was missing the main builder because `pc_build_marimo_WASM_SAFE.py` had stale embedded data and an invalid default build name. Some build presets referenced case/cooler IDs that existed in the live CSV but not in `PARTS_CSV_DATA`. The app width was also changed from invalid WASM value `wide` to `full`.

The final local/hosted mismatch came from editing the local app while the WASM-safe hosted app still had older UI cells. When the screenshots look different, compare both Python files, not only `docs/planner.html`.

## Lessons Learned

- Do not delete useful comparison columns just to make a table cleaner. The `Delta HUF` and `Delta UAH` columns are part of the buying logic.
- Numeric cells and numeric headers both need `pc-num`; otherwise the numbers can align correctly while the headers sit in the wrong place.
- Generated `docs/planner.html` can hold stale text until the WASM-safe notebook is exported again.
- Avoid many temporary guide files. Keep durable knowledge in this code map, `PC_BUILD_TOOLING.md`, and the main `README.md`.
- Raw captures can keep exact offer IDs as evidence, but the dashboard store labels should stay clean for reading.
- Marimo is a good Python/data dashboard for this project. It is not a full app backend, so static GitHub Pages features should stay simple.

## Future Ideas To Keep Small

- For now, keep the build selector simple. One best-value build is enough until Roman gives the next exact build option to add.
- A product-comparison tab can come later, but it is not needed for the current Dad-facing planner. The current dropdowns plus the selected build table already cover the buying decision.
- Price updates should prefer Arukereso/Ceneo broad pages for fast refreshes, then exact seller pages only for parts close to purchase. This keeps updates practical instead of re-downloading every retailer page every time.
- If a comparison tab is added later, start with one category at a time: selected part vs same-category alternatives, price difference, market/store, risk, and short note.
