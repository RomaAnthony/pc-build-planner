import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")


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
CASE_01_HU,Case,1,Corsair 3500X ARGB Black,Hungary,Arukereso lead,31990,HUF,31990,Pick,Low,Current case baseline; local because glass case logistics,Raw_Captures/Case_Cooling
CASE_02_HU,Case,2,Corsair 3500X Black plain,Hungary,Arukereso lead,21326,HUF,21326,Watch,Low,Cheapest Corsair path; fan planning needed,Raw_Captures/Case_Cooling
CASE_03_HU,Case,3,Phanteks XT View TG D-RGB Black,Hungary,Arukereso lead,27901,HUF,27901,Backup,Medium,Cheap visual backup; check clearance/build quality,Raw_Captures/Case_Cooling
CASE_04_HU,Case,4,NZXT H6 Flow RGB All Black,Hungary,Arukereso lead,44444,HUF,44444,Watch,Low,Nice case but Corsair is cheaper,Raw_Captures/Case_Cooling
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

    # Parse CSV from embedded string (no filesystem)
    parts = pd.read_csv(StringIO(PARTS_CSV_DATA))
    parts["Price"] = pd.to_numeric(parts["Price"], errors="coerce").fillna(0)
    parts["HUF_Est"] = pd.to_numeric(parts["HUF_Est"], errors="coerce").fillna(0)
    
    return datetime, html, json, mo, parts, pd, StringIO


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
        "Main 64GB, GPU later": {
            "CPU": "CPU_01_PL",
            "Main board": "MB_01_PL",
            "Memory": "RAM_01_PL",
            "Storage": "SSD_01_PL",
            "Power supply": "PSU_03_PL",
            "Cooler": "COOL_01_HU",
            "Case": "CASE_01_HU",
            "Graphics card": "GPU_00_NONE",
        },
        "Budget 32GB, GPU later": {
            "CPU": "CPU_01_PL",
            "Main board": "MB_01_PL",
            "Memory": "RAM_04_PL",
            "Storage": "SSD_01_PL",
            "Power supply": "PSU_03_PL",
            "Cooler": "COOL_01_HU",
            "Case": "CASE_01_HU",
            "Graphics card": "GPU_00_NONE",
        },
        "Full build with RTX 5080": {
            "CPU": "CPU_01_PL",
            "Main board": "MB_01_PL",
            "Memory": "RAM_01_PL",
            "Storage": "SSD_01_PL",
            "Power supply": "PSU_03_PL",
            "Cooler": "COOL_01_HU",
            "Case": "CASE_01_HU",
            "Graphics card": "GPU_01_PL",
        },
    }

    build_descriptions = {
        "Main 64GB, GPU later": "Strong work PC now. Expensive graphics card can be bought later.",
        "Budget 32GB, GPU later": "Lower first price, but weaker long-term memory setup.",
        "Full build with RTX 5080": "Full setup including the high-end graphics card for the 4K OLED monitor.",
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
def _(html, parts, pd, rates):
    parts_by_id = parts.set_index("ID")

    def esc(value):
        return html.escape(str(value))

    def huf_text(value):
        return f"{int(round(value)):,.0f} HUF"

    def number_text(value):
        return f"{int(round(value)):,.0f}"

    def price_to_huf(item):
        currency = str(item["Currency"]).upper()
        price = float(item["Price"])
        if currency == "HUF":
            return price
        if currency == "PLN":
            return price * rates["pln_to_huf"]
        if currency == "EUR":
            return price * rates["eur_to_huf"]
        return float(item["HUF_Est"])

    def original_price(item):
        currency = str(item["Currency"]).upper()
        price = float(item["Price"])
        return f"{price:,.0f} {currency}"

    def build_table(build_parts, compare_map):
        rows = []
        for part_name, item_id in build_parts.items():
            item = parts_by_id.loc[item_id]
            huf = price_to_huf(item)
            uah = huf * rates["huf_to_uah"]
            compare_id = compare_map.get(item_id, "")
            compare_huf = (
                price_to_huf(parts_by_id.loc[compare_id])
                if compare_id in parts_by_id.index
                else 0
            )
            saving = max(0, compare_huf - huf) if compare_huf else 0
            rows.append(
                {
                    "Part": part_name,
                    "Model": item["Option"],
                    "Market": item["Market"],
                    "Store": item["Store"],
                    "Price": original_price(item),
                    "HUF": int(round(huf)),
                    "UAH": int(round(uah)),
                    "Saving": int(round(saving)),
                }
            )
        return pd.DataFrame(rows)

    return build_table, esc, huf_text, number_text


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
        value="Main 64GB, GPU later",
        label="Choose build",
        full_width=True,
    )
    build_choice
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
    selected_description = build_descriptions[selected_name]
    return selected_description, selected_name, selected_table


@app.cell
def _(esc, mo, number_text, selected_description, selected_name, selected_table):
    body_rows = []
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
              <td>{esc(row["Price"])}</td>
              <td>{number_text(row["UAH"])} UAH</td>
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
              <tr><th>Part</th><th>Selected model</th><th>Buy from</th><th>Store</th><th>Store price</th><th>UAH estimate</th></tr>
            </thead>
            <tbody>{''.join(body_rows)}</tbody>
          </table>
        </div>
        """
    )
    return


@app.cell
def _(builds, compare_ids, build_table, huf_text, mo, number_text, rates, selected_table):
    total_huf = int(selected_table["HUF"].sum())
    total_eur = int(round(total_huf / rates["eur_to_huf"]))
    total_uah = int(round(total_huf * rates["huf_to_uah"]))
    total_saving = int(selected_table["Saving"].sum())
    pay_poland = int(selected_table.loc[selected_table["Market"].eq("Poland"), "HUF"].sum())
    pay_hungary = int(selected_table.loc[selected_table["Market"].eq("Hungary"), "HUF"].sum())

    scenario_rows = []
    for scenario_name, scenario_parts in builds.items():
        scenario_table = build_table(scenario_parts, compare_ids)
        scenario_total = int(scenario_table["HUF"].sum())
        scenario_rows.append(
            f"""
            <tr>
              <td>{scenario_name}</td>
              <td>{huf_text(scenario_total)}</td>
              <td>{number_text(scenario_total / rates["eur_to_huf"])} EUR</td>
              <td>{huf_text(int(scenario_table["Saving"].sum()))}</td>
            </tr>
            """
        )

    mo.Html(
        f"""
        <div class="pc-wrap pc-section">
          <h2>Numbers</h2>
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
          <table class="pc-table">
            <thead><tr><th>Build</th><th>Total</th><th>EUR view</th><th>Estimated saving</th></tr></thead>
            <tbody>{''.join(scenario_rows)}</tbody>
          </table>
          <div class="pc-note">
            Exchange assumption: 1 PLN = {rates["pln_to_huf"]:.2f} HUF. Source: {rates["source"]}. Checked: {rates["checked"]}.
          </div>
          
          <h2 style="margin-top: 40px; color: #ffffff;">Payment Options (Your Cards)</h2>
          <p style="color: #a0aec0; margin-bottom: 16px;">Compare what you pay with different cards</p>
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
          <div class="pc-note" style="background: rgba(66,153,225,.1); border-left: 3px solid #4299e1; color: #cbd5e1;">
            💡 <strong>Tip:</strong> Your HUF card is better for this build. You save {huf_text(total_saving)} HUF by buying from Poland instead of Hungary.
          </div>
        </div>
        """
    )
    return pay_hungary, pay_poland, total_huf, total_saving


@app.cell
def _(mo, parts):
    mo.accordion({"Advanced: full parts database": mo.ui.table(parts, selection=None)})
    return


if __name__ == "__main__":
    app.run()
