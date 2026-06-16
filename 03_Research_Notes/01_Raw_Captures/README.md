# Raw Captures - Fast Navigation

Purpose:

- This folder stores the saved market pages.
- Treat it like a product evidence library, not a conclusion note.
- Before downloading another page, first check `../00_Working_Shortlists/CAPTURE_SOURCE_INDEX.md`.

## Folder Rule

- `CPU/` -> CPUs and sometimes motherboard pages captured during CPU work
- `GPU/` -> RTX 5080 pages
- `RAM/` -> DDR5 pages
- `SSD/` -> SSD pages
- `PSU/` -> power supply pages
- `Motherboard/` -> AM5 board pages
- `Case_Cooling/` -> cases and CPU coolers
- `MacBook_Comparison/` -> separate side comparison only

## What A Good Capture Looks Like

Best:

- exact product page
- exact seller/store page
- exact part number visible
- current price visible

Acceptable:

- Ceneo / Arukereso / Allegro compare page with the seller list visible

Weak:

- broad category page only
- page where the exact seller is still hidden

## Naming Rule Going Forward

Prefer:

- `YYYY-MM-DD Store Country - Product exact model.md`

Examples:

- `2026-06-15 Allegro PL - Patriot Viper Venom 64GB 6000 CL30 PVV564G600C30K.md`
- `2026-06-15 Jacob DE - Kingston KC3000 2TB SKC3000D2048G.md`

Keep old filenames if they already work. Do not rename files only for style if the content is already linked in notes.

## Current Most Useful Exact Pages

- CPU:
  - `CPU/AMD Ryzen 9 9900X - Procesor AMD Ryzen 9 - najlepsze ceny, tysiące opinii w x-kom.pl.md`
  - `CPU/AMD Procesor Ryzen™ 9900X, 12 rdzeni_24 nieuszkodzone wątki, architektura Zen 5, pamięć podręczna 76MB L3, 120 W TDP, do 5,6 GHz, gniazdo AM5, DDR5 i PCIe 5.0, bez ventirad _ Amazon.pl_ Elektronika.md`
- RAM:
  - `RAM/2026-06-15 Allegro PL - Patriot Viper Venom 64GB 6000 CL30 PVV564G600C30K.md`
  - `RAM/2026-06-15 Allegro PL compare offers - Patriot Viper Venom 64GB 6000 CL30.md`
  - `RAM/KR System - Kingston DDR5 Fury Beast 64GB(2_32GB)_6000 CL30 EXPO czarna.md`
- SSD:
  - `SSD/Dysk SSD Kingston KC3000 2TB M.2 Pcie 4.0 NVMe (SKC3000D2048G) - Opinie i ceny na Ceneo.pl.md`
  - `SSD/2026-06-15 Jacob DE - Kingston KC3000 2TB SKC3000D2048G.md`
- PSU:
  - `PSU/Zasilacz Corsair RM1000x 1000W 80 Plus Gold ATX 3.1 (CP9020271EU) - Opinie i ceny na Ceneo.pl.md`
- GPU:
  - `GPU/MSI GeForce RTX 5080 Ventus 3X OC 16GB GDDR7 DLSS4 - Karta graficzna NVIDIA - najlepsze ceny, tysiące opinii w x-kom.pl.md`

## Workflow

1. Save new page into `00_Hub/`.
2. Move it into the correct category here.
3. Update `../00_Working_Shortlists/CAPTURE_SOURCE_INDEX.md` if it is now part of active build logic.
4. Only then update the shortlist note or CSV.
