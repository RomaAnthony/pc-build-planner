# Why Browser Sandbox Breaks Your Export

## The Core Issue

When marimo exports to **HTML-WASM**, the code runs in a **browser sandbox**—not on your computer. This means:

```
YOUR COMPUTER (Desktop)        vs        BROWSER (Sandbox)
═══════════════════════════════════════════════════════════
✅ pathlib.Path(__file__)              ❌ No filesystem access
✅ Read files from disk                ❌ No disk I/O
✅ urllib.urlopen() requests           ⚠️  Only certain origins allowed
✅ Direct HTTP calls                   ⚠️  CORS restrictions apply
```

---

## Example: Why It Crashes

### ❌ Original Code (Fails in Browser)
```python
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]      # ← ERROR: No __file__ in browser
PARTS_CSV = ROOT / "02_PC_Builds" / "..."
parts = pd.read_csv(PARTS_CSV)                  # ← ERROR: Can't read disk
```

**Error in browser:** `"An internal error occurred"` → marimo catches the exception, display fails.

---

### ✅ Fixed Code (Works in Browser)
```python
from io import StringIO

# CSV embedded as a string literal
PARTS_CSV_DATA = """ID,Part,Priority,Option,...
CPU_01_HU,CPU,1,AMD Ryzen 9 9900X Box,...
..."""

# Parse from string, not disk
parts = pd.read_csv(StringIO(PARTS_CSV_DATA))
```

**Why this works:** Strings are bundled in the HTML file. No filesystem needed.

---

## The HTTP/API Problem

### ❌ Original (Can fail in WASM)
```python
from urllib.request import Request, urlopen

req = Request("https://api.monobank.ua/bank/currency", ...)
mono = json.load(urlopen(req, timeout=6))  # ← urllib doesn't work in Pyodide
```

### ✅ Fixed (Graceful fallback)
```python
try:
    from urllib.request import Request, urlopen
    # ... try to load live rates
    mono = json.load(urlopen(req, timeout=6))
except Exception:
    # API call failed → use hardcoded fallback
    # Still works, just using last-known rates
    pass
```

**Result:** If the API fails (or CORS blocks it), you get fallback rates. The app doesn't crash.

---

## What Happens During Export

```
Step 1: marimo export html-wasm cmd
           ↓
Step 2: Compiles Python to WebAssembly (Pyodide)
           ↓
Step 3: Bundles everything into a single HTML file
           ↓
Step 4: ⚠️ Pyodide runs in browser context
           ├─ No __file__ path available
           ├─ No filesystem mounts
           └─ urllib.request unavailable
           ↓
Step 5: Browser runs HTML → Python code executes
           ├─ CSV loads from embedded string ✅
           ├─ Dropdowns and tables work ✅
           ├─ Exchange rates load if possible ✅
           └─ Falls back gracefully ✅
```

---

## Testing the Fix

### 1. Local (Desktop) — Uses Original Code
```bash
marimo run 04_Tools/pc_build_marimo.py
```
✅ All features work. Live API calls work. Everything fast.

### 2. Export (WASM) — Uses WASM-Safe Code
```bash
marimo export html-wasm 04_Tools/pc_build_marimo_WASM_SAFE.py -o docs/planner.html
```
✅ No "internal error". All UI works. Rates may be fallback (that's OK).

### 3. Browser (Sandbox) — Testing Deployment
```
Open docs/planner.html in browser
```
✅ Dropdowns work. Tables update. No crashes.

---

## Lessons

| Don't Do | Do This | Why |
|----------|---------|-----|
| `Path(__file__)` | Remove it | No `__file__` in browser |
| `read_csv("/path/file.csv")` | Embed CSV string | No disk access |
| `urllib.urlopen()` in WASM | `try/except` + fallback | Pyodide limitation |
| Assume APIs always work | Include fallback rates | CORS may block API |

---

## Extra: If You Need Live Exchange Rates

If fallback rates aren't good enough, use a CORS proxy:

```python
async def fetch_rates():
    from js import fetch
    # CORS proxy unwraps the API response
    resp = await fetch(
        "https://api.allorigins.win/get?url=https%3A%2F%2Fapi.monobank.ua%2Fbank%2Fcurrency"
    )
    data = (await resp.json())["contents"]
    return json.loads(data)
```

But honestly? **Fallback rates are fine for a static build tool.** Users don't expect them to update every load.

---

## Summary

**Original problem:** Code designed for desktop can't run in browser sandbox.

**Solution:** 
1. Embed data instead of loading from disk
2. Add try/except for APIs
3. Use fallback values

**Result:** One HTML file that works offline and online. Ship it to GitHub Pages. Done.
