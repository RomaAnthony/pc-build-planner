# Build Options CSV Prep

Updated: 2026-06-14

Purpose:
- Prepare the future CSV/Excel build table.
- Show Dad that the first-stage desktop without RTX 5080 is in the same price zone as a MacBook Pro.
- Keep 3-4 practical options per part, but do not create the final CSV yet.

Clean Dad-facing note:
- `DAD_PC_BUILD_SUMMARY.md`

## Exchange Rates For The Future Spreadsheet

Use one small exchange-rate table in the workbook and reference it from every option row. Do not hardcode conversions inside each row.

Official reference rates captured 2026-06-14:

| Source | Rate date | Pair / source quote | Derived spreadsheet rate |
|---|---|---:|---:|
| ECB euro reference rates | 2026-06-12 | 1 EUR = 352.88 HUF | 1 EUR = 352.88 HUF |
| ECB euro reference rates | 2026-06-12 | 1 EUR = 4.2480 PLN | 1 PLN = 83.07 HUF |
| NBU exchange rates | 2026-06-15 | 1 HUF = 0.147019 UAH | 1 UAH = 6.80 HUF |
| NBU exchange rates | 2026-06-15 | 1 EUR = 51.8592 UAH | 1 EUR = 51.8592 UAH |
| NBU exchange rates | 2026-06-15 | 1 PLN = 12.2107 UAH | 1 PLN = 12.2107 UAH |

Planning formulas:
- `HUF_from_PLN = PLN_price * 83.07`
- `HUF_from_EUR = EUR_price * 352.88`
- `HUF_from_UAH = UAH_price * 6.80`
- `UAH_from_HUF = HUF_price / 6.80`
- `EUR_from_HUF = HUF_price / 352.88`

These are planning rates only. Recheck exchange rates before final purchase and before showing Dad a final number.

## Simple Excel Shape

For Roman alone, 3 sheets is enough. For showing Dad, use **4 sheets**:

1. `Dashboard`
2. `Builds`
3. `Parts`
4. `Rates`

This keeps the workbook simple but makes it presentable.

## Dad Presentation Workbook Logic

The file should not look like a random PC-parts spreadsheet.

It should answer four questions:
1. What are we buying first?
2. Why does Poland save money?
3. What are the cheaper/safer alternatives?
4. Why is this useful for Roman's future, not only gaming?

### Sheet 1 - `Dashboard`

This is the page to show Dad first.

Layout:

| Block | Content |
|---|---|
| Top title | `Roman PC Build Plan - Platform First, GPU Later` |
| Big number 1 | Main build without GPU: total HUF / UAH / EUR |
| Big number 2 | Saving versus Hungary-only path |
| Big number 3 | Later full build with RTX 5080 |
| Small note | `GPU is not part of first purchase. PC works first with integrated graphics.` |
| Scenario cards | Main 64GB, Safer Kingston, Budget 32GB, Full RTX 5080 later |
| Dad logic | 4-5 short bullets explaining work/AI/SQL/finance value |

Dashboard should be visually calm:
- Big totals at the top.
- Use green only for savings.
- Use yellow/orange only for risk/watch items.
- Avoid showing every source link here.

Dad-facing wording:
- `This is a workstation and learning machine first.`
- `The GPU can be delayed.`
- `Poland saves money mainly on RAM, SSD, and later GPU.`
- `The build supports SQL, finance analysis, AI tools, automation, and future local AI/server work.`

### Sheet 2 - `Builds`

This is the decision model.

Columns are scenarios. Rows are parts.

| Category | Main 64GB No GPU | Safer Kingston | Budget 32GB | Full RTX 5080 Later |
|---|---|---|---|---|
| CPU | CPU_01 | CPU_01 | CPU_01 | CPU_01 |
| Motherboard | MB_01 | MB_01 | MB_01 | MB_01 |
| RAM | RAM_01 | RAM_02 | RAM_03 | RAM_01 |
| SSD | SSD_01 | SSD_01 | SSD_01 | SSD_01 |
| PSU | PSU_01 | PSU_01 | PSU_01 | PSU_01 |
| Cooler | COOL_01 | COOL_01 | COOL_01 | COOL_01 |
| Case | CASE_01 | CASE_01 | CASE_01 | CASE_01 |
| GPU | GPU_00 | GPU_00 | GPU_00 | GPU_01 |
| Total HUF | formula | formula | formula | formula |
| Total UAH | formula | formula | formula | formula |
| Total EUR | formula | formula | formula | formula |
| Comment | main plan | safer RAM | cheaper RAM | later GPU |

Later, each part cell can be a dropdown from `Parts[ID]`.

This sheet is where we quickly test:
- What if we use Kingston RAM?
- What if we use 32GB RAM?
- What if we add RTX 5080 later?
- What if motherboard changes?

### Sheet 3 - `Parts`

This is the database.

Keep columns simple:

| Column | Example |
|---|---|
| Category | RAM |
| ID | RAM_01 |
| Rank | 1 |
| Model | Patriot Viper Venom 64GB |
| Specs | 2x32 DDR5-6000 CL30 |
| Market | Poland |
| Store | Allegro |
| Price | 2941.98 |
| Currency | PLN |
| HUF | formula |
| Status | Pick |
| Risk | Medium |
| Saving vs HU | formula or manual |
| Comment | Best value if seller/warranty clean |
| Link | URL or local capture |

Add 3-4 options per category:
- CPU: 9900X, 9700X, 9950X maybe.
- Motherboard: MSI B850 Tomahawk MAX, ASRock X870 Pro RS WiFi, MSI B850 Tomahawk non-MAX.
- RAM: Patriot 64GB, Kingston 64GB, Patriot 32GB, GOODRAM 64GB.
- SSD: Kingston KC3000, Lexar NM790, Samsung 990 Pro.
- PSU: be quiet 1000W, Seasonic 1000W, Corsair RM1000x.
- Cooler: Arctic A-RGB, Arctic non-RGB.
- Case: Corsair 3500X ARGB, Corsair 3500X plain, Phanteks XT View, NZXT H6 Flow RGB.
- GPU: No GPU yet, MSI RTX 5080 Ventus, MSI Gaming Trio, Gigabyte Gaming OC, RTX 5070/5070 Ti placeholder if we want a budget check.

### Sheet 4 - `Rates`

Purpose:
- Change exchange rates in one place.
- All HUF / UAH / EUR totals update automatically.

Simple layout:

| Currency | HUF per unit | Note |
|---|---:|---|
| HUF | 1.00 | Base currency |
| PLN | 83.07 | ECB-derived, checked 2026-06-14 |
| EUR | 352.88 | ECB, checked 2026-06-14 |
| UAH | 6.80 | NBU-derived, checked 2026-06-14 |

Daily update logic:
- For tomorrow's talk, manual update is enough.
- Later, we can add Power Query or Excel currency data types.
- Do not make the first workbook depend on fragile live internet formulas.

## Visual Design For Dad

Make it look like a small investment decision deck inside Excel:

- `Dashboard`: clean and pretty.
- `Builds`: scenario comparison.
- `Parts`: detailed backup if he asks.
- `Rates`: assumptions.

Color logic:
- Green = saving / selected good value.
- Blue = neutral selected build.
- Yellow = watch / risk.
- Red = avoid or not recommended.
- Grey = not included yet, such as GPU in first-stage build.

Important:
- Dad should not need to understand every motherboard or RAM timing.
- He should see that Roman has a controlled plan, compared options, and is not randomly buying expensive parts.

### Sheet 1 - `Rates`

Purpose:
- Change exchange rates in one place.
- All HUF / UAH / EUR totals update automatically.

Simple layout:

| Currency | HUF per unit | Note |
|---|---:|---|
| HUF | 1.00 | Base currency |
| PLN | 83.07 | ECB-derived, checked 2026-06-14 |
| EUR | 352.88 | ECB, checked 2026-06-14 |
| UAH | 6.80 | NBU-derived, checked 2026-06-14 |

Only these four numbers need to be updated later.

### Sheet 2 - `Parts`

Purpose:
- One row per possible part.
- Easy to add more options later.
- Easy to filter by category.

Use these columns only:

| Column | Example | Why it stays |
|---|---|---|
| Category | RAM | Needed for filtering. |
| ID | RAM_01 | Used by the build selector. |
| Rank | 1 | Shows best/backup order. |
| Model | Patriot Viper Venom 64GB | Main readable name. |
| Specs | 2x32 DDR5-6000 CL30 | Short useful spec. |
| Market | Poland | Country/source market. |
| Store | Allegro / x-kom / Alza | Seller/store. |
| Price | 2941.98 | Original price. |
| Currency | PLN | HUF/PLN/UAH/EUR. |
| HUF | formula | Converted comparison price. |
| Status | Pick / Backup / Watch / Avoid | Decision state. |
| Risk | Low / Medium / High | Simple warning. |
| Comment | Best value if seller clean | Human reason. |
| Link | URL or local capture | Audit trail. |

Do not add more columns unless we really need them. Store quality, warranty, logistics, shipping, and source file can live inside `Comment` for now.

Example row:

| Category | ID | Rank | Model | Specs | Market | Store | Price | Currency | HUF | Status | Risk | Comment | Link |
|---|---|---:|---|---|---|---|---:|---|---:|---|---|---|---|
| RAM | RAM_01 | 1 | Patriot Viper Venom 64GB | 2x32 DDR5-6000 CL30 | Poland | Allegro | 2941.98 | PLN | formula | Pick | Medium | Best value if seller/warranty clean | captured page |

### Sheet 3 - `Builds`

Purpose:
- Pick parts by ID.
- See totals immediately.
- Compare a few build scenarios side by side.

Best layout:

| Category | Main 64GB No GPU | Safer Kingston | Budget 32GB | Full RTX 5080 |
|---|---|---|---|---|
| CPU | CPU_01 | CPU_01 | CPU_01 | CPU_01 |
| Motherboard | MB_01 | MB_01 | MB_01 | MB_01 |
| RAM | RAM_01 | RAM_02 | RAM_03 | RAM_01 |
| SSD | SSD_01 | SSD_01 | SSD_01 | SSD_01 |
| PSU | PSU_01 | PSU_01 | PSU_01 | PSU_01 |
| Cooler | COOL_01 | COOL_01 | COOL_01 | COOL_01 |
| Case | CASE_01 | CASE_01 | CASE_01 | CASE_01 |
| GPU | GPU_00 | GPU_00 | GPU_00 | GPU_01 |
| Total HUF | formula | formula | formula | formula |
| Total UAH | formula | formula | formula | formula |
| Total EUR | formula | formula | formula | formula |

In Excel, each `CPU_01`, `RAM_01`, etc. can later become a dropdown.

Dad-facing view:
- Hide or visually soften technical rows if needed.
- Make the scenario columns pretty.
- Show totals big at the bottom/top.
- Add one short note under each scenario.

This is the cleanest structure:
- `Rates` = assumptions.
- `Parts` = database.
- `Builds` = decision model.

## Build Logic Sanity Check - 2026-06-14

Current assessment: the build direction is good. We are not blindly overspending, but we are also not making a fragile budget PC.

What is already strong:
- Ryzen 9 9900X is still the best fit for Roman's non-gaming work: SQL, databases, analysis, multitasking, light AI/data work. 9700X saves money, but 9900X is the better long-term productivity choice.
- 64GB RAM is justified. 32GB is a real budget branch, but it is not the best default for database/AI/productivity learning.
- 2TB Gen4 SSD is the correct main-drive size. PCIe 5.0 is not worth the heat/price right now.
- 1000W ATX 3.1 / PCIe 5.1 PSU is sensible because RTX 5080 later is part of the plan.
- The LG UltraGear 32GS95UV-B.AEU 4K 240Hz OLED makes RTX 5080-class GPU planning logical. This is not just buying a GPU for no reason.
- Case/cooler prices improved enough that the visual build no longer destroys the budget.

Where we can still save:
- Use 32GB RAM: saves about 126k HUF, but hurts the long-term workstation logic.
- Switch Ryzen 9 9900X to Ryzen 7 9700X: saves money, but weakens the productivity story.
- Skip AIO and use cheaper air cooling: possible technically, but loses the clean build look and future CPU headroom.
- Delay GPU: already planned. This is the biggest smart saving.

GPU class sanity check:
- RTX 5080 is the right long-term target for the 4K 240Hz OLED if Roman wants serious gaming/AI acceleration later.
- RTX 5070 / 5070 Ti could save a lot, but it changes the story: it becomes a good 1440p / lighter 4K card, not a strong "use the OLED properly for years" card.
- Since the PC is being bought first and GPU later, do not downgrade the platform now. Keep PSU/case ready, then decide GPU later by real market price.

Motherboard sanity check:
- MSI B850 Tomahawk MAX WiFi remains a good default.
- ASRock X870 PRO RS WiFi is a real value challenger if Roman wants to save about 10k HUF and is comfortable with ASRock.
- MSI B850 Tomahawk non-MAX is another possible saving branch, but only after checking exact feature differences.
- Do not pay for X870E or MAX WiFi II unless a feature has a clear use.

Verdict:
- We have enough information to build the first spreadsheet model.
- We do not yet need more broad research.
- The next missing information is exact final seller pages for the 3-4 options per category that will go into the Excel.

## Dad-Facing Reason For The PC

Short version:
- This is not only for gaming.
- It is a workstation for learning data, AI, SQL, finance, and analyst-style projects.
- The GPU can be bought later, so the first purchase is a strong platform, not the full dream build at once.

Concrete project examples:
- Build a personal finance and investment research database.
- Import bank/card/export data, clean it, categorize it, and analyze it in SQL.
- Build dashboards for spending, savings, income, investments, and scenarios.
- Create AI-assisted research workflows for company analysis, financial statements, product strategy, and market notes.
- Run local AI models later for private document analysis, notes, coding help, spreadsheet automation, and research summarization.
- Learn modern data stack skills: SQL, Python, databases, APIs, dashboards, vector search, and AI agents.
- Build analyst portfolio projects that can be shown in interviews: finance dashboard, company research database, automated report generator, and AI-assisted assessment-management project.

Dad-facing argument:
- A MacBook at a similar price gives portability, but usually much less RAM/storage and almost no upgrade path.
- This desktop gives 64GB RAM, 2TB SSD, strong CPU, future GPU path, and can become a serious learning/work machine.
- Buying without the RTX 5080 first keeps the cost controlled while preserving the future path.

## Current Main Build To Use As Baseline

Best money-safe first-stage desktop, without RTX 5080:

| Part | Current pick | Market | Captured estimate |
|---|---|---|---:|
| CPU | AMD Ryzen 9 9900X Box | Hungary | 124,050 HUF |
| Motherboard | MSI MAG B850 Tomahawk MAX WiFi | Hungary | 82,340 HUF |
| RAM | Patriot Viper Venom 64GB 2x32 DDR5-6000 CL30 | Poland | 2,941.98 PLN / ~244,390 HUF |
| SSD | Kingston KC3000 2TB | Poland | 939 PLN / ~78,003 HUF |
| PSU | be quiet! Pure Power 13 M 1000W | Hungary | 49,100 HUF |
| Cooler | ARCTIC Liquid Freezer III Pro 360 A-RGB black | Hungary | 31,500 HUF |
| Case | Corsair 3500X ARGB Black | Hungary/local | 31,990 HUF |

Estimated first-stage total without GPU:
- ~641,373 HUF using the 124,050 HUF CPU lead.
- ~94,319 UAH at 1 UAH = 6.80 HUF.

If using the newer landcomputer.hu 9900X seller-page price at 123,750 HUF, the same build is about **641,073 HUF**.

Later GPU:
- MSI RTX 5080 Ventus 3X OC from Poland if seller/warranty is clean.
- 4,899 PLN / ~406,960 HUF.

Estimated full build with later RTX 5080:
- ~1,048,333 HUF with the updated exchange rate and case/cooler pricing.
- ~154,167 UAH at 1 UAH = 6.80 HUF.

## MacBook Pro Comparison From Captured iStore Page

Source file:
- `03_Research_Notes/01_Raw_Captures/MacBook_Comparison/2026-06-13_istore_ua_macbook_pro_page2.md`

Source page:
- `https://www.istore.ua/catalog/apple-mac/macbook-pro/?PAGEN_6=2`

Captured examples:

| MacBook option | Captured price | HUF estimate at 1 UAH = 6.80 HUF | Read |
|---|---:|---:|---|
| MacBook Pro M5 14, 16GB / 512GB | 73,979 UAH | ~503,057 HUF | Cheaper than first-stage desktop, but much less RAM/storage and no desktop upgrade path. |
| MacBook Pro M5 14, 16GB / 1TB | 79,269 UAH | ~539,029 HUF | Cheaper than first-stage desktop, but still only 16GB RAM. |
| MacBook Pro M5 14, 24GB / 1TB | 91,199 UAH | ~620,153 HUF | Closer, but still far below desktop RAM and storage. |
| MacBook Pro M5 Pro 14, 24GB / 1TB | 103,999 UAH | ~707,193 HUF | Similar price zone to desktop, but only 24GB RAM / 1TB SSD. |
| MacBook Pro M5 14 custom, 32GB / 1TB | 113,199 UAH | ~769,753 HUF | More expensive than first-stage desktop while still half the RAM and half the SSD. |
| MacBook Pro M5 Pro 16, 24GB / 1TB | 122,289 UAH | ~831,565 HUF | Above first-stage desktop, different portability/screen/battery value. |
| MacBook Pro M5 Pro 16, 48GB / 1TB | 162,049 UAH | ~1,101,933 HUF | Close to full desktop with RTX 5080, but still less RAM/storage. |
| MacBook Pro M4 Max 16, 48GB / 1TB | 180,739 UAH | ~1,229,025 HUF | Above full desktop estimate. |

Dad-facing read:
- With real current exchange rates, base MacBook Pro options are cheaper than the desktop, but they are not comparable workstation specs.
- The planned desktop without the video card is similar to or cheaper than MacBook Pro options once RAM starts moving toward 24GB/32GB, while the desktop gives 64GB RAM and 2TB SSD.
- The MacBook gives portability, screen, battery, and Apple ecosystem.
- The desktop gives RAM, storage, upgrade path, future RTX 5080 readiness, and much better fit for SQL/database/AI learning projects.

## Draft Build Options For Later Excel

### Option A - Money-Safe 64GB, No GPU Yet

Use this as the main current plan.

Estimated total:
- ~641,373 HUF.

Key logic:
- Patriot RAM from Poland.
- Kingston KC3000 SSD from Poland.
- CPU, motherboard, PSU, cooler, case from Hungary/local.

### Option B - Safer Kingston 64GB, No GPU Yet

Use this if Patriot seller/spec is not clean.

Estimated total:
- ~736,873 HUF if using Kingston Fury Beast EXPO 64GB at 339,890 HUF from the clean Hungary capture.

Main difference:
- Switch Patriot RAM to Kingston Fury Beast EXPO 64GB.
- Saves less money, but RAM choice is more conservative.

### Option C - 32GB Budget Check, No GPU Yet

Status:
- Now usable as a budget branch, not the preferred branch.

Captured budget RAM options:

| RAM option | Market | Captured estimate | HUF estimate | Read |
|---|---|---:|---:|---|
| Patriot Viper Venom 32GB 2x16 DDR5-6000 CL30, PVV532G600C30K | Poland / Ceneo | 1,589.90 PLN | ~147,861 HUF | Best 32GB value lead. |
| Kingston Fury Beast EXPO 32GB 2x16 DDR5-6000 CL30, KF560C30BBEK2-32 | Hungary / Arukereso | 167,990 HUF | 167,990 HUF | Safer brand/spec but worse value than Patriot Poland. |
| Kingston Fury Beast EXPO 32GB 2x16 DDR5-6000 CL30 | Poland / Allegro | 1,850.96 PLN | ~172,139 HUF | Too expensive versus Hungary Kingston and Patriot. |
| G.Skill Flare X5 32GB 2x16 DDR5-6000 CL36 EXPO | Poland / Allegro | 1,835.55 PLN | ~170,706 HUF | CL36 and expensive; not first. |

Goal:
- See whether dropping from 64GB to 32GB saves enough to matter.
- For Roman's database/SQL/productivity use, 64GB is still the preferred direction unless the 32GB saving is very large.

Estimated total with Patriot 32GB instead of Patriot 64GB:
- ~529,056 HUF without GPU.
- This saves about **125,700 HUF** versus the 64GB Patriot build, but halves RAM.

### Option D - Full Build With RTX 5080 Later

Use this to show the final long-term build.

Estimated total:
- ~1,048,333 HUF with MSI RTX 5080 Ventus 3X OC from Poland.

Warning:
- If the GPU changes to a pricier MSI/Gigabyte model, total savings can shrink.
- Do not buy Gigabyte GPU in Poland just because it is Poland; captured Gigabyte Gaming OC was better in Hungary.

## Future CSV / Excel Columns

Recommended columns:

| Column | Meaning |
|---|---|
| Category | CPU, motherboard, RAM, SSD, PSU, cooler, case, GPU, MacBook comparison. |
| Option group | Money-safe, safer, budget, premium, comparison. |
| Included in build | A, B, C, D, or comparison only. |
| Exact model | Full model name and SKU if known. |
| Key specs | Short useful spec summary. |
| Market | Hungary, Poland, Ukraine, or comparison. |
| Store / seller | Exact store if known. |
| Source URL | Product or captured source URL. |
| Source file | Local capture path. |
| Price local | Original price number. |
| Currency | HUF, PLN, UAH. |
| HUF estimate | Converted HUF estimate. |
| Shipping | Known shipping cost or TBD. |
| Warranty / return risk | Low, medium, high, or TBD. |
| Logistics risk | Low, medium, high. |
| Confidence | High, medium, low. |
| Decision | Buy, watch, backup, avoid, comparison only. |
| Notes | Short reason. |

## What More Information Is Needed

Before making the final CSV/Excel:

1. 32GB RAM captures
   - Ceneo search: `32GB 2x16 DDR5 6000 CL30 EXPO`
   - Arukereso search: `32GB 2x16 DDR5 6000 CL30 EXPO`
   - Also search exact safer models: `Kingston Fury Beast 32GB 2x16 6000 CL30 EXPO`, `Patriot Viper Venom 32GB 6000 CL30`, `GOODRAM IRDM 32GB 6000 CL30`.

2. Seller pages for current chosen PC parts
   - Patriot Viper Venom 64GB Poland cheapest offer.
   - Kingston KC3000 2TB Poland offer.
   - Ryzen 9 9900X Box Hungary seller page.
   - MSI MAG B850 Tomahawk MAX WiFi Hungary seller page.
   - be quiet! Pure Power 13 M 1000W Hungary seller page.
   - ARCTIC Liquid Freezer III Pro 360 A-RGB black Hungary seller page.
   - Local case page once the case is chosen.

3. MacBook comparison pages
   - Capture iStore page 1 if it contains lower/base MacBook Pro models.
   - Capture product pages for the exact comparison options:
     - M5 14 16GB / 512GB.
     - M5 14 16GB / 1TB.
     - M5 14 24GB / 1TB.
     - M5 14 custom 32GB / 1TB.
   - Optional: capture one official/large-store alternative if Dad asks about store trust.

4. Case local options
   - Since Poland case logistics are bad, capture Hungary/local pages for realistic cases.
   - Start with Corsair 3500X black, Montech King 95 Pro black, NZXT H6 Flow black, and any case Roman visually likes.

5. Final exchange rates
   - Before presenting the final Excel, update PLN/HUF and UAH/HUF rates.

## Current Recommendation Before CSV

Do not build the final CSV yet.

Next useful captures:
1. 32GB RAM Hungary and Poland.
2. MacBook page 1 plus exact MacBook product pages.
3. Seller pages for Patriot RAM and Kingston KC3000.

After that, the Excel will be much cleaner and can show:
- Money-safe 64GB desktop without GPU.
- Safer Kingston 64GB desktop without GPU.
- Possible 32GB budget desktop without GPU.
- Full desktop with RTX 5080 later.
- MacBook Pro comparison rows.
