# Next Chat Handoff - PC Build Ordering Workflow

Workspace:

`/Users/romaantonyak/Library/CloudStorage/OneDrive-Personal/Files_Roman/06_Personal/Personal_Projects/Hungarian_PC_Parts_Market`

## Read Order

Be token-smart. Do not open raw captures first.

1. `README.md`
2. `PROJECT_STRUCTURE.md`
3. `VAULT_NAVIGATION.md`
4. `00_Hub/Current_Order/README.md`
5. `00_Hub/Current_Order/REMAINING_PARTS.md`
6. Relevant part `ORDER_SUMMARY.md`
7. `02_PC_Builds/parts_options_seed.csv` only if planner prices/options need updating
8. Raw market captures only when extracting or auditing a specific source

## Current Purchase State

Real purchases and pending orders live in `00_Hub/Current_Order/`.

Ordered/paid or pending:

- GPU: MSI RTX 5080 Gaming Trio OC from KR System.
- RAM: Patriot Viper Venom 64GB 6000 CL30 from RTV EURO AGD.
- SSD: Kingston KC3000 2TB from Empik / Okazje-Centrum.
- Case: NZXT H7 Flow RGB Black from Compzone.
- CPU cooler: ARCTIC Liquid Freezer III Pro 360 A-RGB from PCGO.
- PSU: be quiet! Pure Power 13 M 1000W from AQUA.
- Extra fans: ARCTIC P12 Pro A-RGB set from AQUA.
- Amazon.pl pending: Ryzen 9 9900X, Gigabyte X870E AORUS Elite WiFi7, ARCTIC MX-7.

Remaining live decision:

- No unchosen part remains. Amazon.pl CPU/motherboard/paste is ordered but still waiting for account/payment approval.

The normal local planner now has one active preset, `Current real build`, using the paid/pending order rows listed in `VAULT_NAVIGATION.md`.

## Current Workflow

For purchase/order work:

1. Start in `00_Hub/Current_Order/README.md`.
2. Update the relevant part folder's `ORDER_SUMMARY.md`.
3. Keep PDFs, receipts, and store pages in the matching part folder.
4. Update `ROBERT_DELIVERY_SUMMARY.md` when delivery/payment details change.
5. Update `REMAINING_PARTS.md` when a part is ordered or the remaining plan changes.

For new price research:

1. Drop new captures in `00_Hub/`.
2. Sort captures into `01_Market_Data/<date>/<part>/`.
3. Update matching dated snapshot files in `02_PC_Builds/01_Price_Refresh/<date>/`.
4. Update `02_PC_Builds/parts_options_seed.csv` only when a row is useful for the planner.
5. Do not touch `04_Tools/pc_build_marimo_WASM_SAFE.py` or `docs/planner.html` unless the user asks for a deliberate hosted export/sync pass.

## Important App Notes

- Normal local Marimo app: `04_Tools/pc_build_marimo.py`
- WASM/GitHub Pages app: `04_Tools/pc_build_marimo_WASM_SAFE.py`
- Hosted export: `docs/planner.html`
- Code map: `04_Tools/PC_BUILD_CODE_MAP.md`

The user is sensitive about breaking the WASM version. For small ordering/pricing work, keep changes local to data files or the normal Marimo app unless explicitly asked.

## Folder Cleanup State

Safe cleanup done on 2026-06-22:

- Removed `.DS_Store`, `__pycache__`, `.pyc`, and Marimo rate cache junk outside active data.
- Moved old active-file backups to `99_Archive/Backups/`.
- Moved legacy raw research from `03_Research_Notes/` to `99_Archive/LegacyRaw/`.
- Moved old Dad/Excel planning notes out of `02_PC_Builds/` to `99_Archive/OldPlans/` and `99_Archive/ExcelOld/`.
- Moved old tooling narrative from `04_Tools/PC_BUILD_TOOLING.md` to `99_Archive/OldTools/`.
- Deleted exact duplicate PSU legacy captures after confirming identical copies exist in `01_Market_Data/2026-06-21/PSU/`.
- Shortened long raw-capture filenames for OneDrive; see `99_Archive/PATH_RENAMES_2026-06-22.csv` for original-name mapping.
- Left `.venv_marimo/` in place because it is large but useful for running the normal local app.

## User Preference

Be practical and careful. Preserve data, archive before deleting, and keep order facts separate from market/research captures.
