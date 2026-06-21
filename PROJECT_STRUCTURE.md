# PC Build Planner Structure

This project has three lanes. Keep them separate so price refreshes stay easy.

## 0. Capture Inbox

Use `00_Hub/` as the only drop zone while collecting.

- Put unsorted browser exports, Markdown files, and screenshots there.
- Do not rename everything while collecting unless it is easy.
- Codex sorts Hub files into `01_Market_Data/<date>/<part>/` after upload.

## 1. Active App Data

These files feed the Marimo planner.

- `02_PC_Builds/parts_options_seed.csv` - main product and price database.
- `02_PC_Builds/eu_lowest_price_seed.csv` - wider EU sanity-check rows.
- `04_Tools/pc_build_marimo.py` - local editable Marimo app.
- `04_Tools/pc_build_marimo_WASM_SAFE.py` - GitHub Pages/WASM-safe app with embedded CSV.
- `docs/planner.html` - exported hosted app.

Rule: after editing `parts_options_seed.csv`, sync the embedded CSV in `pc_build_marimo_WASM_SAFE.py` and export `docs/planner.html`.

## 2. Active Price Refresh

Use one dated folder per refresh round.

- `02_PC_Builds/01_Price_Refresh/2026-06-21/FOCUSED_BUILD_SEARCHES.md` - short click list for the current build.
- `02_PC_Builds/01_Price_Refresh/2026-06-21/PRICE_COLLECTION.md` - full three-market collection checklist.
- `02_PC_Builds/01_Price_Refresh/2026-06-21/price_changes.csv` - old vs new price log.

Rule: collect captures first, update `price_changes.csv` second, update the app CSV last.

## 3. Raw Market Evidence

Raw pages live in `01_Market_Data/<date>/<part>/`.

Examples:

- `01_Market_Data/2026-06-21/CPU/`
- `01_Market_Data/2026-06-21/Motherboard/`
- `01_Market_Data/2026-06-16/GPU/`

Rule: raw captures are evidence, not conclusions. Do not edit the app CSV from memory; every new price should point back to a capture path in the `Source` column or to a clearly named working note.

## Archive / Notes

- `02_PC_Builds/99_Archive_Excel_Attempt/` - old spreadsheet attempt, not active app logic.
- `03_Research_Notes/00_Working_Shortlists/` - decision notes and older shortlist thinking.
- `04_Tools/PC_BUILD_CODE_MAP.md` - quick map for editing the Marimo code.

## Current Refresh Target

Focused 64GB build:

- Ryzen 9 9900X
- MSI MAG B850 Tomahawk MAX WiFi
- 64GB DDR5-6000 CL30
- Kingston KC3000 2TB unless PCIe 5 becomes close in price
- 1000W ATX 3.1 PSU
- Arctic 360 AIO
- Lian Li Lancool 207 Digital from Hungary if possible
- cheapest sensible RTX 5080 candidate across HU/PL/UA
