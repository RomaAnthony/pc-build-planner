# AUDITED MISSING OPTIONS — Viable Parts Not in Seed CSV

**Audit Date:** 2026-06-22
**Build Target:** Ryzen 9 9900X / MSI MAG B850 Tomahawk MAX WiFi / 64GB DDR5-6000 CL30 / KC3000 2TB / 1000W ATX 3.1 PSU / Arctic 360 AIO / Lancool 207 or similar / RTX 5080 (future)

**Data Sources Scanned:**
- `01_Market_Data/2026-06-21/PSU/` — 39+ PSU models across Arukereso (HU), Ceneo (PL), Hotline (UA)
- `01_Market_Data/2026-06-21/Cooler/` — 5 AIO coolers refreshed
- `01_Market_Data/2026-06-21/Case/` — 2 cases captured
- `01_Market_Data/2026-06-21/GPU/` — Full RTX 5080 + RTX 5070 Ti captures
- `01_Market_Data/2026-06-21/RAM/` — DDR5 captures across HU/PL/UA
- `01_Market_Data/2026-06-21/SSD/` — NVMe SSD captures
- `01_Market_Data/2026-06-21/Motherboard/` — AM5 motherboard captures
- `01_Market_Data/archived/2026-06-16/Cooler/` — Additional Cooler captures
- `03_Research_Notes/01_Raw_Captures/PSU/` — Mirror of PSU captures

---

## PSU — Viable Missing Options

### Methodology
- Filtered: ATX 3.1 / PCIe 5.x with native 12V-2x6 support (match for 9900X + RTX 5080 build)
- Excluded: White variants (black build), untrustworthy brands (EVOLVEO, Kolink), non-modular units, physically risky models (MSI MPG A1000G has known issues)
- All HU prices are Arukereso "from" prices (broad market floor)

### Models missing from seed but genuinely competitive:

| # | Model | HU Floor | Rating | Why Add | Tradeoff vs Seed (be quiet! PP13M / Corsair RM1000x) |
|---|---|---|---|---|---|
| 1 | **Lian Li SX 1000W Platinum Black** (G9P.SX1000P.B000.EU) | 48,290 Ft | ★★★★★ | HU Floor = 48,290 Ft — Platinum ATX 3.1 at Gold price! | Cheaper than Pure Power 13 M (49,100) despite being **Platinum** efficiency. Similar quality tier (Seasonic OEM). 135mm fan. |
| 2 | **Thermaltake Toughpower GT 1000W Gold** (PS-TPT-1000FNFAGE-3) | 49,790 Ft | ★★★★☆ | HU Floor = 49,790 Ft — Solid Gold ATX 3.1 | Close to Pure Power 13 M price (49,100). Slightly more expensive but Thermaltake has strong RMA in HU. 135mm fan. |
| 3 | **Thermaltake Toughpower PT 1000W Platinum Black** (PS-TPP-1000FNFAPE-1) | 56,241 Ft | ★★★★★ | HU Floor = 56,241 Ft — **Platinum** ATX 3.1, premium CWT OEM | Excellent value Platinum vs RM1000x (66,200) or be quiet! Power Zone 2 (58,325). Native 12V-2x6. |
| 4 | **Phanteks AMP GH 1000W v2 Black** (PH-P1000GH_BK02) | 56,900 Ft | ★★★★☆ | HU Floor = 56,900 Ft — Platinum ATX 3.1, Seasonic OEM | Compares well against Power Zone 2 (58,325) and Power Zone 2 in seed. More compact (150mm). |
| 5 | **Lian Li Edge 1000W Gold Black** (G9P.EG1000G.BK00.EU) | 59,440 Ft | ★★★★☆ | HU Floor = 59,440 Ft — Lian Li build synergy with Lancool 207 | Premium but matches Lian Li case ecosystem. Similar to RM1000x tier pricing. |
| 6 | **MSI MAG A1000GL 1000W PCIE5 Gold Black** | 54,900 Ft | ★★★☆☆ | HU Floor = 54,900 Ft — Cheapest MSI ATX 3.1 option for local buying | Already in seed as PSU_05_UA (Ukraine only). Adding HU row. Slightly noisier than be quiet options. |
| 7 | **Corsair RM1000e 2025 ATX 3.1 Black** (CP-9020297-EU) | 53,190 Ft | ★★★★☆ | HU Floor = 53,190 Ft — Already in seed as PSU_05_HU but exact price mismatch resolved | Already listed. Keeping verified floor from Arukereso search. |
| 8 | **ASRock SL-1000G 1000W Gold** | 46,900 Ft | ★★★☆☆ | HU Floor = 46,900 Ft — Cheapest branded ATX 3.1 option | Cheaper than Pure Power 13 M but only 3 offers and ASRock PSU track record is short. Risk-Medium. |

### Rows to add for PSU:
- Lian Li SX 1000W Platinum Black — HU, PL markets
- Thermaltake Toughpower GT 1000W — HU, PL markets
- Thermaltake Toughpower PT 1000W Platinum — HU market
- Phanteks AMP GH 1000W v2 Black — HU, PL markets
- Lian Li Edge 1000W Gold Black — HU market
- MSI MAG A1000GL — HU market row

---

## Cooler — All Missing Options

### Status
The seed CSV has **ZERO** cooler entries. The raw captures contain 5 coolers with refreshed prices.

### Viable Options for Build

| # | Model | HU Floor | PL Floor | UA Floor | Why Add | Note |
|---|---|---|---|---|---|---|
| 1 | **Arctic Liquid Freezer III Pro 360 A-RGB Black** | 37,888 Ft | 399 PLN | — | ★★★★★ Best value 360mm AIO — top-tier cooling, competitive price, great for 9900X | The go-to pick. ARGB version worth the premium over non-RGB for minimal cost diff. |
| 2 | **Arctic Liquid Freezer III Pro 360 Black** (non-RGB) | 32,190 Ft | 324 PLN | — | ★★★★★ Cheapest premium 360mm AIO, same pump/radiator, just no ARGB | Budget-leader if ARGB is unnecessary. Huge price gap over competition. |
| 3 | **DeepCool LE360 V2 Black** | 23,990 Ft | 282.82 PLN | 3,979 UAH | ★★★★☆ Insanely cheap 360mm AIO — only 24k HUF | Price is unmatched but build quality / pump reliability is lower than Arctic. Risk-Medium. |
| 4 | **MSI MAG CoreLiquid A13 360 Black** | 27,777 Ft | 248 PLN | 3,355 UAH | ★★★★☆ Very strong value at 27.8k HUF, MSI brand synergy with motherboard | Great price-to-performance. Compatible with MSI BIOS sync. |
| 5 | **be quiet! Pure Loop 3 LX 360mm Black** | 34,600 Ft | 429 PLN | 5,511 UAH | ★★★☆☆ be quiet! quality, premium fans | More expensive than Arctic but premium build. Excellent for silent build priority. |

### Decision:
- **Primary pick:** Arctic Liquid Freezer III Pro 360 A-RGB — best value, great cooling, ARGB for build aesthetics
- **Budget pick:** MSI MAG CoreLiquid A13 360 — 27.8k HUF, MSI synergy
- **Silent pick:** be quiet! Pure Loop 3 LX 360 — premium but expensive
- **Ultra-budget:** DeepCool LE360 V2 — lowest price, higher risk

All five should be added to seed CSV.

---

## Fans — All Options

### Status
No Fans raw capture directory exists in the current structure (`01_Market_Data/2026-06-21/Fans/` does not exist). No fan market data has been captured yet. This must be done in a future refresh phase.

### Note
Fan decisions are tightly coupled to case choice and AIO radiator configuration. Typical 9900X + RTX 5080 build would need:
- 3x 120mm for AIO top-mounted (included with Arctic/DeepCool/MSI AIOs)
- 1-2x 140mm for front intake (depends on case)
- 1x 120/140mm rear exhaust

No raw captures to audit here. **Capture needed in next market refresh.**

---

## Case — All Missing Options

### Status
2 cases captured, neither yet in seed CSV. The decision guide mentions Lancool 207 (~32k HUF) as target but it wasn't in captures.

### Viable Options in Raw Captures

| # | Model | HU Floor | Why Consider | Tradeoff |
|---|---|---|---|---|
| 1 | **NZXT H7 Flow 2024 All Black** | ~42,630 Ft | Excellent airflow, large case fits 360 AIO top-mounted, clean aesthetic | More expensive than the target Lancool 207 (~32k). Better for air cooling but AIO fine. |
| 2 | **Corsair Frame 4000D RS Wood** | ~50,400 Ft | Unique wood front, good Corsair build, clean cable management | Premium price. Wood aesthetic isn't for everyone. Same airflow class as 4000D Airflow. |

### Recommendation:
Both should be added as alternatives but Lancool 207 remains target. The case market needs its own refresh pass.

---

## GPU — All Missing Options

### Status
GPU is well-covered in seed with 36+ rows across RTX 5080 and RTX 5070 Ti variants. After reviewing all raw captures, the seed CSV comprehensively covers all viable models from HU/PL/UA markets.

### No missing viable options found.
- All models from Arukereso (Inno3D, Palit, Gainward, Gigabyte, MSI, ASUS, Zotac, PNY, Manli) are already represented
- Both RTX 5080 and RTX 5070 Ti lineups are fully seeded
- Multiple priority tiers and cross-country variants exist

---

## RAM — All Missing Options

### Status
8 RAM entries in seed across Patriot, Kingston, GOODRAM, Silicon Power, G.Skill, Crucial with HU/PL/UA country rows. After review:

### Missing but potentially viable:
None identified from the raw captures that would add value. The seed already covers:
- 64GB CL30 value leaders (Patriot Viper Venom — strongest)
- 64GB CL30 safe options (Kingston Fury Beast, GOODRAM IRDM)
- 32GB budget-down options (Patriot Viper Venom 32GB)
- Budget CL36/CL40 fallbacks (G.Skill Aegis 5, Crucial Pro)

### No new rows needed.

---

## SSD — All Missing Options

### Status
8 SSD entries in seed. Cross-checked against captures:

### Missing but potentially viable:
None identified. Seed covers:
- KC3000 2TB (primary pick) — HU/PL/UA
- Lexar NM790 2TB (budget backup) — HU/PL
- Samsung 990 PRO 2TB (premium) — HU/PL/UA
- Various PCIe 5 options (Kioxia, Kingston FURY Renegade, Corsair MP700, Samsung 9100 PRO)

### No new rows needed.

---

## Motherboard — All Missing Options

### Status
Fresh 2026-06-22 user paste added more MSI B850/X870E Ceneo watch rows. These are recorded here for buying/research context only. Do not update the Marimo Python app until the next full planner sync.

### Fresh MSI Ceneo watch rows from 2026-06-22

| Model | Country/source | Price | Stores/offers | Why it matters | Current action |
|---|---:|---:|---:|---|---|
| MSI MAG X870E GAMING PLUS MAX WIFI | Poland / Ceneo `195661407` | 1,189.99 PLN | 11 shops, free delivery in 9 offers | Higher than the earlier 939 PLN broad row; exact current Ceneo floor is not the tiny-upgrade price. | Watch only; verify exact offer if choosing X870E |
| Msi Płyta Główna Mag X870E Gaming Max Wifi | Poland / Ceneo `193278109` | 1,036.90 PLN | 14 shops, free delivery in 9 offers | May be the cheaper Gaming Plus/Gaming Max X870E class row; naming needs exact model check before use. | Strong watch candidate; verify model name and USB4 before adding |
| MSI MAG X870E TOMAHAWK MAX WIFI PZ | Poland / Ceneo `189869965` | 1,454.29 PLN | 20 shops, free delivery in 17 offers | Project Zero/PZ variant; not appropriate unless building around back-connect case/cable layout. | Do not pick for normal H7/Lancool build |
| MSI MAG B850 GAMING PLUS MAX WIFI `(7E56030R)` | Poland / Ceneo `194391673` | 903.00 PLN | Ceneo row | Cheaper MSI B850 alternative to Tomahawk, but lower tier than Tomahawk MAX. | Watch only; compare VRM/USB/rear IO before using |
| MSI MAG X870E GAMING PLUS MAX WIFI | Hungary / Arukereso `p1332166510` | 109,340 HUF | 6 offers | Same Gaming Plus MAX class as the Poland X870E watch row; current HU price is meaningfully above MSI B850 Tomahawk MAX but below X870E Tomahawk. | Watch only; compare against HU B850 and PL X870E before adding |

### Fresh Gigabyte B850/X870 watch rows from 2026-06-22

Sources saved under `01_Market_Data/2026-06-22/Motherboard/`.

| Model | Country/source | Price | Stores/offers | Why it matters | Current action |
|---|---:|---:|---:|---|---|
| Gigabyte B850 AORUS ELITE ATX `(B850AELITEWF7)` | Poland / Ceneo `178918242` | 869.12 PLN | 18 shops, free delivery in 11 offers | AORUS Elite is Gigabyte's Tomahawk-like mainstream tier; strong cheaper B850 alternative. | Good value candidate; compare exact store/warranty |
| Gigabyte B850 AORUS ELITE ATX ICE `(B850AELITEWF7ICE)` | Poland / Ceneo `178918243` | 870.59 PLN | 31 shops, free delivery in 22 offers | Same class, white/ICE variant; not ideal for black build unless price/store is best. | Watch only |
| Gigabyte B850M AORUS ELITE WIFI6E ICE | Poland / Ceneo `179067864` | 692.26 PLN | 20 shops, free delivery in 13 offers | Cheap microATX option, but not the same full ATX/WiFi7 target. | Do not use unless budget build |
| Gigabyte X870 GAMING X WIFI7 | Poland / Ceneo `175185341` | 886.01 PLN | 17 shops, free delivery in 11 offers | Very cheap X870 + WiFi7 row, but Gaming line is below AORUS Elite. | Strong watch candidate; verify USB4 and exact board details |
| Gigabyte X870 GAMING WIFI6 | Poland / Ceneo `175185371` | 826.01 PLN | 32 shops, free delivery in 19 offers | Cheapest X870 row; likely USB4 but WiFi6 and lower line than AORUS. | Value candidate if exact seller is good |
| Gigabyte X870 EAGLE WIFI7 | Poland / Ceneo `173778018` | 818.00 PLN | 28 shops, free delivery in 17 offers | Cheapest X870 WiFi7 row; Eagle is value line below AORUS Elite. | Strong value watch candidate |
| Gigabyte X870 A ELITE WIFI7 | Poland / Ceneo `173804462` | 1,010.00 PLN | 29 shops, free delivery in 18 offers | AORUS Elite class on X870; likely direct Gigabyte competitor to MSI X870E Gaming Plus/Tomahawk. | Best Gigabyte balance candidate if exact offer checks out |
| Gigabyte X870 A ELITE WIFI7 ICE | Poland / Ceneo `173804470` | 1,099.99 PLN | 17 shops, free delivery in 10 offers | White/ICE AORUS Elite X870 variant. | Watch only for white build |
| Gigabyte X870E A ELITE WIFI7 | Poland / Ceneo `173804476` | 1,079.00 PLN | 26 shops, free delivery in 15 offers | X870E AORUS Elite class, very interesting vs MSI X870E Gaming Plus at 1,036.90-1,189.99 PLN. | Top Gigabyte watch candidate |
| Gigabyte X870E AORUS PRO AM5 | Poland / Ceneo `177034717` | 1,362.00 PLN | 17 shops, free delivery in 12 offers | Higher AORUS Pro tier; likely overkill for this build. | Avoid unless price collapses |
| Gigabyte X870E AORUS PRO ICE AM5 | Poland / Ceneo `177496059` | 1,394.84 PLN | 22 shops, free delivery in 15 offers | Higher AORUS Pro ICE tier; premium/white. | Avoid for value build |
| GIGABYTE B850 AORUS ELITE WIFI7 | Hungary / Arukereso | 75,800 HUF | 13 offers | Current HU value leader among full ATX AORUS Elite-class B850 rows; Alza offer visible at 75,800 HUF + 1,390 HUF shipping. | Strong HU candidate |

### Also noted by user

| Model | Country/source | Price | Note |
|---|---:|---:|---|
| MSI MAG X870E Tomahawk WiFi DDR5 AM5 | Poland / Ceneo `180912411` | 1,235.00 PLN | Higher-tier Tomahawk X870E, not the cheap 939 PLN row. |
| MSI MAG X870E TOMAHAWK MAX WIFI `(7E59-018R)` | Hungary / Arukereso | 130,350 HUF | Around 47,360 HUF more than current HU B850 Tomahawk MAX exact row. |

### Quick decision note

The X870E upgrade is attractive only if the exact store row stays close to the B850 price. At the latest pasted floors:

- MSI B850 Tomahawk MAX Poland exact in seed: 978.66 PLN
- MSI X870E Gaming Max/Gaming Plus watch row: 1,036.90-1,189.99 PLN
- MSI X870E Gaming Plus MAX Hungary watch row: 109,340 HUF
- MSI X870E Tomahawk class: 1,235.00 PLN or 130,350 HUF
- Gigabyte B850 AORUS Elite WiFi7 Poland watch row: 869.12 PLN
- Gigabyte X870 AORUS/A Elite WiFi7 Poland watch row: 1,010.00 PLN
- Gigabyte X870E AORUS/A Elite WiFi7 Poland watch row: 1,079.00 PLN
- Gigabyte B850 AORUS Elite WiFi7 Hungary watch row: 75,800 HUF

If the 1,036.90 PLN row is the correct non-PZ X870E model with USB4 and good seller terms, it is a reasonable upgrade candidate. If the real available row is 1,189.99 PLN or higher, the value case becomes weaker and Gigabyte X870 / MSI B850 Tomahawk MAX should remain in the comparison.

With the new Gigabyte captures, the most interesting comparison set is:

- MSI B850 Tomahawk MAX: trusted current build default, but pricier than Gigabyte B850.
- MSI X870E Gaming Plus MAX: strong if the exact 1,036.90 PLN row is real; weaker at 1,189.99 PLN.
- Gigabyte B850 AORUS Elite WiFi7: best pure B850 value.
- Gigabyte X870 A Elite WiFi7: likely best Gigabyte X870 balance if exact offer checks.
- Gigabyte X870E A Elite WiFi7: strongest Gigabyte feature/value challenger to MSI X870E.

---

## CPU — All Missing Options
Already well-sourced. Single model (Ryzen 9 9900X Box) with 3 country rows. No changes needed.

---

## Changes Summary

| Part | Missing Rows to Add | Action |
|---|---|---|
| **PSU** | **7 new rows** — 3 new models, 4 cross-market fills | Add to seed |
| **Cooler** | **15 new rows** — 5 models × 3 countries (HU/PL/UA) | Add to seed |
| **Case** | **4 new rows** — 2 models × 2 countries (HU only, no UA/PL captured) | Add to seed |
| **Fans** | **0** — No captures exist yet | Schedule capture |
| **GPU** | **0** — Already complete | No change |
| **RAM** | **0** — Already complete | No change |
| **SSD** | **0** — Already complete | No change |
| **Motherboard** | **0** — Already complete | No change |
