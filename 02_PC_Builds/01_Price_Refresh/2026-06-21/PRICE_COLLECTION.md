# Price Refresh Collection - 2026-06-21

Goal: collect fresh Hungary Arukereso, Poland Ceneo, and Ukraine Hotline prices before we update the Marimo planner CSV.

## Capture Rules

- Save each capture as Markdown in `01_Market_Data/2026-06-21/`.
- If you are still collecting quickly, drop files into `00_Hub/`; Codex will sort them into `01_Market_Data/2026-06-21/<Part>/`.
- Use one file per product per market when possible.
- Capture the product title, lowest price, store name, currency, product URL, and whether it is exact or only a broad-search match.
- For CPUs, keep BOX vs Tray separate. Do not replace a Box row with Tray unless we intentionally choose Tray.
- For GPUs and cases, match exact model/color when possible.
- For PSU, only count ATX 3.0/3.1 and native 12V-2x6/12VHPWR units unless we explicitly choose otherwise.
- If a site shows a cheaper non-exact item, write it in notes but do not use it as the real comparison price.

## Spec Tier Rules

Do not treat every non-target row as useless. The workflow has two different jobs:

1. Find the best exact target part.
2. If target parts are too expensive, keep a controlled list of downgrade/value alternatives.

For RAM, the target tier is `64GB or 32GB, 2-stick kit, DDR5-6000, CL30`. Fallback tiers are allowed and should be recorded when they save real money:

- Tier A: exact target, 6000 CL30.
- Tier B: same capacity, 6000 CL32/CL34/CL36 if much cheaper.
- Tier C: same capacity, 5600 CL30/CL36 or 6000 CL40 if the saving is large.
- Reject only when the row is clearly wrong for the build: DDR4, laptop/server RAM, single stick when we need a kit, 4-stick kit for AM5 unless intentional, weird capacity, unclear SKU, or price not competitive.

For GPU, the target tier is RTX 5080 16GB. Fallback tiers like RTX 5070 Ti and RTX 4080 Super are future separate snapshots, not mixed into the RTX 5080 file.

Snapshot files should therefore have:

- `*_market_snapshot.csv`: shortlist and decision candidates.
- `*_reviewed_options.csv`: wider audit list, including exact target rows, fallback rows, and rejected rows with reasons.

## Hub To CSV Rules

When new files arrive in `00_Hub/`, process them in this order:

1. Move raw captures to `01_Market_Data/<date>/<part>/`.
2. Update that part folder's `_capture_index.csv`.
3. If the capture is a broad category/search page, update the part snapshot file, not the app CSV.
4. If the capture is an exact product/store page with clear price, update `price_changes.csv`.
5. If the new price changes the actual planned build, update `parts_options_seed.csv`.
6. After changing `parts_options_seed.csv`, sync `04_Tools/pc_build_marimo_WASM_SAFE.py` and export `docs/planner.html`.

Do not let broad-search rows overwrite exact app rows. Broad search tells us what to investigate next; exact store/product pages tell us what to buy.

## Current RAM Focus

Motherboard is paused for now. RAM is the active market study because it can change the build price by around 20k UAH if we step down from 64GB to 32GB.

Use:

- `RAM_MARKET_SNAPSHOT.md` for the current conclusion.
- `ram_market_snapshot.csv` for ranked candidate rows.
- `ram_reviewed_options.csv` for the wider audit list, including valid backups and rejected/noisy market rows.
- `price_changes.csv` only after exact store/product verification.

Capture priority:

1. Verify Silicon Power XPower Zenith 64GB 6000 CL30 in Hungary because the captured price is unusually low.
2. Exact Patriot Viper Venom 64GB CL30 store/product pages in Poland and Ukraine.
3. Exact GOODRAM IRDM 64GB CL30 store/product pages in Poland and Ukraine.
4. Exact Kingston Fury Beast 64GB CL30 store/product pages in Poland, Hungary, and Ukraine.
5. Exact Patriot Viper Venom 32GB CL30 store/product pages in Poland, Hungary, and Ukraine.

Price-comparison pages are allowed for market discovery. Direct store pages are preferred for final price updates.

## Current GPU Focus

RTX 5080 now follows the same workflow as RAM:

- `GPU_MARKET_SNAPSHOT.md` for the current conclusion.
- `gpu_market_snapshot.csv` for ranked candidate rows.
- `gpu_reviewed_options.csv` for the wider audit list, including non-winning Poland/Hungary variants and Ukraine seller-row notes.
- `price_changes.csv` only after exact store/product verification.

Capture priority:

1. Ukraine MSI RTX 5080 Ventus 3X OC exact seller rows: store, warranty, payment fee, delivery, stock.
2. Poland Inno3D RTX 5080 X3 / X3 OC, Gigabyte Windforce OC SFF, and MSI Ventus exact store rows.
3. Ukraine MSI Gaming Trio exact seller rows if premium cooler is still interesting.
4. Hungary Gainward Phoenix V1, Palit GamingPro, Inno3D X3 OC, and Gigabyte Windforce exact store rows if local warranty matters.

For GPU, do not choose purely by lowest broad-search price. Warranty, seller quality, payment fees, and cooler class can matter more than a few thousand UAH.

## How To Send Back

For each product, paste or save a short block like this:

```md
Product: MSI RTX 5080 Ventus 3X OC 16GB
Market: Ukraine
Site: Hotline
Store: example.ua
Price: 65000 UAH
URL: https://...
Match: Exact
Notes: warranty/delivery/stock
```

## Search Checklist

| Done | Part | Priority | Product | In CSV | Hungary Arukereso | Poland Ceneo | Ukraine Hotline |
|---|---|---:|---|---|---|---|---|
| [ ] | CPU | 1 | AMD Ryzen 9 9900X Box | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=AMD%20Ryzen%209%209900X%20Box) | [PL](https://www.ceneo.pl/;szukaj-AMD%20Ryzen%209%209900X%20Box) | [UA](https://hotline.ua/ua/sr/?q=AMD%20Ryzen%209%209900X%20Box) |
| [ ] | CPU | 2 | AMD Ryzen 7 9700X Box | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=AMD%20Ryzen%207%209700X%20Box) | [PL](https://www.ceneo.pl/;szukaj-AMD%20Ryzen%207%209700X%20Box) | [UA](https://hotline.ua/ua/sr/?q=AMD%20Ryzen%207%209700X%20Box) |
| [ ] | CPU | 3 | AMD Ryzen 9 9950X Box | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=AMD%20Ryzen%209%209950X%20Box) | [PL](https://www.ceneo.pl/;szukaj-AMD%20Ryzen%209%209950X%20Box) | [UA](https://hotline.ua/ua/sr/?q=AMD%20Ryzen%209%209950X%20Box) |
| [ ] | Motherboard | 1 | MSI MAG B850 Tomahawk MAX WiFi | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=MSI%20MAG%20B850%20Tomahawk%20MAX%20WiFi) | [PL](https://www.ceneo.pl/;szukaj-MSI%20MAG%20B850%20Tomahawk%20MAX%20WiFi) | [UA](https://hotline.ua/ua/sr/?q=MSI%20MAG%20B850%20Tomahawk%20MAX%20WiFi) |
| [ ] | Motherboard | 2 | ASRock X870 PRO RS WiFi | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=ASRock%20X870%20PRO%20RS%20WiFi) | [PL](https://www.ceneo.pl/;szukaj-ASRock%20X870%20PRO%20RS%20WiFi) | [UA](https://hotline.ua/ua/sr/?q=ASRock%20X870%20PRO%20RS%20WiFi) |
| [ ] | Motherboard | 3 | MSI MAG B850 Tomahawk WiFi non-MAX | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=MSI%20MAG%20B850%20Tomahawk%20WiFi%20non-MAX) | [PL](https://www.ceneo.pl/;szukaj-MSI%20MAG%20B850%20Tomahawk%20WiFi%20non-MAX) | [UA](https://hotline.ua/ua/sr/?q=MSI%20MAG%20B850%20Tomahawk%20WiFi%20non-MAX) |
| [ ] | Motherboard | 4 | Gigabyte X870E AORUS Elite WiFi7 | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Gigabyte%20X870E%20AORUS%20Elite%20WiFi7) | [PL](https://www.ceneo.pl/;szukaj-Gigabyte%20X870E%20AORUS%20Elite%20WiFi7) | [UA](https://hotline.ua/ua/sr/?q=Gigabyte%20X870E%20AORUS%20Elite%20WiFi7) |
| [ ] | RAM | 1 | Patriot Viper Venom 64GB 2x32 DDR5-6000 CL30 | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Patriot%20Viper%20Venom%2064GB%202x32%20DDR5-6000%20CL30) | [PL](https://www.ceneo.pl/;szukaj-Patriot%20Viper%20Venom%2064GB%202x32%20DDR5-6000%20CL30) | [UA](https://hotline.ua/ua/sr/?q=Patriot%20Viper%20Venom%2064GB%202x32%20DDR5-6000%20CL30) |
| [ ] | RAM | 2 | Kingston Fury Beast EXPO 64GB 2x32 DDR5-6000 CL30 | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Kingston%20Fury%20Beast%20EXPO%2064GB%202x32%20DDR5-6000%20CL30) | [PL](https://www.ceneo.pl/;szukaj-Kingston%20Fury%20Beast%20EXPO%2064GB%202x32%20DDR5-6000%20CL30) | [UA](https://hotline.ua/ua/sr/?q=Kingston%20Fury%20Beast%20EXPO%2064GB%202x32%20DDR5-6000%20CL30) |
| [ ] | RAM | 3 | GOODRAM IRDM 64GB 2x32 DDR5-6000 CL30 | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=GOODRAM%20IRDM%2064GB%202x32%20DDR5-6000%20CL30) | [PL](https://www.ceneo.pl/;szukaj-GOODRAM%20IRDM%2064GB%202x32%20DDR5-6000%20CL30) | [UA](https://hotline.ua/ua/sr/?q=GOODRAM%20IRDM%2064GB%202x32%20DDR5-6000%20CL30) |
| [ ] | RAM | 4 | Patriot Viper Venom 32GB 2x16 DDR5-6000 CL30 | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Patriot%20Viper%20Venom%2032GB%202x16%20DDR5-6000%20CL30) | [PL](https://www.ceneo.pl/;szukaj-Patriot%20Viper%20Venom%2032GB%202x16%20DDR5-6000%20CL30) | [UA](https://hotline.ua/ua/sr/?q=Patriot%20Viper%20Venom%2032GB%202x16%20DDR5-6000%20CL30) |
| [ ] | SSD | 1 | Kingston KC3000 2TB | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Kingston%20KC3000%202TB) | [PL](https://www.ceneo.pl/;szukaj-Kingston%20KC3000%202TB) | [UA](https://hotline.ua/ua/sr/?q=Kingston%20KC3000%202TB) |
| [ ] | SSD | 2 | Lexar NM790 2TB | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Lexar%20NM790%202TB) | [PL](https://www.ceneo.pl/;szukaj-Lexar%20NM790%202TB) | [UA](https://hotline.ua/ua/sr/?q=Lexar%20NM790%202TB) |
| [ ] | SSD | 3 | Samsung 990 PRO 2TB | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Samsung%20990%20PRO%202TB) | [PL](https://www.ceneo.pl/;szukaj-Samsung%20990%20PRO%202TB) | [UA](https://hotline.ua/ua/sr/?q=Samsung%20990%20PRO%202TB) |
| [ ] | PSU | 1 | be quiet! Pure Power 13 M 1000W | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=be%20quiet%21%20Pure%20Power%2013%20M%201000W) | [PL](https://www.ceneo.pl/;szukaj-be%20quiet%21%20Pure%20Power%2013%20M%201000W) | [UA](https://hotline.ua/ua/sr/?q=be%20quiet%21%20Pure%20Power%2013%20M%201000W) |
| [ ] | PSU | 2 | Seasonic Focus GX-1000 2024 | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Seasonic%20Focus%20GX-1000%202024) | [PL](https://www.ceneo.pl/;szukaj-Seasonic%20Focus%20GX-1000%202024) | [UA](https://hotline.ua/ua/sr/?q=Seasonic%20Focus%20GX-1000%202024) |
| [ ] | PSU | 2 | Seasonic Focus GX-1000 v4 | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Seasonic%20Focus%20GX-1000%20v4) | [PL](https://www.ceneo.pl/;szukaj-Seasonic%20Focus%20GX-1000%20v4) | [UA](https://hotline.ua/ua/sr/?q=Seasonic%20Focus%20GX-1000%20v4) |
| [ ] | PSU | 3 | Corsair RM1000x ATX 3.1 | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Corsair%20RM1000x%20ATX%203.1) | [PL](https://www.ceneo.pl/;szukaj-Corsair%20RM1000x%20ATX%203.1) | [UA](https://hotline.ua/ua/sr/?q=Corsair%20RM1000x%20ATX%203.1) |
| [ ] | Cooler | 1 | Arctic Liquid Freezer III Pro 360 A-RGB Black | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Arctic%20Liquid%20Freezer%20III%20Pro%20360%20A-RGB%20Black) | [PL](https://www.ceneo.pl/;szukaj-Arctic%20Liquid%20Freezer%20III%20Pro%20360%20A-RGB%20Black) | [UA](https://hotline.ua/ua/sr/?q=Arctic%20Liquid%20Freezer%20III%20Pro%20360%20A-RGB%20Black) |
| [ ] | Cooler | 2 | Arctic Liquid Freezer III Pro 360 Black | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Arctic%20Liquid%20Freezer%20III%20Pro%20360%20Black) | [PL](https://www.ceneo.pl/;szukaj-Arctic%20Liquid%20Freezer%20III%20Pro%20360%20Black) | [UA](https://hotline.ua/ua/sr/?q=Arctic%20Liquid%20Freezer%20III%20Pro%20360%20Black) |
| [ ] | Cooler | 3 | DeepCool LE360 V2 ARGB Black | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=DeepCool%20LE360%20V2%20ARGB%20Black) | [PL](https://www.ceneo.pl/;szukaj-DeepCool%20LE360%20V2%20ARGB%20Black) | [UA](https://hotline.ua/ua/sr/?q=DeepCool%20LE360%20V2%20ARGB%20Black) |
| [ ] | Cooler | 4 | MSI MAG CoreLiquid A13 360 Black | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=MSI%20MAG%20CoreLiquid%20A13%20360%20Black) | [PL](https://www.ceneo.pl/;szukaj-MSI%20MAG%20CoreLiquid%20A13%20360%20Black) | [UA](https://hotline.ua/ua/sr/?q=MSI%20MAG%20CoreLiquid%20A13%20360%20Black) |
| [ ] | Cooler | 5 | Gigabyte GME 360 Gaming CPU Cooler Black | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Gigabyte%20GME%20360%20Gaming%20CPU%20Cooler%20Black) | [PL](https://www.ceneo.pl/;szukaj-Gigabyte%20GME%20360%20Gaming%20CPU%20Cooler%20Black) | [UA](https://hotline.ua/ua/sr/?q=Gigabyte%20GME%20360%20Gaming%20CPU%20Cooler%20Black) |
| [ ] | Cooler | 6 | be quiet! Pure Loop 3 LX 360mm Black | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=be%20quiet%21%20Pure%20Loop%203%20LX%20360mm%20Black) | [PL](https://www.ceneo.pl/;szukaj-be%20quiet%21%20Pure%20Loop%203%20LX%20360mm%20Black) | [UA](https://hotline.ua/ua/sr/?q=be%20quiet%21%20Pure%20Loop%203%20LX%20360mm%20Black) |
| [ ] | Case | 1 | Corsair 3500X ARGB Black | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Corsair%203500X%20ARGB%20Black) | [PL](https://www.ceneo.pl/;szukaj-Corsair%203500X%20ARGB%20Black) | [UA](https://hotline.ua/ua/sr/?q=Corsair%203500X%20ARGB%20Black) |
| [ ] | Case | 2 | Corsair 3500X Black plain | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Corsair%203500X%20Black%20plain) | [PL](https://www.ceneo.pl/;szukaj-Corsair%203500X%20Black%20plain) | [UA](https://hotline.ua/ua/sr/?q=Corsair%203500X%20Black%20plain) |
| [ ] | Case | 3 | Phanteks XT View TG D-RGB Black | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Phanteks%20XT%20View%20TG%20D-RGB%20Black) | [PL](https://www.ceneo.pl/;szukaj-Phanteks%20XT%20View%20TG%20D-RGB%20Black) | [UA](https://hotline.ua/ua/sr/?q=Phanteks%20XT%20View%20TG%20D-RGB%20Black) |
| [ ] | Case | 4 | NZXT H6 Flow RGB All Black | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=NZXT%20H6%20Flow%20RGB%20All%20Black) | [PL](https://www.ceneo.pl/;szukaj-NZXT%20H6%20Flow%20RGB%20All%20Black) | [UA](https://hotline.ua/ua/sr/?q=NZXT%20H6%20Flow%20RGB%20All%20Black) |
| [ ] | Case | 5 | Lian Li O11 Vision Compact Black | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Lian%20Li%20O11%20Vision%20Compact%20Black) | [PL](https://www.ceneo.pl/;szukaj-Lian%20Li%20O11%20Vision%20Compact%20Black) | [UA](https://hotline.ua/ua/sr/?q=Lian%20Li%20O11%20Vision%20Compact%20Black) |
| [ ] | Case | 6 | NZXT H9 Flow Black | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=NZXT%20H9%20Flow%20Black) | [PL](https://www.ceneo.pl/;szukaj-NZXT%20H9%20Flow%20Black) | [UA](https://hotline.ua/ua/sr/?q=NZXT%20H9%20Flow%20Black) |
| [ ] | Case | 7 | Montech KING 95 PRO TG ARGB Black | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Montech%20KING%2095%20PRO%20TG%20ARGB%20Black) | [PL](https://www.ceneo.pl/;szukaj-Montech%20KING%2095%20PRO%20TG%20ARGB%20Black) | [UA](https://hotline.ua/ua/sr/?q=Montech%20KING%2095%20PRO%20TG%20ARGB%20Black) |
| [ ] | Case | 8 | Lian Li O11D EVO RGB TG Black | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Lian%20Li%20O11D%20EVO%20RGB%20TG%20Black) | [PL](https://www.ceneo.pl/;szukaj-Lian%20Li%20O11D%20EVO%20RGB%20TG%20Black) | [UA](https://hotline.ua/ua/sr/?q=Lian%20Li%20O11D%20EVO%20RGB%20TG%20Black) |
| [ ] | Case | 9 | Lian Li O11 Dynamic Mini V2 TG Black | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Lian%20Li%20O11%20Dynamic%20Mini%20V2%20TG%20Black) | [PL](https://www.ceneo.pl/;szukaj-Lian%20Li%20O11%20Dynamic%20Mini%20V2%20TG%20Black) | [UA](https://hotline.ua/ua/sr/?q=Lian%20Li%20O11%20Dynamic%20Mini%20V2%20TG%20Black) |
| [ ] | Case | 10 | Phanteks NV9 MK2 Black | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Phanteks%20NV9%20MK2%20Black) | [PL](https://www.ceneo.pl/;szukaj-Phanteks%20NV9%20MK2%20Black) | [UA](https://hotline.ua/ua/sr/?q=Phanteks%20NV9%20MK2%20Black) |
| [ ] | Case | 11 | Lian Li O11 Dynamic EVO XL Black | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Lian%20Li%20O11%20Dynamic%20EVO%20XL%20Black) | [PL](https://www.ceneo.pl/;szukaj-Lian%20Li%20O11%20Dynamic%20EVO%20XL%20Black) | [UA](https://hotline.ua/ua/sr/?q=Lian%20Li%20O11%20Dynamic%20EVO%20XL%20Black) |
| [ ] | GPU | 1 | MSI RTX 5080 Ventus 3X OC 16GB | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=MSI%20RTX%205080%20Ventus%203X%20OC%2016GB) | [PL](https://www.ceneo.pl/;szukaj-MSI%20RTX%205080%20Ventus%203X%20OC%2016GB) | [UA](https://hotline.ua/ua/sr/?q=MSI%20RTX%205080%20Ventus%203X%20OC%2016GB) |
| [ ] | GPU | 2 | MSI RTX 5080 Gaming Trio OC 16GB | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=MSI%20RTX%205080%20Gaming%20Trio%20OC%2016GB) | [PL](https://www.ceneo.pl/;szukaj-MSI%20RTX%205080%20Gaming%20Trio%20OC%2016GB) | [UA](https://hotline.ua/ua/sr/?q=MSI%20RTX%205080%20Gaming%20Trio%20OC%2016GB) |
| [ ] | GPU | 3 | Gigabyte RTX 5080 Gaming OC 16GB | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Gigabyte%20RTX%205080%20Gaming%20OC%2016GB) | [PL](https://www.ceneo.pl/;szukaj-Gigabyte%20RTX%205080%20Gaming%20OC%2016GB) | [UA](https://hotline.ua/ua/sr/?q=Gigabyte%20RTX%205080%20Gaming%20OC%2016GB) |
| [ ] | GPU | 4 | Inno3D RTX 5080 X3 OC 16GB | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Inno3D%20RTX%205080%20X3%20OC%2016GB) | [PL](https://www.ceneo.pl/;szukaj-Inno3D%20RTX%205080%20X3%20OC%2016GB) | [UA](https://hotline.ua/ua/sr/?q=Inno3D%20RTX%205080%20X3%20OC%2016GB) |
| [ ] | GPU | 5 | Gigabyte RTX 5080 Windforce OC SFF 16GB | yes | [HU](https://www.arukereso.hu/CategorySearch.php?st=Gigabyte%20RTX%205080%20Windforce%20OC%20SFF%2016GB) | [PL](https://www.ceneo.pl/;szukaj-Gigabyte%20RTX%205080%20Windforce%20OC%20SFF%2016GB) | [UA](https://hotline.ua/ua/sr/?q=Gigabyte%20RTX%205080%20Windforce%20OC%20SFF%2016GB) |
| [ ] | Case | NEW | Lian Li Lancool 207 Digital Black | no | [HU](https://www.arukereso.hu/CategorySearch.php?st=Lian%20Li%20Lancool%20207%20Digital%20Black) | [PL](https://www.ceneo.pl/;szukaj-Lian%20Li%20Lancool%20207%20Digital%20Black) | [UA](https://hotline.ua/ua/sr/?q=Lian%20Li%20Lancool%20207%20Digital%20Black) |
| [ ] | SSD | NEW | Kingston FURY Renegade G5 2TB PCIe 5.0 | no | [HU](https://www.arukereso.hu/CategorySearch.php?st=Kingston%20FURY%20Renegade%20G5%202TB%20PCIe%205.0) | [PL](https://www.ceneo.pl/;szukaj-Kingston%20FURY%20Renegade%20G5%202TB%20PCIe%205.0) | [UA](https://hotline.ua/ua/sr/?q=Kingston%20FURY%20Renegade%20G5%202TB%20PCIe%205.0) |
| [ ] | SSD | NEW | Kingston KC3000 2TB PCIe 4.0 | no | [HU](https://www.arukereso.hu/CategorySearch.php?st=Kingston%20KC3000%202TB%20PCIe%204.0) | [PL](https://www.ceneo.pl/;szukaj-Kingston%20KC3000%202TB%20PCIe%204.0) | [UA](https://hotline.ua/ua/sr/?q=Kingston%20KC3000%202TB%20PCIe%204.0) |
| [ ] | PSU | NEW | Corsair RM1000x ATX 3.1 1000W | no | [HU](https://www.arukereso.hu/CategorySearch.php?st=Corsair%20RM1000x%20ATX%203.1%201000W) | [PL](https://www.ceneo.pl/;szukaj-Corsair%20RM1000x%20ATX%203.1%201000W) | [UA](https://hotline.ua/ua/sr/?q=Corsair%20RM1000x%20ATX%203.1%201000W) |
| [ ] | PSU | NEW | Seasonic Focus GX-1000 ATX 3.1 1000W | no | [HU](https://www.arukereso.hu/CategorySearch.php?st=Seasonic%20Focus%20GX-1000%20ATX%203.1%201000W) | [PL](https://www.ceneo.pl/;szukaj-Seasonic%20Focus%20GX-1000%20ATX%203.1%201000W) | [UA](https://hotline.ua/ua/sr/?q=Seasonic%20Focus%20GX-1000%20ATX%203.1%201000W) |
| [ ] | Fan | NEW | Lian Li UNI FAN SL-INF 120 Reverse Blade Black | no | [HU](https://www.arukereso.hu/CategorySearch.php?st=Lian%20Li%20UNI%20FAN%20SL-INF%20120%20Reverse%20Blade%20Black) | [PL](https://www.ceneo.pl/;szukaj-Lian%20Li%20UNI%20FAN%20SL-INF%20120%20Reverse%20Blade%20Black) | [UA](https://hotline.ua/ua/sr/?q=Lian%20Li%20UNI%20FAN%20SL-INF%20120%20Reverse%20Blade%20Black) |
| [ ] | Fan | NEW | Lian Li UNI FAN SL-INF 140 Reverse Blade Black | no | [HU](https://www.arukereso.hu/CategorySearch.php?st=Lian%20Li%20UNI%20FAN%20SL-INF%20140%20Reverse%20Blade%20Black) | [PL](https://www.ceneo.pl/;szukaj-Lian%20Li%20UNI%20FAN%20SL-INF%20140%20Reverse%20Blade%20Black) | [UA](https://hotline.ua/ua/sr/?q=Lian%20Li%20UNI%20FAN%20SL-INF%20140%20Reverse%20Blade%20Black) |
| [ ] | Fan | NEW | Lian Li UNI FAN SL-INF 120 Black | no | [HU](https://www.arukereso.hu/CategorySearch.php?st=Lian%20Li%20UNI%20FAN%20SL-INF%20120%20Black) | [PL](https://www.ceneo.pl/;szukaj-Lian%20Li%20UNI%20FAN%20SL-INF%20120%20Black) | [UA](https://hotline.ua/ua/sr/?q=Lian%20Li%20UNI%20FAN%20SL-INF%20120%20Black) |

## Known Baseline Notes

- Current app has Poland and Hungary only; Ukraine will need either new rows in `parts_options_seed.csv` or a small app update if we want Ukraine baskets/cards displayed separately.
- Existing source CSV was sorted on 2026-06-21 by Part > Priority > Option > Market.
- `price_changes.csv` is the working log for old price vs new price.
