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
    PARTS_CSV_DATA = """ID,Part,Priority,Option,Market,Store,Price,Currency,HUF_Est,Status,Risk,Note,Source
CPU_01_HU,CPU,1,AMD Ryzen 9 9900X Box,Hungary,landcomputer.hu,123750,HUF,123750,Pick,Low,Current target CPU; local warranty route is simple,Raw_Captures/CPU
CPU_01_PL,CPU,1,AMD Ryzen 9 9900X Box,Poland,x-kom.pl,1349,PLN,112061,Compare,Medium,Same CPU cheaper at current FX; compare warranty/logistics before choosing Poland,Raw_Captures/CPU
CPU_01_PL_AMZ,CPU,1,AMD Ryzen 9 9900X Box,Poland,Amazon.pl,1398.99,PLN,116214,Backup,Low,Safe seller but worse than x-kom and local warranty still matters,Raw_Captures/CPU
CPU_02_HU,CPU,2,AMD Ryzen 7 9700X Box,Hungary,Arukereso lead,103490,HUF,103490,Backup,Low,Budget fallback if platform cost must drop,CPU_WORKING_SHORTLIST
CPU_03_HU,CPU,3,AMD Ryzen 9 9950X Box,Hungary,Konzolvilag,174090,HUF,174090,Watch,Medium,16-core productivity upgrade; not default value choice,Raw_Captures/CPU
MB_01_HU,Motherboard,1,MSI MAG B850 Tomahawk MAX WiFi,Hungary,Arukereso lead,82340,HUF,82340,Pick,Low,Default motherboard choice,Raw_Captures/Motherboard
MB_01_PL,Motherboard,1,MSI MAG B850 Tomahawk MAX WiFi,Poland,Amazon.pl,792.95,PLN,65870,Compare,Medium,Cheaper at current FX; verify exact MAX model and warranty route,Raw_Captures/Motherboard
MB_02_HU,Motherboard,2,ASRock X870 PRO RS WiFi,Hungary,Arukereso lead,72290,HUF,72290,Backup,Medium,Strong value challenger if comfortable with ASRock,Raw_Captures/Motherboard
MB_03_HU,Motherboard,3,MSI MAG B850 Tomahawk WiFi non-MAX,Hungary,Arukereso lead,68590,HUF,68590,Watch,Medium,Cheaper MSI path; check what is lost vs MAX,Raw_Captures/Motherboard
MB_04_HU,Motherboard,4,Gigabyte X870E AORUS Elite WiFi7,Hungary,Arukereso lead,109899,HUF,109899,Watch,Medium,Premium board; probably unnecessary unless features matter,Raw_Captures/Motherboard
RAM_01_PL,RAM,1,Patriot Viper Venom 64GB 2x32 DDR5-6000 CL30,Poland,Allegro,2941.98,PLN,244390,Pick,Medium,Best value RAM if seller/warranty are clean,Raw_Captures/RAM
RAM_01_HU,RAM,1,Patriot Viper Venom 64GB 2x32 DDR5-6000 CL30,Hungary,elektroshock.hu,328435,HUF,328435,Compare,Medium,Same model local comparison; Arukereso capture shows 36-month warranty plus EU and 2-3 day delivery,Raw_Captures/RAM
RAM_02_HU,RAM,2,Kingston Fury Beast EXPO 64GB 2x32 DDR5-6000 CL30,Hungary,foramax.hu,339890,HUF,339890,Backup,Low,Safest RAM option; better warranty comfort,Raw_Captures/RAM
RAM_02_PL,RAM,2,Kingston Fury Beast EXPO 64GB 2x32 DDR5-6000 CL30,Poland,KR System / Ceneo lead,3635.5,PLN,302001,Backup,Medium,Safer RAM option from Poland but not as cheap as Patriot,Raw_Captures/RAM
RAM_03_PL,RAM,3,GOODRAM IRDM 64GB 2x32 DDR5-6000 CL30,Poland,Allegro,3333,PLN,276872,Backup,Medium,Third practical 64GB option,Raw_Captures/RAM
RAM_03_HU,RAM,3,GOODRAM IRDM 64GB 2x32 DDR5-6000 CL30,Hungary,sky-frames.hu,332760,HUF,332760,Backup,Medium,Local GOODRAM option; not cheaper than Kingston enough,Raw_Captures/RAM
RAM_04_PL,RAM,4,Patriot Viper Venom 32GB 2x16 DDR5-6000 CL30,Poland,Ceneo lead,1589.9,PLN,132073,Watch,Medium,Budget branch; saves money but halves RAM,Raw_Captures/RAM
RAM_04_HU,RAM,4,Patriot Viper Venom 32GB 2x16 DDR5-6000 CL30,Hungary,alza.hu,150290,HUF,150290,Compare,Low,Same model local comparison from Arukereso capture; Alza stock offer plus 1390 HUF delivery,Raw_Captures/RAM
SSD_01_PL,SSD,1,Kingston KC3000 2TB,Poland,Ceneo lead,939,PLN,78003,Pick,Medium,Best current SSD value from Poland,Raw_Captures/SSD
SSD_01_HU,SSD,1,Kingston KC3000 2TB,Hungary,Arukereso lead,106336,HUF,106336,Compare,Low,Same SSD local route; more expensive but simpler warranty,Raw_Captures/SSD
SSD_02_HU,SSD,2,Lexar NM790 2TB,Hungary,Arukereso lead,96695,HUF,96695,Backup,Low,Best Hungary SSD value; DRAM-less/HMB,Raw_Captures/SSD
SSD_02_PL,SSD,2,Lexar NM790 2TB,Poland,Ceneo lead,1038.03,PLN,86229,Backup,Medium,Good SSD but KC3000 Poland is cleaner value,Raw_Captures/SSD
SSD_03_HU,SSD,3,Samsung 990 PRO 2TB,Hungary,Alza / Arukereso lead,119990,HUF,119990,Watch,Low,Premium SSD; only if close to KC3000 price,Raw_Captures/SSD
SSD_03_PL,SSD,3,Samsung 990 PRO 2TB,Poland,Ceneo lead,1469,PLN,122030,Avoid,Medium,Too expensive versus KC3000,Raw_Captures/SSD
PSU_01_HU,PSU,1,be quiet! Pure Power 13 M 1000W,Hungary,Arukereso lead,49100,HUF,49100,Pick,Low,Current value PSU; 1000W ATX 3.1 / PCIe 5.1 direction,Raw_Captures/PSU
PSU_02_HU,PSU,2,Seasonic Focus GX-1000 2024,Hungary,Arukereso lead,59990,HUF,59990,Backup,Low,Safer premium PSU option,Raw_Captures/PSU
PSU_02_PL,PSU,2,Seasonic Focus GX-1000 v4,Poland,Ceneo lead,687,PLN,57069,Compare,Medium,Good unit; Poland price now competitive but warranty/logistics decide,Raw_Captures/PSU
PSU_03_HU,PSU,3,Corsair RM1000x ATX 3.1,Hungary,Arukereso lead,66200,HUF,66200,Watch,Low,Strong premium PSU but pricier,Raw_Captures/PSU
PSU_03_PL,PSU,3,Corsair RM1000x ATX 3.1,Poland,Ceneo lead,647,PLN,53746,Backup,Medium,Strong Poland PSU option if bundling,Raw_Captures/PSU
COOL_01_HU,Cooler,1,Arctic Liquid Freezer III Pro 360 A-RGB Black,Hungary,Arukereso lead,31500,HUF,31500,Pick,Low,Preferred clean visual cooler,Raw_Captures/Case_Cooling
COOL_02_HU,Cooler,2,Arctic Liquid Freezer III Pro 360 Black,Hungary,Arukereso lead,29200,HUF,29200,Backup,Low,Saves little versus A-RGB; good if lights do not matter,Raw_Captures/Case_Cooling
COOL_02_PL,Cooler,2,Arctic Liquid Freezer III Pro 360 Black,Poland,Ceneo lead,324,PLN,26915,Compare,Medium,Cheap but cooler is easy to buy locally; not worth trouble alone,Raw_Captures/Case_Cooling
COOL_03_HU,Cooler,3,DeepCool LE360 V2 ARGB Black,Hungary,Arukereso broad search,22499,HUF,22499,Backup,Medium,Cheap visual 360 AIO backup if Arctic direction changes,Raw_Captures/Case_Cooling
COOL_04_HU,Cooler,4,MSI MAG CoreLiquid A13 360 Black,Hungary,Arukereso broad search,27777,HUF,27777,Watch,Medium,MSI-branded visual alternative; still less trusted than Arctic on value,Raw_Captures/Case_Cooling
COOL_05_HU,Cooler,5,Gigabyte GME 360 Gaming CPU Cooler Black,Hungary,Arukereso broad search,31800,HUF,31800,Watch,Medium,Looks fine on paper but not clearly better than Arctic at similar money,Raw_Captures/Case_Cooling
COOL_06_HU,Cooler,6,be quiet! Pure Loop 3 LX 360mm Black,Hungary,Arukereso broad search,34801,HUF,34801,Watch,Low,Premium quiet-brand alternative if aesthetics or brand preference matter,Raw_Captures/Case_Cooling
CASE_01_HU,Case,1,Corsair 3500X ARGB Black,Hungary,Arukereso lead,31990,HUF,31990,Pick,Low,Current case baseline; local because glass case logistics,Raw_Captures/Case_Cooling
CASE_02_HU,Case,2,Corsair 3500X Black plain,Hungary,Arukereso lead,21326,HUF,21326,Watch,Low,Cheapest Corsair path; fan planning needed,Raw_Captures/Case_Cooling
CASE_03_HU,Case,3,Phanteks XT View TG D-RGB Black,Hungary,Arukereso lead,27901,HUF,27901,Backup,Medium,Cheap visual backup; check clearance/build quality,Raw_Captures/Case_Cooling
CASE_04_HU,Case,4,NZXT H6 Flow RGB All Black,Hungary,Arukereso lead,44444,HUF,44444,Watch,Low,Nice case but Corsair is cheaper,Raw_Captures/Case_Cooling
CASE_05_HU,Case,5,Lian Li O11 Vision Compact Black,Hungary,Arukereso lead,43290,HUF,43290,Compare,Medium,Best compact premium look for Ventus-sized GPU; fan cost still needs to be added,Raw_Captures/Case_Cooling
CASE_06_HU,Case,6,NZXT H9 Flow Black,Hungary,oaziscomputer.hu,54190,HUF,54190,Compare,Low,Best roomy clean-look case if pairing with larger premium GPU; includes fans,Raw_Captures/Case_Cooling
CASE_07_HU,Case,7,Montech KING 95 PRO TG ARGB Black,Hungary,Arukereso lead,55790,HUF,55790,Compare,Medium,Best all-in value if included fans are counted honestly,Raw_Captures/Case_Cooling
CASE_08_HU,Case,8,Lian Li O11D EVO RGB TG Black,Hungary,Arukereso lead,59990,HUF,59990,Watch,Medium,Beautiful premium Lian Li direction but real cost rises after fans,Raw_Captures/Case_Cooling
CASE_09_HU,Case,9,Lian Li O11 Dynamic Mini V2 TG Black,Hungary,Arukereso lead,33090,HUF,33090,Watch,Medium,Compact and pretty but more experimental for Ryzen 9 plus future RTX 5080,Raw_Captures/Case_Cooling
CASE_10_HU,Case,10,Phanteks NV9 MK2 Black,Hungary,Arukereso lead,84499,HUF,84499,Avoid,Medium,Beautiful oversized showcase case but too expensive and fan cost still needs to be added,Raw_Captures/Case_Cooling
CASE_11_HU,Case,11,Lian Li O11 Dynamic EVO XL Black,Hungary,Arukereso lead,89900,HUF,89900,Avoid,Medium,Too expensive and too large for the current build logic,Raw_Captures/Case_Cooling
GPU_00_NONE,GPU,0,No GPU yet,No GPU,Local,0,HUF,0,Pick,Low,First purchase excludes expensive GPU; phase 1 uses Ryzen integrated graphics,RTX5080_WORKING_SHORTLIST
GPU_01_PL,GPU,1,MSI RTX 5080 Ventus 3X OC 16GB,Poland,x-kom.pl,4899,PLN,406960,Watch,Medium,Best RTX 5080 value lead; 303mm 16-pin 36-month warranty shown,Raw_Captures/GPU
GPU_01_HU,GPU,1,MSI RTX 5080 Ventus 3X OC 16GB,Hungary,Arukereso lead,499090,HUF,499090,Compare,Medium,Same model local route; much more expensive at current FX,Raw_Captures/GPU
GPU_02_PL,GPU,2,MSI RTX 5080 Gaming Trio OC 16GB,Poland,Ceneo lead,5599,PLN,465109,Backup,Medium,Better cooler/class than Ventus; costs more,Raw_Captures/GPU
GPU_02_HU,GPU,2,MSI RTX 5080 Gaming Trio OC 16GB,Hungary,Arukereso lead,528465,HUF,528465,Compare,Medium,Premium MSI local comparison,Raw_Captures/GPU
GPU_03_PL,GPU,3,Gigabyte RTX 5080 Gaming OC 16GB,Poland,Ceneo lead,5799,PLN,481723,Backup,Medium,Good long-term Gigabyte option; compare seller/warranty,Raw_Captures/GPU
GPU_03_HU,GPU,3,Gigabyte RTX 5080 Gaming OC 16GB,Hungary,Arukereso lead,526400,HUF,526400,Compare,Medium,Best Gigabyte Hungary premium-value comparison,Raw_Captures/GPU
GPU_04_HU,GPU,4,Inno3D RTX 5080 X3 OC 16GB,Hungary,Arukereso lead,465640,HUF,465640,Backup,Medium,Best cheap Hungary RTX 5080 value lead,RTX5080_WORKING_SHORTLIST
GPU_05_PL,GPU,5,Gigabyte RTX 5080 Windforce OC SFF 16GB,Poland,Ceneo lead,5343.54,PLN,443888,Watch,High,Cheap but SFF/basic cooler risk; not first long-term choice,Raw_Captures/GPU
GPU_05_HU,GPU,5,Gigabyte RTX 5080 Windforce OC SFF 16GB,Hungary,Arukereso lead,470000,HUF,470000,Watch,High,Cheap local option but SFF cooler risk,RTX5080_WORKING_SHORTLIST"""

    EU_LOWEST_CSV_DATA = """Selected_ID,EU_Model,EU_Price,EU_Currency,EU_Store,EU_Country,Match_Quality,Note,Source
GPU_01_PL,MSI RTX 5080 Ventus 3X OC 16GB,1332,EUR,GPUTracker low range,EU market,Good,"Exact model appeared around 1332-1373 EUR in wider EU tracker listings; verify seller/shipping/warranty before treating as buyable.",PC_BUILD_TOOLING.md
RAM_01_PL,Patriot Viper Venom 64GB 2x32 DDR5-6000 CL30,,,,,Need exact capture,"Current EU-wide RAM capture is too broad; many listings are laptop SO-DIMM or wrong speed/latency. Need exact PVV564G600C30K EU-low capture.",PC_BUILD_TOOLING.md
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
        "Budget: Ventus + 32GB Viper": {
            "CPU": "CPU_02_HU",
            "Main board": "MB_02_HU",
            "Memory": "RAM_04_PL",
            "Storage": "SSD_02_HU",
            "Power supply": "PSU_01_HU",
            "Cooler": "COOL_03_HU",
            "Case": "CASE_03_HU",
            "Graphics card": "GPU_01_PL",
        },
        "Budget: Ventus + 32GB Kingston": {
            "CPU": "CPU_02_HU",
            "Main board": "MB_02_HU",
            "Memory": "RAM_04_HU",
            "Storage": "SSD_01_PL",
            "Power supply": "PSU_01_HU",
            "Cooler": "COOL_03_HU",
            "Case": "CASE_03_HU",
            "Graphics card": "GPU_01_PL",
        },
        "Mid: Ventus + 64GB Viper (no GPU)": {
            "CPU": "CPU_01_PL",
            "Main board": "MB_01_PL",
            "Memory": "RAM_01_PL",
            "Storage": "SSD_01_PL",
            "Power supply": "PSU_01_HU",
            "Cooler": "COOL_02_HU",
            "Case": "CASE_05_HU",
            "Graphics card": "GPU_00_NONE",
        },
        "Mid: Ventus + 64GB Viper": {
            "CPU": "CPU_01_PL",
            "Main board": "MB_01_PL",
            "Memory": "RAM_01_PL",
            "Storage": "SSD_01_PL",
            "Power supply": "PSU_01_HU",
            "Cooler": "COOL_02_HU",
            "Case": "CASE_05_HU",
            "Graphics card": "GPU_01_PL",
        },
        "Showcase: Trio + 64GB Viper": {
            "CPU": "CPU_01_PL",
            "Main board": "MB_04_HU",
            "Memory": "RAM_01_PL",
            "Storage": "SSD_03_HU",
            "Power supply": "PSU_03_HU",
            "Cooler": "COOL_01_HU",
            "Case": "CASE_06_HU",
            "Graphics card": "GPU_02_PL",
        },
        "Luxury: Gigabyte OC + 64GB Kingston": {
            "CPU": "CPU_03_HU",
            "Main board": "MB_04_HU",
            "Memory": "RAM_02_HU",
            "Storage": "SSD_03_HU",
            "Power supply": "PSU_03_HU",
            "Cooler": "COOL_06_HU",
            "Case": "CASE_11_HU",
            "Graphics card": "GPU_03_HU",
        },
    }

    build_descriptions = {
        "Budget: Ventus + 32GB Viper": "Best value entry: 9700X + 32GB Viper PL + MSI Ventus PL. Lowest total cost, great 1440p gaming.",
        "Budget: Ventus + 32GB Kingston": "Budget build with safer HU RAM + KC3000 SSD. Good if you prefer local warranty.",
        "Mid: Ventus + 64GB Viper (no GPU)": "Mid-range without GPU. 9900X + 64GB Viper PL + KC3000 PL. Buy GPU later.",
        "Mid: Ventus + 64GB Viper": "Mid-range complete. 9900X + 64GB Viper PL + Ventus PL. Best price/performance.",
        "Showcase: Trio + 64GB Viper": "Premium mid: X870E Aorus + Trio + Samsung 990 PRO + H9 Flow. Looks as good as it performs.",
        "Luxury: Gigabyte OC + 64GB Kingston": "Top-end: 9950X + X870E Aorus + Gigabyte Gaming OC + O11 XL. No compromises.",
    }

    compare_ids = {
        "CPU_01_PL": "CPU_01_HU",
        "MB_01_PL": "MB_01_HU",
        "RAM_01_PL": "RAM_01_HU",
        "RAM_02_PL": "RAM_02_HU",
        "RAM_03_PL": "RAM_03_HU",
        "RAM_04_PL": "RAM_04_HU",
        "SSD_01_PL": "SSD_01_HU",
        "SSD_02_PL": "SSD_02_HU",
        "PSU_02_PL": "PSU_02_HU",
        "PSU_03_PL": "PSU_03_HU",
        "GPU_01_PL": "GPU_01_HU",
        "GPU_02_PL": "GPU_02_HU",
        "GPU_03_PL": "GPU_03_HU",
    }
    return build_descriptions, builds, compare_ids


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
            compare_huf = (
                price_to_huf(parts_by_id.loc[compare_id])
                if compare_id in parts_by_id.index
                else 0
            )
            compare_uah = (
                price_to_uah(parts_by_id.loc[compare_id])
                if compare_id in parts_by_id.index
                else 0
            )
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
          /* LIGHT, HIGH-CONTRAST THEME – WORKS IN ANY BROWSER */
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
            font-weight: 650;
            letter-spacing: 0;
          }

          .pc-wrap {
            max-width: 1080px;
            margin: 0 auto;
            padding: 20px;
            background: #ffffff;
            color: #111111;
            font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
          }
          .pc-title {
            font-size: 42px;
            font-weight: 700;
            margin: 8px 0 8px;
            color: #111111;
          }
          .pc-subtitle {
            color: #4a5568;
            font-size: 16px;
            max-width: 780px;
            margin-bottom: 24px;
          }
          .pc-section {
            margin-top: 30px;
          }
          .pc-panel {
            margin-top: 10px;
            padding: 16px 20px;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            background: #fbfdff;
            box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
          }
          .pc-control-shell {
            padding: 14px 18px 12px;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            background: #fbfdff;
            box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);
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
            margin-bottom: 10px;
          }
          .pc-card-row {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 14px;
            margin-top: 14px;
          }
          .pc-card {
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            background: #f7fafc;
            padding: 16px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
          }
          .pc-label {
            color: #4a5568;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: .03em;
          }
          .pc-value {
            color: #111111;
            font-size: 26px;
            font-weight: 800;
            margin-top: 8px;
          }
          .pc-muted {
            color: #718096;
            font-size: 13px;
            margin-top: 6px;
          }
          .pc-save {
            color: #2c7a4d;
            font-weight: 800;
          }
          .pc-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 16px;
            font-size: 15px;
            background: #ffffff;
          }
          .pc-table th {
            color: #4a5568;
            text-align: left;
            padding: 10px 8px;
            border-bottom: 1px solid #e2e8f0;
            background: #f8fafc;
          }
          .pc-table td {
            padding: 11px 8px;
            border-bottom: 1px solid #e2e8f0;
            vertical-align: top;
            color: #111111;
          }
          .pc-table tfoot td {
            background: #f8fafc;
            border-top: 2px solid #cbd5e1;
            font-weight: 750;
          }
          .pc-num {
            text-align: right;
            white-space: nowrap;
            font-variant-numeric: tabular-nums;
          }
          .pc-pill {
            display: inline-block;
            padding: 3px 9px;
            border-radius: 999px;
            font-size: 12px;
            background: #e2e8f0;
            color: #111111;
          }
          .pc-pol {
            background: #e6fffa;
            color: #234e52;
          }
          .pc-hu {
            background: #e0f2fe;
            color: #075985;
          }
          .pc-note {
            border-left: 3px solid #3182ce;
            padding-left: 12px;
            color: #2d3748;
            margin-top: 10px;
            background: #ebf8ff;
            padding: 10px;
            border-radius: 4px;
          }
          .pc-basket-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 14px;
            margin-top: 12px;
          }
          .pc-basket-card {
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            background: #ffffff;
            padding: 14px;
          }
          .pc-basket-title {
            font-size: 15px;
            font-weight: 750;
            color: #111111;
          }
          .pc-basket-subtitle {
            color: #64748b;
            font-size: 12px;
            margin-top: 3px;
          }
          .pc-basket-total {
            display: flex;
            justify-content: space-between;
            gap: 12px;
            margin-top: 10px;
            padding-top: 10px;
            border-top: 1px solid #e2e8f0;
            font-weight: 750;
            color: #111111;
          }
          @media (max-width: 900px) {
            .pc-card-row,
            .pc-basket-grid {
              grid-template-columns: 1fr;
            }
          }
          input, select, textarea {
            background: #ffffff !important;
            color: #111111 !important;
            border: 1px solid #cbd5e1 !important;
          }
        </style>
        <div class="pc-wrap">
          <div class="pc-title">PC Build Planner</div>
          <div class="pc-subtitle">
            Choose one build. The parts list changes below. Totals, exchange rate, and estimated saving are shown at the end.
          </div>
        </div>
        """
    )
    return


@app.cell
def _(builds, mo):
    build_choice = mo.ui.dropdown(
        options=list(builds.keys()),
        value="Mid: Ventus + 64GB Viper (no GPU)",
        label="",
        full_width=True,
    )
    mo.vstack(
        [
            mo.Html(
                """
                <div class="pc-wrap pc-section" style="margin-top: 0;">
                  <div class="pc-control-shell">
                    <div class="pc-section-title">Build selection</div>
                    <div class="pc-section-subtitle">Start from a prepared build, then fine-tune parts below.</div>
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
    return (build_choice,)


@app.cell
def _(build_choice, builds, mo, parts):
    def options_for(part):
        _data = parts[parts["Part"].eq(part)].copy()
        _data = _data.sort_values(["Priority", "Market", "Store"])
        return {
            f'{row["Option"]} | {row["Market"]} | {row["Store"]}': row["ID"]
            for _, row in _data.iterrows()
        }

    def label_for(options, item_id):
        for _label, _value in options.items():
            if _value == item_id:
                return _label
        return next(iter(options))

    base_parts = builds[build_choice.value]

    cpu_options = options_for("CPU")
    board_options = options_for("Motherboard")
    memory_options = options_for("RAM")
    storage_options = options_for("SSD")
    psu_options = options_for("PSU")
    cooler_options = options_for("Cooler")
    case_options = options_for("Case")
    gpu_options = options_for("GPU")

    cpu_choice = mo.ui.dropdown(
        options=cpu_options,
        value=label_for(cpu_options, base_parts["CPU"]),
        full_width=True,
    )
    board_choice = mo.ui.dropdown(
        options=board_options,
        value=label_for(board_options, base_parts["Main board"]),
        full_width=True,
    )
    memory_choice = mo.ui.dropdown(
        options=memory_options,
        value=label_for(memory_options, base_parts["Memory"]),
        full_width=True,
    )
    storage_choice = mo.ui.dropdown(
        options=storage_options,
        value=label_for(storage_options, base_parts["Storage"]),
        full_width=True,
    )
    psu_choice = mo.ui.dropdown(
        options=psu_options,
        value=label_for(psu_options, base_parts["Power supply"]),
        full_width=True,
    )
    cooler_choice = mo.ui.dropdown(
        options=cooler_options,
        value=label_for(cooler_options, base_parts["Cooler"]),
        full_width=True,
    )
    case_choice = mo.ui.dropdown(
        options=case_options,
        value=label_for(case_options, base_parts["Case"]),
        full_width=True,
    )
    gpu_choice = mo.ui.dropdown(
        options=gpu_options,
        value=label_for(gpu_options, base_parts["Graphics card"]),
        full_width=True,
    )

    mo.vstack(
        [
            mo.md("## Change Parts"),
            mo.Html('<div class="pc-muted">Optional: change any part and the numbers below update.</div>'),
            mo.hstack([mo.md("**CPU**"), cpu_choice]),
            mo.hstack([mo.md("**Main board**"), board_choice]),
            mo.hstack([mo.md("**Memory**"), memory_choice]),
            mo.hstack([mo.md("**Storage**"), storage_choice]),
            mo.hstack([mo.md("**Power supply**"), psu_choice]),
            mo.hstack([mo.md("**Cooler**"), cooler_choice]),
            mo.hstack([mo.md("**Case**"), case_choice]),
            mo.hstack([mo.md("**Graphics card**"), gpu_choice]),
        ]
    )
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
    build_descriptions,
    case_choice,
    compare_ids,
    cooler_choice,
    cpu_choice,
    gpu_choice,
    memory_choice,
    psu_choice,
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
    selected_description = build_descriptions[selected_name]
    return selected_description, selected_eu_table, selected_name, selected_table


@app.cell
def _(esc, mo, number_text, selected_description, selected_name, selected_table):
    body_rows = []
    _total_uah = int(selected_table["UAH"].sum())
    for _, row in selected_table.iterrows():
        market_class = "pc-pol" if row["Market"] == "Poland" else "pc-hu"
        if row["Market"] == "No GPU":
            market_class = ""
        body_rows.append(
            f"""
            <tr>
              <td>{esc(row["Part"])}</td>
              <td>{esc(row["Model"])}</td>
              <td><span class="pc-pill {market_class}">{esc(row["Market"])}</span></td>
              <td>{esc(row["Store"])}</td>
              <td class="pc-num">{esc(row["Price"])}</td>
              <td class="pc-num">{number_text(row["UAH"])} UAH</td>
            </tr>
            """
        )

    mo.Html(
        f"""
        <div class="pc-wrap pc-section">
          <h2>{esc(selected_name)}</h2>
          <div class="pc-note">{esc(selected_description)}</div>
          <table class="pc-table">
            <thead>
              <tr><th>Part</th><th>Selected model</th><th>Buy from</th><th>Store</th><th class="pc-num">Store price</th><th class="pc-num">UAH estimate</th></tr>
            </thead>
            <tbody>{''.join(body_rows)}</tbody>
            <tfoot>
              <tr><td colspan="5">Total UAH estimate</td><td class="pc-num">{number_text(_total_uah)} UAH</td></tr>
            </tfoot>
          </table>
        </div>
        """
    )
    return


@app.cell
def _(huf_text, mo, number_text, rates, selected_table):
    total_huf = int(selected_table["HUF"].sum())
    total_eur = int(round(total_huf / rates["eur_to_huf"]))
    total_uah = int(selected_table["UAH"].sum())
    total_saving = int(selected_table["Saving"].sum())
    pay_poland = int(selected_table.loc[selected_table["Market"].eq("Poland"), "HUF"].sum())
    pay_hungary = int(selected_table.loc[selected_table["Market"].eq("Hungary"), "HUF"].sum())

    mo.Html(
        f"""
        <div class="pc-wrap" style="padding-top: 8px;">
          <div class="pc-card-row">
            <div class="pc-card">
              <div class="pc-label">Total price</div>
              <div class="pc-value">{huf_text(total_huf)}</div>
              <div class="pc-muted">{number_text(total_eur)} EUR / {number_text(total_uah)} UAH</div>
            </div>
            <div class="pc-card">
              <div class="pc-label">Where money goes</div>
              <div class="pc-muted">Polish stores: {huf_text(pay_poland)}</div>
              <div class="pc-muted">Hungarian stores: {huf_text(pay_hungary)}</div>
            </div>
            <div class="pc-card">
              <div class="pc-label">Estimated saving</div>
              <div class="pc-value pc-save">{huf_text(total_saving)}</div>
              <div class="pc-muted">Compared with Hungarian reference prices</div>
            </div>
          </div>
          <div class="pc-note" style="margin-top: 14px;">
            Exchange assumption: 1 PLN = {rates["pln_to_huf"]:.2f} HUF. Source: {rates["source"]}. Checked: {rates["checked"]}.
          </div>
          
          <h2 style="margin-top: 40px;">Payment Options (Your Cards)</h2>
          <p class="pc-muted" style="margin-bottom: 16px;">Compare what you pay with different cards</p>
          <table class="pc-table">
            <thead>
              <tr>
                <th>Build</th>
                <th>HUF (Hungarian card)</th>
                <th>UAH (Ukrainian card)</th>
                <th>Better option</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Main 64GB, GPU later</strong></td>
                <td style="color: #68d391; font-weight: 600;">{huf_text(total_huf)}</td>
                <td>{number_text(total_uah)} UAH</td>
                <td><span class="pc-pill" style="background: rgba(104,211,145,.2); color: #68d391;">HUF card saves</span></td>
              </tr>
              <tr>
                <td><strong>Current vs Hungarian ref</strong></td>
                <td colspan="2" style="color: #68d391; font-weight: 600;">Save {huf_text(total_saving)} HUF by buying from Poland</td>
                <td></td>
              </tr>
            </tbody>
          </table>
          <div class="pc-note">
            <strong>Tip:</strong> Check the real card rate before purchase. The current build saves {huf_text(total_saving)} by buying selected parts from Poland instead of Hungarian reference prices.
          </div>
        </div>
        """
    )
    return pay_hungary, pay_poland, total_huf, total_saving


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
                  <td class="pc-num">{esc(row["Price"])}</td>
                  <td class="pc-num">{number_text(row["UAH"])} UAH</td>
                </tr>
                """
            )
        return "".join(rows)

    poland_df = selected_table[selected_table["Market"].eq("Poland")].copy()
    hungary_df = selected_table[selected_table["Market"].eq("Hungary")].copy()

    poland_pln_total = poland_df.loc[poland_df["Currency"].eq("PLN"), "RawPrice"].sum()
    hungary_huf_total = hungary_df.loc[hungary_df["Currency"].eq("HUF"), "RawPrice"].sum()
    poland_uah_total = int(poland_df["UAH"].sum())
    hungary_uah_total = int(hungary_df["UAH"].sum())

    mo.Html(
        f"""
        <div class="pc-wrap pc-section">
          <div class="pc-panel">
            <div class="pc-section-title">Purchase baskets</div>
            <div class="pc-section-subtitle">Parts automatically move between Poland and Hungary based on the selected store.</div>
            <div class="pc-basket-grid">
              <div class="pc-basket-card">
                <div class="pc-basket-title">Poland basket</div>
                <div class="pc-basket-subtitle">Paid in PLN where possible, then converted to UAH for the real spend view.</div>
                <table class="pc-table">
                  <thead>
                    <tr>
                      <th>Part</th>
                      <th>Selected model</th>
                      <th class="pc-num">Store price</th>
                      <th class="pc-num">UAH</th>
                    </tr>
                  </thead>
                  <tbody>{_basket_rows(poland_df)}</tbody>
                </table>
                <div class="pc-basket-total">
                  <span>Subtotal</span>
                  <span>{number_text(poland_pln_total)} PLN / {number_text(poland_uah_total)} UAH</span>
                </div>
              </div>
              <div class="pc-basket-card">
                <div class="pc-basket-title">Hungary basket</div>
                <div class="pc-basket-subtitle">Local items stay in HUF and are also shown in UAH.</div>
                <table class="pc-table">
                  <thead>
                    <tr>
                      <th>Part</th>
                      <th>Selected model</th>
                      <th class="pc-num">Store price</th>
                      <th class="pc-num">UAH</th>
                    </tr>
                  </thead>
                  <tbody>{_basket_rows(hungary_df)}</tbody>
                </table>
                <div class="pc-basket-total">
                  <span>Subtotal</span>
                  <span>{number_text(hungary_huf_total)} HUF / {number_text(hungary_uah_total)} UAH</span>
                </div>
              </div>
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
    if huf_per_pln < 82:
        fx_takeaway = "Lower PLN/HUF helps Poland. The Polish basket converts into fewer HUF, so savings vs Hungary rise."
    elif huf_per_pln > 83:
        fx_takeaway = "Higher PLN/HUF hurts Poland. The Polish basket converts into more HUF, so savings vs Hungary fall."
    else:
        fx_takeaway = "Poland is still cheaper at this rate, but small PLN/HUF moves can still swing the saving by a few thousand HUF."

    mo.Html(
        f"""
        <div class="pc-wrap pc-section">
          <div class="pc-panel">
            <h2>FX logic</h2>
            <div class="pc-muted">
              Monobank-only view: UAH is the real payment currency first, and HUF is the comparison view for Poland vs Hungary.
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
                  <td>1 PLN compared with Hungary</td>
                  <td class="pc-num">{huf_per_pln:.2f} HUF</td>
                  <td>This is derived from Monobank only: PLN to UAH divided by HUF to UAH.</td>
                </tr>
              </tbody>
            </table>
            <div class="pc-note" style="margin-top: 12px;">{fx_takeaway}</div>
          </div>
        </div>
        """
    )
    return


@app.cell
def _(esc, huf_text, mo, number_text, selected_eu_table):
    rows = []
    for _, _row in selected_eu_table.iterrows():
        if _row["Difference_HUF"] is None or str(_row["Difference_HUF"]) == "nan":
            diff_text = "-"
            eu_huf_text = "-"
            eu_uah_text = "-"
        else:
            diff_value = int(_row["Difference_HUF"])
            diff_text = (
                f"+{huf_text(diff_value)}"
                if diff_value > 0
                else huf_text(diff_value)
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
              <td class="pc-num">{eu_huf_text}</td>
              <td class="pc-num">{eu_uah_text}</td>
              <td class="pc-num">{diff_text}</td>
              <td>{esc(_row["Match"])}</td>
            </tr>
            """
        )

    mo.Html(
        f"""
        <div class="pc-wrap pc-section">
          <h2>EU lowest-price check</h2>
          <div class="pc-muted">
            This is only a sanity check: it shows whether the selected part looks expensive compared with wider EU listings.
          </div>
          <table class="pc-table">
            <thead>
              <tr>
                <th>Part</th>
                <th>Selected model</th>
                <th class="pc-num">Our store price</th>
                <th class="pc-num">Lowest EU seen</th>
                <th class="pc-num">EU in HUF</th>
                <th class="pc-num">EU in UAH</th>
                <th class="pc-num">Gap</th>
                <th>Data</th>
              </tr>
            </thead>
            <tbody>{''.join(rows)}</tbody>
          </table>
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
