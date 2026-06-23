# PC Build Ordering Hub

Ukraine-first PC build planner, price evidence folder, and live order hub.

## Start Here

1. `00_Hub/Current_Order/README.md` - real purchase status, order folders, delivery details.
2. `00_Hub/Current_Order/REMAINING_PARTS.md` - remaining pending approvals and final open status.
3. `VAULT_NAVIGATION.md` - surgical map for Codex/AI helpers, current build row IDs, and where to edit.
4. `PROJECT_STRUCTURE.md` - where every kind of file belongs.
5. `04_Tools/PC_BUILD_CODE_MAP.md` - where to edit the Marimo planner, if app work is needed.

## Current Truth

- `00_Hub/Current_Order/` is the source of truth for real purchases, receipts, pending orders, and Robert delivery notes.
- `02_PC_Builds/parts_options_seed.csv` is the planner data file, not the proof of what was actually bought.
- `01_Market_Data/` and `02_PC_Builds/01_Price_Refresh/` are price evidence and candidate snapshots.
- `05_Knowledge_Base/` is long-term part research: PSU, cooling, motherboard, RAM, GPU, SSD, case.

## Current Purchase State

Ordered/paid or pending:

- GPU: MSI RTX 5080 Gaming Trio OC from KR System.
- RAM: Patriot Viper Venom 64GB 6000 CL30 from RTV EURO AGD.
- SSD: Kingston KC3000 2TB from Empik / Okazje-Centrum.
- Case: NZXT H7 Flow RGB Black from Compzone.
- CPU cooler: ARCTIC Liquid Freezer III Pro 360 A-RGB from PCGO.
- PSU: be quiet! Pure Power 13 M 1000W from AQUA.
- Extra fans: ARCTIC P12 Pro A-RGB set from AQUA.
- Amazon.pl pending: Ryzen 9 9900X, Gigabyte X870E AORUS Elite WiFi7, ARCTIC MX-7.

Remaining live issue: Amazon.pl CPU/motherboard/paste approval. No unchosen part remains after the fan order.

## Planner App Files

- `04_Tools/pc_build_marimo.py` - normal local Marimo app.
- `04_Tools/pc_build_marimo_WASM_SAFE.py` - WASM/GitHub Pages version. Do not touch for small local edits unless explicitly asked.
- `docs/planner.html` - exported hosted app.
- `02_PC_Builds/parts_options_seed.csv` - main product and price database.

## Price Refresh Workflow

For a new price update:

1. Put raw captures in `00_Hub/` first.
2. Sort them into `01_Market_Data/<date>/<part>/`.
3. Update or create the matching `02_PC_Builds/01_Price_Refresh/<date>/<part>_market_snapshot.csv`.
4. Update `02_PC_Builds/parts_options_seed.csv` only after a row is useful for the planner.
5. Touch the WASM app and `docs/planner.html` only for a deliberate export/update pass.

## Archive

- `99_Archive/` contains old history, backups, and retired working files.
- `02_PC_Builds/99_Archive_Excel_Attempt/` is an old spreadsheet attempt and is not active planner logic.
