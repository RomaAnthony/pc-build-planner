# Hungarian PC Parts Market

This personal project stores research and data for the Hungarian computer-parts market and Roman's PC build planning.

This README is the main memory note for the project. Keep normal notes, decisions, and research questions here.

Exception:

- [[DEEP_SEARCH_PROMPT]] is a separate reusable prompt for market research.
- [[03_Research_Notes/00_Working_Shortlists/RAM_WORKING_SHORTLIST]] is the current detailed RAM note.
- [[03_Research_Notes/00_Working_Shortlists/RTX5080_WORKING_SHORTLIST]] is the current detailed RTX 5080 note.
- [[03_Research_Notes/00_Working_Shortlists/CPU_WORKING_SHORTLIST]] is the current CPU note.
- [[03_Research_Notes/00_Working_Shortlists/SSD_WORKING_SHORTLIST]] is the current detailed SSD note.
- [[03_Research_Notes/00_Working_Shortlists/MOTHERBOARD_WORKING_SHORTLIST]] is the current motherboard shortlist.
- [[03_Research_Notes/00_Working_Shortlists/PSU_WORKING_SHORTLIST]] is the current PSU shortlist.
- [[03_Research_Notes/00_Working_Shortlists/CASE_COOLING_WORKING_SHORTLIST]] is the current case and CPU-cooling shortlist.
- [[02_PC_Builds/BUILD_OPTIONS_CSV_PREP]] is the current prep note for the future CSV/Excel comparison.
- [[02_PC_Builds/DAD_PC_BUILD_SUMMARY]] is the clean Dad-facing summary of current options, Hungary vs Poland savings, and why the PC makes sense.
- [[04_Tools/PC_BUILD_TOOLING]] is the current Marimo/Python tooling note for the live build comparison app.

Use this folder for:

- Hungarian PC component price research
- shop/source notes
- market comparisons
- PC build CSV files
- purchase-decision notes

## Current Build Context

Date: 2026-06-12

Main use:

- database work
- SQL work
- finance work
- general productivity
- light gaming

Current monitor setup:

- LG UltraGear 32GS95UV-B.AEU, 32-inch flat 4K 240Hz 16:9 FreeSync OLED gamer monitor, product code / cikkszam 1477851, captured price 486,400 HUF
- 4K 60Hz monitor
- 1920x1080 144Hz monitor

Implication:

- The future GPU choice matters. The LG 32-inch 4K 240Hz OLED makes RTX 5080-class performance logical if gaming becomes more important.
- The monitor itself is a high-end part of the setup, so the RTX 5080 plan is not only "buying an expensive GPU"; it is making proper use of an already-owned/targeted premium 4K OLED display.
- The PC should be useful before the GPU purchase because Ryzen 9000 CPUs include basic integrated graphics.
- The first purchase can be a strong platform build, with the graphics card bought separately later.

Current working direction:

- CPU: AMD Ryzen 9 9900X Box is the current preferred direction; Ryzen 7 9700X remains the value fallback.
- RAM: Patriot Viper Venom 64GB 2x32 DDR5-6000 CL30 is the current money-safe pick if the Polish seller is clean; Kingston Fury Beast EXPO remains the safer fallback if Patriot seller/spec is unclear.
- SSD: 2TB Gen4 TLC NVMe; Poland pick Kingston KC3000 2TB, Hungary value pick Lexar NM790 2TB, Hungary safer pick KC3000/FURY Renegade.
- PSU: 1000W ATX 3.1 / PCIe 5.1 with native 12V-2x6; current leads are be quiet! Pure Power 13 M 1000W for value and Seasonic Focus GX-1000 2024 for safest pick.
- Cooler: ARCTIC Liquid Freezer III Pro 360 black, likely A-RGB version for the clean black glass look; new Hungary broad capture shows A-RGB around 31,500 HUF and non-RGB around 29,200 HUF.
- Case: Corsair 3500X black style is the visual baseline, but buy case locally/Hungary because large glass case logistics from Poland are not worth it. New Hungary broad capture shows Corsair 3500X ARGB Black around 31,990 HUF.
- GPU: build around RTX 5080 if the right offer is found
- GPU price target: about HUF 500,000
- Current research focus: PSU/case/cooling final platform choices before GPU purchase timing.

Status:

- CPU and SSD are working choices from Roman's initial market review.
- GPU is the main budget anchor.
- RAM research is good enough for now. The best current path is Patriot/Kingston, with GOODRAM as the third practical option.
- RTX 5080 broad-market pass is done. Next step is exact seller-page checks, not more broad pages.
- Motherboard light shortlist is started. Next step is Hungary/Poland market captures for exact board prices.
- PSU wide-market pass is done. Next PSU step is exact seller-page checking, not more broad pages.
- Case/cooling first pass is done: cooler likely Hungary; case local/Hungary because it is too large and fragile for the Poland route.
- Build comparison tooling has moved away from manual Excel as the main brain. Current working path is CSV data plus a Marimo app in `04_Tools/pc_build_marimo.py`.

## Current Tooling

Date: 2026-06-15

Current build-comparison workflow:

- Keep product options in `02_PC_Builds/parts_options_seed.csv`.
- Use `04_Tools/pc_build_marimo.py` for live build scenarios, totals, currency estimates, and Poland/Hungary savings.
- Use Excel only as an export/presentation option later, not as the main working model.
- Exchange-rate logic matters because the real payment path may be EUR salary -> UAH card, EUR cash/card in Hungary, Hungarian card, or Polish PLN card/payment conversion. The Marimo app now has live/default rates plus manual override controls.

Start the current Marimo app from the project folder:

```bash
.venv_marimo/bin/marimo run 04_Tools/pc_build_marimo.py --host 127.0.0.1 --port 2718
```

Open:

```text
http://127.0.0.1:2718
```

Tooling note:

- [[04_Tools/PC_BUILD_TOOLING]]

## New Chat Handoff - 2026-06-12

Roman is moving to a new Codex chat because this one became slow.

Open this README first, then open [[03_Research_Notes/00_Working_Shortlists/RAM_WORKING_SHORTLIST]] only if detailed RAM prices are needed.

Current build logic:

- Build the computer first without the RTX 5080.
- Use the CPU integrated graphics temporarily.
- Buy the RTX 5080 later when price, warranty, and seller quality are good.
- Main use is database/SQL/finance/productivity, with light gaming.
- Three existing monitors include the LG UltraGear 32GS95UV-B.AEU 32-inch 4K 240Hz OLED, so RTX 5080-class GPU still makes sense long term.

Current likely first-stage build:

- CPU target: Ryzen 9 9900X Box.
- CPU fallback: Ryzen 7 9700X only if the total platform budget needs to drop.
- RAM target: Patriot Viper Venom 64GB, 2x32GB, DDR5-6000 CL30 if Polish seller/spec is clean; Kingston Fury Beast EXPO 64GB CL30 if paying extra for safer RAM branding/warranty.
- SSD target: 2TB Gen4 TLC NVMe. Captured 2026-06-13 prices: Poland favors Kingston KC3000 2TB at 939 PLN; Hungary value favors Lexar NM790 2TB at 96,695 HUF, while Kingston FURY Renegade 2TB at 103,460 HUF or Kingston KC3000 2TB at 106,336 HUF are safer DRAM-style choices. Avoid QLC/variable-NAND drives for the main database/work drive.
- Motherboard target: ATX AM5 board with strong VRM for Ryzen 9 9900X, stable 2x32GB DDR5-6000 EXPO, at least 3 M.2 slots preferred, BIOS Flashback, WiFi 6E/7, and good GPU clearance.
- PSU target: 1000W ATX 3.1 / PCIe 5.1 with native 12V-2x6 if price is reasonable.
- Case target: black glass/panoramic "Batman" look, strong airflow, enough room for RTX 5080. Current local lead: Corsair 3500X ARGB Black around 31,990 HUF; plain Corsair 3500X Black around 21,326 HUF if fan planning still works.
- Cooler target: ARCTIC Liquid Freezer III Pro 360 black; A-RGB preferred if the price gap is small. Current local lead: A-RGB black around 31,500 HUF; non-RGB black around 29,200 HUF.

RAM result:

- Best value: Patriot Viper Venom PVV564G600C30K, especially Poland if seller/warranty are clean.
- Safest choice: Kingston Fury Beast EXPO 64GB 2x32 DDR5-6000 CL30.
- Strong backup: GOODRAM IRDM 64GB 2x32 DDR5-6000 CL30, especially Poland.
- Premium/watch only: G.Skill Flare X5 / Trident Z5 Neo, technically excellent but usually too expensive.
- Skip for now: Corsair CL30 example CMK64GX5M2B6000Z30 at 4,741.66 PLN. Good spec, bad value.

RTX 5080 result so far:

- Do not choose the absolute cheapest card automatically; choose best long-term value.
- ASUS Prime/TUF/ROG/Noctua/ProArt are dropped for now because captured prices are too high.
- Zotac is not attractive enough versus cheaper Palit/Inno3D/Gainward/MSI/Gigabyte options.
- Avoid compact/SFF/dual-fan bias unless the price, seller, and cooler are clearly right.
- Best Poland lead: MSI RTX 5080 Ventus 3X OC at 4,899 PLN from x-kom direct page, with 36-month manufacturer warranty shown. It is the current price/value GPU to beat, but still a Ventus/value-tier cooler.
- Best detailed Hungary value lead: Inno3D RTX 5080 X3 OC at 465,640 HUF, seller check needed.
- Cheap Hungary watch: Gigabyte RTX 5080 Windforce OC SFF at 470,000 HUF, but cooler/SFF risk must be checked.
- Strong Hungary backup: Gainward RTX 5080 Phoenix / Phoenix GS around 474,420-479,190 HUF.
- Palit update: new detailed Palit GamingPro OC capture is 492,620 HUF / 5,367 PLN, so it is no longer the first Hungary value lead unless seller/warranty is much better.
- PNY Triple Fan OC is acceptable in Hungary around 487,240 HUF, but not better than Inno3D/Gainward on value.
- MSI/Gigabyte focus: MSI Ventus 3X OC is the pure-price Poland lead; MSI Gaming Trio OC and Gigabyte Gaming OC are the best long-term-value pair to compare; MSI Shadow and Gigabyte Windforce OC SFF are backups unless pricing is much better.
- Used Hungarian benchmark: below 430,000 HUF is excellent; 430,000-450,000 HUF is possible only with transferable warranty; 450,000 HUF or more is usually not worth used risk.

Next research area:

- RTX 5080 seller-level pages for the current shortlist.
- Focus on Hungary and Poland first; Ukraine only if it clearly beats both after warranty/logistics risk.
- Goal is not to pick by brand blindly. Compare exact models, cooler quality, card length, noise/thermals, warranty, seller, and final price.
- Keep a short list of about 3 best RTX 5080 options, plus maybe 1 premium option if price gap is small.

Important workflow:

- Use manual captures from Arukereso, Ceneo, Hotline/E-Katalog, and real retailer pages.
- Put raw downloaded pages in `03_Research_Notes`.
- Keep conclusions short in this README or one working note per active category.
- Do not create lots of separate Markdown files unless Roman asks.
- Do not create permanent CSVs yet. CSVs can come later when the build is closer to final.

## Preferred Research Workflow

Use manual market capture as the primary workflow.

Reason:

- Price-comparison sites are current and visual.
- Roman can filter directly for exact requirements.
- Browser/Obsidian capture preserves the real market options.
- Codex can then compare actual candidates instead of guessing from search results.

Workflow:

1. Pick one part category, such as RAM.
2. Filter the market manually on Arukereso, Ceneo, Hotline/E-Katalog, or key retailer sites.
3. Save/export the useful pages into this project folder using the browser/Obsidian extension.
4. Feed the saved market pages or copied tables to Codex.
5. Codex compares exact options, flags risks, and helps choose the best candidate.
6. Repeat for the next part category.

Deep search is secondary:

- Use [[DEEP_SEARCH_PROMPT]] for broader knowledge, missing context, or extra checks.
- Do not rely on deep search as the main price source when manual market captures are available.

Recommended part-by-part order:

1. RAM
2. SSD
3. PSU
4. case and cooling
5. motherboard
6. CPU
7. RTX 5080 watchlist later

For each captured market page, keep:

- date captured
- country/market
- filters used
- exact model names
- price
- seller/shop
- stock/warranty notes if visible
- link if available

Current RAM target:

- 64GB total
- 2x32GB kit
- DDR5-6000
- CL30 preferred
- AMD EXPO preferred
- avoid 4x16GB DDR5
- future upgrade path should be considered, but assume 2-stick stability matters most now

## Budget Logic

The build should be planned in two phases:

1. Build the computer now without the RTX 5080.
2. Buy the RTX 5080 later when price, market, and warranty conditions are good.

Budget cases:

- If the first-stage budget is around HUF 700,000, prioritize value and platform quality.
- If the first-stage budget is around HUF 900,000-1,000,000, consider a stronger CPU and better cooling/case choices.
- Do not spend GPU money early unless the RTX 5080 deal is clearly excellent.

Current baseline totals after 2026-06-13 large capture pass:

- Money-safe first-stage desktop without RTX 5080: about **641,100-641,400 HUF**.
- Same build with later MSI RTX 5080 Ventus 3X OC from x-kom Poland: about **1,048,000-1,048,400 HUF**.
- 32GB budget RAM branch with Patriot Viper Venom 32GB 2x16 DDR5-6000 CL30 Poland: about **529,000 HUF** without GPU.

Baseline parts behind those totals:

- CPU: Ryzen 9 9900X Box, Hungary, about 123,750-124,050 HUF.
- Motherboard: MSI MAG B850 Tomahawk MAX WiFi, Hungary, 82,340 HUF.
- RAM: Patriot Viper Venom 64GB 2x32 DDR5-6000 CL30, Poland, 2,941.98 PLN / about 244,390 HUF.
- SSD: Kingston KC3000 2TB, Poland, 939 PLN / about 78,003 HUF.
- PSU: be quiet! Pure Power 13 M 1000W, Hungary, 49,100 HUF.
- Cooler: ARCTIC Liquid Freezer III Pro 360 A-RGB black, Hungary, about 31,500 HUF.
- Case: Corsair 3500X ARGB Black, Hungary/local, about 31,990 HUF.
- Later GPU: MSI RTX 5080 Ventus 3X OC from x-kom Poland, 4,899 PLN / about 406,960 HUF.

32GB branch logic:

- Patriot 32GB Poland at 1,589.90 PLN saves about **125,700 HUF** versus Patriot 64GB Poland.
- It is useful for the Excel as a budget branch.
- It is not the preferred build for Roman's SQL/database/productivity use.

Priority order before GPU:

1. Good AM5 motherboard
2. 64 GB DDR5 RAM if price is reasonable
3. 2 TB Gen4 SSD
4. Future-ready ATX 3.1 / PCIe 5.1 PSU
5. Airflow case with space for a large RTX 5080
6. Sensible CPU cooler
7. CPU upgrade only after the platform basics are strong

## CPU Decision Logic

Options to compare in Hungary, Poland, and Ukraine:

- Ryzen 7 9700X
- Ryzen 9 9900X
- Ryzen 7 9800X3D
- Ryzen 9 9900X3D
- Ryzen 9 9950X3D only if price is surprisingly good

Working logic:

- Ryzen 7 9700X = best value platform choice.
- Ryzen 9 9900X = better work, multitasking, VM, database, and productivity upgrade.
- Ryzen 7 9800X3D = gaming-first choice; not automatically best for SQL/database/finance work.
- Ryzen 9 9900X3D = best balanced upgrade if budget allows and price gap is reasonable.
- Ryzen 9 9950X3D = no-compromise option, probably overkill unless the total budget is very comfortable.

Current leaning:

- Current CPU target after 2026-06-12 captures: Ryzen 9 9900X Box.
- Captured prices: Poland / Ceneo around 1,349 PLN; Hungary / Arukereso around 124,050 HUF.
- 2026-06-13 seller check: Hungary is the cleaner CPU-buy route because price is similar or better and warranty/returns are simpler. Good Hungary leads include landcomputer.hu 124,050 HUF + 2,100 shipping, younit.hu 124,100 HUF, firstshop.hu 124,620 HUF, and Alza 126,290 HUF + 1,390 shipping.
- Poland only makes sense for CPU if bundling with other Polish parts, especially x-kom at 1,349 PLN with free shipping. Other good Polish stores around 1,399 PLN are fine but not clearly better than Hungary.
- Ryzen 7 9700X remains the value fallback: Hungary Box around 103,490 HUF, Tray around 84,888 HUF.
- Ryzen 9 9900X3D is too expensive for a mostly non-gaming build at captured prices: Poland around 2,039.99 PLN Box, Hungary around 189,900 HUF Box.
- Ryzen 9 9950X is the only serious productivity upgrade above 9900X, but only if budget/cooling/seller warranty are comfortable: Hungary Tray around 159,480 HUF, Box around 174,090 HUF; Poland Tray around 1,890.47 PLN, Box around 1,948 PLN.
- Ryzen 9 9950X3D is watch/no-compromise only, not value: Hungary around 216,700-221,840 HUF, Poland around 2,549-2,564.49 PLN.
- Final CPU decision should use seller-level pages for 9900X in Hungary and Poland, not more broad pages.

## Case And Cooling Logic

Roman likes a black, visible-inside, "Batman" style case.

Current case style preference:

- black case
- glass/panoramic side or front
- visible internals
- clean but aggressive look
- good airflow for a future RTX 5080

Known candidate:

- Corsair 3500X RS-R ARGB

Reason it is attractive:

- black glass/panoramic look
- includes three pre-installed reverse ARGB fans
- supports large graphics cards
- supports 360mm radiator layouts
- visually fits Roman's preferred style

Cooling rules:

- Do not assume included case fans are enough for a future RTX 5080.
- Prefer at least three intake fans and one rear exhaust fan.
- If using a 360mm AIO, verify radiator position, fan thickness, and GPU clearance.
- For Ryzen 7 9700X, a 360mm AIO is not required; it is mostly for noise/aesthetics/future CPU headroom.
- For Ryzen 9 or X3D CPUs, better cooling becomes more reasonable.

Case research should compare:

- Corsair 3500X RS-R ARGB
- Corsair 4000D / Frame 4000D-style airflow options if available at good price
- NZXT H5 Flow RGB 2024, but only if cooler/GPU clearance is clean
- Fractal, Lian Li, Montech, Phanteks, DeepCool, and be quiet! alternatives if they fit the style and airflow requirements

Case must support:

- ATX motherboard
- large RTX 5080 card, ideally 360mm+ clearance
- future-ready PSU
- good cable management
- enough fan mounts for GPU airflow
- black/glass aesthetic preference

## PSU Logic

Target:

- 1000W ATX 3.1 / PCIe 5.1 if price gap is reasonable.
- High-quality 850W ATX 3.1 only if the budget is tight and the model is trusted.

Required:

- native 12V-2x6 / PCIe 5.1 connector for RTX 5080
- reputable platform/reviews
- enough cable length for chosen case
- good warranty

Brands/models should be chosen by market price and quality, not by brand loyalty.

## Market Research Scope

Countries to compare:

- Hungary
- Poland
- Ukraine

Main research tools and shops:

Hungary:

- Arukereso.hu
- Argep.hu
- iPon
- PCX
- Alza Hungary
- Aqua
- HardverApro for second-hand or special deals, especially GPU

Poland:

- Ceneo
- x-kom
- Morele
- Komputronik
- Proline
- Media Expert
- Allegro, only if seller/warranty risk is clearly assessed

Ukraine:

- Rozetka
- Hotline
- E-Katalog / catalog-style price comparison
- Telemart / Brain / other reputable computer shops if available

For every part, compare:

- local price
- converted HUF price
- warranty
- stock status
- seller trust
- delivery route
- return risk
- whether Roman can realistically receive it through Hungary, Poland, or Ukraine

## Deep Search Brief

The reusable market-research prompt is in [[DEEP_SEARCH_PROMPT]].

Use it as a secondary research tool, not the main price source.

It is intentionally flexible:

- It allows exact prices or ranges.
- It asks for confidence levels.
- It allows `not found` or `needs manual check` when data is blocked or unclear.
- It does not force every table to be perfect before giving useful conclusions.
- It includes hard constraints and stop conditions to prevent bad recommendations.

## Imported Research Packs

### `03_Research_Notes/99_Imported_Research/deepseek_markdown_20260611_5b44b7.md`

Status: imported, useful, not fully verified.

Use as:

- first-pass market map
- candidate list
- source leads for manual checking
- ideas for value and premium platform builds

Do not use as final truth yet because:

- many table rows do not include direct source links
- some prices need fresh verification
- some claims are too confident for the visible evidence
- a few model names/spec claims may be mixed up and need checking before purchase

Important leads from the file:

- Value-platform idea: Ryzen 7 9700X, MSI B650 Tomahawk WiFi, 64GB DDR5-6000 CL30, 2TB Gen4 SSD, 1000W ATX 3.1 PSU, Corsair 3500X-style case.
- Premium-platform idea: Ryzen 9 9900X or 9900X3D, MSI B850 Tomahawk MAX WiFi, 64GB DDR5-6000 CL30, 2TB Gen4 SSD, stronger case/cooling.
- Watch/verify: Seasonic Focus GX-1000 2024, be quiet! 1000W alternatives, Corsair 3500X, Montech King 95 Pro, Thermalright/Arctic cooler options.
- Verify carefully: RAM prices, RTX 5080 prices, seller reputation, exact PSU model warnings, and case/cooler/GPU clearance.

## Verification Pass 1 - 2026-06-12

Purpose: first surgical check of the imported research pack across Hungary, Poland, and Ukraine.

Status: partial verification only. Use this as direction for the next deeper search, not as a final shopping list.

### Key Corrections

- Do not treat budget numbers as thresholds. The goal is the cheapest trusted option, not forcing the build into a preset number.
- The researcher should map options and evidence, not make the final decision.
- Hungary, Poland, and Ukraine all need to be checked, but not every category will be equally useful in every country.
- GPU buying should remain watchlist-first. RTX 5080 prices still need careful seller/warranty checking.
- RAM pricing is a major uncertainty and may change the whole 32GB vs 64GB timing decision.
- PSU model names must be checked carefully. Do not mix MSI MPG A1000G PCIE5 with MSI MAG A1000GL PCIE5.

### Early Market Signals

- CPU: Poland may be strong for Ryzen 9 9900X and Ryzen 7 9700X, but Ukraine also shows surprisingly competitive 9900X ranges that require warranty/logistics checking.
- Motherboard: B650 Tomahawk remains a strong value option; B850 Tomahawk MAX WiFi is the stronger future-looking option but price varies by country and seller.
- Motherboard 2026-06-13 captured-market update: best practical lead is MSI MAG B850 Tomahawk MAX WiFi in Hungary at 82,340 HUF. Strong value challenger is ASRock X870 PRO RS WiFi in Hungary at 72,290 HUF, but verify exact specs/comfort with ASRock. Poland has MSI MAG B850 Tomahawk WiFi at 841.78 PLN, but verify MAX vs non-MAX and it is not clearly better after logistics. X870/X870E premium only if price/features justify it.
- RAM: 64GB DDR5-6000 CL30/EXPO is technically right, but prices look very inflated. This needs the next pass.
- SSD: Kingston KC3000 2TB is the baseline. Captured Poland price is 939 PLN and better than proper Lexar NM790 at 1,027.12 PLN. Captured Hungary value is Lexar NM790 96,695 HUF; safer Hungary choices are Kingston FURY Renegade 103,460 HUF or Kingston KC3000 106,336 HUF. Samsung 990 PRO / WD SN850X are premium only if close in price. Avoid QLC as the main database/work drive.
- PSU: 2026-06-13 captured-market update: be quiet! Pure Power 13 M 1000W in Hungary at 49,100 HUF is the current value lead; Seasonic Focus GX-1000 2024 in Hungary at 59,990 HUF is the safest clean lead; Corsair RM1000x ATX 3.1 is strong but pricier. Poland is not clearly better for PSU after logistics unless bundling.
- Case/cooling: 2026-06-13 updated broad captures: ARCTIC Liquid Freezer III Pro 360 A-RGB black is around 31,500 HUF in Hungary; non-RGB black is around 29,200 HUF. Corsair 3500X ARGB Black is around 31,990 HUF in Hungary, with plain 3500X Black around 21,326 HUF. Because the case is large/glass, use Hungary/local for case even if Poland sometimes looks cheaper on paper.
- Case: Corsair 3500X remains the style baseline. Montech King 95 Pro and similar black glass airflow cases should be compared with included fans counted.
- GPU: Hungarian RTX 5080 listings around the low-to-mid HUF 500k range are plausible. Polish and Ukrainian listings do not automatically beat Hungary after warranty/logistics risk.

### Current Best Money-Safe Build - 2026-06-13

This is the current practical build to use for planning. It saves money where Poland clearly helps, but keeps heavy, fragile, or local-warranty-sensitive parts in Hungary.

Rough planning conversion used: 1 PLN = 93 HUF. This is not a final checkout list.

| Part | Current best money-safe pick | Market plan | Captured estimate | Why |
|---|---|---|---:|---|
| CPU | AMD Ryzen 9 9900X Box | Hungary | 123,750-124,050 HUF | Poland does not clearly save; local warranty is cleaner. |
| Motherboard | MSI MAG B850 Tomahawk MAX WiFi | Hungary | 82,340 HUF | Strong default board; Poland saving is small and may be non-MAX. |
| RAM | Patriot Viper Venom 64GB 2x32 DDR5-6000 CL30 | Poland | 2,941.98 PLN / ~244,390 HUF | Biggest first-stage Poland saving; verify exact SKU and seller. |
| SSD | Kingston KC3000 2TB | Poland | 939 PLN / ~78,003 HUF | Strong Gen4 TLC/DRAM drive; real Poland saving. |
| PSU | be quiet! Pure Power 13 M 1000W | Hungary | 49,100 HUF | Best captured 1000W value; verify exact ATX 3.1 / 12V-2x6. |
| Cooler | ARCTIC Liquid Freezer III Pro 360 A-RGB black | Hungary | 31,500 HUF | Current Hungary visual/value lead. |
| Case | Corsair 3500X ARGB Black | Hungary/local | 31,990 HUF | Do not ship a large glass case through Poland unless a very easy route appears. |
| Later GPU | MSI RTX 5080 Ventus 3X OC | Poland / x-kom | 4,899 PLN / ~406,960 HUF | Best captured MSI price lead; direct x-kom page captured. |

Current estimated totals:

- First-stage PC without GPU: about 641,100-641,400 HUF.
- Full build with later MSI RTX 5080 Ventus: about 1,048,000-1,048,400 HUF.
- Compared with all-Hungary equivalents using the same/similar money-safe choices, Poland saves about 72,626 HUF before GPU and about 116,109 HUF with the MSI Ventus GPU.

Main caveats:

- If Patriot RAM seller/spec is unclear, switch to Kingston Fury Beast EXPO; the first-stage total becomes about 746k HUF with the current clean Hungary Kingston capture.
- If GPU choice changes from MSI Ventus Poland to a pricier MSI/Gigabyte tier, the GPU saving may shrink or disappear.
- Do not buy Gigabyte GPU in Poland just because it is Poland; captured Gigabyte Gaming OC is better in Hungary.
- Case stays local unless Roman finds a very simple and safe transport route.

### Build Cost Snapshot - Kingston/MSI Scenario - 2026-06-13

Rough planning conversion used: 1 PLN = 93 HUF. This is not a final checkout list.

Chosen baseline for this snapshot:

- CPU: Ryzen 9 9900X Box.
- Motherboard: MSI MAG B850 Tomahawk MAX/WiFi class.
- RAM: Kingston Fury Beast EXPO 64GB 2x32 DDR5-6000 CL30.
- SSD: Kingston KC3000 2TB.
- PSU: be quiet! Pure Power 13 M 1000W, because MSI MPG A1000G is avoided and MSI MAG A1000GL still needs exact spec confirmation.
- Cooler: ARCTIC Liquid Freezer III Pro 360 A-RGB black.
- Case: Corsair 3500X ARGB Black local/Hungary; Poland case shipping is not attractive because it is large/glass.
- Later GPU: MSI RTX 5080 Ventus 3X OC as the best captured MSI price/value lead.

Read:

- First-stage PC without GPU saves only about 19,000 HUF by using Poland, mainly from the Kingston KC3000 SSD.
- Full build including later RTX 5080 saves about 62,000 HUF by using Poland for SSD and GPU.
- With Kingston RAM, Poland RAM does not really save money. The big RAM saving was Patriot, not Kingston.
- Motherboard Poland saving is small and may be non-MAX vs MAX, so Hungary remains cleaner.
- CPU, PSU, cooler, and case currently look better or simpler from Hungary.

Current practical plan:

| Part | Current value pick | Hungary estimate | Poland estimate | Current buy plan |
|---|---|---:|---:|---|
| CPU | Ryzen 9 9900X Box | 124,050 HUF | 1,349 PLN / ~125,457 HUF | Hungary |
| Motherboard | MSI MAG B850 Tomahawk MAX/WiFi | 82,340 HUF | 841.78 PLN / ~78,286 HUF | Hungary unless exact Polish MAX is much cheaper |
| RAM | Kingston Fury Beast EXPO 64GB 6000 CL30 | 339,890 HUF clean seller | 3,635.50 PLN / ~338,102 HUF | Hungary/Poland neutral; not worth Poland for Kingston alone |
| SSD | Kingston KC3000 2TB | 106,336 HUF | 939 PLN / ~78,003 HUF | Poland if bundling |
| PSU | be quiet! Pure Power 13 M 1000W | 49,100 HUF | not better from captures | Hungary |
| Cooler | ARCTIC Liquid Freezer III Pro 360 A-RGB black | 31,500 HUF | 324 PLN / ~30,132 HUF for non-RGB Poland | Hungary; A-RGB local is cleaner |
| Case | Corsair 3500X ARGB Black | 31,990 HUF | Poland not preferred because case logistics are bad | Hungary/local |
| Later GPU | MSI RTX 5080 Ventus 3X OC | 499,090 HUF | 4,899 PLN / ~406,960 HUF | Poland if seller/warranty is clean |

Approximate totals:

- All-Hungary-style baseline with later GPU: about 1,264,296 HUF.
- Smart Poland-only-where-worth-it baseline with later GPU: about 1,143,833 HUF.
- Estimated saving with Poland: about 120,463 HUF.
- First-stage PC without GPU, keeping case local: about 28,333 HUF saving only.

### Build Cost Snapshot - Poland Savings Scenario - 2026-06-13

This version uses the parts where Poland actually has a meaningful captured advantage, instead of forcing Kingston/MSI everywhere.

Assumptions:

- RAM switches from Kingston to Patriot Viper Venom 64GB 2x32 DDR5-6000 CL30.
- SSD stays Kingston KC3000 2TB.
- Case stays local because it is big/glass and not worth Poland logistics.
- GPU comparison uses MSI RTX 5080 Ventus 3X OC as the Poland value lead.

First-stage PC without GPU:

| Part | Hungary baseline | Smart Poland/local plan | Saving |
|---|---:|---:|---:|
| CPU Ryzen 9 9900X Box | 124,050 HUF | 124,050 HUF / Hungary | 0 |
| MSI B850 Tomahawk MAX/WiFi | 82,340 HUF | 82,340 HUF / Hungary | 0 |
| Patriot Viper Venom 64GB CL30 | 327,290 HUF | 2,941.98 PLN / ~244,390 HUF / Poland | ~82,900 HUF |
| Kingston KC3000 2TB | 106,336 HUF | 939 PLN / ~78,003 HUF / Poland | ~28,333 HUF |
| be quiet! Pure Power 13 M 1000W | 49,100 HUF | 49,100 HUF / Hungary | 0 |
| ARCTIC LF III Pro 360 A-RGB | 31,500 HUF | 31,500 HUF / Hungary | 0 |
| Corsair 3500X ARGB Black | 31,990 HUF | 31,990 HUF / Hungary | 0 |

Totals:

- Hungary baseline without GPU: about 752,606 HUF.
- Smart Poland/local without GPU: about 641,100-641,400 HUF.
- First-stage saving: about 111,200 HUF.

With later GPU:

| GPU comparison | Hungary GPU | Poland GPU | Total saving versus that Hungary path |
|---|---:|---:|---:|
| Same MSI Ventus model | 499,090 HUF | 4,899 PLN / ~406,960 HUF | ~203,363 HUF |
| Best cheap Hungary value Inno3D vs Poland MSI Ventus | 465,640 HUF | ~406,960 HUF | ~169,913 HUF |
| Gainward Phoenix Hungary vs Poland MSI Ventus | 474,420 HUF | ~406,960 HUF | ~178,693 HUF |
| Premium Hungary Gigabyte Gaming OC vs Poland MSI Gaming Trio | 526,400 HUF | 5,599 PLN / ~465,120 HUF | ~172,513 HUF |
| Exact Gigabyte Gaming OC Hungary vs Poland | 526,400 HUF | 5,799 PLN / ~481,734 HUF | ~155,899 HUF total saving; Poland also looks cheaper at this rate, but exact seller/warranty still decides |

Read:

- Poland can save around 70k HUF before GPU if RAM is Patriot and SSD is KC3000.
- With the later GPU, total saving can cross 100k HUF only if the Poland GPU is the cheaper MSI Ventus path and the Hungary comparison is the same MSI model.
- If choosing a more expensive Gigabyte/MSI premium GPU in Poland, the GPU saving almost disappears or can become negative.
- Do not buy Gigabyte in Poland just because it is Poland; captured Gigabyte Gaming OC is cheaper in Hungary than Poland.

### Next Search Focus

1. CPU table: 9700X, 9900X, 9800X3D, 9900X3D, 9950X3D across all three countries.
2. RAM table: 64GB 2x32 DDR5-6000 CL30/CL32 EXPO only, plus a fallback 32GB timing option.
3. PSU table: exact 1000W ATX 3.1 / PCIe 5.1 models, with no model-name confusion.
4. GPU watchlist: RTX 5080 only, with seller trust and warranty risk.

## RAM Research Questions

1. Is 32 GB enough, or is 64 GB worth it for database, SQL, finance, productivity, and light gaming?
2. What DDR5 speed and latency make sense for Ryzen 7 9700X?
3. Which RAM kits have stable AMD EXPO support?
4. Which options are best value in Hungary?

For each RAM candidate, capture:

- brand and model
- capacity and kit format, such as 2x16 GB or 2x32 GB
- DDR5 speed and CAS latency
- EXPO/XMP support
- price in HUF
- retailer/source
- date checked
- link, if available

## Folder Map

### `00_Hub`

Inbox for new captures from Obsidian/browser.

Keep this folder mostly empty. After a page is analyzed, move it into `03_Research_Notes/01_Raw_Captures/<part category>/`.

### `01_Market_Data`

Market data files such as scraped/exported prices, retailer comparisons, product availability, and historical price snapshots.

Recommended CSV pattern:

- `YYYY-MM-DD_hungary_pc_parts_prices.csv`
- `YYYY-MM-DD_gpu_market_snapshot.csv`
- `YYYY-MM-DD_cpu_market_snapshot.csv`

### `02_PC_Builds`

Roman's own PC build files.

Save the PC build CSV here.

Current prep note:

- [[02_PC_Builds/BUILD_OPTIONS_CSV_PREP]]

Recommended CSV pattern:

- `YYYY-MM-DD_pc_build.csv`
- `YYYY-MM-DD_pc_build_budget_version.csv`
- `YYYY-MM-DD_pc_build_final_candidate.csv`

### `03_Research_Notes`

Research folder.

Current structure:

- `00_Working_Shortlists/`: clean decision notes. Open these first when researching a part.
- `01_Raw_Captures/CPU/`: raw CPU market captures.
- `01_Raw_Captures/GPU/`: raw RTX 5080 market captures.
- `01_Raw_Captures/Motherboard/`: raw motherboard market captures.
- `01_Raw_Captures/PSU/`: raw PSU market captures.
- `01_Raw_Captures/RAM/`: raw RAM market captures.
- `01_Raw_Captures/SSD/`: raw SSD market captures.
- `01_Raw_Captures/MacBook_Comparison/`: MacBook comparison captures for the Dad/Excel comparison.
- `99_Imported_Research/`: imported external/deep-search notes. Useful for leads, not final truth.

Current working shortlists:

- [[03_Research_Notes/00_Working_Shortlists/CASE_COOLING_WORKING_SHORTLIST]]
- [[03_Research_Notes/00_Working_Shortlists/CPU_WORKING_SHORTLIST]]
- [[03_Research_Notes/00_Working_Shortlists/MOTHERBOARD_WORKING_SHORTLIST]]
- [[03_Research_Notes/00_Working_Shortlists/PSU_WORKING_SHORTLIST]]
- [[03_Research_Notes/00_Working_Shortlists/RAM_WORKING_SHORTLIST]]
- [[03_Research_Notes/00_Working_Shortlists/RTX5080_WORKING_SHORTLIST]]
- [[03_Research_Notes/00_Working_Shortlists/SSD_WORKING_SHORTLIST]]

### `99_Archive`

Old build versions, outdated market snapshots, and superseded notes.

## Rules

- Keep normal project memory in this README.
- Use [[DEEP_SEARCH_PROMPT]] only as the reusable research prompt.
- Keep raw market data separate from final build decisions.
- For price claims, keep the date, currency, retailer/source, product name, and link if available.
- Archive old CSVs instead of overwriting them when the build changes meaningfully.
- This belongs in `06_Personal/Personal_Projects`, because it supports Roman's own PC build and purchase decision.
