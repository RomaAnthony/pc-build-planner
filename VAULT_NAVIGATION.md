# Vault Navigation for Surgical PC Build Work

Date: 2026-06-22

Purpose: fast map for Codex/AI helpers. Read this before changing prices, Marimo code, or order notes.

## First Rule

`00_Hub/Current_Order/` is the real purchase truth. The planner CSV is a model of the build, not the proof of purchase.

For a surgical update, start with these files in order:

1. `README.md`
2. `PROJECT_STRUCTURE.md`
3. `00_Hub/Current_Order/README.md`
4. `00_Hub/Current_Order/REMAINING_PARTS.md`
5. The relevant part folder's `ORDER_SUMMARY.md`
6. `04_Tools/PC_BUILD_CODE_MAP.md` only if changing Marimo
7. `02_PC_Builds/parts_options_seed.csv` only when the planner needs a price/option update

Do not open raw captures unless a price/source is missing or disputed.

## Current Active Build

The normal Marimo app has one active preset: `Current real build`.

Active planner row IDs:

| Build line | Seed ID | Real status |
|---|---:|---|
| CPU | `CPU_01_PL_AMZ` | Amazon.pl ordered, pending account/payment approval |
| Main board | `MB_04_PL` | Amazon.pl ordered, pending account/payment approval |
| Memory | `RAM_01_PL` | Paid |
| Storage | `SSD_01_PL` | Paid |
| Power supply | `PSU_01_HU` | Paid |
| Cooler | `COOL_01_HU` | Ordered, pickup/payment pending |
| Thermal paste | `PASTE_01_PL` | Amazon.pl ordered, pending account/payment approval |
| Case | `CASE_14_HU` | Paid |
| Extra fans | `FAN_04_HU` | Paid |
| Graphics card | `GPU_02_PL` | Paid |

Current paid/pending prices in the seed:

| Part | Store | Price |
|---|---|---:|
| Ryzen 9 9900X | Amazon.pl | 1,398.99 PLN |
| Gigabyte X870E AORUS Elite WiFi7 | Amazon.pl | 1,079.00 PLN |
| Patriot Viper Venom 64GB 6000 CL30 | RTV EURO AGD | 3,209.00 PLN |
| Kingston KC3000 2TB | Empik / Okazje-Centrum | 1,097.99 PLN |
| be quiet! Pure Power 13 M 1000W | AQUA | 50,780 HUF |
| ARCTIC Liquid Freezer III Pro 360 A-RGB | PCGO | 33,128 HUF |
| ARCTIC MX-7 4g incl. MX Cleaner | Amazon.pl | 35.08 PLN |
| NZXT H7 Flow RGB Black | Compzone | 54,840 HUF |
| MSI RTX 5080 Gaming Trio OC | KR System | 5,762.73 PLN |
| ARCTIC P12 Pro A-RGB fan set | AQUA | 17,480 HUF |

Current accounting total including fans: 176,548.10 UAH.

UAH accounting rule:

- Paid rows use exact receipt UAH from `Paid_UAH` in `02_PC_Builds/parts_options_seed.csv`.
- Pending/unpaid rows use fixed order-planning rates until exact receipts exist.
- Fixed PLN planning rate: 1 PLN = 12.1970 UAH.
- Fixed HUF planning rate: 100 HUF = 14.77 UAH.
- HUF comparison rate: 1 PLN = 82.58 HUF.

## Where to Edit

Use `02_PC_Builds/parts_options_seed.csv` for planner option rows.

Use `04_Tools/pc_build_marimo.py` for the normal local app:

- `builds` dictionary: active preset row IDs.
- `compare_ids` dictionary: Hungary comparison references for Poland/Ukraine rows.
- country and part picker cells: add a new part category such as thermal paste.
- selected table/summary cells: total and basket display logic.

Use `04_Tools/audit_parts_seed_against_refresh.py` after edits:

```bash
python3 04_Tools/audit_parts_seed_against_refresh.py
```

Only run the WASM sync check when deliberately updating the hosted page:

```bash
python3 04_Tools/audit_parts_seed_against_refresh.py --check-wasm
```

Do not edit `04_Tools/pc_build_marimo_WASM_SAFE.py` or `docs/planner.html` during small local ordering work unless the user explicitly asks for a hosted/export sync.

## Order Hub Map

Real current order folders:

- `00_Hub/Current_Order/GPU_RTX_5080/`
- `00_Hub/Current_Order/RAM_64GB_CL30/`
- `00_Hub/Current_Order/SSD_KC3000/`
- `00_Hub/Current_Order/CASE_NZXT_H7_FLOW_RGB/`
- `00_Hub/Current_Order/CPU_COOLER_ARCTIC_LFIII_PRO_360_ARGB/`
- `00_Hub/Current_Order/PSU_BEQUIET_PURE_POWER_13_M_1000W/`
- `00_Hub/Current_Order/AMAZON_PL_CPU_MOTHERBOARD_PASTE/`
- `00_Hub/Current_Order/FANS_ARCTIC_P12_PRO_ARGB/`

Cross-order files:

- `00_Hub/Current_Order/ROBERT_DELIVERY_SUMMARY.md`
- `00_Hub/Current_Order/REMAINING_PARTS.md`
- `00_Hub/Current_Order/PSU_AND_FANS_DECISION.md`
- `00_Hub/Current_Order/CURRENT_BUILD_AUDIT_2026-06-23.md`

## Price Research Map

Use these only when doing fresh market work:

- `01_Market_Data/<date>/<part>/` - raw evidence and capture indexes.
- `02_PC_Builds/01_Price_Refresh/<date>/` - curated market snapshots and reviewed option CSVs.
- `05_Knowledge_Base/<part>/` - durable non-price decision notes.

## Safety Notes

- Preserve old market options unless the user asks to delete historical rows. They are useful for dropdown comparison.
- Delete old build presets from the Marimo `builds` dictionary when the user wants a single active build; do not mass-delete seed rows for that.
- Fan price is locked from the AQUA/Monobank receipt. The active row is `FAN_04_HU` at 17,480 HUF.
- `PSU_01_HU` intentionally differs from old snapshot rows: the planner now uses the paid AQUA total of 50,780 HUF.
- OneDrive path cleanup is documented in `99_Archive/PATH_RENAMES_2026-06-22.csv`.
