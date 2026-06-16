import marimo

__generated_with = "0.23.9"
app = marimo.App(width="full")


@app.cell
def _():
    import html
    import json
    from datetime import datetime
    from pathlib import Path
    from urllib.request import Request, urlopen

    import marimo as mo
    import pandas as pd

    ROOT = Path(__file__).resolve().parents[1]
    PARTS_CSV = ROOT / "02_PC_Builds" / "parts_options_seed.csv"
    EU_LOWEST_CSV = ROOT / "02_PC_Builds" / "eu_lowest_price_seed.csv"

    parts = pd.read_csv(PARTS_CSV)
    parts["Price"] = pd.to_numeric(parts["Price"], errors="coerce").fillna(0)
    parts["HUF_Est"] = pd.to_numeric(parts["HUF_Est"], errors="coerce").fillna(0)
    eu_lowest = pd.read_csv(EU_LOWEST_CSV)
    eu_lowest["EU_Price"] = pd.to_numeric(eu_lowest["EU_Price"], errors="coerce")
    return Path, Request, datetime, eu_lowest, html, json, mo, parts, pd, urlopen


@app.cell
def _(Path, Request, datetime, json, urlopen):
    def load_rates():
        cache_path = (
            Path(__file__).resolve().parents[1]
            / "04_Tools"
            / ".rate_cache.json"
        )
        cache_ttl_minutes = 15
        rates = {
            "source": "saved fallback",
            "checked": "offline fallback",
            "eur_to_huf": 352.88,
            "eur_to_uah": 52.3396,
            "pln_to_uah": 12.2981,
            "huf_to_uah": 0.1484,
        }

        cached_rates = None
        if cache_path.exists():
            try:
                cached_rates = json.loads(cache_path.read_text(encoding="utf-8"))
            except Exception:
                cached_rates = None

        if cached_rates:
            fetched_at = cached_rates.get("fetched_at")
            if fetched_at:
                try:
                    fetched_dt = datetime.fromisoformat(fetched_at)
                    age_minutes = (
                        datetime.now() - fetched_dt
                    ).total_seconds() / 60
                    if age_minutes <= cache_ttl_minutes:
                        return cached_rates
                except Exception:
                    pass

        mono_ok = False
        try:
            req = Request(
                "https://api.monobank.ua/bank/currency",
                headers={"User-Agent": "pc-build-research/1.0"},
            )
            mono = json.load(urlopen(req, timeout=6))
            mono_ok = True
            for row in mono:
                pair = (row.get("currencyCodeA"), row.get("currencyCodeB"))
                if pair == (978, 980):
                    rates["eur_to_uah"] = float(row.get("rateSell") or row.get("rateCross"))
                elif pair == (985, 980):
                    rates["pln_to_uah"] = float(row.get("rateCross"))
                elif pair == (348, 980):
                    rates["huf_to_uah"] = float(row.get("rateCross"))
        except Exception:
            if cached_rates:
                cached_rates["source"] = (
                    f'{cached_rates.get("source", "cached live snapshot")} (cached)'
                )
                cached_rates["checked"] = (
                    f'{cached_rates.get("checked", "unknown")} | reused after Monobank limit'
                )
                return cached_rates
            mono_ok = False

        if mono_ok:
            rates["eur_to_huf"] = rates["eur_to_uah"] / rates["huf_to_uah"]
            rates["source"] = "Monobank public card/payment rates"
            rates["checked"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            rates["pln_to_huf"] = rates["pln_to_uah"] / rates["huf_to_uah"]
            rates["fetched_at"] = datetime.now().isoformat(timespec="seconds")

            try:
                cache_path.write_text(
                    json.dumps(rates, ensure_ascii=True, indent=2),
                    encoding="utf-8",
                )
            except Exception:
                pass

            return rates

        rates["pln_to_huf"] = rates["pln_to_uah"] / rates["huf_to_uah"]
        return rates

    rates = load_rates()
    return (rates,)


@app.cell
def _():
    builds = {
        "Best value: Poland + Lian Li": {
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
        "CPU_02_PL": "CPU_02_HU",
        "CPU_03_PL": "CPU_03_HU",
        "MB_01_PL": "MB_01_HU",
        "MB_02_PL": "MB_02_HU",
        "MB_04_PL": "MB_04_HU",
        "RAM_01_PL": "RAM_01_HU",
        "RAM_02_PL": "RAM_02_HU",
        "RAM_03_PL": "RAM_03_HU",
        "RAM_04_PL": "RAM_04_HU",
        "SSD_01_PL": "SSD_01_HU",
        "SSD_02_PL": "SSD_02_HU",
        "COOL_02_PL": "COOL_02_HU",
        "COOL_03_PL": "COOL_03_HU",
        "COOL_04_PL": "COOL_04_HU",
        "COOL_06_PL": "COOL_06_HU",
        "PSU_02_PL": "PSU_02_HU",
        "PSU_03_PL": "PSU_03_HU",
        "GPU_01_PL": "GPU_01_HU",
        "GPU_02_PL": "GPU_02_HU",
        "GPU_03_PL": "GPU_03_HU",
        "GPU_04_PL": "GPU_04_HU",
        "GPU_05_PL": "GPU_05_HU",
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
            grid-template-columns: repeat(2, 1fr);
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
            Choose one build, then adjust any part if needed. Totals, live FX, and estimated saving update below.
          </div>
        </div>
        """
    )
    return


@app.cell
def _(builds, mo):
    build_choice = mo.ui.dropdown(
        options=list(builds.keys()),
        value="Best value: Poland + Lian Li",
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

    parts_ui = mo.vstack(
        [
            mo.Html(
                """
                <div class="pc-wrap pc-section" style="margin-top: 0;">
                  <div class="pc-control-shell pc-parts-shell" style="padding-top: 12px; padding-bottom: 12px;">
                    <div class="pc-section-title">Change Parts</div>
                    <div class="pc-section-subtitle" style="margin-bottom: 10px;">Optional: change any part and the numbers below update.</div>
                """
            ),
            mo.hstack([mo.Html('<div class="pc-build-label">CPU</div>'), cpu_choice], justify="start"),
            mo.hstack([mo.Html('<div class="pc-build-label">Main board</div>'), board_choice], justify="start"),
            mo.hstack([mo.Html('<div class="pc-build-label">Memory</div>'), memory_choice], justify="start"),
            mo.hstack([mo.Html('<div class="pc-build-label">Storage</div>'), storage_choice], justify="start"),
            mo.hstack([mo.Html('<div class="pc-build-label">Power supply</div>'), psu_choice], justify="start"),
            mo.hstack([mo.Html('<div class="pc-build-label">Cooler</div>'), cooler_choice], justify="start"),
            mo.hstack([mo.Html('<div class="pc-build-label">Case</div>'), case_choice], justify="start"),
            mo.hstack([mo.Html('<div class="pc-build-label">Graphics card</div>'), gpu_choice], justify="start"),
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
    pay_poland = int(selected_table.loc[selected_table["Market"].eq("Poland"), "HUF"].sum())
    pay_hungary = int(selected_table.loc[selected_table["Market"].eq("Hungary"), "HUF"].sum())
    total_eur = int(round(total_huf / rates["eur_to_huf"]))

    summary_values = {
        "build-total:huf": total_huf,
        "build-total:uah": total_uah,
        "summary-total:huf": total_huf,
        "summary-total:uah": total_uah,
        "summary-total:eur": total_eur,
        "summary-poland:huf": pay_poland,
        "summary-hungary:huf": pay_hungary,
        "summary-saving:huf": total_saving,
        "summary-saving:uah": total_saving_uah,
    }

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
    for _, _row in selected_table.iterrows():
        market_class = "pc-pol" if _row["Market"] == "Poland" else "pc-hu"
        if _row["Market"] == "No GPU":
            market_class = ""
        row_key = str(_row["Part"])
        body_rows.append(
            f"""
            <tr class="pc-compare-row">
              <td>{esc(_row["Part"])}</td>
              <td>{esc(_row["Model"])}</td>
              <td><span class="pc-pill {market_class}">{esc(_row["Market"])}</span></td>
              <td>{esc(_row["Store"])}</td>
              <td class="pc-num pc-col-price">{esc(_row["Price"])}</td>
              <td class="pc-num pc-col-huf {_diff_class_table(f"{row_key}:huf")}">{number_text(_row["HUF"])} HUF</td>
              <td class="pc-num pc-delta {_delta_class(f"{row_key}:huf")}">{_delta_text(f"{row_key}:huf")}</td>
              <td class="pc-num pc-col-uah {_diff_class_table(f"{row_key}:uah")}">{number_text(_row["UAH"])} UAH</td>
              <td class="pc-num pc-delta {_delta_class(f"{row_key}:uah")}">{_delta_text(f"{row_key}:uah")}</td>
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
              <col class="pc-col-huf-est">
              <col class="pc-col-delta">
              <col class="pc-col-uah-est">
              <col class="pc-col-delta">
            </colgroup>
            <thead>
              <tr>
                <th>Part</th>
                <th>Selected model</th>
                <th>Buy from</th>
                <th>Store</th>
                <th class="pc-num pc-col-head-price">Store price</th>
                <th class="pc-num pc-col-head-huf"><span class="pc-head-compact">HUF<br>est.</span></th>
                <th class="pc-num pc-th-delta"><span class="pc-head-compact">Δ<br>HUF</span></th>
                <th class="pc-num pc-col-head-uah"><span class="pc-head-compact">UAH<br>est.</span></th>
                <th class="pc-num pc-th-delta"><span class="pc-head-compact">Δ<br>UAH</span></th>
              </tr>
            </thead>
            <tbody>{''.join(body_rows)}</tbody>
            <tfoot>
              <tr>
                <td colspan="5" class="pc-col-total">Total estimate</td>
                <td class="pc-num pc-col-huf pc-col-total {_diff_class_table("build-total:huf")}">{number_text(_total_huf)} HUF</td>
                <td class="pc-num pc-delta"></td>
                <td class="pc-num pc-col-uah pc-col-total {_diff_class_table("build-total:uah")}">{number_text(_total_uah)} UAH</td>
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
    _pay_poland = int(selected_table.loc[selected_table["Market"].eq("Poland"), "UAH"].sum())
    _pay_hungary = int(selected_table.loc[selected_table["Market"].eq("Hungary"), "UAH"].sum())
    _pay_poland_huf = int(selected_table.loc[selected_table["Market"].eq("Poland"), "HUF"].sum())
    _pay_hungary_huf = int(selected_table.loc[selected_table["Market"].eq("Hungary"), "HUF"].sum())

    mo.Html(
        f"""
        <div class="pc-wrap pc-section" style="margin-top: 14px; padding-top: 0;">
          <div class="pc-card-row">
            <div class="pc-card {_flash_class(_card_state('summary-total:huf', 'summary-total:uah'), 'pc-card-flash')}">
              <div class="pc-label">Total price</div>
              <div class="pc-value {_diff_class_summary("summary-total:uah")}">{number_text(_total_uah)} UAH</div>
              <div class="pc-muted pc-col-huf {_diff_class_summary("summary-total:huf")}">{huf_text(_total_huf)} / {number_text(_total_eur)} EUR</div>
            </div>
            <div class="pc-card {_flash_class(_card_state('summary-poland:huf', 'summary-hungary:huf'), 'pc-card-flash')}">
              <div class="pc-label">Where money goes</div>
              <div class="pc-muted {_diff_class_summary("summary-poland:huf")}">Paid to Poland stores: {number_text(_pay_poland)} UAH / {huf_text(_pay_poland_huf)}</div>
              <div class="pc-muted {_diff_class_summary("summary-hungary:huf")}">Paid to Hungary stores: {number_text(_pay_hungary)} UAH / {huf_text(_pay_hungary_huf)}</div>
            </div>
            <div class="pc-card {_flash_class(_card_state('summary-saving:huf', 'summary-saving:uah'), 'pc-card-flash')}">
              <div class="pc-label">Estimated saving</div>
              <div class="pc-value pc-save {_diff_class_summary("summary-saving:uah")}">{number_text(_total_saving_uah)} UAH</div>
              <div class="pc-value-small pc-save {_diff_class_summary("summary-saving:huf")}">{huf_text(_total_saving)}</div>
              <div class="pc-muted">Compared with Hungarian reference prices</div>
            </div>
          </div>
          <div class="pc-note" style="margin-top: 14px;">
            Monobank rates used. 1 PLN = {rates["pln_to_uah"]:.4f} UAH, 100 HUF = {(rates["huf_to_uah"] * 100):.2f} UAH, so 1 PLN = {rates["pln_to_huf"]:.2f} HUF. Checked: {rates["checked"]}.
          </div>
        </div>
        """
    )
    return _pay_hungary, _pay_poland, _total_huf, _total_saving


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
                <div class="pc-basket-subtitle">Paid in store currency, then converted to UAH for your real spend view.</div>
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
                <div class="pc-basket-subtitle">Local-market items stay in HUF and are also shown in UAH for direct comparison.</div>
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
        fx_takeaway = "Lower PLN/HUF helps Poland. Your Polish basket converts into fewer HUF, so savings vs Hungary rise."
    elif huf_per_pln > 83:
        fx_takeaway = "Higher PLN/HUF hurts Poland. Your Polish basket converts into more HUF, so savings vs Hungary fall."
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
                <td>This is derived from Monobank only: PLN→UAH divided by HUF→UAH.</td>
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
          <div class="pc-panel">
          <h2>EU lowest-price check</h2>
          <div class="pc-muted">
            A quick sanity check against wider EU listings. Empty rows need exact product captures.
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
