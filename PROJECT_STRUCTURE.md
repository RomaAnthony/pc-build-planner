# PC Build Planner Structure

This project has **four lanes**. Keep them separate.

## 0. Capture Inbox

Use `00_Hub/` as the only drop zone while collecting.

- Put unsorted browser exports, Markdown files, and screenshots there.
- Do not rename everything while collecting unless it is easy.
- Codex sorts Hub files into `01_Market_Data/<date>/<part>/` after upload.
- Hub files are never conclusions. After sorting, Codex should classify each capture as one of:
  - exact store/product evidence for `price_changes.csv`;
  - broad market evidence for a dated snapshot CSV;
  - rejected/mismatch evidence that stays only in raw market data.

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
- `02_PC_Builds/01_Price_Refresh/2026-06-21/ram_market_snapshot.csv` - current RAM candidate ranking across HU/PL/UA.
- `02_PC_Builds/01_Price_Refresh/2026-06-21/RAM_MARKET_SNAPSHOT.md` - RAM decision notes and capture priorities.
- `02_PC_Builds/01_Price_Refresh/2026-06-21/ram_reviewed_options.csv` - wider RAM audit list for valid backups and rejected/noisy rows.
- `02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_market_snapshot.csv` - current RTX 5080 candidate ranking across HU/PL/UA.
- `02_PC_Builds/01_Price_Refresh/2026-06-21/GPU_MARKET_SNAPSHOT.md` - RTX 5080 decision notes and capture priorities.
- `02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv` - wider RTX 5080 audit list for non-winning variants and seller-row notes.
- `02_PC_Builds/01_Price_Refresh/2026-06-21/motherboard_market_snapshot.csv` - current motherboard market snapshot.
- `02_PC_Builds/01_Price_Refresh/2026-06-21/psu_market_snapshot.csv` - current PSU market snapshot.
- `02_PC_Builds/01_Price_Refresh/2026-06-21/ssd_market_snapshot.csv` - current SSD market snapshot.

Rule: collect captures first, update `price_changes.csv` second, update the app CSV last.
For every part, broad search captures update that part's dated market snapshot first. The app CSV changes only after exact product/store pages confirm the price.

Token rule: read small files first. Do not open raw market captures until a specific source needs extraction or audit.

Snapshot naming pattern:

- `<PART>_MARKET_SNAPSHOT.md` - human decision notes, caveats, next captures.
- `<part>_market_snapshot.csv` - ranked candidate rows for filtering and later app updates.
- `<part>_reviewed_options.csv` - wider audit list with fallback rows and rejects.

## 3. Raw Market Evidence

Raw pages live in `01_Market_Data/<date>/<part>/`.

Examples:

- `01_Market_Data/2026-06-21/CPU/`
- `01_Market_Data/2026-06-21/Motherboard/`
- `01_Market_Data/2026-06-21/GPU/`
- `01_Market_Data/2026-06-21/RAM/`

Each active raw folder should have `_capture_index.csv`. Read that first; it maps raw files to the small summary files and explains when the raw file is worth opening.

Rule: raw captures are evidence, not conclusions. Do not edit the app CSV from memory; every new price should point back to a capture path in the `Source` column or to a clearly named working note.

## 4. Knowledge Base (Part Research)

Permanent deep research — what parts mean, why you'd pick one over another, what tradeoffs exist.

These files stay static between price refreshes. They do not contain market data.

Structure:

```
05_Knowledge_Base/
  RAM/
    RAM_DECISION_GUIDE.md          - Why DDR5-6000 CL30 is ideal for AM5, when CL36/CL40 is acceptable,
                                     2x32GB vs 4x16GB, safe brands, SKUs to avoid.
    RAM_SPEC_TIERS.md              - What the spec numbers mean (timings, voltages, ranks, Hynix vs Samsung ICs).
    RAM_COMPATIBILITY_NOTES.md     - Motherboard QVL quirks, clearance issues, common AM5 problems.

  GPU/
    GPU_DECISION_GUIDE.md          - How to evaluate a GPU: raster, ray tracing, VRAM, DLSS/FSR.
    GPU_MODEL_TIERS.md             - 5070 vs 5070 Ti vs 5080 family stack, which coolers matter.
    RTX_5080_VS_5070_TI_VS_4080_SUPER.md  - Direct comparison: perf, price, value.

  Motherboard/
    MOTHERBOARD_DECISION_GUIDE.md  - What you actually need vs what marketing says.
    B850_VS_X870_VS_X870E.md       - Chipset diff, lane config, when to pay up.

  SSD/
    SSD_DECISION_GUIDE.md          - Gen4 vs Gen5 in real workloads, DRAM vs DRAM-less, TLC vs QLC.
    PCIE4_VS_PCIE5.md              - Real-world performance difference, price premium.

  PSU/
    PSU_DECISION_GUIDE.md          - How to pick wattage, efficiency tier, ATX 3.1 requirements.
    ATX_3_1_AND_12V_2X6_NOTES.md   - 12V-2x6 connector, native vs adapter, safety.

  Case/
    CASE_DECISION_GUIDE.md         - Airflow, GPU length, radiator support, fan configuration.
    LANCOOL_207_DIGITAL_NOTES.md    - Specific notes for this case.

  Cooling/
    COOLING_DECISION_GUIDE.md      - AIO vs air for 9900X, radiator placement, fan curves.
    AIO_360_COMPARISON.md          - Arctic vs other common options.
```

**Rule:** Knowledge base is populated *after* a price refresh finishes. Do not mix part research with price scraping.

## Archive / Notes

- `02_PC_Builds/99_Archive_Excel_Attempt/` - old spreadsheet attempt, not active app logic.
- `99_Archive/README_History/README_FULL_HISTORY_2026-06-21.md` - old long README/project memory.
- `99_Archive/Old_Shortlists/00_Working_Shortlists_2026-06-21/` - older shortlist thinking.
- `01_Market_Data/archived/2026-06-16/` - previous refresh raw captures.
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

Current RAM focus:

- Leave motherboard alone until RAM is clearer.
- Verify the suspicious Hungary Silicon Power 64GB 6000 CL30 lead before treating it as real.
- Capture exact Patriot, GOODRAM, and Kingston 64GB CL30 store pages in Poland and Ukraine.
- Capture Patriot 32GB CL30 in Poland, Ukraine, and Hungary for the budget-down build.

Current GPU focus:

- Treat Ukraine MSI RTX 5080 Ventus at 59,250 UAH as the strongest exact lead, pending seller/warranty/payment details.
- Verify Poland Inno3D X3, Gigabyte Windforce, and MSI Ventus exact store rows.
- Verify Hungary Gainward / Palit / Inno3D exact store rows only if local warranty convenience matters.
