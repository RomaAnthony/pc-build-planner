# WASM Export Fix Guide

## The Problem
When exporting with `marimo export html-wasm`, the notebook crashes because:
1. **`pathlib.Path(__file__)`** — no filesystem in browser
2. **`pd.read_csv(PARTS_CSV)`** — can't load files from disk  
3. **`urllib.urlopen()`** — Pyodide can't make HTTP this way

## Solution: 3 Key Changes

### 1. **Embed CSV as a Python String**

❌ **BEFORE:**
```python
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
PARTS_CSV = ROOT / "02_PC_Builds" / "parts_options_seed.csv"
parts = pd.read_csv(PARTS_CSV)
```

✅ **AFTER:**
```python
from io import StringIO

PARTS_CSV_DATA = """ID,Part,Priority,...
CPU_01_HU,CPU,1,...
..."""

parts = pd.read_csv(StringIO(PARTS_CSV_DATA))
```

**Why:** Strings are bundled in the JS, no file I/O needed.

---

### 2. **Replace `urllib` with Fetch API**

❌ **BEFORE:**
```python
from urllib.request import Request, urlopen

req = Request("https://api.monobank.ua/...", 
              headers={"User-Agent": "..."})
mono = json.load(urlopen(req, timeout=6))
```

✅ **AFTER:**
```python
import asyncio
from js import fetch

async def fetch_mono():
    resp = await fetch("https://api.monobank.ua/...",
                       headers={"User-Agent": "..."})
    if resp.ok:
        return await resp.json()
    return None

mono = asyncio.run(fetch_mono())
```

**Why:** Pyodide's `js` module gives direct access to browser fetch.

---

### 3. **Remove Path Imports**

Delete all `from pathlib import Path` and any `Path(__file__)` references.

---

## Testing Before Export

1. **Run locally first:**
   ```bash
   cd /path/to/Hungarian_PC_Parts_Market
   marimo run 04_Tools/pc_build_marimo_WASM_SAFE.py
   ```
   Should work exactly the same.

2. **Export to HTML:**
   ```bash
   marimo export html-wasm 04_Tools/pc_build_marimo_WASM_SAFE.py -o docs/planner.html
   ```

3. **Test in browser:**
   - Open `docs/planner.html` locally
   - No "internal error" — all dropdowns work, rates load, tables populate
   - Rates may show fallback if API is blocked by CORS (that's OK, fallback works)

---

## Deployment to GitHub Pages

1. After successful export, commit:
   ```bash
   git add docs/planner.html
   git commit -m "Update: WASM-safe marimo export"
   git push origin main
   ```

2. GitHub Pages serves from `docs/` automatically (if enabled in Settings)

3. Visit: `https://<username>.github.io/<repo>/planner.html`

---

## If CORS Blocks API Calls

The exchange rate APIs may block cross-origin requests. Solution:

**Option A:** Use CORS proxy (cheap/reliable):
```python
resp = await fetch(
    "https://api.allorigins.win/get?url=https%3A%2F%2Fapi.monobank.ua%2Fbank%2Fcurrency"
)
data = (await resp.json())["contents"]
mono = json.loads(data)
```

**Option B:** Pre-compute rates, ship as constants (simplest):
```python
rates = {
    "eur_to_huf": 352.88,  # Last known good rate
    "eur_to_uah": 52.3396,
    # ... fallback always works
}
# (remove async fetch, just use these)
```

---

## Files to Update

- `04_Tools/pc_build_marimo.py` → keep original (desktop use)
- `04_Tools/pc_build_marimo_WASM_SAFE.py` → **use this for export**
- `docs/planner.html` → regenerate with export command

---

## Key Differences Summary

| Aspect | Desktop | WASM |
|--------|---------|------|
| CSV loading | `Path` + `read_csv()` | Embedded string + `StringIO` |
| HTTP requests | `urllib.request` | `js.fetch` + `asyncio` |
| File system | Direct access | No access (sandbox) |
| Exchange rates | Works always | May need CORS workaround |

---

## Next Steps

1. ✅ Read this guide
2. ✅ Copy `pc_build_marimo_WASM_SAFE.py` and test locally
3. ✅ Export to HTML
4. ✅ Verify in browser
5. ✅ Push to `docs/`
6. ✅ Test on GitHub Pages

Done!
