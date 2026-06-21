# Next Chat Handoff - PC Build Market Workflow

Workspace:

`/Users/romaantonyak/Library/CloudStorage/OneDrive-Personal/Files_Roman/06_Personal/Personal_Projects/Hungarian_PC_Parts_Market`

## Read Order

Be token-smart. Do not open raw captures first.

1. `README.md`
2. `PROJECT_STRUCTURE.md`
3. `02_PC_Builds/01_Price_Refresh/2026-06-21/PRICE_COLLECTION.md`
4. Relevant part snapshot CSV/MD
5. Relevant `01_Market_Data/2026-06-21/<Part>/_capture_index.csv`
6. Raw `.md` capture only when extracting/auditing a specific source

## Current Workflow

User drops market captures into `00_Hub/`.

Process Hub like this:

1. Move captures into `01_Market_Data/2026-06-21/<Part>/`.
2. Rebuild that part folder's `_capture_index.csv`.
3. Broad search pages update part market snapshot/reviewed options.
4. Exact store/product pages update `price_changes.csv`.
5. Only update `02_PC_Builds/parts_options_seed.csv` when the row is confident enough for the actual build.
6. If app CSV changes, sync `04_Tools/pc_build_marimo_WASM_SAFE.py` and export `docs/planner.html`.

## Current State

RAM is already deeply captured.

- Target: 64GB or 32GB, 2-stick DDR5-6000 CL30.
- Controlled fallback tiers matter if prices are too high: 6000 CL32/CL36, 5600 CL30/CL36, 6000 CL40 only if savings are real.
- Exact Poland Patriot Viper Venom 64GB CL30 from RTV EURO AGD is captured at 3,209 PLN with lifetime warranty.
- Hungary Silicon Power XPower Zenith 64GB CL30 at 225,090 HUF is suspicious/verify, not final pick.

GPU is also enough for now.

- Best current lead: Ukraine MSI RTX 5080 Ventus 3X OC at 59,250 UAH from LuckyLink/Hotline, needs warranty/payment/delivery confidence.
- Poland exact candidates captured: Inno3D X3, Zotac Solid Core OC, Gainward Phoenix x-kom, Palit GamingPro OC.
- Future GPU options like RTX 5070 Ti and RTX 4080 Super belong in later snapshots, not mixed into RTX 5080.

Newer captures now exist for motherboard, PSU, and SSD. Their snapshots exist:

- `motherboard_market_snapshot.csv`
- `psu_market_snapshot.csv`
- `ssd_market_snapshot.csv`

## Current Active Raw Folders

- `01_Market_Data/2026-06-21/CPU/`
- `01_Market_Data/2026-06-21/Motherboard/`
- `01_Market_Data/2026-06-21/RAM/`
- `01_Market_Data/2026-06-21/GPU/`
- `01_Market_Data/2026-06-21/PSU/`
- `01_Market_Data/2026-06-21/SSD/`

Each has `_capture_index.csv`.

## Knowledge Base Plan

`05_Knowledge_Base/` is for deep technical research, not prices.

Use it later to write durable guides:

- RAM timing/capacity tiers
- RTX 5080 vs 5070 Ti vs 4080 Super
- B850 vs X870/X870E motherboards
- PCIe 4 vs PCIe 5 SSDs
- ATX 3.1 / 12V-2x6 PSU rules
- Lancool 207 Digital and case airflow
- 360 AIO cooling choices

Do this after market captures are organized.

## Important User Preference

The user wants professional file sorting and low token use. Be decisive and avoid rereading huge raw captures unless necessary. Preserve data; archive before deleting. Broad pages are discovery; exact product/store pages are buy evidence.
