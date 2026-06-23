import marimo

__generated_with = "0.23.9"
app = marimo.App(width="full")


@app.cell
def _():
    import html
    from pathlib import Path

    import marimo as mo
    import pandas as pd

    ROOT = Path(__file__).resolve().parents[1]
    PARTS_CSV = ROOT / "02_PC_Builds" / "parts_options_seed.csv"
    EU_LOWEST_CSV = ROOT / "02_PC_Builds" / "eu_lowest_price_seed.csv"

    parts = pd.read_csv(PARTS_CSV)
    parts["Price"] = pd.to_numeric(parts["Price"], errors="coerce").fillna(0)
    parts["HUF_Est"] = pd.to_numeric(parts["HUF_Est"], errors="coerce").fillna(0)
    if "Paid_UAH" not in parts.columns:
        parts["Paid_UAH"] = 0
    parts["Paid_UAH"] = pd.to_numeric(parts["Paid_UAH"], errors="coerce").fillna(0)
    eu_lowest = pd.read_csv(EU_LOWEST_CSV)
    eu_lowest["EU_Price"] = pd.to_numeric(eu_lowest["EU_Price"], errors="coerce")
    return eu_lowest, html, mo, parts, pd


@app.cell
def _():
    def load_rates():
        # Fixed order-planning rates. Paid rows use exact receipt UAH via
        # Paid_UAH; pending/unpaid rows use these stable rates until receipts exist.
        rates = {
            "source": "fixed order-planning rates plus exact receipt UAH",
            "checked": "locked from 2026-06-22 to 2026-06-23 order receipts",
            "eur_to_uah": 51.709,
            "pln_to_uah": 12.1970,
            "huf_to_uah": 0.1477,
        }
        rates["eur_to_huf"] = rates["eur_to_uah"] / rates["huf_to_uah"]
        rates["pln_to_huf"] = rates["pln_to_uah"] / rates["huf_to_uah"]
        return rates

    rates = load_rates()
    return (rates,)


@app.cell
def _():
    builds = {
        "Current real build": {
            "CPU": "CPU_01_PL_AMZ",
            "Main board": "MB_04_PL",
            "Memory": "RAM_01_PL",
            "Storage": "SSD_01_PL",
            "Power supply": "PSU_01_HU",
            "Cooler": "COOL_01_HU",
            "Case": "CASE_14_HU",
            "Extra fans": "FAN_04_HU",
            "Thermal paste": "PASTE_01_PL",
            "Graphics card": "GPU_02_PL",
        },
    }

    # Hungarian references for the savings card. Prefer exact model matches;
    # use same-class snapshot rows only where an exact Hungary row is absent.
    compare_ids = {
        "CPU_01_PL": "CPU_01_HU",
        "CPU_01_PL_AMZ": "CPU_01_HU",
        "CPU_01_UA": "CPU_01_HU",
        "CPU_02_PL": "CPU_02_HU",
        "CPU_03_PL": "CPU_03_HU",
        "MB_01_PL": "MB_01_HU",
        "MB_01_UA": "MB_01_HU",
        "MB_02_PL": "MB_02_HU",
        "MB_04_PL": "MB_04_HU",
        "MB_08_PL": "MB_03_HU",
        "MB_05_PL": "MB_05_HU",
        "MB_06_PL": "MB_07_HU",
        "MB_09_PL": "MB_08_HU",
        "MB_10_PL": "MB_10_HU",
        "MB_11_PL": "MB_10_HU",
        "MB_12_PL": "MB_08_HU",
        "MB_13_PL": "MB_04_HU",
        "MB_14_PL": "MB_10_HU",
        "MB_15_PL": "MB_03_HU",
        "RAM_01_PL": "RAM_01_HU",
        "RAM_01_UA": "RAM_01_HU",
        "RAM_02_PL": "RAM_02_HU",
        "RAM_03_PL": "RAM_03_HU",
        "RAM_04_PL": "RAM_04_HU",
        "RAM_04_UA": "RAM_04_HU",
        "RAM_05_UA": "RAM_03_HU",
        "SSD_01_PL": "SSD_01_HU",
        "SSD_01_UA": "SSD_01_HU",
        "SSD_02_PL": "SSD_02_HU",
        "SSD_03_PL": "SSD_03_HU",
        "SSD_03_UA": "SSD_03_HU",
        "SSD_04_PL": "SSD_04_HU",
        "COOL_02_PL": "COOL_02_HU",
        "COOL_03_PL": "COOL_03_HU",
        "COOL_03_UA": "COOL_07_HU",
        "COOL_04_PL": "COOL_04_HU",
        "COOL_04_UA": "COOL_04_HU",
        "COOL_06_PL": "COOL_06_HU",
        "COOL_06_UA": "COOL_06_HU",
        "COOL_07_PL": "COOL_01_HU",
        "COOL_08_PL": "COOL_07_HU",
        "PSU_01_PL": "PSU_01_HU",
        "PSU_01_UA": "PSU_01_HU",
        "PSU_02_PL": "PSU_02_HU",
        "PSU_02_UA": "PSU_02_HU",
        "PSU_03_PL": "PSU_03_HU",
        "PSU_03_UA": "PSU_03_HU",
        "PSU_04_PL": "PSU_06_HU",
        "PSU_04_UA": "PSU_04_HU",
        "PSU_06_UA": "PSU_06_HU",
        "PSU_10_PL": "PSU_05_HU",
        "PSU_10_UA": "PSU_05_HU",
        "PSU_11_PL": "PSU_12_HU",
        "PSU_11_UA": "PSU_12_HU",
        "PSU_12_UA": "PSU_14_HU",
        "PSU_15_UA": "PSU_09_UA",
        "PSU_16_UA": "PSU_15_HU",
        "PSU_12_PL": "PSU_15_HU",
        "PSU_13_PL": "PSU_15_HU",
        "FAN_01_PL": "FAN_01_HU",
        "FAN_01_UA": "FAN_01_HU",
        "GPU_01_PL": "GPU_01_HU",
        "GPU_01_UA": "GPU_01_HU",
        "GPU_02_PL": "GPU_02_HU",
        "GPU_02_UA": "GPU_02_HU",
        "GPU_03_UA": "GPU_02_HU",
        "GPU_04_UA": "GPU_02_HU",
        "GPU_03_PL": "GPU_03_HU",
        "GPU_04_PL": "GPU_04_HU",
        "GPU_05_PL": "GPU_05_HU",
        "GPU_07_PL": "GPU_07_HU",
        "GPU_08_PL": "GPU_13_HU",
        "GPU_10_PL": "GPU_14_HU",
        "GPU_12_PL": "GPU_12_HU",
        "GPU_15_PL": "GPU_08_HU",
        "GPU_16_HU": "GPU_17_HU",
        "GPU_17_HU": "GPU_19_HU",
        "GPU_18_HU": "GPU_19_HU",
        "GPU_22_PL": "GPU_17_HU",
        "GPU_23_PL": "GPU_17_HU",
        "GPU_24_PL": "GPU_17_HU",
        "GPU_26_PL": "GPU_18_HU",
        "GPU_27_PL": "GPU_20_HU",
        "GPU_30_UA": "GPU_17_HU",
        "GPU_31_UA": "GPU_17_HU",
        "GPU_34_UA": "GPU_20_HU",
        "GPU_35_UA": "GPU_21_HU",
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

    def item_paid_uah(item):
        try:
            paid_uah = float(item.get("Paid_UAH", 0) or 0)
        except Exception:
            paid_uah = 0
        return paid_uah

    def price_to_huf(item):
        return price_value_to_huf(item["Price"], item["Currency"], item["HUF_Est"])

    def price_to_uah(item):
        paid_uah = item_paid_uah(item)
        if paid_uah > 0:
            return paid_uah
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
                    "UAH_Mode": "receipt" if item_paid_uah(item) > 0 else "rate estimate",
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
        value="Current real build",
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
                    <div class="pc-section-subtitle">Current paid/pending build from the hub. Swap only if a real order changes.</div>
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
    paste_country = mo.ui.dropdown(
        options=markets_for("Thermal paste"),
        value=market_for(_base_parts["Thermal paste"]),
        full_width=True,
    )
    case_country = mo.ui.dropdown(
        options=markets_for("Case"),
        value=market_for(_base_parts["Case"]),
        full_width=True,
    )
    fan_country = mo.ui.dropdown(
        options=markets_for("Fan"),
        value=market_for(_base_parts["Extra fans"]),
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
        fan_country,
        gpu_country,
        memory_country,
        paste_country,
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
    fan_country,
    gpu_country,
    memory_country,
    mo,
    paste_country,
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
    paste_choice = picker("Thermal paste", _base_parts["Thermal paste"], paste_country)
    case_choice = picker("Case", _base_parts["Case"], case_country)
    fan_choice = picker("Fan", _base_parts["Extra fans"], fan_country)
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
            part_row("Thermal paste", paste_country, paste_choice),
            part_row("Case", case_country, case_choice),
            part_row("Extra fans", fan_country, fan_choice),
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
        fan_choice,
        gpu_choice,
        memory_choice,
        paste_choice,
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
    fan_choice,
    gpu_choice,
    get_previous_snapshot,
    memory_choice,
    paste_choice,
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
        "Thermal paste": paste_choice.value,
        "Case": case_choice.value,
        "Extra fans": fan_choice.value,
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
                <th class="pc-num pc-col-head-uah"><span class="pc-head-compact">UAH<br>cash</span></th>
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
            UAH cash view uses exact receipt UAH where paid. Pending/unpaid rows use locked order-planning rates: 1 PLN = {rates["pln_to_uah"]:.4f} UAH, 100 HUF = {(rates["huf_to_uah"] * 100):.2f} UAH. HUF comparison only: 1 PLN = {rates["pln_to_huf"]:.2f} HUF.
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
    fx_takeaway = (
        "These are locked accounting rates for the current build, not live Monobank rates. "
        "Paid rows use receipt UAH first; rates only fill pending rows and comparisons."
    )

    mo.Html(
        f"""
        <div class="pc-wrap pc-section">
          <div class="pc-panel">
          <h2>FX logic</h2>
          <div class="pc-muted">
            UAH is the real cash view. Receipt UAH wins for paid items; fixed order-planning rates keep pending items and comparisons stable.
          </div>
          <table class="pc-table" style="margin-top: 12px;">
            <thead>
              <tr>
                <th>What we use</th>
                <th class="pc-num">Locked rate</th>
                <th>Why it matters</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1 PLN order-planning rate</td>
                <td class="pc-num">{uah_per_pln:.4f} UAH</td>
                <td>Used for pending Polish rows and stable PLN comparisons until exact payment receipts exist.</td>
              </tr>
              <tr>
                <td>100 HUF order-planning rate</td>
                <td class="pc-num">{uah_per_100_huf:.2f} UAH</td>
                <td>Used for pending Hungarian rows and stable HUF comparisons where exact UAH receipt is absent.</td>
              </tr>
              <tr>
                <td>1 PLN in HUF comparison</td>
                <td class="pc-num">{huf_per_pln:.2f} HUF</td>
                <td>Secondary comparison only: fixed PLN->UAH divided by fixed HUF->UAH.</td>
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
