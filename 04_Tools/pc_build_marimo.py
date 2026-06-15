import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")


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

    parts = pd.read_csv(PARTS_CSV)
    parts["Price"] = pd.to_numeric(parts["Price"], errors="coerce").fillna(0)
    parts["HUF_Est"] = pd.to_numeric(parts["HUF_Est"], errors="coerce").fillna(0)
    return Request, datetime, html, json, mo, parts, pd, urlopen


@app.cell
def _(Request, datetime, json, urlopen):
    def load_rates():
        rates = {
            "source": "saved fallback",
            "checked": "offline fallback",
            "eur_to_huf": 352.88,
            "eur_to_uah": 52.3396,
            "pln_to_uah": 12.2981,
            "huf_to_uah": 0.1484,
        }

        try:
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
            pass

        try:
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
          /* DARK MODE THEME - FORCE DARK */
          :root { color-scheme: dark; }
          html { background: #0f1419 !important; }
          body { 
            background: #0f1419 !important; 
            color: #e3e8ef !important;
            margin: 0;
            padding: 0;
          }
          * { color-scheme: dark !important; }
          
          .pc-wrap { max-width: 1080px; }
          .pc-title { font-size: 42px; font-weight: 760; margin: 8px 0 8px; color: #ffffff; }
          .pc-subtitle { color: #a0aec0; font-size: 16px; max-width: 780px; margin-bottom: 24px; }
          .pc-section { margin-top: 30px; }
          
          .pc-card-row { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; margin-top: 14px; }
          .pc-card { border: 1px solid #2d3748; border-radius: 12px; background: #1a202c; padding: 16px; }
          .pc-label { color: #a0aec0; font-size: 12px; text-transform: uppercase; letter-spacing: .03em; }
          .pc-value { color: #ffffff; font-size: 26px; font-weight: 800; margin-top: 8px; }
          .pc-muted { color: #a0aec0; font-size: 13px; margin-top: 6px; }
          .pc-save { color: #68d391; font-weight: 800; }
          
          .pc-table { width: 100%; border-collapse: collapse; margin-top: 16px; font-size: 15px; }
          .pc-table th { color: #a0aec0; text-align: left; padding: 10px 8px; border-bottom: 1px solid #2d3748; background: #111827; }
          .pc-table td { padding: 11px 8px; border-bottom: 1px solid #2d3748; vertical-align: top; color: #e3e8ef; }
          
          .pc-pill { display: inline-block; padding: 3px 9px; border-radius: 999px; font-size: 12px; background: #2d3748; }
          .pc-pol { color: #9ae6b4; background: rgba(56,178,72,.2); }
          .pc-hu { color: #90cdf4; background: rgba(66,153,225,.2); }
          
          .pc-note { border-left: 3px solid #4299e1; padding-left: 12px; color: #cbd5e1; margin-top: 10px; background: rgba(66,153,225,.1); padding: 10px; border-radius: 4px; }
          .pc-editor { display: grid; grid-template-columns: 160px 1fr; gap: 10px 14px; align-items: center; margin-top: 14px; }
          .pc-editor-label { color: #cbd5e1; font-weight: 700; }
          
          /* Marimo input styling */
          input, select, textarea { background: #2d3748 !important; color: #e3e8ef !important; border: 1px solid #4a5568 !important; }
          input::placeholder { color: #718096; }
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
    part_sources = {
        "CPU": "CPU",
        "Main board": "Motherboard",
        "Memory": "RAM",
        "Storage": "SSD",
        "Power supply": "PSU",
        "Cooler": "Cooler",
        "Case": "Case",
        "Graphics card": "GPU",
    }

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
