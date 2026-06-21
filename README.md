# PC Build Planner

Token-smart entry point for the PC build price tracker.

## Read First

1. `PROJECT_STRUCTURE.md` - folders, files, and workflow rules.
2. `02_PC_Builds/01_Price_Refresh/2026-06-21/PRICE_COLLECTION.md` - current three-market collection checklist.
3. Part snapshots before raw pages:
   - `02_PC_Builds/01_Price_Refresh/2026-06-21/RAM_MARKET_SNAPSHOT.md`
   - `02_PC_Builds/01_Price_Refresh/2026-06-21/GPU_MARKET_SNAPSHOT.md`

## Token Order (always)

1. `PROJECT_STRUCTURE.md`
2. active `PRICE_COLLECTION.md`
3. part `*_MARKET_SNAPSHOT.md`
4. part `*_market_snapshot.csv`
5. part `*_reviewed_options.csv`
6. `01_Market_Data/<date>/<part>/_capture_index.csv`
7. raw `.md` capture only when extracting, auditing, or asked.

## Active App Files

- `02_PC_Builds/parts_options_seed.csv` - main planner data.
- `04_Tools/pc_build_marimo.py` - local app.
- `04_Tools/pc_build_marimo_WASM_SAFE.py` - GitHub Pages-safe app.
- `docs/planner.html` - exported hosted app.

## Active Refresh

Current refresh folder: `02_PC_Builds/01_Price_Refresh/2026-06-21/`

Current raw market folder: `01_Market_Data/2026-06-21/`

Drop new captures into: `00_Hub/`

## Knowledge Base (Part Research)

`05_Knowledge_Base/` - permanent research on part specs, tradeoffs, and what to pick.

Populated after each price refresh. See `PROJECT_STRUCTURE.md` §4 for the planned layout.

## Archive

Old long README: `99_Archive/README_History/README_FULL_HISTORY_2026-06-21.md`

Older shortlists: `99_Archive/Old_Shortlists/00_Working_Shortlists_2026-06-21/`
