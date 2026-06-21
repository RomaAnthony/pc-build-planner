# RTX 5080 Market Snapshot - 2026-06-21

Scope: RTX 5080 16GB desktop cards across Poland, Hungary, and Ukraine.

FX used for comparison:

- 1 PLN = 12.2981 UAH
- 100 HUF = 14.84 UAH
- UAH rows use the captured UAH price directly

## Evidence State

Current capture quality is mixed:

- Ukraine: exact Hotline product pages for MSI Ventus 3X OC and MSI Gaming Trio OC.
- Hungary: broad Arukereso RTX 5080 search pages.
- Poland: broad Ceneo RTX 5080 search page.

Do not update the app CSV from the broad rows yet. Use this snapshot to decide what exact product/store pages to capture next.

## Decision Read

The best current exact evidence is Ukraine MSI Ventus 3X OC at 59,250 UAH.

Poland has a cheaper broad-search Inno3D RTX 5080 X3 lead at about 62,708 UAH equivalent, but it still needs exact store verification before becoming a buy row. Hungary is currently not winning on pure price, but it has several local cheap-ish broad leads around 66,882-69,101 UAH equivalent.

Practical direction:

1. Capture exact Ukraine MSI Ventus store rows first, because this is the cleanest current value.
2. Capture exact Poland Inno3D X3 and Gigabyte Windforce rows, because Poland may still be competitive if the store/warranty is good.
3. Capture exact Hungary Gainward Phoenix V1 / Palit GamingPro / Inno3D X3 rows only if local warranty convenience matters.

## Audit Pass - All RTX 5080 Captures Re-read

This pass re-read the full Poland Ceneo RTX 5080 page, both Hungary Arukereso RTX 5080 pages, and the Ukraine Hotline product captures. Extra reviewed rows are stored in `gpu_reviewed_options.csv`.

Important result: the decision did not change. Ukraine MSI Ventus at 59,250 UAH remains the strongest current price lead, but it is still incomplete because the capture has only the top price, not seller/warranty/payment details.

Poland has several valid broad-search alternatives, but none beat Ukraine Ventus after conversion:

| Product | PLN | UAH est. | Read |
|---|---:|---:|---|
| Inno3D RTX 5080 X3 | 5,099 | 62,708 | Best Poland broad lead |
| Zotac RTX 5080 Solid Core OC | 5,199 | 63,938 | Good broad lead |
| MSI RTX 5080 Shadow 3X OC | 5,299 | 65,168 | Cheap, but only 2 shops shown |
| Palit RTX 5080 GamingPro / GamingPro OC | 5,275-5,351 | 64,878-65,809 | Good broad backup |
| Inno3D RTX 5080 X3 OC White | 5,384 | 66,212 | Valid but above non-OC X3 |
| Gigabyte Windforce OC SFF | 5,475.58 | 67,339 | Good compact/basic-cooler row |
| ASUS Prime OC / MSI Ventus / PNY rows | 5,506-5,638 | 67,723-69,336 | Valid but not price-leading |
| ASUS TUF / ROG / Noctua / Waterforce | 5,899+ | 72,549+ | Reject for value unless premium cooler/noise matters |

Hungary also has several valid broad rows, but they are mostly local-warranty backups:

| Product | HUF | UAH est. | Read |
|---|---:|---:|---|
| Gainward Phoenix V1 | 450,690 | 66,882 | Best current HU broad lead |
| Manli Nebula | 460,250 | 68,301 | Cheap but lower brand confidence |
| Gainward Phoenix / Palit GamingPro | 458,390 | 68,025 | Good local backups |
| Inno3D X3 OC / Gigabyte Windforce SFF | 465,640-469,990 | 69,101-69,747 | Valid local rows |
| ASUS Prime OC / Palit OC / Inno3D White | 487,590-488,590 | 72,352-72,501 | Valid but not leading |
| MSI Gaming Trio / ASUS premium rows | 538,440+ | 79,825+ | Too expensive for value route |

Ukraine exact Gaming Trio rows also confirm why we need seller details:

| Price | Warranty/payment read |
|---:|---|
| 65,400 UAH | Best Gaming Trio row; 24-month manufacturer warranty; payment includes bank transfer without VAT / COD |
| 70,796 UAH | 12-month warranty; available today |
| 71,248 UAH | Only 3-month shop warranty and card-card payment fee; weak despite stock |
| 73,485 UAH | 36-month manufacturer warranty; cleaner but higher price |

## Exact Store Captures Added

New exact product/store captures from the Hub confirm the strongest Poland and Ukraine RTX 5080 rows:

| Country | Product | Store/source | Price | UAH est. | Read |
|---|---|---|---:|---:|---|
| Ukraine | MSI RTX 5080 Ventus 3X OC | LuckyLink via Hotline | 59,250 UAH | 59,250 | Best current price, still needs warranty/payment/delivery check |
| Poland | Inno3D RTX 5080 X3 | Techberg via Ceneo | 5,099 PLN | 62,708 | Best exact Poland row so far |
| Poland | Zotac RTX 5080 Solid Core OC | Allegro via Ceneo | 5,199 PLN | 63,938 | Strong, but seller/warranty needs check |
| Poland | Gainward RTX 5080 Phoenix | x-kom.pl | 5,299 PLN | 65,168 | Stronger store confidence |
| Poland | Palit RTX 5080 GamingPro OC | Allegro via Ceneo | 5,351 PLN | 65,807 | Good backup, seller/warranty needs check |

Conclusion after full pass: no broad GPU page should update the app CSV directly. Exact store rows can update `price_changes.csv`, but final app selection still needs seller confidence. Ukraine Ventus remains cheapest; x-kom Gainward may be safer if we prefer a known Polish store over a lower Ukraine price.

## Top RTX 5080 Rows By Country

| Rank | Country | Product | Captured price | UAH estimate | Evidence | Notes |
|---:|---|---|---:|---:|---|---|
| 1 | Ukraine | MSI GeForce RTX 5080 16G VENTUS 3X OC | 59,250 UAH | 59,250 UAH | Exact product page | Best current exact evidence |
| 2 | Ukraine | MSI GeForce RTX 5080 16G GAMING TRIO OC | 65,400 UAH | 65,400 UAH | Exact product page | Better cooler/class than Ventus |
| 3 | Poland | Inno3D GeForce RTX 5080 X3 16GB | 5,099 PLN | 62,708 UAH | Broad Ceneo search | Strong broad lead; exact store needed |
| 4 | Poland | Zotac GeForce RTX 5080 Solid Core OC 16GB | 5,199 PLN | 63,938 UAH | Broad Ceneo search | Good broad lead; exact store needed |
| 5 | Poland | Palit RTX 5080 GamingPro 16GB | 5,275.47 PLN | 64,878 UAH | Broad Ceneo search | Good broad lead; exact store needed |
| 6 | Poland | Gainward RTX 5080 Phoenix 16GB | 5,299 PLN | 65,168 UAH | Broad Ceneo search | Good broad lead; exact store needed |
| 7 | Hungary | Gainward RTX 5080 Phoenix V1 16GB | 450,690 HUF | 66,882 UAH | Broad Arukereso search | Best current Hungary broad lead |
| 8 | Hungary | Gainward RTX 5080 Phoenix 16GB | 458,390 HUF | 68,025 UAH | Broad Arukereso search | Local backup |
| 9 | Hungary | Palit RTX 5080 GamingPro 16GB | 458,390 HUF | 68,025 UAH | Broad Arukereso search | Local backup |
| 10 | Hungary | Inno3D RTX 5080 X3 OC 16GB | 465,640 HUF | 69,101 UAH | Broad Arukereso search | Matches older app candidate |

## Existing App Baseline To Re-check

These are already in `parts_options_seed.csv`, but most are stale or broad:

| Existing ID | Product | Current app market | Current app price | Status |
|---|---|---|---:|---|
| GPU_01_PL | MSI RTX 5080 Ventus 3X OC 16GB | Poland | 4,899 PLN | Re-check; old row is cheaper than new Ceneo broad Ventus |
| GPU_01_HU | MSI RTX 5080 Ventus 3X OC 16GB | Hungary | 499,090 HUF | Re-check; Hungary broad row now shows 498,580 HUF |
| GPU_02_PL | MSI RTX 5080 Gaming Trio OC 16GB | Poland | 5,599 PLN | Re-check |
| GPU_02_HU | MSI RTX 5080 Gaming Trio OC 16GB | Hungary | 528,465 HUF | Re-check; Hungary broad row now shows 538,440 HUF |
| GPU_03_PL | Gigabyte RTX 5080 Gaming OC 16GB | Poland | 5,799 PLN | Re-check |
| GPU_03_HU | Gigabyte RTX 5080 Gaming OC 16GB | Hungary | 526,400 HUF | Re-check; Hungary broad row now shows 525,855 HUF |
| GPU_04_PL | Inno3D RTX 5080 X3 OC 16GB | Poland | 5,579 PLN | Re-check; new broad Ceneo has non-OC X3 at 5,099 PLN and X3 OC White at 5,384 PLN |
| GPU_04_HU | Inno3D RTX 5080 X3 OC 16GB | Hungary | 465,640 HUF | Still matches Arukereso broad row |
| GPU_05_PL | Gigabyte RTX 5080 Windforce OC SFF 16GB | Poland | 5,343.54 PLN | Re-check; new Ceneo broad has 5,475.58 PLN |
| GPU_05_HU | Gigabyte RTX 5080 Windforce OC SFF 16GB | Hungary | 470,000 HUF | Still close to Arukereso broad row at 469,990 HUF |

## Capture Next

Priority order:

1. Ukraine exact store rows for MSI Ventus 3X OC: capture store name, warranty, payment fee, delivery, stock.
2. Poland exact product/store pages for Inno3D RTX 5080 X3, Inno3D X3 OC, Gigabyte Windforce OC SFF, MSI Ventus 3X OC.
3. Ukraine exact Gaming Trio page if premium cooler is still interesting.
4. Hungary exact product/store pages for Gainward Phoenix V1, Palit GamingPro, Inno3D X3 OC, Gigabyte Windforce SFF.

## Direct Store Checks To Add

Use comparison sites for discovery, then exact store pages for app updates.

- Poland: x-kom, Morele, Komputronik, Proshop, Amazon.pl, Media Expert / Euro / OleOle if Ceneo points there.
- Hungary: Alza.hu, Oazis, iPon, Aqua, Foramax, Konzolvilag, exact Arukereso store rows.
- Ukraine: Hotline-linked seller pages first, then TELEMART, CAN.UA, Rozetka, MOYO, ITbox / Brain if exact SKU appears.

Rule: for GPU, warranty and seller quality matter more than a small price gap. Mark risky low-price rows as `Watch`, not `Pick`, until store/warranty is clear.
