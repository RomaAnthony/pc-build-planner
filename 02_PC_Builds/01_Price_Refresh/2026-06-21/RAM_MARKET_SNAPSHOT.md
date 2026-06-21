# RAM Market Snapshot - 2026-06-21

Scope: DDR5 6000 CL30 desktop kits, split into the real 64GB target and the 32GB budget-down route.

FX used for comparison:

- 1 PLN = 12.2981 UAH
- 100 HUF = 14.84 UAH
- UAH rows use the captured UAH price directly

## Decision Read

RAM is now one of the biggest levers to reduce the build price.

- Best clean 64GB direction if Poland is used: Patriot Viper Venom 64GB at about 39,465 UAH.
- Best clean 64GB Ukraine direction: Patriot Viper Venom 64GB at 43,196 UAH.
- Best clean 64GB Hungary normal-brand direction: Kingston Fury Beast at 46,957 UAH, unless the Silicon Power 225,090 HUF row is verified as real and trustworthy.
- Best 32GB budget-down route: Patriot Viper Venom 32GB in Poland or Ukraine, around 19,665-20,172 UAH.

Practical result: dropping from 64GB Patriot Poland to 32GB Patriot Poland saves about 19,800 UAH. That is a real build-price lever, not a tiny optimization.

## Audit Pass - All RAM Captures Re-read

This pass re-checked the broad Poland, Hungary, and Ukraine RAM captures, including the large Hungary/Pepita file. The extra reviewed rows are stored in `ram_reviewed_options.csv` so the main snapshot can stay readable.

Important result: the Hungary dump does not hide a better exact 6000 CL30 option. Rows that miss the target spec are not automatically useless; they are kept as fallback candidates only when the saving is large enough. Rows are rejected only when they are clearly wrong for this build, such as DDR4, laptop/server RAM, single modules when we need a kit, 4-stick AM5 kits unless intentional, weird capacities, unclear SKU, or no real price advantage.

The one disruptive Hungary row remains:

- Silicon Power XPower Zenith 64GB 2x32 DDR5-6000 CL30 at 225,090 HUF from Pepita marketplace. It is exact spec, but the price is far below the second exact offer from bluechip.hu at 383,899 HUF, so it stays `Verify`, not `Pick`.

Reviewed Hungary 64GB CL30 candidates:

| Product | HUF | UAH est. | Read |
|---|---:|---:|---|
| Silicon Power XPower Zenith 64GB 6000 CL30 - Pepita | 225,090 | 33,403 | Verify; suspiciously cheap |
| GOODRAM 64GB 6000 CL30 | 330,580 | 49,058 | Best normal broad HU lead |
| G.Skill Trident Z5 64GB 6000 CL30 | 362,100 | 53,737 | Valid, not leading |
| G.Skill Ripjaws S5 64GB 6000 CL30 | 377,650 | 56,041 | Valid, not leading |
| Kingston Fury Beast 64GB 6000 CL30 White | 379,340 | 56,292 | Valid safer-brand row |
| Patriot Viper Venom 64GB 6000 CL30 | 392,890 | 58,303 | Valid, but Poland/Ukraine are better |
| Corsair Vengeance 64GB 6000 CL30 | 491,020+ | 72,827+ | Reject for value |

Reviewed Hungary 32GB CL30 candidates:

| Product | HUF | UAH est. | Read |
|---|---:|---:|---|
| Patriot Viper Venom 32GB 6000 CL30 | 149,590 | 22,199 | Best HU 32GB route |
| Patriot Viper Venom RGB 32GB 6000 CL30 | 152,690 | 22,659 | Valid, small RGB premium |
| Kingston Fury Beast 32GB 6000 CL30 | 159,840 | 23,720 | Safer-brand backup |
| G.Skill Flare X5 32GB 6000 CL30 | 187,000 | 27,751 | Valid, too expensive |
| Corsair Vengeance 32GB 6000 CL30 | 213,190 | 31,637 | Reject for value |

Conclusion after full pass: no change to the exact-spec RAM decision. Poland/Ukraine still look better for normal 64GB CL30, Hungary only becomes interesting if the Silicon Power Pepita row is confirmed as safe. If exact 64GB CL30 stays too expensive, use `ram_reviewed_options.csv` to compare controlled fallback tiers like 6000 CL36, 5600 CL30/CL36, or 6000 CL40.

## 64GB 6000 CL30 - Top Rows

| Rank | Country | Product | Captured price | UAH estimate | Notes |
|---:|---|---|---:|---:|---|
| 1 | Hungary | Silicon Power XPower Zenith 64GB 2x32 6000 CL30 | 225,090 HUF | 33,403 UAH | Very strong but suspiciously cheap; verify exact product and store before app CSV |
| 2 | Poland | Patriot Viper Venom 64GB 2x32 6000 CL30 | 3,209 PLN | 39,465 UAH | Best normal clean 64GB lead from Ceneo capture |
| 3 | Poland | GOODRAM IRDM 64GB 2x32 6000 CL30 | 3,333 PLN | 40,990 UAH | Strong Polish backup |
| 4 | Poland | Kingston Fury Beast RGB 64GB 6000 CL30 | 3,417.77-3,425.99 PLN | 42,032-42,133 UAH | Good safer-brand backup |
| 5 | Ukraine | Patriot Viper Venom 64GB 2x32 6000 CL30 | 43,196 UAH | 43,196 UAH | Best clean Ukraine 64GB lead |
| 6 | Ukraine | GOODRAM IRDM 64GB 2x32 6000 CL30 | 44,472 UAH | 44,472 UAH | Ukraine backup |
| 7 | Ukraine | Kingston Fury Beast 64GB 6000 CL30 | 45,499 UAH | 45,499 UAH | Ukraine safer-brand backup |
| 8 | Hungary | Kingston Fury Beast 64GB 2x32 6000 CL30 | 316,420 HUF | 46,957 UAH | Best normal Hungary lead |
| 9 | Hungary | GOODRAM 64GB 6000 CL30 | 330,580 HUF | 49,058 UAH | Hungary backup |

## 32GB 6000 CL30 - Top Rows

| Rank | Country | Product | Captured price | UAH estimate | Notes |
|---:|---|---|---:|---:|---|
| 1 | Ukraine | Exceleram Aurum 32GB 2x16 6000 CL30 | 18,485 UAH | 18,485 UAH | Cheapest, lower confidence brand |
| 2 | Poland | Patriot Viper Venom 32GB 2x16 6000 CL30 | 1,599 PLN | 19,665 UAH | Best clean 32GB value |
| 3 | Ukraine | Patriot Viper Venom 32GB 2x16 6000 CL30 | 20,172 UAH | 20,172 UAH | Strong Ukraine budget-down option |
| 4 | Poland | Lexar Ares 32GB 2x16 6000 CL30 | 1,666.66 PLN | 20,497 UAH | Polish backup |
| 5 | Ukraine | Patriot Viper Elite 5 32GB 6000 CL30 | 20,562 UAH | 20,562 UAH | Ukraine backup |
| 6 | Poland | GOODRAM IRDM 32GB 2x16 6000 CL30 | 1,699 PLN | 20,894 UAH | Good Polish backup |
| 7 | Hungary | Patriot Viper Venom 32GB 2x16 6000 CL30 | 149,590 HUF | 22,199 UAH | Best Hungary 32GB lead |
| 8 | Hungary | Patriot Viper Venom RGB 32GB 2x16 6000 CL30 | 152,690 HUF | 22,659 UAH | Hungary backup |
| 9 | Hungary | Kingston Fury Beast 32GB 6000 CL30 | 159,840 HUF | 23,720 UAH | Safer-brand Hungary backup |

## Cheap Non-CL30 Watchlist

Use these only if we intentionally accept slower timings to reduce the price.

| Country | Capacity | Product | Captured price | UAH estimate | Why separate |
|---|---:|---|---:|---:|---|
| Ukraine | 64GB | Crucial Pro 6000 CL40 | 36,058 UAH | 36,058 UAH | Much cheaper, but CL40 |
| Poland | 64GB | G.Skill Aegis 5 6000 CL36 | 2,999 PLN | 36,882 UAH | Cheaper than CL30, but CL36 |
| Poland | 64GB | Patriot Viper Venom 6000 CL36 | 3,099.99 PLN | 38,124 UAH | Same family, slower SKU |
| Ukraine | 64GB | G.Skill Ripjaws M5 Neo RGB 6000 CL36 | 39,999 UAH | 39,999 UAH | Good price, but CL36 |
| Ukraine | 32GB | Crucial Pro OC 6000 CL36 | 16,999 UAH | 16,999 UAH | Cheap 32GB fallback, but CL36 |

## Capture Next

Leave motherboard alone for now. RAM needs exact store-level verification.

Priority order:

1. Verify Hungary Silicon Power 64GB 6000 CL30 exact product and store because it changes the 64GB decision if real.
2. Capture exact Patriot Viper Venom 64GB CL30 store pages in Poland and Ukraine.
3. Capture exact GOODRAM IRDM 64GB CL30 store pages in Poland and Ukraine.
4. Capture exact Kingston Fury Beast 64GB CL30 store pages in all three countries.
5. Capture 32GB Patriot Viper Venom CL30 in Poland, Ukraine, and Hungary for the budget-down route.

## Direct Store Checks To Add

Price comparison sites are still useful, but they can miss stock, delivery, or store-specific listings. After broad captures, check direct stores for the top RAM rows:

- Poland: x-kom, Morele, Komputronik, Proshop, Amazon.pl, Allegro only if seller looks safe.
- Hungary: Alza.hu, iPon, Aqua, Oazis, Foramax, stores shown by Arukereso for the specific product page.
- Ukraine: Hotline-linked top stores first, then TELEMART, CAN.UA, Rozetka, MOYO, ITbox / Brain if they appear for the exact SKU.

Rule: direct-store pages can update `price_changes.csv`; broad search pages only create candidate rows unless the product match and store price are clear.
