import marimo

__generated_with = "0.23.9"
app = marimo.App(width="full")


@app.cell
def _():
    import html
    import json
    from datetime import datetime
    from io import StringIO
    
    import marimo as mo
    import pandas as pd

    # ====== EMBEDDED CSV DATA (no filesystem needed for WASM) ======
    PARTS_CSV_DATA = """ID,Part,Priority,Option,Market,Store,Price,Currency,HUF_Est,Status,Risk,Note,Source,URL
CPU_01_PL,CPU,1,AMD Ryzen 9 9900X Box,Poland,Ceneo lead,1398.99,PLN,116214,Compare,Medium,Current Poland broad lead from the 2026-06-21 CPU refresh; exact seller should be rechecked before ordering,01_Market_Data/2026-06-21/CPU/2026-06-21_cpu_web_refresh.md,
CPU_01_PL_AMZ,CPU,1,AMD Ryzen 9 9900X Box,Poland,Amazon.pl,1398.99,PLN,116214,Backup,Low,Safe seller but no longer cheaper than the fresh broad-market lead,01_Market_Data/2026-06-21/CPU/2026-06-21_cpu_web_refresh.md,
CPU_01_HU,CPU,1,AMD Ryzen 9 9900X Box,Hungary,Arukereso floor,123050,HUF,123050,Pick,Low,Fresh local 9900X floor from the 2026-06-21 Arukereso capture,01_Market_Data/2026-06-21/CPU/2026-06-21_cpu_web_refresh.md,
CPU_01_UA,CPU,1,AMD Ryzen 9 9900X Box,Ukraine,Hotline exact product,15549,UAH,104778,Watch,Medium,Strong Ukraine CPU lead from Hotline exact product page; store-level warranty comfort still matters,01_Market_Data/2026-06-21/CPU/2026-06-21_cpu_web_refresh.md,
CPU_02_PL,CPU,2,AMD Ryzen 7 9700X Box,Poland,Ceneo lead,1024.2,PLN,85080,Compare,Medium,Straight Poland BOX comparison for CPU_02_HU from Ceneo capture 2026-06-16,01_Market_Data/2026-06-16/CPU/Ryzen 7 9700x - Komputery.md,
CPU_02_HU,CPU,2,AMD Ryzen 7 9700X Box,Hungary,Arukereso lead,103490,HUF,103490,Backup,Low,Budget fallback if platform cost must drop,CPU_WORKING_SHORTLIST,
CPU_03_PL,CPU,3,AMD Ryzen 9 9950X Box,Poland,Ceneo lead,1899,PLN,157750,Compare,Medium,Straight Poland BOX comparison; tray row is slightly cheaper but not same retail box route,01_Market_Data/2026-06-16/CPU/Ryzen 9 9950x - Komputery.md,
CPU_03_HU,CPU,3,AMD Ryzen 9 9950X Box,Hungary,Konzolvilag,174090,HUF,174090,Watch,Medium,16-core productivity upgrade; not default value choice,Raw_Captures/CPU,
MB_01_PL,Motherboard,1,MSI MAG B850 Tomahawk MAX WiFi,Poland,Amazon.pl,978.66,PLN,65870,Compare,Medium,Fresh exact Poland row visible on the Ceneo product page,01_Market_Data/2026-06-21/Motherboard/2026-06-21_motherboard_web_refresh.md,
MB_01_HU,Motherboard,1,MSI MAG B850 Tomahawk MAX WiFi,Hungary,aqua.hu,82990,HUF,82990,Pick,Low,Fresh exact Hungary row from Arukereso product page,01_Market_Data/2026-06-21/Motherboard/2026-06-21_motherboard_web_refresh.md,
MB_01_UA,Motherboard,1,MSI MAG B850 Tomahawk MAX WiFi,Ukraine,Hotline seller row SKU 911-7E62-002,12989,UAH,87527,Watch,Medium,Cleaner exact Ukraine row than the unlabeled 8553 capture; 36-month warranty is visible,01_Market_Data/2026-06-21/Motherboard/2026-06-21_hotline_msi_mag_b850_tomahawk_max_wifi_exact.md,
MB_02_PL,Motherboard,2,ASRock X870 PRO RS WiFi,Poland,Amazon.pl,849.74,PLN,70588,Compare,Medium,Exact Ceneo product page capture with Amazon offer on 2026-06-16,01_Market_Data/2026-06-16/Motherboard/Płyta główna PC Asrock X870 Pro Rs Wifi (X870PRORSWIFI) - Opinie i ceny na Ceneo.pl.md,
MB_02_HU,Motherboard,2,ASRock X870 PRO RS WiFi,Hungary,Arukereso lead,72290,HUF,72290,Backup,Medium,Strong value challenger if comfortable with ASRock,Raw_Captures/Motherboard,
MB_03_HU,Motherboard,3,MSI MAG B850 Tomahawk WiFi non-MAX,Hungary,Arukereso lead,80860,HUF,80860,Watch,Medium,Fresh non-MAX Hungary broad row; still mainly a budget MSI fallback,02_PC_Builds/01_Price_Refresh/2026-06-21/motherboard_market_snapshot.csv,
MB_04_PL,Motherboard,4,Gigabyte X870E AORUS Elite WiFi7,Poland,Ceneo lead,1079,PLN,89633,Compare,Medium,Closest Poland row is Gigabyte X870E A ELITE WIFI7; verify AORUS naming before buying,01_Market_Data/2026-06-16/Motherboard/Gigabyte x870e aorus elite wifi7 - Komputery.md,
MB_04_HU,Motherboard,4,Gigabyte X870E AORUS Elite WiFi7,Hungary,Arukereso lead,108900,HUF,108900,Watch,Medium,Fresh Hungary broad row for the premium board class,02_PC_Builds/01_Price_Refresh/2026-06-21/motherboard_market_snapshot.csv,
RAM_01_PL,RAM,1,Patriot Viper Venom 64GB 2x32 DDR5-6000 CL30,Poland,RTV EURO AGD,3209,PLN,243619,Pick,Medium,Fresh exact Poland row with correct CL30 SKU PVV564G600C30K,"01_Market_Data/2026-06-21/RAM/Pamięć RAM Patriot Viper Venom DDR5 64GB (2 x 32GB) 6000 CL30 Szary - Opinie, Cena - RTV EURO AGD.md",
RAM_01_HU,RAM,1,Patriot Viper Venom 64GB 2x32 DDR5-6000 CL30,Hungary,Arukereso lead,392890,HUF,392890,Compare,High,Fresh same-model Hungary broad row shows how expensive the Patriot route currently is locally,01_Market_Data/2026-06-21/RAM/Árak és termékek összehasonlítása online boltok teljes kínálatából.md,
RAM_01_UA,RAM,1,Patriot Viper Venom 64GB 2x32 DDR5-6000 CL30,Ukraine,Hotline broad lead,43196,UAH,291078,Watch,Medium,Best clean Ukraine 64GB CL30 row from the current RAM refresh,02_PC_Builds/01_Price_Refresh/2026-06-21/ram_market_snapshot.csv,
RAM_02_PL,RAM,2,Kingston Fury Beast EXPO 64GB 2x32 DDR5-6000 CL30,Poland,KR System,3635.5,PLN,302001,Backup,Medium,Safer RAM option from Poland but not as cheap as Patriot,Raw_Captures/RAM,
RAM_02_HU,RAM,2,Kingston Fury Beast EXPO 64GB 2x32 DDR5-6000 CL30,Hungary,foramax.hu,339890,HUF,339890,Backup,Low,Safest RAM option; better warranty comfort,Raw_Captures/RAM,
RAM_03_PL,RAM,3,GOODRAM IRDM 64GB 2x32 DDR5-6000 CL30,Poland,Allegro,3333,PLN,276872,Backup,Medium,Third practical 64GB option,Raw_Captures/RAM,
RAM_03_HU,RAM,3,GOODRAM IRDM 64GB 2x32 DDR5-6000 CL30,Hungary,Arukereso lead,330580,HUF,330580,Backup,Medium,Fresh Hungary broad row; still not cheap enough to beat Poland meaningfully,02_PC_Builds/01_Price_Refresh/2026-06-21/ram_market_snapshot.csv,
RAM_04_PL,RAM,4,Patriot Viper Venom 32GB 2x16 DDR5-6000 CL30,Poland,Ceneo lead,1599,PLN,132073,Watch,Medium,Fresh Poland budget-down row for the 32GB branch,02_PC_Builds/01_Price_Refresh/2026-06-21/ram_market_snapshot.csv,
RAM_04_HU,RAM,4,Patriot Viper Venom 32GB 2x16 DDR5-6000 CL30,Hungary,Arukereso lead,149590,HUF,149590,Compare,Low,Same model local comparison from the current Arukereso capture,02_PC_Builds/01_Price_Refresh/2026-06-21/ram_market_snapshot.csv,
RAM_04_UA,RAM,4,Patriot Viper Venom 32GB 2x16 DDR5-6000 CL30,Ukraine,Hotline broad lead,20172,UAH,135930,Watch,Medium,Strong Ukraine budget-down option from the current RAM refresh,02_PC_Builds/01_Price_Refresh/2026-06-21/ram_market_snapshot.csv,
SSD_01_PL,SSD,1,Kingston KC3000 2TB,Poland,Ceneo lead,1119,PLN,78003,Pick,Medium,Fresh Poland SSD market floor now sits at 1119 PLN,01_Market_Data/2026-06-21/SSD/2026-06-21_ssd_web_refresh.md,
SSD_01_HU,SSD,1,Kingston KC3000 2TB,Hungary,senetic.hu,114281,HUF,114281,Compare,Low,Fresh exact Hungary SSD leader from Arukereso product page,01_Market_Data/2026-06-21/SSD/2026-06-21_ssd_web_refresh.md,
SSD_01_UA,SSD,1,Kingston KC3000 2TB,Ukraine,Hotline broad lead,14044,UAH,94636,Watch,Medium,Strong Ukraine SSD row with 60-month warranty seller rows visible,01_Market_Data/2026-06-21/SSD/2026-06-21_ssd_web_refresh.md,
SSD_02_PL,SSD,2,Lexar NM790 2TB,Poland,Ceneo lead,1038.03,PLN,86229,Backup,Medium,Good SSD but KC3000 Poland is cleaner value,Raw_Captures/SSD,
SSD_02_HU,SSD,2,Lexar NM790 2TB,Hungary,Arukereso lead,96695,HUF,96695,Backup,Low,Best Hungary SSD value; DRAM-less/HMB,Raw_Captures/SSD,
SSD_03_PL,SSD,3,Samsung 990 PRO 2TB,Poland,Ceneo lead,1499,PLN,122030,Avoid,Medium,Fresh Poland premium SSD row; still meaningfully above KC3000,01_Market_Data/2026-06-21/SSD/2026-06-21_ssd_web_refresh.md,
SSD_03_HU,SSD,3,Samsung 990 PRO 2TB,Hungary,Alza / Arukereso lead,119990,HUF,119990,Watch,Low,Premium SSD; only if close to KC3000 price,Raw_Captures/SSD,
SSD_03_UA,SSD,3,Samsung 990 PRO 2TB,Ukraine,Hotline broad lead,16689,UAH,112460,Watch,Medium,Fresh Ukraine premium SSD alternative,01_Market_Data/2026-06-21/SSD/2026-06-21_ssd_web_refresh.md,
PSU_01_PL,PSU,1,be quiet! Pure Power 13 M 1000W,Poland,Media Expert / Avans,499,PLN,49100,Compare,Medium,Fresh exact Poland budget-leader row for compact 1000W ATX 3.1,01_Market_Data/2026-06-21/PSU/2026-06-21_psu_web_refresh.md,
PSU_01_HU,PSU,1,be quiet! Pure Power 13 M 1000W,Hungary,firstshop.hu,48240,HUF,48240,Pick,Low,Fresh exact Hungary PSU leader from Arukereso page,01_Market_Data/2026-06-21/PSU/2026-06-21_psu_web_refresh.md,
PSU_01_UA,PSU,1,be quiet! Pure Power 13 M 1000W,Ukraine,Hotline broad lead,7013,UAH,47257,Watch,Medium,Strong Ukraine budget PSU row with visible 10-year warranty seller rows,01_Market_Data/2026-06-21/PSU/2026-06-21_psu_web_refresh.md,
PSU_02_PL,PSU,2,Seasonic Focus GX-1000 v4,Poland,proshop.pl,687,PLN,57069,Compare,Medium,Good unit; Poland exact store row is now freshly confirmed,01_Market_Data/2026-06-21/PSU/2026-06-21_psu_web_refresh.md,
PSU_02_HU,PSU,2,Seasonic Focus GX-1000 2024,Hungary,Arukereso lead,57070,HUF,57070,Backup,Low,Fresh Hungary broad row for the Seasonic premium-value option,02_PC_Builds/01_Price_Refresh/2026-06-21/psu_market_snapshot.csv,
PSU_02_UA,PSU,2,Seasonic Focus GX-1000 ATX 3.1,Ukraine,Hotline broad lead,8620,UAH,58086,Watch,Medium,Fresh Ukraine broad row for the Seasonic 1000W option,02_PC_Builds/01_Price_Refresh/2026-06-21/psu_market_snapshot.csv,
PSU_03_PL,PSU,3,Corsair RM1000x ATX 3.1,Poland,Amazon.pl,647,PLN,53746,Backup,Medium,Strong Poland PSU option; fresh exact Amazon row still holds,01_Market_Data/2026-06-21/PSU/2026-06-21_psu_web_refresh.md,
PSU_03_HU,PSU,3,Corsair RM1000x ATX 3.1,Hungary,oaziscomputer.hu,66200,HUF,66200,Watch,Low,Strong premium PSU but pricier,Raw_Captures/PSU,
PSU_03_UA,PSU,3,Corsair RM1000x ATX 3.1,Ukraine,Hotline broad lead,8804,UAH,59326,Watch,Medium,Fresh Ukraine mainstream premium PSU row with visible warranty notes,01_Market_Data/2026-06-21/PSU/2026-06-21_psu_web_refresh.md,
COOL_01_HU,Cooler,1,Arctic Liquid Freezer III Pro 360 A-RGB Black,Hungary,Arukereso lead,37888,HUF,37888,Pick,Low,Fresh Hungary A-RGB Arctic row from the 2026-06-21 cooler refresh,01_Market_Data/2026-06-21/Cooler/2026-06-21_cooler_web_refresh.md,
COOL_02_PL,Cooler,2,Arctic Liquid Freezer III Pro 360 Black,Poland,Ceneo lead,324,PLN,26915,Compare,Medium,Fresh Poland non-RGB Arctic row; still a strong value anchor,01_Market_Data/2026-06-21/Cooler/2026-06-21_cooler_web_refresh.md,
COOL_02_HU,Cooler,2,Arctic Liquid Freezer III Pro 360 Black,Hungary,Arukereso lead,32190,HUF,32190,Backup,Low,Fresh Hungary non-RGB Arctic row,01_Market_Data/2026-06-21/Cooler/2026-06-21_cooler_web_refresh.md,
COOL_03_PL,Cooler,3,DeepCool LE360 V2 ARGB Black,Poland,Ceneo lead,282.82,PLN,23028,Compare,Medium,Fresh Poland DeepCool broad row; exact black/ARGB naming should still be sanity-checked before ordering,01_Market_Data/2026-06-21/Cooler/2026-06-21_cooler_web_refresh.md,
COOL_03_HU,Cooler,3,DeepCool LE360 V2 ARGB Black,Hungary,Arukereso lead,23990,HUF,23990,Backup,Medium,Fresh Hungary DeepCool broad row,01_Market_Data/2026-06-21/Cooler/2026-06-21_cooler_web_refresh.md,
COOL_03_UA,Cooler,3,DeepCool LE360 V2 Black,Ukraine,Hotline broad lead,3979,UAH,26813,Watch,Medium,Cheapest confidently captured Ukraine 360 mm cooler option today,01_Market_Data/2026-06-21/Cooler/2026-06-21_cooler_web_refresh.md,
COOL_04_PL,Cooler,4,MSI MAG CoreLiquid A13 360 Black,Poland,Ceneo lead,248,PLN,20601,Compare,Medium,Straight Poland comparison from the fresh cooler refresh,01_Market_Data/2026-06-21/Cooler/2026-06-21_cooler_web_refresh.md,
COOL_04_HU,Cooler,4,MSI MAG CoreLiquid A13 360 Black,Hungary,Arukereso broad search,27777,HUF,27777,Watch,Medium,MSI-branded visual alternative; still less trusted than Arctic on value,Raw_Captures/Case_Cooling,
COOL_04_UA,Cooler,4,MSI MAG CoreLiquid A13 360 Black,Ukraine,Hotline broad lead,3355,UAH,22608,Watch,Medium,"Lowest captured Ukraine cooler floor, but product-level quality comfort is lower than Arctic",01_Market_Data/2026-06-21/Cooler/2026-06-21_cooler_web_refresh.md,
COOL_05_HU,Cooler,5,Gigabyte GME 360 Gaming CPU Cooler Black,Hungary,Arukereso broad search,31800,HUF,31800,Watch,Medium,Looks fine on paper but not clearly better than Arctic at similar money,Raw_Captures/Case_Cooling,
COOL_06_PL,Cooler,6,be quiet! Pure Loop 3 LX 360mm Black,Poland,Ceneo lead,429,PLN,32786,Compare,Medium,Fresh Poland premium quiet-brand row from the current cooler refresh,01_Market_Data/2026-06-21/Cooler/2026-06-21_cooler_web_refresh.md,
COOL_06_HU,Cooler,6,be quiet! Pure Loop 3 LX 360mm Black,Hungary,Arukereso broad search,34600,HUF,34600,Watch,Low,Premium quiet-brand alternative if aesthetics or brand preference matter,01_Market_Data/2026-06-21/Cooler/2026-06-21_cooler_web_refresh.md,
COOL_06_UA,Cooler,6,be quiet! Pure Loop 3 LX 360mm Black,Ukraine,Hotline broad lead,5511,UAH,37136,Watch,Medium,Fresh Ukraine premium quiet-brand 360 row,01_Market_Data/2026-06-21/Cooler/2026-06-21_cooler_web_refresh.md,
CASE_01_HU,Case,1,Corsair 3500X ARGB Black,Hungary,Arukereso lead,31990,HUF,31990,Pick,Low,Current case baseline; local because glass case logistics,Raw_Captures/Case_Cooling,
CASE_02_HU,Case,2,Corsair 3500X Black plain,Hungary,Arukereso lead,21326,HUF,21326,Watch,Low,Cheapest Corsair path; fan planning needed,Raw_Captures/Case_Cooling,
CASE_03_HU,Case,3,Phanteks XT View TG D-RGB Black,Hungary,Arukereso lead,27901,HUF,27901,Backup,Medium,Cheap visual backup; check clearance/build quality,Raw_Captures/Case_Cooling,
CASE_04_HU,Case,4,NZXT H6 Flow RGB All Black,Hungary,Arukereso lead,44444,HUF,44444,Watch,Low,Nice case but Corsair is cheaper,Raw_Captures/Case_Cooling,
CASE_05_HU,Case,5,Lian Li O11 Vision Compact Black,Hungary,Arukereso lead,43290,HUF,43290,Compare,Medium,Best compact premium look for Ventus-sized GPU; fan cost still needs to be added,Raw_Captures/Case_Cooling,
CASE_06_HU,Case,6,NZXT H9 Flow Black,Hungary,oaziscomputer.hu,54190,HUF,54190,Compare,Low,Best roomy clean-look case if pairing with larger premium GPU; includes fans,Raw_Captures/Case_Cooling,
CASE_07_HU,Case,7,Montech KING 95 PRO TG ARGB Black,Hungary,Arukereso lead,55790,HUF,55790,Compare,Medium,Best all-in value if included fans are counted honestly,Raw_Captures/Case_Cooling,
CASE_08_HU,Case,8,Lian Li O11D EVO RGB TG Black,Hungary,Arukereso lead,59990,HUF,59990,Watch,Medium,Beautiful premium Lian Li direction but real cost rises after fans,Raw_Captures/Case_Cooling,
CASE_09_HU,Case,9,Lian Li O11 Dynamic Mini V2 TG Black,Hungary,Arukereso lead,33090,HUF,33090,Watch,Medium,Compact and pretty but more experimental for Ryzen 9 plus future RTX 5080,Raw_Captures/Case_Cooling,
CASE_10_HU,Case,10,Phanteks NV9 MK2 Black,Hungary,Arukereso lead,84499,HUF,84499,Avoid,Medium,Beautiful oversized showcase case but too expensive and fan cost still needs to be added,Raw_Captures/Case_Cooling,
CASE_11_HU,Case,11,Lian Li O11 Dynamic EVO XL Black,Hungary,Arukereso lead,89900,HUF,89900,Avoid,Medium,Too expensive and too large for the current build logic,Raw_Captures/Case_Cooling,
CASE_12_HU,Case,12,NZXT H7 Flow 2024 All Black (CM-H72FB-01),Hungary,Arukereso exact product,42630,HUF,42630,Watch,Low,Fresh airflow-oriented case candidate from the sorted 2026-06-21 capture,01_Market_Data/2026-06-21/Case/2026-06-21_case_web_refresh.md,
CASE_13_HU,Case,13,Corsair Frame 4000D RS Wood (CC-9011340-WW),Hungary,Arukereso exact product,50400,HUF,50400,Watch,Medium,Fresh premium airflow and aesthetics case candidate from the sorted 2026-06-21 capture,01_Market_Data/2026-06-21/Case/2026-06-21_case_web_refresh.md,
GPU_00_NONE,GPU,0,No GPU yet,No GPU,Local,0,HUF,0,Pick,Low,First purchase excludes expensive GPU; phase 1 uses Ryzen integrated graphics,RTX5080_WORKING_SHORTLIST,
GPU_01_PL,GPU,1,MSI RTX 5080 Ventus 3X OC 16GB,Poland,Ceneo broad lead,5599.99,PLN,406960,Watch,Medium,Fresh Poland Ventus broad row is much higher than the older x-kom capture,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_market_snapshot.csv,
GPU_01_HU,GPU,1,MSI RTX 5080 Ventus 3X OC 16GB,Hungary,Arukereso broad lead,498580,HUF,498580,Compare,Medium,Fresh Hungary Ventus broad row remains far above the Ukraine lead,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_market_snapshot.csv,
GPU_01_UA,GPU,1,MSI RTX 5080 Ventus 3X OC 16GB,Ukraine,LuckyLink via Hotline,59250,UAH,399259,Watch,Medium,Best current exact Ukraine GPU evidence; still check warranty/payment/delivery before final purchase,"01_Market_Data/2026-06-21/GPU/Відеокарта MSI GeForce RTX 5080 16G VENTUS 3X OC - купити в Києві та Україні, вигідна ціна.md",
GPU_02_PL,GPU,2,MSI RTX 5080 Gaming Trio OC 16GB,Poland,Ceneo lead,5599,PLN,465109,Backup,Medium,Better cooler/class than Ventus; costs more,Raw_Captures/GPU,
GPU_02_HU,GPU,2,MSI RTX 5080 Gaming Trio OC 16GB,Hungary,Arukereso broad lead,538440,HUF,538440,Compare,Medium,Fresh Hungary premium MSI row; currently expensive versus Ukraine,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_market_snapshot.csv,
GPU_03_PL,GPU,3,Gigabyte RTX 5080 Gaming OC 16GB,Poland,Ceneo lead,5799,PLN,481723,Backup,Medium,Good long-term Gigabyte option; compare seller/warranty,Raw_Captures/GPU,
GPU_03_HU,GPU,3,Gigabyte RTX 5080 Gaming OC 16GB,Hungary,oaziscomputer.hu,526400,HUF,526400,Compare,Medium,Best Gigabyte Hungary premium-value comparison,Raw_Captures/GPU,
GPU_04_PL,GPU,4,Inno3D RTX 5080 X3 OC 16GB,Poland,Techberg via Ceneo,5099,PLN,463448,Compare,Medium,Fresh exact Poland row is much better than the older broad X3 figure,01_Market_Data/2026-06-21/GPU/Karta graficzna INNO3D GeForce RTX 5080 X3 16 GB GDDR7 DLSS4.md,
GPU_04_HU,GPU,4,Inno3D RTX 5080 X3 OC 16GB,Hungary,Arukereso lead,465640,HUF,465640,Backup,Medium,Best cheap Hungary RTX 5080 value lead,RTX5080_WORKING_SHORTLIST,
GPU_05_PL,GPU,5,Gigabyte RTX 5080 Windforce OC SFF 16GB,Poland,Ceneo lead,5475.58,PLN,443888,Watch,High,Fresh Poland SFF/basic-cooler row; not first long-term choice,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_market_snapshot.csv,
GPU_05_HU,GPU,5,Gigabyte RTX 5080 Windforce OC SFF 16GB,Hungary,Arukereso lead,469990,HUF,469990,Watch,High,Cheap local option but SFF cooler risk,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_market_snapshot.csv,
GPU_02_UA,GPU,2,MSI RTX 5080 Gaming Trio OC 16GB,Ukraine,Hotline exact product,65400,UAH,444596,Watch,Medium,Better cooler class than Ventus from current Ukraine GPU snapshot; seller terms still need final audit,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_market_snapshot.csv,
GPU_06_PL,GPU,6,Zotac RTX 5080 Solid Core OC 16GB,Poland,Allegro exact,5199,PLN,429821,Watch,Medium,Exact Allegro offer captured; check seller and warranty before purchase,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
GPU_07_PL,GPU,7,Gainward RTX 5080 Phoenix 16GB,Poland,x-kom exact,5299,PLN,438088,Watch,Low,Exact x-kom offer with stronger store confidence than marketplace rows,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
GPU_08_PL,GPU,8,Palit RTX 5080 GamingPro OC 16GB,Poland,Allegro exact,5351,PLN,442387,Watch,Medium,Exact Allegro row; valid fallback if seller terms check out,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
GPU_09_PL,GPU,9,MSI RTX 5080 Shadow 3X OC 16GB,Poland,Ceneo broad search,5299,PLN,438088,Watch,High,Cheap broad Poland row with only two shops; exact seller still needed,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
GPU_06_HU,GPU,6,Gainward RTX 5080 Phoenix V1 16GB,Hungary,Arukereso broad lead,450690,HUF,450690,Watch,Medium,Best current Hungary broad RTX 5080 lead; exact store still needed,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_market_snapshot.csv,
GPU_07_HU,GPU,7,Gainward RTX 5080 Phoenix 16GB,Hungary,Arukereso broad lead,458390,HUF,458390,Watch,Medium,Local broad backup; exact store still needed,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_market_snapshot.csv,
GPU_08_HU,GPU,8,Palit RTX 5080 GamingPro 16GB,Hungary,Arukereso broad lead,458390,HUF,458390,Watch,Medium,Local broad backup; exact store still needed,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_market_snapshot.csv,
GPU_09_HU,GPU,9,Manli RTX 5080 Nebula 16GB,Hungary,Arukereso broad search,460250,HUF,460250,Watch,High,Very cheap Hungary broad row but brand and cooler confidence are lower,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
MB_01_PL_BROAD,Motherboard,1,MSI MAG B850 Tomahawk MAX WiFi,Poland,Ceneo broad floor,918.90,PLN,75980,Watch,Medium,Current broad Poland floor across many stores; exact seller still needed before purchase,02_PC_Builds/01_Price_Refresh/2026-06-21/motherboard_market_snapshot.csv,
MB_05_PL,Motherboard,5,ASRock B850 PRO RS AM5,Poland,Ceneo broad lead,578.11,PLN,47794,Backup,Medium,Cheapest decent B850 option in Poland snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/motherboard_market_snapshot.csv,
MB_06_PL,Motherboard,6,Gigabyte B850 AORUS Elite WiFi7,Poland,Ceneo broad lead,751.30,PLN,62113,Backup,Medium,Strong cheaper B850 WiFi7 alternative from Poland snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/motherboard_market_snapshot.csv,
MB_07_PL,Motherboard,7,ASUS TUF Gaming B850 Plus WiFi,Poland,Ceneo broad lead,789.99,PLN,65311,Backup,Medium,ASUS TUF B850 fallback from Poland snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/motherboard_market_snapshot.csv,
MB_05_HU,Motherboard,5,ASRock B850 STEEL LEGEND WiFi,Hungary,Arukereso broad lead,65600,HUF,65600,Backup,Medium,Best-value Hungary B850 backup in current snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/motherboard_market_snapshot.csv,
MB_06_HU,Motherboard,6,ASUS TUF Gaming B850M-Plus WiFi7,Hungary,Arukereso broad lead,67490,HUF,67490,Backup,Medium,Cheaper MicroATX WiFi7 alternative from Hungary snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/motherboard_market_snapshot.csv,
MB_07_HU,Motherboard,7,GIGABYTE B850 AORUS Elite WiFi7,Hungary,Arukereso broad lead,75800,HUF,75800,Backup,Medium,Hungary ATX WiFi7 backup board from snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/motherboard_market_snapshot.csv,
MB_08_HU,Motherboard,8,GIGABYTE X870 EAGLE WiFi7,Hungary,Arukereso broad lead,75930,HUF,75930,Watch,Medium,Legit X870 at B850-like pricing from Hungary snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/motherboard_market_snapshot.csv,
RAM_05_UA,RAM,5,GOODRAM IRDM 64GB 2x32 DDR5-6000 CL30,Ukraine,Hotline broad lead,44472,UAH,302325,Watch,Medium,Ukraine 64GB CL30 backup from current RAM snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/ram_market_snapshot.csv,
RAM_06_UA,RAM,6,Kingston Fury Beast 64GB DDR5-6000 CL30,Ukraine,Hotline broad lead,45499,UAH,309307,Watch,Medium,Ukraine Kingston 64GB CL30 backup from current RAM snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/ram_market_snapshot.csv,
RAM_07_UA,RAM,7,Crucial Pro 64GB DDR5-6000 CL40,Ukraine,Hotline broad lead,36058,UAH,245126,Backup,High,Cheaper 64GB fallback but CL40 is a performance compromise,02_PC_Builds/01_Price_Refresh/2026-06-21/ram_market_snapshot.csv,
RAM_05_PL,RAM,5,Kingston Fury Beast RGB 64GB DDR5-6000 CL30,Poland,Ceneo broad lead,3417.77,PLN,282560,Watch,Medium,Poland Kingston 64GB CL30 backup from current RAM snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/ram_market_snapshot.csv,
RAM_06_PL,RAM,6,G.Skill Aegis 5 64GB DDR5-6000 CL36,Poland,Ceneo broad lead,2999,PLN,247938,Backup,High,Cheaper 64GB fallback but CL36 is below target CL30 tier,02_PC_Builds/01_Price_Refresh/2026-06-21/ram_market_snapshot.csv,
RAM_07_PL,RAM,7,Patriot Viper Venom 64GB DDR5-6000 CL36,Poland,Ceneo broad lead,3099.99,PLN,256288,Backup,High,Cheaper Patriot fallback but CL36 is below target CL30 tier,02_PC_Builds/01_Price_Refresh/2026-06-21/ram_market_snapshot.csv,
RAM_05_HU,RAM,5,Kingston Fury Beast 64GB 2x32 DDR5-6000 CL30,Hungary,Arukereso broad lead,316420,HUF,316420,Backup,Medium,Hungary Kingston 64GB CL30 backup from current RAM snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/ram_market_snapshot.csv,
RAM_06_HU,RAM,6,Silicon Power XPower Zenith 64GB 2x32 DDR5-6000 CL30,Hungary,Pepita marketplace,225090,HUF,225090,Watch,High,Suspiciously cheap exact marketplace row; verify before treating as buyable,02_PC_Builds/01_Price_Refresh/2026-06-21/ram_reviewed_options.csv,
SSD_04_PL,SSD,4,Kioxia Exceria Plus G4 2TB PCIe 5,Poland,Ceneo broad lead,949,PLN,78457,Watch,Medium,Interesting PCIe 5 anomaly cheaper than many PCIe 4 drives; exact store validation needed,02_PC_Builds/01_Price_Refresh/2026-06-21/ssd_market_snapshot.csv,
SSD_05_PL,SSD,5,MSI Spatium M470 PRO 2TB,Poland,Ceneo broad lead,1026.50,PLN,84865,Backup,Medium,Poland PCIe 4 budget option from current SSD snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/ssd_market_snapshot.csv,
SSD_06_PL,SSD,6,Kingston FURY Renegade G5 2TB PCIe 5,Poland,Ceneo broad lead,1475,PLN,121944,Watch,Medium,PCIe 5 backup from current SSD snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/ssd_market_snapshot.csv,
SSD_04_HU,SSD,4,Samsung 990 EVO Plus 2TB,Hungary,Arukereso broad lead,97820,HUF,97820,Backup,Medium,Cheaper Hungary SSD fallback but slower than KC3000 and 990 PRO,02_PC_Builds/01_Price_Refresh/2026-06-21/ssd_market_snapshot.csv,
PSU_04_UA,PSU,4,CHIEFTEC Stealth 1000W Platinum,Ukraine,Hotline broad lead,6453,UAH,43868,Watch,High,Cheapest captured Ukraine Platinum 1000W option; quality and connector details need check,02_PC_Builds/01_Price_Refresh/2026-06-21/psu_market_snapshot.csv,
PSU_05_UA,PSU,5,MSI MAG A1000GL PCIE5,Ukraine,Hotline broad lead,6043,UAH,41081,Watch,High,Very cheap Ukraine 1000W option; verify ATX version and connector details,02_PC_Builds/01_Price_Refresh/2026-06-21/psu_market_snapshot.csv,
PSU_06_UA,PSU,6,be quiet! Power Zone 2 1000W Platinum,Ukraine,Hotline broad lead,8630,UAH,58668,Backup,Medium,Ukraine Platinum be quiet backup from current PSU snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/psu_market_snapshot.csv,
PSU_04_PL,PSU,4,be quiet! Power Zone 2 1000W Platinum,Poland,Ceneo broad lead,639.99,PLN,52910,Backup,Medium,Platinum at Gold-like pricing in Poland snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/psu_market_snapshot.csv,
PSU_04_HU,PSU,4,CHIEFTEC Stealth 1000W Platinum,Hungary,Arukereso broad lead,45000,HUF,45000,Watch,High,Cheapest captured Hungary Platinum 1000W option; quality and connector details need check,02_PC_Builds/01_Price_Refresh/2026-06-21/psu_market_snapshot.csv,
PSU_05_HU,PSU,5,Corsair RM1000e 2025 ATX 3.1,Hungary,Arukereso broad lead,52790,HUF,52790,Backup,Medium,Cheaper Corsair Hungary fallback from current PSU snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/psu_market_snapshot.csv,
PSU_06_HU,PSU,6,be quiet! Power Zone 2 1000W Platinum,Hungary,Arukereso broad lead,57836,HUF,57836,Backup,Medium,Hungary Platinum be quiet backup from current PSU snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/psu_market_snapshot.csv,
COOL_07_PL,Cooler,7,Arctic Liquid Freezer III Pro 360 A-RGB Black,Poland,Ceneo broad lead,399,PLN,32987,Backup,Medium,Poland ARGB Arctic option from current cooler snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/cooler_market_snapshot.csv,
COOL_07_HU,Cooler,7,DeepCool LE360 V2 Black,Hungary,Arukereso broad lead,23990,HUF,23990,Watch,Medium,Hungary non-ARGB DeepCool naming from current cooler snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/cooler_market_snapshot.csv,
GPU_10_PL,GPU,10,Inno3D RTX 5080 X3 OC White 16GB,Poland,Ceneo broad search,5384,PLN,445115,Watch,Medium,White variant captured in Poland broad review; not value leader,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
GPU_11_PL,GPU,11,PNY RTX 5080 Overclocked Triple Fan 16GB,Poland,Ceneo broad search,5506.99,PLN,455283,Watch,Medium,Middle-pack Poland broad GPU row,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
GPU_12_PL,GPU,12,ASUS RTX 5080 Prime OC 16GB,Poland,Ceneo broad search,5590,PLN,462146,Watch,Medium,ASUS Poland option but not value leader,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
GPU_13_PL,GPU,13,Zotac RTX 5080 Solid Core 16GB non-OC,Poland,Ceneo broad search,5599,PLN,462890,Watch,Medium,Valid Poland broad row but above exact Solid Core OC captured lead,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
GPU_14_PL,GPU,14,PNY RTX 5080 ARGB Epic-X Triple Fan OC 16GB,Poland,Ceneo broad search,5637.99,PLN,466113,Watch,Medium,PNY ARGB Poland option but not value leader,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
GPU_15_PL,GPU,15,Palit RTX 5080 GamingPro 16GB,Poland,Ceneo broad lead,5275.47,PLN,436143,Watch,Medium,Good broad Poland lead; exact store still needed,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_market_snapshot.csv,
GPU_10_HU,GPU,10,Gigabyte RTX 5080 Windforce SFF 16GB non-OC,Hungary,Arukereso broad search,465990,HUF,465990,Watch,High,Cheap local Gigabyte row but exact model versus OC row needs care,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
GPU_11_HU,GPU,11,Gainward RTX 5080 Phoenix GS 16GB,Hungary,Arukereso broad search,473690,HUF,473690,Watch,Medium,Valid Hungary row but above Phoenix V1,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
GPU_12_HU,GPU,12,ASUS RTX 5080 Prime OC 16GB,Hungary,Arukereso broad search,487590,HUF,487590,Watch,Medium,ASUS Hungary option but above cheapest local cards,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
GPU_13_HU,GPU,13,Palit RTX 5080 GamingPro OC 16GB,Hungary,Arukereso broad search,488100,HUF,488100,Watch,Medium,OC Palit Hungary row; non-OC Palit is cheaper,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
GPU_14_HU,GPU,14,Inno3D RTX 5080 X3 OC White 16GB,Hungary,Arukereso broad search,488590,HUF,488590,Watch,Medium,White premium variant; not value leader,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
GPU_03_UA,GPU,3,MSI RTX 5080 Gaming Trio OC 16GB offer row 2,Ukraine,Hotline seller row,70796,UAH,481278,Watch,Medium,12-month warranty row for Gaming Trio; worse than 65400 UAH lead,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
GPU_04_UA,GPU,4,MSI RTX 5080 Gaming Trio OC 16GB offer row 4,Ukraine,Hotline seller row,73485,UAH,499558,Watch,Medium,36-month manufacturer warranty row but much higher price,02_PC_Builds/01_Price_Refresh/2026-06-21/gpu_reviewed_options.csv,
MB_08_PL,Motherboard,8,MSI MAG B850 Tomahawk WiFi non-MAX,Poland,Ceneo broad lead,852.37,PLN,70469,Backup,Medium,Cheaper non-MAX MSI variant in Poland snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/motherboard_market_snapshot.csv,
MB_09_PL,Motherboard,9,GIGABYTE X870 GAMING WiFi6,Poland,Ceneo broad lead,818,PLN,67627,Backup,Medium,Cheapest X870 entry in Poland snapshot; WiFi6 not WiFi7,02_PC_Builds/01_Price_Refresh/2026-06-21/motherboard_market_snapshot.csv,
MB_10_PL,Motherboard,10,MSI MAG X870E GAMING PLUS MAX WiFi,Poland,Ceneo broad lead,939,PLN,77631,Watch,Medium,X870E chipset row with good value in Poland snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/motherboard_market_snapshot.csv,
MB_11_PL,Motherboard,11,MSI PRO X870E-P WiFi,Poland,Ceneo broad lead,986,PLN,81516,Backup,Medium,Entry-level X870E board from Poland snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/motherboard_market_snapshot.csv,
PSU_07_HU,PSU,7,be quiet! Pure Power 12 1000W,Hungary,Arukereso broad lead,46900,HUF,46900,Watch,Medium,Older generation 1000W be quiet option in Hungary snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/psu_market_snapshot.csv,
PSU_08_HU,PSU,8,Corsair HX1000i 1000W Platinum,Hungary,Arukereso broad lead,82901,HUF,82901,Watch,Low,Premium Hungary PSU option from current snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/psu_market_snapshot.csv,
PSU_07_UA,PSU,7,be quiet! Dark Power 14 1000W,Ukraine,Hotline broad lead,11920,UAH,81033,Watch,Low,Premium Ukraine PSU option from current snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/psu_market_snapshot.csv,
PSU_08_UA,PSU,8,FSP Hydro G PRO ATX 3.0 1000W,Ukraine,Hotline broad lead,7521,UAH,51128,Watch,Medium,ATX 3.0 not 3.1 but useful Ukraine fallback,02_PC_Builds/01_Price_Refresh/2026-06-21/psu_market_snapshot.csv,
PSU_09_UA,PSU,9,Fractal Design Ion 3 Gold 1000W,Ukraine,Hotline broad lead,9548,UAH,64908,Watch,Medium,Premium Ukraine fallback from current PSU snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/psu_market_snapshot.csv,
SSD_07_PL,SSD,7,Corsair MP700 ELITE 2TB PCIe 5,Poland,Ceneo broad lead,2278,PLN,188331,Watch,Medium,PCIe 5 premium SSD captured in Poland snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/ssd_market_snapshot.csv,
SSD_08_PL,SSD,8,Samsung 9100 PRO 2TB PCIe 5,Poland,Ceneo broad lead,1870.25,PLN,154620,Watch,Medium,High-end PCIe 5 Samsung option captured in Poland snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/ssd_market_snapshot.csv,
COOL_08_PL,Cooler,8,DeepCool LE360 V2 Black,Poland,Ceneo broad lead,282.82,PLN,23382,Watch,Medium,Poland non-ARGB DeepCool naming from current cooler snapshot,02_PC_Builds/01_Price_Refresh/2026-06-21/cooler_market_snapshot.csv,
GPU_16_HU,GPU,1,Palit RTX 5070 Ti GamingPro-S OC 16GB,Hungary,Arukereso lead,331500,HUF,331500,Compare,Medium,Cheapest HU 5070 Ti by far; 8 offers available,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_HU_Arukereso.md,https://www.arukereso.hu/videokartya-c3142/palit/geforce-rtx-5070-ti-gamingpro-s-oc-16gb-gddr7-256bit-ne7507ts19t2-gb2031u-p1177187171/
GPU_17_HU,GPU,1,MSI RTX 5070 Ti Ventus 3X OC 16GB,Hungary,Arukereso lead,368390,HUF,368390,Compare,Medium,Value MSI 5070 Ti; 15 offers,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_HU_Arukereso.md,https://www.arukereso.hu/videokartya-c3142/msi/geforce-rtx-5070-ti-ventus-3x-oc-16gb-gddr7-256bit-p1178125444/
GPU_18_HU,GPU,1,Gigabyte RTX 5070 Ti Windforce OC SFF 16GB,Hungary,Arukereso lead,369690,HUF,369690,Compare,Medium,Good value Gigabyte; 27 offers,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_HU_Arukereso.md,https://www.arukereso.hu/videokartya-c3142/gigabyte/geforce-rtx-5070-ti-windforce-oc-sff-16gb-gddr7-256bit-gv-n507twf3oc-16gd-p1178125681/
GPU_19_HU,GPU,2,ASUS RTX 5070 Ti Prime OC 16GB,Hungary,Arukereso lead,372350,HUF,372350,Compare,Medium,Well-priced ASUS; 29 offers,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_HU_Arukereso.md,https://www.arukereso.hu/videokartya-c3142/asus/geforce-rtx-5070-ti-prime-oc-16gb-gddr7-256bit-prime-rtx5070ti-o16g-p1178128726/
GPU_20_HU,GPU,3,MSI RTX 5070 Ti Gaming Trio OC 16GB,Hungary,Arukereso lead,418445,HUF,418445,Backup,Medium,Premium MSI Trio; 21 offers,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_HU_Arukereso.md,https://www.arukereso.hu/videokartya-c3142/msi/geforce-rtx-5070-ti-gaming-trio-oc-16gb-gddr7-256bit-p1178125445/
GPU_21_HU,GPU,3,Gigabyte RTX 5070 Ti Gaming OC 16GB,Hungary,Arukereso lead,386450,HUF,386450,Compare,Medium,Premium Gigabyte; 15 offers,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_HU_Arukereso.md,https://www.arukereso.hu/videokartya-c3142/gigabyte/geforce-rtx-5070-ti-gaming-oc-16gb-gddr7-256bit-gv-n507tgaming-oc-16gd-p1178125683/
GPU_22_PL,GPU,1,Palit RTX 5070 Ti Gaming Pro-S 16GB,Poland,Ceneo lead,3899,PLN,322371,Compare,Low,Cheapest 5070 Ti in Poland across all brands,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_PL_Ceneo.md,https://www.ceneo.pl/184542084
GPU_23_PL,GPU,1,Zotac RTX 5070 Ti Solid OC 16GB,Poland,Ceneo lead,3999,PLN,330641,Compare,Low,Good entry OC value,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_PL_Ceneo.md,https://www.ceneo.pl/182025000
GPU_24_PL,GPU,1,MSI RTX 5070 Ti Ventus 3X OC 16GB,Poland,Ceneo lead,4095,PLN,338578,Compare,Medium,Value MSI; known brand,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_PL_Ceneo.md,https://www.ceneo.pl/182025028
GPU_25_PL,GPU,2,Inno3D RTX 5070 Ti X3 16GB,Poland,Ceneo lead,4229,PLN,349670,Compare,Medium,Entry Inno3D; valid fallback,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_PL_Ceneo.md,https://www.ceneo.pl/181517101
GPU_26_PL,GPU,2,Gigabyte RTX 5070 Ti Eagle OC SFF 16GB,Poland,Ceneo lead,4221.79,PLN,349072,Compare,Low,Compact SFF; good temps,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_PL_Ceneo.md,https://www.ceneo.pl/181816778
GPU_27_PL,GPU,3,MSI RTX 5070 Ti Gaming Trio OC 16GB,Poland,Ceneo lead,4299,PLN,355457,Backup,Low,Premium MSI Trio cooler in Poland,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_PL_Ceneo.md,https://www.ceneo.pl/184542114
GPU_28_PL,GPU,4,Asus TUF RTX 5070 Ti OC 16GB,Poland,Ceneo lead,4499,PLN,371996,Backup,Medium,Mid-tier ASUS TUF series,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_PL_Ceneo.md,https://www.ceneo.pl/183871886
GPU_29_PL,GPU,5,Asus ROG Strix RTX 5070 Ti OC 16GB,Poland,Ceneo lead,5299,PLN,438088,Watch,Medium,Premium ROG; expensive,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_PL_Ceneo.md,https://www.ceneo.pl/183156256
GPU_30_UA,GPU,1,Gigabyte RTX 5070 Ti Eagle OC ICE SFF 16GB,Ukraine,Hotline exact,45146,UAH,304266,Compare,Medium,Cheapest 5070 Ti in UA; white SFF,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_UA_Hotline.md,https://hotline.ua/ua/computer-videokarty/gigabyte-geforce-rtx-5070-ti-eagle-oc-ice-sff-16g-gv-n507teagleoc-ice-16gd/
GPU_31_UA,GPU,1,MSI RTX 5070 Ti Ventus 3X OC 16GB,Ukraine,Hotline exact,45795,UAH,308678,Compare,Medium,Value MSI; 73 offers (most),01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_UA_Hotline.md,https://hotline.ua/ua/computer-videokarty/msi-geforce-rtx-5070-ti-16g-ventus-3x-oc-plus/
GPU_32_UA,GPU,2,Gigabyte RTX 5070 Ti Eagle OC SFF 16GB,Ukraine,Hotline exact,45542,UAH,306951,Compare,Medium,SFF Gigabyte compact,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_UA_Hotline.md,https://hotline.ua/ua/computer-videokarty/gigabyte-geforce-rtx-5070-ti-eagle-oc-sff-16g-gv-n507teagle-oc-16gd/
GPU_33_UA,GPU,2,Palit RTX 5070 Ti GamingPro-S 16GB,Ukraine,Hotline exact,46479,UAH,313238,Compare,Medium,Value Palit; 20 offers,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_UA_Hotline.md,https://hotline.ua/ua/computer-videokarty/palit-geforce-rtx-5070-ti-gamingpro-s-ne7507t019t2-gb2031u/
GPU_34_UA,GPU,3,MSI RTX 5070 Ti Gaming Trio OC 16GB,Ukraine,Hotline exact,52000,UAH,350477,Backup,Medium,Premium MSI; 42 offers,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_UA_Hotline.md,https://hotline.ua/ua/computer-videokarty/msi-geforce-rtx-5070-ti-16g-gaming-trio-oc/
GPU_35_UA,GPU,3,Gigabyte RTX 5070 Ti Gaming OC 16GB,Ukraine,Hotline exact,49299,UAH,333266,Backup,Medium,Premium Gigabyte; 57 offers,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_UA_Hotline.md,https://hotline.ua/ua/computer-videokarty/gigabyte-geforce-rtx-5070-ti-gaming-oc-16g-gv-n507tgaming-oc-16gd/
GPU_36_UA,GPU,3,INNO3D RTX 5070 Ti X3 OC 16GB,Ukraine,Hotline exact,48400,UAH,326214,Backup,Medium,Entry Inno3D compact,01_Market_Data/2026-06-21/GPU/5070_Ti/2026-06-21_5070_Ti_UA_Hotline.md,https://hotline.ua/ua/computer-videokarty/inno3d-geforce-rtx-5070-ti-x3-oc-n507t3-16d7x-176068n/"""

    EU_LOWEST_CSV_DATA = """Selected_ID,EU_Model,EU_Price,EU_Currency,EU_Store,EU_Country,Match_Quality,Note,Source
GPU_01_PL,MSI RTX 5080 Ventus 3X OC 16GB,1332,EUR,GPUTracker low range,EU market,Good,"Exact model appeared around 1332-1373 EUR in wider EU tracker listings; verify seller/shipping/warranty before treating as buyable.",PC_BUILD_TOOLING.md
RAM_01_PL,Patriot Viper Venom 64GB 2x32 DDR5-6000 CL30,900,EUR,Proshop.pl,Poland,Good,"Exact PVV564G600C30K / CL30 wider-EU sanity check from GPUtracker/Proshop. Not cheaper than the Allegro/Ceneo Poland lead, but confirms CL30 and separates it from CL36 SKU PVV564G600C36K.",Raw_Captures/RAM
RAM_02_PL,Kingston Fury Beast EXPO 64GB 2x32 DDR5-6000 CL30,,,,,Need exact capture,"Need exact EU-low capture for Kingston 64GB DDR5-6000 CL30 EXPO kit, not generic 64GB DDR5 search.",PC_BUILD_TOOLING.md
RAM_03_PL,GOODRAM IRDM 64GB 2x32 DDR5-6000 CL30,,,,,Need exact capture,"Need exact EU-low capture for GOODRAM IRDM 64GB 6000 CL30 kit.",PC_BUILD_TOOLING.md
RAM_04_PL,Patriot Viper Venom 32GB 2x16 DDR5-6000 CL30,,,,,Need exact capture,"Need exact PVV532G600C30K EU-low capture. Current Poland/Hungary comparison exists, but wider EU-low is not locked.",PC_BUILD_TOOLING.md"""

    # Parse CSV from embedded string (no filesystem)
    parts = pd.read_csv(StringIO(PARTS_CSV_DATA))
    parts["Price"] = pd.to_numeric(parts["Price"], errors="coerce").fillna(0)
    parts["HUF_Est"] = pd.to_numeric(parts["HUF_Est"], errors="coerce").fillna(0)

    eu_lowest = pd.read_csv(StringIO(EU_LOWEST_CSV_DATA))
    eu_lowest["EU_Price"] = pd.to_numeric(eu_lowest["EU_Price"], errors="coerce")
    
    return datetime, eu_lowest, html, json, mo, parts, pd, StringIO


@app.cell
def _(datetime, json):
    def load_rates():
        """Load exchange rates from public APIs with fallback."""
        rates = {
            "source": "saved fallback",
            "checked": "offline fallback",
            "eur_to_huf": 352.88,
            "eur_to_uah": 52.3396,
            "pln_to_uah": 12.2981,
            "huf_to_uah": 0.1484,
        }

        # On desktop, use urllib; in WASM, fetch API handles it
        try:
            from urllib.request import Request, urlopen
            
            req = Request(
                "https://api.monobank.ua/bank/currency",
                headers={"User-Agent": "pc-build-research/1.0"},
            )
            mono = json.load(urlopen(req, timeout=6))
            for row in mono:
                pair = (row.get("currencyCodeA"), row.get("currencyCodeB"))
                if pair == (978, 980):
                    rates["eur_to_uah"] = float(row.get("rateSell") or row.get("rateCross"))
                elif pair == (985, 980):
                    rates["pln_to_uah"] = float(row.get("rateCross"))
                elif pair == (348, 980):
                    rates["huf_to_uah"] = float(row.get("rateCross"))
            rates["source"] = "Monobank public card/payment rates"
            rates["checked"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        except Exception:
            # urllib won't work in WASM, but that's OK—fallback rates are hardcoded
            pass

        try:
            from urllib.request import Request, urlopen
            
            req = Request(
                "https://api.frankfurter.app/latest?from=EUR&to=HUF",
                headers={"User-Agent": "pc-build-research/1.0"},
            )
            ecb = json.load(urlopen(req, timeout=6))
            rates["eur_to_huf"] = float(ecb["rates"]["HUF"])
        except Exception:
            pass

        rates["pln_to_huf"] = rates["pln_to_uah"] / rates["huf_to_uah"]
        return rates

    rates = load_rates()
    return (rates,)


@app.cell
def _():
    builds = {
        "HU-core (5080)": {
            "CPU": "CPU_01_HU",
            "Main board": "MB_01_HU",
            "Memory": "RAM_01_HU",
            "Storage": "SSD_01_HU",
            "Power supply": "PSU_01_HU",
            "Cooler": "COOL_02_HU",
            "Case": "CASE_12_HU",
            "Graphics card": "GPU_01_UA",
        },
        "PL-core (5080)": {
            "CPU": "CPU_01_PL",
            "Main board": "MB_01_PL",
            "Memory": "RAM_01_PL",
            "Storage": "SSD_01_PL",
            "Power supply": "PSU_01_PL",
            "Cooler": "COOL_02_PL",
            "Case": "CASE_12_HU",
            "Graphics card": "GPU_01_UA",
        },
        "Lowest UA+PL+HU (5080)": {
            "CPU": "CPU_01_UA",
            "Main board": "MB_05_PL",
            "Memory": "RAM_01_PL",
            "Storage": "SSD_04_PL",
            "Power supply": "PSU_01_PL",
            "Cooler": "COOL_04_PL",
            "Case": "CASE_02_HU",
            "Graphics card": "GPU_01_UA",
        },
        "5070 Ti value mix": {
            "CPU": "CPU_01_UA",
            "Main board": "MB_01_PL",
            "Memory": "RAM_01_PL",
            "Storage": "SSD_01_PL",
            "Power supply": "PSU_01_PL",
            "Cooler": "COOL_02_PL",
            "Case": "CASE_12_HU",
            "Graphics card": "GPU_22_PL",
        },
        "All PL (5080)": {
            "CPU": "CPU_01_PL",
            "Main board": "MB_01_PL",
            "Memory": "RAM_01_PL",
            "Storage": "SSD_01_PL",
            "Power supply": "PSU_03_PL",
            "Cooler": "COOL_02_PL",
            "Case": "CASE_05_HU",
            "Graphics card": "GPU_01_PL",
        },
    }

    compare_ids = {
        "CPU_01_PL": "CPU_01_HU",
        "CPU_01_UA": "CPU_01_HU",
        "CPU_02_PL": "CPU_02_HU",
        "CPU_03_PL": "CPU_03_HU",
        "MB_01_PL": "MB_01_HU",
        "MB_01_UA": "MB_01_HU",
        "MB_02_PL": "MB_02_HU",
        "MB_04_PL": "MB_04_HU",
        "RAM_01_PL": "RAM_01_HU",
        "RAM_01_UA": "RAM_01_HU",
        "RAM_02_PL": "RAM_02_HU",
        "RAM_03_PL": "RAM_03_HU",
        "RAM_04_PL": "RAM_04_HU",
        "RAM_04_UA": "RAM_04_HU",
        "SSD_01_PL": "SSD_01_HU",
        "SSD_01_UA": "SSD_01_HU",
        "SSD_02_PL": "SSD_02_HU",
        "SSD_03_UA": "SSD_03_HU",
        "COOL_02_PL": "COOL_02_HU",
        "COOL_03_PL": "COOL_03_HU",
        "COOL_03_UA": "COOL_03_HU",
        "COOL_04_PL": "COOL_04_HU",
        "COOL_04_UA": "COOL_04_HU",
        "COOL_06_PL": "COOL_06_HU",
        "COOL_06_UA": "COOL_06_HU",
        "PSU_01_PL": "PSU_01_HU",
        "PSU_01_UA": "PSU_01_HU",
        "PSU_02_PL": "PSU_02_HU",
        "PSU_02_UA": "PSU_02_HU",
        "PSU_03_PL": "PSU_03_HU",
        "PSU_03_UA": "PSU_03_HU",
        "GPU_01_PL": "GPU_01_HU",
        "GPU_01_UA": "GPU_01_HU",
        "GPU_02_PL": "GPU_02_HU",
        "GPU_03_PL": "GPU_03_HU",
        "GPU_04_PL": "GPU_04_HU",
        "GPU_05_PL": "GPU_05_HU",
        "GPU_16_HU": "GPU_17_HU",
        "GPU_17_HU": "GPU_19_HU",
        "GPU_18_HU": "GPU_19_HU",
        "GPU_22_PL": "GPU_17_HU",
        "GPU_23_PL": "GPU_17_HU",
        "GPU_24_PL": "GPU_17_HU",
        "GPU_26_PL": "GPU_18_HU",
        "GPU_30_UA": "GPU_17_HU",
        "GPU_31_UA": "GPU_17_HU",
    }
    return builds, compare_ids


@app.cell
def _(eu_lowest, html, parts, pd, rates):
    parts_by_id = parts.set_index("ID")
    eu_lowest_by_id = eu_lowest.set_index("Selected_ID")

    def esc(value):
        return html.escape(str(value))

    def huf_text(value):
        return f"{int(round(value)):,.0f} HUF"

    def number_text(value):
        return f"{int(round(value)):,.0f}"

    def price_value_to_huf(price, currency, fallback=0):
        currency = str(currency).upper()
        price = float(price)
        if currency == "HUF":
            return price
        if currency == "UAH":
            return price / rates["huf_to_uah"]
        if currency == "PLN":
            return price * rates["pln_to_huf"]
        if currency == "EUR":
            return price * rates["eur_to_huf"]
        return float(fallback)

    def price_value_to_uah(price, currency, fallback=0):
        currency = str(currency).upper()
        price = float(price)
        if currency == "UAH":
            return price
        if currency == "HUF":
            return price * rates["huf_to_uah"]
        if currency == "PLN":
            return price * rates["pln_to_uah"]
        if currency == "EUR":
            return price * rates["eur_to_uah"]
        return float(fallback)

    def price_to_huf(item):
        return price_value_to_huf(item["Price"], item["Currency"], item["HUF_Est"])

    def price_to_uah(item):
        return price_value_to_uah(item["Price"], item["Currency"], 0)

    def original_price(item):
        currency = str(item["Currency"]).upper()
        price = float(item["Price"])
        return f"{price:,.0f} {currency}"

    def build_table(build_parts, compare_map):
        rows = []
        for part_name, item_id in build_parts.items():
            item = parts_by_id.loc[item_id]
            huf = price_to_huf(item)
            uah = price_to_uah(item)
            compare_id = compare_map.get(item_id, "")
            compare_huf = price_to_huf(parts_by_id.loc[compare_id]) if compare_id in parts_by_id.index else 0
            compare_uah = price_to_uah(parts_by_id.loc[compare_id]) if compare_id in parts_by_id.index else 0
            saving = max(0, compare_huf - huf) if compare_huf else 0
            saving_uah = max(0, compare_uah - uah) if compare_uah else 0
            rows.append(
                {
                    "ID": item_id,
                    "Part": part_name,
                    "Model": item["Option"],
                    "Market": item["Market"],
                    "Store": item["Store"],
                    "Currency": str(item["Currency"]).upper(),
                    "RawPrice": float(item["Price"]),
                    "Price": original_price(item),
                    "HUF": int(round(huf)),
                    "UAH": int(round(uah)),
                    "Saving": int(round(saving)),
                    "Saving_UAH": int(round(saving_uah)),
                    "URL": str(item.get("URL", "")),
                }
            )
        return pd.DataFrame(rows)

    def eu_lowest_table(selected_df):
        rows = []
        for _, selected in selected_df.iterrows():
            item_id = selected["ID"]
            own_huf = float(selected["HUF"])
            own_uah = float(selected["UAH"])
            if item_id in eu_lowest_by_id.index:
                market = eu_lowest_by_id.loc[item_id]
                eu_price = market.get("EU_Price")
                eu_currency = str(market.get("EU_Currency") or "").upper()
                if pd.notna(eu_price) and eu_currency:
                    eu_huf = price_value_to_huf(eu_price, eu_currency)
                    eu_uah = eu_huf * rates["huf_to_uah"]
                    eu_text = f"{float(eu_price):,.0f} {eu_currency}"
                    diff_huf = own_huf - eu_huf
                    diff_uah = own_uah - eu_uah
                else:
                    eu_huf = None
                    eu_uah = None
                    eu_text = "Need capture"
                    diff_huf = None
                    diff_uah = None
                rows.append(
                    {
                        "Part": selected["Part"],
                        "Selected": selected["Model"],
                        "Our_Price": selected["Price"],
                        "Our_HUF": int(round(own_huf)),
                        "Our_UAH": int(round(own_uah)),
                        "EU_Low": eu_text,
                        "EU_HUF": int(round(eu_huf)) if eu_huf is not None else None,
                        "EU_UAH": int(round(eu_uah)) if eu_uah is not None else None,
                        "Difference_HUF": int(round(diff_huf)) if diff_huf is not None else None,
                        "Difference_UAH": int(round(diff_uah)) if diff_uah is not None else None,
                        "Match": market.get("Match_Quality", ""),
                        "Note": market.get("Note", ""),
                    }
                )
            else:
                rows.append(
                    {
                        "Part": selected["Part"],
                        "Selected": selected["Model"],
                        "Our_Price": selected["Price"],
                        "Our_HUF": int(round(own_huf)),
                        "Our_UAH": int(round(own_uah)),
                        "EU_Low": "Need capture",
                        "EU_HUF": None,
                        "EU_UAH": None,
                        "Difference_HUF": None,
                        "Difference_UAH": None,
                        "Match": "Missing",
                        "Note": "No wider-EU lowest-price capture yet for this selected option.",
                    }
                )
        return pd.DataFrame(rows)

    return build_table, esc, eu_lowest_table, huf_text, number_text


@app.cell
def _(mo):
    mo.Html(
        """
        <style>
          /* ===== WIDER, CONSISTENT LAYOUT ===== */
          body {
            background: #ffffff;
            color: #111111;
            margin: 0;
            padding: 0;
            font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
          }

          h1, h2, h3, p, label, select, button {
            font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif !important;
          }
          h2 {
            color: #111111;
            font-weight: 700;
            letter-spacing: -0.01em;
            font-size: 18px;
            margin: 0 0 8px;
          }

          .pc-wrap {
            width: 100% !important;
            max-width: 98% !important;
            margin-left: auto !important;
            margin-right: auto !important;
            padding: 0 16px !important;
            background: #ffffff;
            color: #111111;
            font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
          }
          .pc-title {
            font-size: 26px;
            font-weight: 700;
            margin: 0 0 4px;
            color: #111111;
            letter-spacing: -0.01em;
          }
          .pc-subtitle {
            color: #4a5568;
            font-size: 13px;
            max-width: 780px;
            line-height: 1.4;
            margin-bottom: 4px;
          }
          .pc-section {
            margin-top: 14px;
            margin-bottom: 0px !important;
          }
          .pc-panel {
            margin-top: 10px;
            margin-bottom: 0px !important;
            padding: 16px 20px;
            padding-bottom: 20px !important;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            background: #fbfdff;
            box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
          }
          .pc-panel-tight {
            padding-top: 14px;
            padding-bottom: 14px;
          }
          .pc-control-shell {
            margin-top: 0;
            padding: 14px 18px 12px;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            background: #fbfdff;
            box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
            width: 100%;
            max-width: 100%;
            box-sizing: border-box;
          }
          .pc-control-shell .pc-section-title {
            margin-bottom: 2px;
          }
          .pc-control-shell .pc-section-subtitle {
            margin-bottom: 10px;
          }
          .pc-section-title {
            margin: 0 0 2px;
            font-size: 16px;
            font-weight: 700;
            color: #111111;
          }
          .pc-section-subtitle {
            color: #64748b;
            font-size: 13px;
            line-height: 1.4;
            margin-bottom: 6px;
          }
          .pc-divider {
            height: 1px;
            background: #e2e8f0;
            margin: 14px 0 0;
          }
          .pc-card-row {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin-top: 8px;
          }
          .pc-pill {
            display: inline-block;
            padding: 4px 9px;
            border-radius: 999px;
            font-size: 11px;
            font-weight: 700;
            line-height: 1;
          }
          .pc-pol {
            background: #e8f0ff;
            color: #1d4ed8;
          }
          .pc-hu {
            background: #eafaf0;
            color: #047857;
          }
          .pc-ua {
            background: #fff4e5;
            color: #b45309;
          }
          .pc-card {
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            background: #f7fafc;
            padding: 14px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            transition: border-color 1.8s ease-out, box-shadow 1.8s ease-out, background-color 1.8s ease-out;
          }
          .pc-label {
            color: #4a5568;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: .05em;
            font-weight: 600;
          }
          .pc-value {
            color: #111111;
            font-size: 22px;
            font-weight: 800;
            margin-top: 6px;
          }
          .pc-value-small {
            font-size: 16px;
            font-weight: 750;
            margin-top: 4px;
          }
          .pc-muted {
            color: #718096;
            font-size: 12px;
            margin-top: 4px;
            line-height: 1.4;
          }
          .pc-save {
            color: #2c7a4d;
            font-weight: 800;
          }
          .pc-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 8px;
            font-size: 12.5px;
            background: #ffffff;
          }
          .pc-table-main {
            table-layout: fixed;
          }
          .pc-table th {
            color: #4a5568;
            text-align: left;
            padding: 7px 6px;
            border-bottom: 1px solid #d8dee8;
            background: #eef4ff;
            line-height: 1.2;
            vertical-align: bottom;
            font-weight: 600;
            transition: background-color 800ms ease, color 800ms ease;
          }
          .pc-table th.pc-num {
            text-align: right;
          }
          .pc-head-compact {
            display: inline-block;
            line-height: 1.1;
          }
          .pc-table td {
            padding: 7px 6px;
            border-bottom: 1px solid #e2e8f0;
            vertical-align: middle;
            color: #111111;
            background: transparent;
            transition: background-color 1.8s ease-out, color 1.8s ease-out, box-shadow 1.8s ease-out;
          }
          .pc-table tfoot td {
            background: #eef4ff;
          }
          .pc-table tfoot td {
            border-top: 2px solid #d8dee8;
            font-weight: 750;
          }
          .pc-num {
            text-align: right;
            white-space: nowrap;
            font-variant-numeric: tabular-nums;
          }
          .pc-col-price,
          .pc-col-huf,
          .pc-col-uah,
          .pc-col-total {
            background: transparent !important;
          }
          .pc-col-part {
            width: 7%;
          }
          .pc-col-model {
            width: 30%;
          }
          .pc-col-market {
            width: 5%;
          }
          .pc-col-store {
            width: 14%;
          }
          .pc-col-store a {
            color: inherit;
            text-decoration: underline;
            text-decoration-style: dotted;
          }
          .pc-col-store a:hover {
            color: #2563eb;
            text-decoration-style: solid;
          }
          .pc-col-store-price {
            width: 10%;
          }
          .pc-col-huf-est,
          .pc-col-uah-est {
            width: 10%;
          }
          .pc-col-delta {
            width: 4%;
          }
          .pc-build-grid {
            display: grid;
            grid-template-columns: 140px minmax(0, 1fr);
            gap: 10px 16px;
            align-items: center;
            margin-top: 6px;
          }
          .pc-build-stack {
            margin-top: 4px;
          }
          .pc-build-label {
            font-weight: 600;
            color: #1f2937;
            font-size: 13px;
            min-width: 120px;
            white-space: nowrap;
          }
          .pc-select-block select {
            min-height: 38px;
            border-radius: 10px !important;
            box-shadow: 0 1px 2px rgba(15, 23, 42, 0.05);
            width: 100% !important;
            max-width: 100% !important;
          }
          .pc-hstack-wrapper {
            width: 100%;
          }
          .pc-hstack-wrapper {
            width: 100%;
          }
          .pc-hstack-wrapper select {
            flex: 1 1 auto !important;
            width: 100% !important;
            min-width: 0 !important;
          }
          /* Make marimo hstack rows in Change Parts fill width */
          .pc-parts-shell .x-rows > div {
            width: 100% !important;
          }
          .pc-parts-shell .x-rows > div > div {
            flex: 1 1 100% !important;
          }
          .pc-parts-shell select {
            width: 100% !important;
            max-width: 100% !important;
          }
          .pc-parts-shell > .x-rows > div {
            width: 100% !important;
          }
          .pc-select-block {
            margin-top: 0;
            margin-bottom: 6px;
          }
          .pc-table-kicker {
            margin: 0 0 10px;
            font-size: 16px;
            font-weight: 700;
            color: #111111;
          }
          .pc-table thead th.pc-th-delta {
            color: #64748b;
            font-size: 12px;
            letter-spacing: 0.01em;
          }
          .pc-table thead th.pc-th-delta .pc-head-compact {
            font-weight: 700;
          }
          .pc-fx-stack {
            display: grid;
            gap: 14px;
          }
          .pc-basket-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 16px;
            margin-top: 14px;
          }
          .pc-basket-card {
            border: 1px solid #e2e8f0;
            border-radius: 14px;
            background: #ffffff;
            padding: 16px 18px 20px;
            display: flex;
            flex-direction: column;
          }
          .pc-basket-title {
            font-size: 15px;
            font-weight: 700;
            color: #111111;
            margin: 0 0 4px;
          }
          .pc-basket-subtitle {
            color: #64748b;
            font-size: 12px;
            margin: 0 0 10px;
          }
          .pc-basket-total {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            gap: 12px;
            border-top: 1px solid #d8dee8;
            margin-top: auto;
            padding-top: 14px;
            font-weight: 700;
          }
          .pc-kicker {
            display: inline-block;
            margin-bottom: 10px;
            padding: 4px 10px;
            border-radius: 999px;
            background: #eef4ff;
            color: #334155;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.04em;
          }
          .pc-note-soft {
            border: 1px solid #dbeafe;
            background: #f8fbff;
            border-radius: 12px;
            padding: 12px 14px;
            color: #334155;
          }
          .pc-note {
            border-left: 3px solid #3182ce;
            padding-left: 12px;
            color: #2d3748;
            margin-top: 10px;
            background: #ebf8ff;
            padding: 10px;
            border-radius: 4px;
            font-size: 12px;
            line-height: 1.45;
          }
          @media (max-width: 980px) {
            .pc-card-row {
              grid-template-columns: 1fr;
              gap: 8px;
            }
            .pc-basket-grid {
              grid-template-columns: 1fr;
              gap: 12px;
            }
            .pc-build-grid {
              grid-template-columns: 1fr;
              gap: 6px;
            }
            .pc-build-label {
              margin-top: 4px;
            }
            .pc-wrap {
              padding: 0 14px !important;
            }
          }

          .pc-flash-up-a,
          .pc-flash-up-b {
            animation: pcFlashUp 5s ease-out;
          }
          .pc-flash-down-a,
          .pc-flash-down-b {
            animation: pcFlashDown 5s ease-out;
          }
          .pc-flash-neutral-a,
          .pc-flash-neutral-b {
            animation: pcFlashNeutral 5s ease-out;
          }
          .pc-card-flash-up-a,
          .pc-card-flash-up-b {
            animation: pcCardFlashUp 5s ease-out;
          }
          .pc-card-flash-down-a,
          .pc-card-flash-down-b {
            animation: pcCardFlashDown 5s ease-out;
          }
          .pc-card-flash-neutral-a,
          .pc-card-flash-neutral-b {
            animation: pcCardFlashNeutral 5s ease-out;
          }
          .pc-delta {
            min-width: 64px;
            font-size: 12px;
            font-weight: 700;
            opacity: 0;
          }
          .pc-delta-up-a,
          .pc-delta-up-b {
            animation: pcDeltaUp 5s ease-out forwards;
          }
          .pc-delta-down-a,
          .pc-delta-down-b {
            animation: pcDeltaDown 5s ease-out forwards;
          }

          @keyframes pcFlashNeutral {
            0% { background: #fff3bf; box-shadow: inset 0 0 0 999px rgba(255, 243, 191, 0.82); }
            100% { background: transparent; box-shadow: inset 0 0 0 999px rgba(255, 243, 191, 0); }
          }

          @keyframes pcFlashUp {
            0% { background: #ffe3e3; color: #8b1e1e; box-shadow: inset 0 0 0 999px rgba(255, 227, 227, 0.92); }
            100% { background: transparent; color: inherit; box-shadow: inset 0 0 0 999px rgba(255, 227, 227, 0); }
          }

          @keyframes pcFlashDown {
            0% { background: #d8f5dc; color: #1b5e20; box-shadow: inset 0 0 0 999px rgba(216, 245, 220, 0.95); }
            100% { background: transparent; color: inherit; box-shadow: inset 0 0 0 999px rgba(216, 245, 220, 0); }
          }

          @keyframes pcCardFlashUp {
            0% { border-color: #ef9a9a; box-shadow: 0 0 0 4px rgba(239, 154, 154, 0.38); background: #fffafa; }
            100% { border-color: #e2e8f0; box-shadow: 0 0 0 0 rgba(239, 154, 154, 0); background: #f7fafc; }
          }

          @keyframes pcCardFlashDown {
            0% { border-color: #86d993; box-shadow: 0 0 0 4px rgba(134, 217, 147, 0.40); background: #fbfffc; }
            100% { border-color: #e2e8f0; box-shadow: 0 0 0 0 rgba(134, 217, 147, 0); background: #f7fafc; }
          }

          @keyframes pcCardFlashNeutral {
            0% { border-color: #f2cc60; box-shadow: 0 0 0 4px rgba(242, 204, 96, 0.38); background: #fffef8; }
            100% { border-color: #e2e8f0; box-shadow: 0 0 0 0 rgba(242, 204, 96, 0); background: #f7fafc; }
          }

          @keyframes pcDeltaUp {
            0% { color: #8b1e1e; opacity: 1; }
            70% { color: #8b1e1e; opacity: 1; }
            100% { color: transparent; opacity: 0; }
          }

          @keyframes pcDeltaDown {
            0% { color: #1b5e20; opacity: 1; }
            70% { color: #1b5e20; opacity: 1; }
            100% { color: transparent; opacity: 0; }
          }

          /* .pc-pill, .pc-pol, .pc-hu, .pc-note — defined above in first stylesheet */
          input, select, textarea {
            background: #ffffff !important;
            color: #111111 !important;
            border: 1px solid #cbd5e1 !important;
          }
        </style>
        <div class="pc-wrap">
          <div class="pc-title">PC Build Planner</div>
          <div class="pc-subtitle">
            Ukraine-first planner for a buyer paying in UAH. Poland and Hungary stay visible as comparison or source baskets.
          </div>
        </div>
        """
    )
    return


@app.cell
def _(builds, mo):
    build_choice = mo.ui.dropdown(
        options=list(builds.keys()),
        value="HU-core (5080)",
        label="",
        full_width=True,
    )
    build_selector_ui = mo.vstack(
        [
            mo.Html(
                """
                <div class="pc-wrap pc-select-block" style="margin-top: 0; margin-bottom: 8px;">
                  <div class="pc-control-shell">
                    <div class="pc-section-title">Build selection</div>
                    <div class="pc-section-subtitle">Start with HU-core build, then swap any part, then swap any source or part below.</div>
                """
            ),
            build_choice,
            mo.Html(
                """
                  </div>
                </div>
                """
            ),
        ],
        gap=0,
    )
    build_selector_ui
    return (build_choice,)


@app.cell
def _(mo):
    get_previous_snapshot, set_previous_snapshot = mo.state(
        {"row_ids": {}, "values": {}, "revision": 0}
    )
    return get_previous_snapshot, set_previous_snapshot


@app.cell
def _(build_choice, builds, mo, parts):
    market_order = ["Ukraine", "Poland", "Hungary", "No GPU"]

    def market_for(item_id):
        match = parts[parts["ID"].eq(item_id)]
        if match.empty:
            return "Ukraine"
        return str(match.iloc[0]["Market"])

    def markets_for(part):
        available = set(parts.loc[parts["Part"].eq(part), "Market"].astype(str))
        return [market for market in market_order if market in available]

    _base_parts = builds[build_choice.value]

    cpu_country = mo.ui.dropdown(
        options=markets_for("CPU"),
        value=market_for(_base_parts["CPU"]),
        full_width=True,
    )
    board_country = mo.ui.dropdown(
        options=markets_for("Motherboard"),
        value=market_for(_base_parts["Main board"]),
        full_width=True,
    )
    memory_country = mo.ui.dropdown(
        options=markets_for("RAM"),
        value=market_for(_base_parts["Memory"]),
        full_width=True,
    )
    storage_country = mo.ui.dropdown(
        options=markets_for("SSD"),
        value=market_for(_base_parts["Storage"]),
        full_width=True,
    )
    psu_country = mo.ui.dropdown(
        options=markets_for("PSU"),
        value=market_for(_base_parts["Power supply"]),
        full_width=True,
    )
    cooler_country = mo.ui.dropdown(
        options=markets_for("Cooler"),
        value=market_for(_base_parts["Cooler"]),
        full_width=True,
    )
    case_country = mo.ui.dropdown(
        options=markets_for("Case"),
        value=market_for(_base_parts["Case"]),
        full_width=True,
    )
    gpu_country = mo.ui.dropdown(
        options=markets_for("GPU"),
        value=market_for(_base_parts["Graphics card"]),
        full_width=True,
    )
    return (
        board_country,
        case_country,
        cooler_country,
        cpu_country,
        gpu_country,
        memory_country,
        psu_country,
        storage_country,
    )


@app.cell
def _(
    board_country,
    build_choice,
    builds,
    case_country,
    cooler_country,
    cpu_country,
    gpu_country,
    memory_country,
    mo,
    parts,
    psu_country,
    storage_country,
):
    def options_for(part, market):
        _data = parts[parts["Part"].eq(part) & parts["Market"].eq(market)].copy()
        _data = _data.sort_values(["Priority", "Store"])
        return {
            f'{row["Option"]} | {row["Store"]} | {row["Price"]:,.0f} {row["Currency"]}': row["ID"]
            for _, row in _data.iterrows()
        }

    def label_for(options, preferred_id):
        for _label, _value in options.items():
            if _value == preferred_id:
                return _label
        return next(iter(options))

    def picker(part, preferred_id, country):
        options = options_for(part, country.value)
        return mo.ui.dropdown(
            options=options,
            value=label_for(options, preferred_id),
            full_width=True,
        )

    _base_parts = builds[build_choice.value]

    cpu_choice = picker("CPU", _base_parts["CPU"], cpu_country)
    board_choice = picker("Motherboard", _base_parts["Main board"], board_country)
    memory_choice = picker("RAM", _base_parts["Memory"], memory_country)
    storage_choice = picker("SSD", _base_parts["Storage"], storage_country)
    psu_choice = picker("PSU", _base_parts["Power supply"], psu_country)
    cooler_choice = picker("Cooler", _base_parts["Cooler"], cooler_country)
    case_choice = picker("Case", _base_parts["Case"], case_country)
    gpu_choice = picker("GPU", _base_parts["Graphics card"], gpu_country)

    def part_row(label, country_picker, part_picker):
        return mo.hstack(
            [
                mo.Html(f'<div class="pc-build-label">{label}</div>'),
                country_picker,
                part_picker,
            ],
            justify="start",
        )

    parts_ui = mo.vstack(
        [
            mo.Html(
                """
                <div class="pc-wrap pc-section" style="margin-top: 0;">
                  <div class="pc-control-shell pc-parts-shell" style="padding-top: 12px; padding-bottom: 12px;">
                    <div class="pc-section-title">Change Parts</div>
                    <div class="pc-section-subtitle" style="margin-bottom: 10px;">First choose country, then choose the specific part available in that country.</div>
                    <div class="pc-build-grid" style="grid-template-columns: 140px 160px minmax(0, 1fr); margin-bottom: 4px;">
                      <div></div>
                      <div class="pc-label">Change country</div>
                      <div class="pc-label">Part option</div>
                    </div>
                """
            ),
            part_row("CPU", cpu_country, cpu_choice),
            part_row("Main board", board_country, board_choice),
            part_row("Memory", memory_country, memory_choice),
            part_row("Storage", storage_country, storage_choice),
            part_row("Power supply", psu_country, psu_choice),
            part_row("Cooler", cooler_country, cooler_choice),
            part_row("Case", case_country, case_choice),
            part_row("Graphics card", gpu_country, gpu_choice),
            mo.Html(
                """
                  </div>
                </div>
                """
            ),
        ],
        gap=0,
    )
    parts_ui
    return (
        board_choice,
        case_choice,
        cooler_choice,
        cpu_choice,
        gpu_choice,
        memory_choice,
        psu_choice,
        storage_choice,
    )


@app.cell
def _(
    board_choice,
    build_choice,
    case_choice,
    compare_ids,
    cooler_choice,
    cpu_choice,
    gpu_choice,
    get_previous_snapshot,
    memory_choice,
    psu_choice,
    rates,
    set_previous_snapshot,
    storage_choice,
    build_table,
    eu_lowest_table,
):
    selected_name = build_choice.value
    selected_parts = {
        "CPU": cpu_choice.value,
        "Main board": board_choice.value,
        "Memory": memory_choice.value,
        "Storage": storage_choice.value,
        "Power supply": psu_choice.value,
        "Cooler": cooler_choice.value,
        "Case": case_choice.value,
        "Graphics card": gpu_choice.value,
    }
    selected_table = build_table(selected_parts, compare_ids)
    selected_eu_table = eu_lowest_table(selected_table)

    previous_snapshot = get_previous_snapshot()
    previous_row_ids = previous_snapshot.get("row_ids", {})
    previous_values = previous_snapshot.get("values", {})
    previous_revision = int(previous_snapshot.get("revision", 0))

    current_values = {}
    cell_diffs = {}
    cell_deltas = {}
    row_diffs = {}

    for _, _row in selected_table.iterrows():
        part_key = str(_row["Part"])
        current_row_id = str(_row["ID"])
        current_values[f"{part_key}:price"] = str(_row["Price"])
        current_values[f"{part_key}:huf"] = int(_row["HUF"])
        current_values[f"{part_key}:uah"] = int(_row["UAH"])
        row_diffs[part_key] = previous_row_ids.get(part_key) not in (None, current_row_id)
        for suffix in ("price", "huf", "uah"):
            key = f"{part_key}:{suffix}"
            prev_value = previous_values.get(key)
            now_value = current_values[key]
            if prev_value is None or prev_value == now_value:
                cell_diffs[key] = "same"
                cell_deltas[key] = 0
            elif suffix == "price":
                cell_diffs[key] = "changed"
                cell_deltas[key] = 0
            else:
                cell_diffs[key] = "down" if now_value < prev_value else "up"
                cell_deltas[key] = now_value - prev_value

    total_huf = int(selected_table["HUF"].sum())
    total_uah = int(selected_table["UAH"].sum())
    total_saving = int(selected_table["Saving"].sum())
    total_saving_uah = int(selected_table["Saving_UAH"].sum())
    market_totals_huf = {
        market: int(selected_table.loc[selected_table["Market"].eq(market), "HUF"].sum())
        for market in selected_table["Market"].unique()
        if market != "No GPU"
    }
    market_totals_uah = {
        market: int(selected_table.loc[selected_table["Market"].eq(market), "UAH"].sum())
        for market in selected_table["Market"].unique()
        if market != "No GPU"
    }
    total_eur = int(round(total_huf / rates["eur_to_huf"]))

    summary_values = {
        "build-total:huf": total_huf,
        "build-total:uah": total_uah,
        "summary-total:huf": total_huf,
        "summary-total:uah": total_uah,
        "summary-total:eur": total_eur,
        "summary-saving:huf": total_saving,
        "summary-saving:uah": total_saving_uah,
    }
    for _market, value in market_totals_huf.items():
        summary_values[f"summary-market:{_market}:huf"] = value
    for _market, value in market_totals_uah.items():
        summary_values[f"summary-market:{_market}:uah"] = value

    for key, now_value in summary_values.items():
        prev_value = previous_values.get(key)
        if prev_value is None or prev_value == now_value:
            cell_diffs[key] = "same"
            cell_deltas[key] = 0
        elif isinstance(now_value, int):
            cell_diffs[key] = "down" if now_value < prev_value else "up"
            cell_deltas[key] = now_value - prev_value
        else:
            cell_diffs[key] = "changed"
            cell_deltas[key] = 0
        current_values[key] = now_value

    has_any_change = any(state != "same" for state in cell_diffs.values())
    revision = previous_revision + 1 if has_any_change else previous_revision

    set_previous_snapshot(
        {
            "row_ids": {str(_row["Part"]): str(_row["ID"]) for _, _row in selected_table.iterrows()},
            "values": current_values,
            "revision": revision,
        }
    )

    return cell_deltas, cell_diffs, revision, row_diffs, selected_eu_table, selected_name, selected_table


@app.cell
def _(cell_deltas, cell_diffs, esc, mo, number_text, revision, row_diffs, selected_name, selected_table):
    def _flash_class(state):
        if state == "same":
            return ""
        suffix = "a" if revision % 2 == 0 else "b"
        if state == "down":
            return f"pc-flash-down-{suffix}"
        if state == "up":
            return f"pc-flash-up-{suffix}"
        return f"pc-flash-neutral-{suffix}"

    def _diff_class_table(key):
        return _flash_class(cell_diffs.get(key, "same"))

    def _delta_class(key):
        state = cell_diffs.get(key, "same")
        if state == "same":
            return ""
        suffix = "a" if revision % 2 == 0 else "b"
        if state == "down":
            return f"pc-delta-down-{suffix}"
        if state == "up":
            return f"pc-delta-up-{suffix}"
        return ""

    def _delta_text(key):
        delta = int(cell_deltas.get(key, 0) or 0)
        if delta == 0:
            return ""
        sign = "+" if delta > 0 else "-"
        return f"{sign}{number_text(abs(delta))}"

    body_rows = []
    _total_uah = int(selected_table["UAH"].sum())
    _total_huf = int(selected_table["HUF"].sum())
    def _market_class(market):
        if market == "Poland":
            return "pc-pol"
        if market == "Hungary":
            return "pc-hu"
        if market == "Ukraine":
            return "pc-ua"
        return ""
    for _, _row in selected_table.iterrows():
        market_class = _market_class(_row["Market"])
        row_key = str(_row["Part"])
        body_rows.append(
            f"""
            <tr class="pc-compare-row">
              <td>{esc(_row["Part"])}</td>
              <td>{esc(_row["Model"])}</td>
              <td><span class="pc-pill {market_class}">{esc(_row["Market"])}</span></td>
              <td><a href="{esc(_row["URL"])}" target="_blank" rel="noopener">{esc(_row["Store"])}</a></td>
              <td class="pc-num pc-col-price">{esc(_row["Price"])}</td>
              <td class="pc-num pc-col-uah {_diff_class_table(f"{row_key}:uah")}">{number_text(_row["UAH"])} UAH</td>
              <td class="pc-num pc-delta {_delta_class(f"{row_key}:uah")}">{_delta_text(f"{row_key}:uah")}</td>
              <td class="pc-num pc-col-huf {_diff_class_table(f"{row_key}:huf")}">{number_text(_row["HUF"])} HUF</td>
              <td class="pc-num pc-delta {_delta_class(f"{row_key}:huf")}">{_delta_text(f"{row_key}:huf")}</td>
            </tr>
            """
        )

    mo.Html(
        f"""
        <div class="pc-wrap pc-section">
          <div class="pc-panel">
          <div class="pc-kicker">Current build</div>
          <h2 style="margin-top: 0; margin-bottom: 10px;">{esc(selected_name)}</h2>
          <table class="pc-table pc-table-main">
            <colgroup>
              <col class="pc-col-part">
              <col class="pc-col-model">
              <col class="pc-col-market">
              <col class="pc-col-store">
              <col class="pc-col-store-price">
              <col class="pc-col-uah-est">
              <col class="pc-col-delta">
              <col class="pc-col-huf-est">
              <col class="pc-col-delta">
            </colgroup>
            <thead>
              <tr>
                <th>Part</th>
                <th>Selected model</th>
                <th>Buy from</th>
                <th>Store</th>
                <th class="pc-num pc-col-head-price">Store price</th>
                <th class="pc-num pc-col-head-uah"><span class="pc-head-compact">UAH<br>est.</span></th>
                <th class="pc-num pc-th-delta"><span class="pc-head-compact">Δ<br>UAH</span></th>
                <th class="pc-num pc-col-head-huf"><span class="pc-head-compact">HUF<br>comp.</span></th>
                <th class="pc-num pc-th-delta"><span class="pc-head-compact">Δ<br>HUF</span></th>
              </tr>
            </thead>
            <tbody>{''.join(body_rows)}</tbody>
            <tfoot>
              <tr>
                <td colspan="5" class="pc-col-total">Total estimate</td>
                <td class="pc-num pc-col-uah pc-col-total {_diff_class_table("build-total:uah")}">{number_text(_total_uah)} UAH</td>
                <td class="pc-num pc-delta"></td>
                <td class="pc-num pc-col-huf pc-col-total {_diff_class_table("build-total:huf")}">{number_text(_total_huf)} HUF</td>
                <td class="pc-num pc-delta"></td>
              </tr>
            </tfoot>
          </table>
          </div>
        </div>
        """
    )
    return


@app.cell
def _(cell_diffs, huf_text, mo, number_text, rates, revision, selected_table):
    def _flash_class(state, prefix="pc-flash"):
        if state == "same":
            return ""
        suffix = "a" if revision % 2 == 0 else "b"
        if state == "down":
            return f"{prefix}-down-{suffix}"
        if state == "up":
            return f"{prefix}-up-{suffix}"
        return f"{prefix}-neutral-{suffix}"

    def _diff_class_summary(key):
        return _flash_class(cell_diffs.get(key, "same"))

    def _card_state(*keys):
        states = [cell_diffs.get(key, "same") for key in keys]
        states = [state for state in states if state != "same"]
        if not states:
            return "same"
        if "up" in states and "down" in states:
            return "changed"
        if "up" in states:
            return "up"
        if "down" in states:
            return "down"
        return "changed"

    _total_huf = int(selected_table["HUF"].sum())
    _total_uah = int(selected_table["UAH"].sum())
    _total_eur = int(round(_total_uah / rates["eur_to_uah"]))
    _total_saving = int(selected_table["Saving"].sum())
    _total_saving_uah = int(selected_table["Saving_UAH"].sum())
    _active_markets = [m for m in selected_table["Market"].unique() if m != "No GPU"]
    _market_lines = []
    for _market in _active_markets:
        _pay_market_uah = int(selected_table.loc[selected_table["Market"].eq(_market), "UAH"].sum())
        _pay_market_huf = int(selected_table.loc[selected_table["Market"].eq(_market), "HUF"].sum())
        _market_lines.append(
            f'<div class="pc-muted {_diff_class_summary(f"summary-market:{_market}:huf")}">{_market}: {number_text(_pay_market_uah)} UAH spend view / {huf_text(_pay_market_huf)} comparison</div>'
        )

    mo.Html(
        f"""
        <div class="pc-wrap pc-section" style="margin-top: 14px; padding-top: 0;">
          <div class="pc-card-row">
            <div class="pc-card {_flash_class(_card_state('summary-total:huf', 'summary-total:uah'), 'pc-card-flash')}">
              <div class="pc-label">Total price</div>
              <div class="pc-value {_diff_class_summary("summary-total:uah")}">{number_text(_total_uah)} UAH</div>
              <div class="pc-muted pc-col-huf {_diff_class_summary("summary-total:huf")}">{huf_text(_total_huf)} / {number_text(_total_eur)} EUR</div>
            </div>
            <div class="pc-card {_flash_class(_card_state(*[f"summary-market:{m}:huf" for m in _active_markets]), 'pc-card-flash')}">
              <div class="pc-label">Where money goes</div>
              {''.join(_market_lines)}
            </div>
            <div class="pc-card {_flash_class(_card_state('summary-saving:huf', 'summary-saving:uah'), 'pc-card-flash')}">
              <div class="pc-label">Estimated saving</div>
              <div class="pc-value pc-save {_diff_class_summary("summary-saving:uah")}">{number_text(_total_saving_uah)} UAH</div>
              <div class="pc-value-small pc-save {_diff_class_summary("summary-saving:huf")}">{huf_text(_total_saving)}</div>
              <div class="pc-muted">Compared with Hungarian reference prices</div>
            </div>
          </div>
          <div class="pc-note" style="margin-top: 14px;">
            UAH-first Monobank rates used. 1 PLN = {rates["pln_to_uah"]:.4f} UAH, 100 HUF = {(rates["huf_to_uah"] * 100):.2f} UAH. HUF comparison only: 1 PLN = {rates["pln_to_huf"]:.2f} HUF. Checked: {rates["checked"]}.
          </div>
        </div>
        """
    )
    return _total_huf, _total_saving


@app.cell
def _(esc, mo, number_text, selected_table):
    def _basket_rows(df):
        rows = []
        for _, row in df.iterrows():
            rows.append(
                f"""
                <tr>
                  <td>{esc(row["Part"])}</td>
                  <td>{esc(row["Model"])}</td>
                  <td class="pc-num">{number_text(row["UAH"])} UAH</td>
                  <td class="pc-num">{esc(row["Price"])}</td>
                </tr>
                """
            )
        return "".join(rows)
    subtitle_map = {
        "Poland": "Comparison and cross-border source basket; PLN is converted into the main UAH spend view.",
        "Hungary": "Secondary source basket for bulky/local items; HUF is shown mainly as comparison.",
        "Ukraine": "Primary buyer view: UAH prices paid directly, with HUF kept secondary.",
    }
    basket_cards = []
    for _market in [m for m in selected_table["Market"].unique() if m != "No GPU"]:
        market_df = selected_table[selected_table["Market"].eq(_market)].copy()
        if market_df.empty:
            continue
        market_currency = str(market_df["Currency"].iloc[0]).upper()
        raw_total = market_df["RawPrice"].sum()
        uah_total = int(market_df["UAH"].sum())
        basket_cards.append(
            f"""
              <div class="pc-basket-card">
                <div class="pc-basket-title">{esc(_market)} basket</div>
                <div class="pc-basket-subtitle">{esc(subtitle_map.get(_market, "Market-specific basket for the selected parts."))}</div>
                <table class="pc-table">
                  <thead>
                    <tr>
                      <th>Part</th>
                      <th>Selected model</th>
                      <th class="pc-num">UAH spend</th>
                      <th class="pc-num">Store price</th>
                    </tr>
                  </thead>
                  <tbody>{_basket_rows(market_df)}</tbody>
                </table>
                <div class="pc-basket-total">
                  <span>Subtotal</span>
                  <span>{number_text(uah_total)} UAH / {number_text(raw_total)} {market_currency}</span>
                </div>
              </div>
            """
        )

    mo.Html(
        f"""
        <div class="pc-wrap pc-section">
          <div class="pc-panel">
            <div class="pc-section-title">Purchase baskets</div>
            <div class="pc-section-subtitle">Ukraine is the main spend view; Poland and Hungary are source baskets for comparison or practical buying.</div>
            <div class="pc-basket-grid">
              {''.join(basket_cards)}
            </div>
          </div>
        </div>
        """
    )
    return


@app.cell
def _(mo, rates):
    huf_per_pln = rates["pln_to_huf"]
    uah_per_pln = rates["pln_to_uah"]
    uah_per_100_huf = rates["huf_to_uah"] * 100
    if uah_per_pln < 12:
        fx_takeaway = "A lower PLN->UAH rate makes Polish source baskets cheaper for a Ukraine-based buyer."
    elif uah_per_pln > 13:
        fx_takeaway = "A higher PLN->UAH rate makes Polish source baskets less attractive against Ukraine and Hungary."
    else:
        fx_takeaway = "PLN->UAH is in the normal watch zone; check the UAH total before treating a Polish lead as better."

    mo.Html(
        f"""
        <div class="pc-wrap pc-section">
          <div class="pc-panel">
          <h2>FX logic</h2>
          <div class="pc-muted">
            Monobank-only view: UAH is the real payment currency first. HUF is kept for Hungarian source comparison, not as the main planner currency.
          </div>
          <table class="pc-table" style="margin-top: 12px;">
            <thead>
              <tr>
                <th>What we watch</th>
                <th class="pc-num">Live rate</th>
                <th>Why it matters</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1 PLN on Ukrainian card</td>
                <td class="pc-num">{uah_per_pln:.4f} UAH</td>
                <td>This is the direct cost of paying Polish stores from Monobank / Ukrainian cards.</td>
              </tr>
              <tr>
                <td>100 HUF on Ukrainian card</td>
                <td class="pc-num">{uah_per_100_huf:.2f} UAH</td>
                <td>This is the Ukrainian-card feel of Hungarian local prices.</td>
              </tr>
              <tr>
                <td>1 PLN in HUF comparison</td>
                <td class="pc-num">{huf_per_pln:.2f} HUF</td>
                <td>Secondary comparison only: PLN->UAH divided by HUF->UAH.</td>
              </tr>
            </tbody>
          </table>
          <div class="pc-note" style="margin-top: 12px;">
            {fx_takeaway}
          </div>
          </div>
        </div>
        """
    )
    return


@app.cell
def _(esc, huf_text, mo, number_text, selected_eu_table):
    rows = []
    for _, _row in selected_eu_table.iterrows():
        if _row["Difference_UAH"] is None or str(_row["Difference_UAH"]) == "nan":
            diff_text = "-"
            eu_huf_text = "-"
            eu_uah_text = "-"
        else:
            diff_value = int(_row["Difference_UAH"])
            diff_text = (
                f"+{number_text(diff_value)} UAH"
                if diff_value > 0
                else f"{number_text(diff_value)} UAH"
            )
            eu_huf_text = huf_text(_row["EU_HUF"])
            eu_uah_text = f'{number_text(_row["EU_UAH"])} UAH'

        rows.append(
            f"""
            <tr>
              <td>{esc(_row["Part"])}</td>
              <td>{esc(_row["Selected"])}</td>
              <td class="pc-num">{esc(_row["Our_Price"])}</td>
              <td class="pc-num">{esc(_row["EU_Low"])}</td>
              <td class="pc-num">{eu_uah_text}</td>
              <td class="pc-num">{eu_huf_text}</td>
              <td class="pc-num">{diff_text}</td>
              <td>{esc(_row["Match"])}</td>
            </tr>
            """
        )

    mo.Html(
        f"""
        <div class="pc-wrap pc-section">
          <div class="pc-panel">
          <h2>EU lowest-price check</h2>
          <div class="pc-muted">
            A UAH-first sanity check against wider EU listings. Empty rows need exact product captures.
          </div>
          <table class="pc-table">
            <thead>
              <tr>
                <th>Part</th>
                <th>Selected model</th>
                <th class="pc-num">Our store price</th>
                <th class="pc-num">Lowest EU seen</th>
                <th class="pc-num">EU in UAH</th>
                <th class="pc-num">EU in HUF</th>
                <th class="pc-num">UAH gap</th>
                <th>Data</th>
              </tr>
            </thead>
            <tbody>{''.join(rows)}</tbody>
          </table>
          </div>
        </div>
        """
    )
    return


@app.cell
def _(mo, parts):
    mo.accordion({"Advanced: full parts database": mo.ui.table(parts, selection=None)})
    return


if __name__ == "__main__":
    app.run()
