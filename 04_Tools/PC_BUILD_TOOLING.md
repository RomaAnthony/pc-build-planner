# PC Build Tooling

Date: 2026-06-15

This note tracks the simple tool stack for the PC build comparison project.

## Current Decision

Use **Marimo + CSV + pandas/DuckDB** as the main working setup.

Reason:

- easier for Codex to edit than Excel
- data stays in simple CSV files
- live totals and dropdowns work without hand-written Excel formulas
- Python/SQL workflow is useful for Roman's finance, SQL, database, and AI-learning goals
- output can later be exported to Excel/PDF only when needed

## Current Architecture Rule

Date: 2026-06-15

Current source of truth:

- Product data lives in `02_PC_Builds/parts_options_seed.csv`.
- Local dashboard logic lives in `04_Tools/pc_build_marimo.py`.
- GitHub Pages/browser dashboard logic lives in `04_Tools/pc_build_marimo_WASM_SAFE.py`.
- Published static page lives at `docs/planner.html`.

Important rule:

- Do not embed the parts database inside `pc_build_marimo.py`; that file is for local work and should read the CSV directly.
- It is acceptable for `pc_build_marimo_WASM_SAFE.py` to embed the parts database, because GitHub Pages / browser WASM cannot reliably read Roman's live local CSV file.
- Keep the two-file boundary explicit: local file = live CSV, WASM-safe file = browser-safe snapshot.

Why this matters:

- CSV is easy for Roman/Codex to update.
- The embedded WASM table can drift from the CSV, so the update workflow must include a sync/copy step before export.
- The long-term improvement is to automate CSV-to-WASM sync, but for now manual sync is acceptable because it is the only proven GitHub Pages route.

## Payment / FX Logic

Date: 2026-06-15

The dashboard must not treat exchange rates as a tiny background detail. Roman's real payment paths can change the best market:

- Dad's salary is effectively EUR-based in Ukraine.
- Money can become UAH automatically and sit on Ukrainian cards.
- Some money can be withdrawn/held as EUR cash in Hungary.
- Some money can be used from Hungarian cards/accounts.
- Girlfriend's Hungarian card may also be usable, with Roman settling separately.
- Polish purchases may be paid from UAH/EUR/HUF routes, so PLN conversion matters.

Current app rule:

- Show live/default rate assumptions at the top.
- Recalculate displayed HUF equivalents from original item currency (`PLN`, `HUF`, `EUR`) instead of trusting old hardcoded `HUF_Est`.
- Use Monobank/card-path rates as the first practical approximation for UAH-card payments.
- Keep ECB-style reference rates as a clean market benchmark.
- Keep manual overrides because K&H / Credit Agricole / exact card rates may be the real purchase rate on the day.

Before purchase:

- Check exact bank/card rate for the actual payment path.
- Use the app's manual rate boxes if Monobank/K&H/Credit Agricole rates differ from public reference rates.
- Treat displayed savings as decision estimates until the payment path is confirmed.

## EU Lowest-Price Sanity Checks

Roman captured GPUTracker pages on 2026-06-15:

- RTX 5080 wider EU low prices start around 1,289 EUR, mainly Palit/Germany listings.
- MSI RTX 5080 Ventus 3X OC appears around 1,332-1,373 EUR in wider EU tracker listings.
- Current Poland MSI Ventus lead at 4,899 PLN remains strong if seller/warranty/logistics are clean.
- 64GB DDR5 tracker page is useful only as a broad sanity check because many early results are laptop SO-DIMM, slower CL40/CL46, or not our target DDR5-6000 CL30 desktop kit.

Use GPUTracker as:

- "Are we overpaying versus the wider EU market?"
- "Which models are generally cheap right now?"

Do not use it as:

- final buy decision without checking exact seller, shipping, return, warranty, and payment route.

## Current Poland-Buy Logic

Date: 2026-06-15

Using Monobank-style PLN path around `1 PLN = 82.87 HUF`, current savings versus Hungarian references are approximately:

| Part | Poland logic | Approx. saving |
|---|---|---:|
| RAM 64GB Patriot | Definitely worth Poland if seller/warranty are clean | 84,600 HUF |
| RAM 32GB Patriot | Budget branch only; now has a clean same-model Hungary reference from Alza | ~18,500 HUF |
| SSD Kingston KC3000 2TB | Definitely worth Poland; small and easy to transport | 28,500 HUF |
| RTX 5080 MSI Ventus | Definitely worth Poland if x-kom/warranty remains clean | 93,100 HUF |
| CPU Ryzen 9 9900X | Worth considering if bundled with Poland order | 12,000 HUF |
| Motherboard MSI B850 Tomahawk MAX | Worth considering if exact model and warranty are clean | 16,600 HUF |
| PSU Corsair RM1000x ATX 3.1 | Worth considering if choosing this PSU anyway | 12,600 HUF |
| PSU Seasonic GX-1000 | Too small a Poland saving by itself | 3,100 HUF |
| Cooler Arctic | Too small a Poland saving; buy locally | 2,400 HUF |
| Case | Buy locally/Hungary because of size and glass logistics | n/a |

Current dashboard builds:

- `Main 64GB no GPU`: smart Poland route without GPU, around 616k HUF.
- `Budget 32GB no GPU`: lower-cost branch, around 504k HUF.
- `Full RTX 5080 later`: same smart platform plus MSI RTX 5080 Ventus from Poland, around 1.02M HUF.

These are not final purchase decisions. They are planning scenarios to show what the purchase could look like and where Poland creates real savings.

Savings rule:

- Count savings only when we have a same-model or clearly comparable Hungary reference.
- Do not count Patriot 32GB Poland against Kingston 32GB Hungary as a clean saving. It is a budget alternative, not the same-model saving proof.

## Dashboard Presentation Logic

The Dad-facing dashboard should show information in this order:

1. Big title and one-sentence explanation.
2. Exchange-rate strip: payment assumption, PLN/HUF, EUR/HUF, update time.
3. Three build cards:
   - Main 64GB no GPU
   - Budget 32GB no GPU
   - Full RTX 5080 later
4. Optional adjustment controls for RAM, SSD, and GPU.
5. Selected plan cards:
   - Total
   - Pay to Poland stores / pay to Hungary stores
   - Estimated saving
6. Simple parts table with only the useful columns.
7. Short decision logic table.
8. Full raw database hidden in an accordion.

Wording rule:

- Do not label a number only as "Hungary" or "Poland." Use "Pay to Hungary stores" and "Pay to Poland stores" so it is clear this is where the money goes, not a full-country comparison.

## GitHub Pages Publishing

Goal:

- Dad should open one website link.
- Roman/Codex should keep editing the Marimo app locally and export a fresh website when prices change.

Current status:

- GitHub account visible through the connector: `RomaAnthony`.
- This folder was not originally a Git repository.
- GitHub CLI (`gh`) is not installed in the local environment.
- The GitHub connector available in Codex can create/update text files in existing repositories, but the Marimo WASM export includes many binary assets, so the connector is not the best way to upload the whole site.

Local desktop command:

```bash
.venv_marimo/bin/marimo run 04_Tools/pc_build_marimo.py --host 127.0.0.1 --port 2718
```

GitHub Pages export command:

```bash
.venv_marimo/bin/marimo export html-wasm 04_Tools/pc_build_marimo_WASM_SAFE.py -o docs/planner.html
```

GitHub Pages setup:

1. Create an empty GitHub repository, for example `pc-build-planner`.
2. Push this project folder to that repository.
3. In GitHub repository settings, enable Pages from the `docs` folder on the main branch.
4. Share the Pages link with Dad.

Current working share link:

```text
https://romaanthony.github.io/pc-build-planner/planner.html
```

Important:

- The exported Marimo assets are large and generated; do not edit generated HTML by hand.
- Browser-based live exchange-rate fetching may depend on API/CORS behavior. The app has fallback rates, but final sharing should be tested from the published link.
- `docs/index.html` is risky/stale if it was generated from the local CSV-reading file. Use or share `docs/planner.html` until `index.html` is replaced with a redirect or a WASM-safe export.

## Active Files

- `02_PC_Builds/parts_options_seed.csv` - current parts database
- `04_Tools/pc_build_marimo.py` - local Marimo build comparison app; reads CSV
- `04_Tools/pc_build_marimo_WASM_SAFE.py` - GitHub Pages / Dad app; embedded CSV snapshot
- `04_Tools/requirements-marimo.txt` - minimal install list
- `docs/planner.html` - generated GitHub Pages export; rebuild after WASM-safe app changes

## Start App

From the project folder:

```bash
.venv_marimo/bin/marimo run 04_Tools/pc_build_marimo.py --host 127.0.0.1 --port 2718
```

Open:

```text
http://127.0.0.1:2718
```

## Reinstall Later

Use a stable Python 3.12 environment if possible.

```bash
python3 -m venv .venv_marimo
.venv_marimo/bin/python -m pip install --upgrade pip
.venv_marimo/bin/python -m pip install -r 04_Tools/requirements-marimo.txt
```

If Homebrew Python 3.14 fails during `venv` creation, use a stable Python 3.12 install instead.

## Tool Radar For This Project

### Use Now

- **Marimo** - best current fit for notebook + small dashboard + AI-friendly editing.
- **pandas** - simple table calculations.
- **DuckDB** - optional SQL layer; good for learning SQL and analyst-style joins/comparisons.
- **Plotly** - optional charts later.
- **openpyxl** - only for exporting a clean Excel file later.

### Maybe Later

- **Streamlit** - good if the Marimo notebook turns into a polished standalone app.
- **Grist** - worth testing if Roman wants a spreadsheet-database interface for manual editing.
- **Mito** - interesting for visual spreadsheet actions inside Python notebooks, but not needed yet.
- **Observable Framework** - powerful, but more JavaScript/web-oriented than needed now.

### Skip For Now

- **Hex** - strong collaborative cloud notebook, but overkill and cloud-first.
- **Rows** - interesting AI spreadsheet, but it brings us back into spreadsheet habits.
- **Taipy** - useful for heavier production apps, too much for this small decision model.
- **Panel/Dash** - powerful, but more code/UI work than Marimo for this stage.
- **Pluto.jl** - good Julia notebook, but not relevant unless we move into Julia.
- **Gradio** - excellent for ML model demos, not for parts/build comparison.

## Cleanup Log

- Removed failed partial `.venv` created by Homebrew Python 3.14.
- Kept `.venv_marimo` as the working local environment.
- Moved old Excel formula/hardcoded build experiments into `02_PC_Builds/99_Archive_Excel_Attempt`.

## Next Morning Checklist

Before improving the app design, audit the source data:

- Recheck every row in `02_PC_Builds/parts_options_seed.csv` against the working Markdown notes.
- Confirm which savings are exact same-model comparisons and which are only equivalent-part comparisons.
- Fix the RAM saving logic labels: Patriot Viper Venom 64GB Poland can now be compared to Hungary as a same-model comparison using the cleaner Elektroshock Hungary offer. Patriot Viper Venom 32GB Poland can now be compared to Hungary using the Alza Hungary offer from the new Arukereso capture.
- Live exchange-rate loading is now started in the Marimo app: Monobank/card path, ECB reference, and manual override controls.
- Redesign the Marimo view for a non-technical reader: fewer columns, bigger decision cards, clear "buy in Hungary" / "buy in Poland" labels, and one simple total.
- Verify the published Pages link after every export. The app should load without the red Marimo internal-error box.
- Verify the exact Dad link is `/planner.html`; the root URL may still serve stale `index.html`.
- Check whether old unpublished commits in GitHub Desktop need to be pushed before presenting to Dad.

Patriot update on 2026-06-15:

- Roman captured the exact Arukereso product page for Patriot Viper Venom PVV564G600C30K in Hungary.
- Lowest listed offer is 325,965 HUF but appears as a possible marketplace offer.
- Cleaner Dad-facing same-model comparison is Elektroshock at 328,435 HUF with 36-month warranty + EU + 2-3 day delivery shown.
- PCLand direct capture is 436,289 HUF and confirms the product exists locally, but it is too expensive for the value comparison.
