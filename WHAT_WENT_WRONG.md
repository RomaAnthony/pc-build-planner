# What Was Wrong — Simple Explanation

## The Original Problem

Your original `pc_build_marimo.py` had this:

```python
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PARTS_CSV = ROOT / "02_PC_Builds" / "parts_options_seed.csv"

parts = pd.read_csv(PARTS_CSV)  # ← Load from disk

# Try to fetch live exchange rates
req = Request("https://api.monobank.ua/bank/currency", ...)
mono = json.load(urlopen(req, timeout=6))  # ← HTTP request
```

### Why It Failed in Browser

When you exported to HTML-WASM:
- **`__file__`** doesn't exist in browser → ERROR
- **`read_csv(path)`** can't access disk → ERROR
- **`urlopen()`** isn't available in Pyodide → ERROR

Browser crashed → **"An internal error occurred"**

---

## The Fix (What We Did)

We created `pc_build_marimo_WASM_SAFE.py`:

```python
from io import StringIO

# CSV embedded as a string (no disk needed)
PARTS_CSV_DATA = """ID,Part,Priority,...
CPU_01_HU,CPU,1,...
..."""

parts = pd.read_csv(StringIO(PARTS_CSV_DATA))  # ← Parse from string

# Try API, but don't crash if it fails
try:
    from urllib.request import Request, urlopen
    mono = json.load(urlopen(req, timeout=6))
except Exception:
    pass  # Use fallback rates instead
```

This works in browser because:
- ✅ No `__file__` path
- ✅ No disk I/O
- ✅ Graceful fallback if API fails

---

## The Two Files Going Forward

### 1. **`pc_build_marimo.py`** (Original)
- **Use for:** Desktop development (`marimo run`)
- **Updates from:** CSV file directly
- **Why:** Fast to test locally, no embedding needed
- **Action:** Leave alone, use for learning/testing

### 2. **`pc_build_marimo_WASM_SAFE.py`** (Fixed)
- **Use for:** Sharing with your dad
- **Updates:** Manual (copy CSV changes into code)
- **Why:** Works in browser, single file
- **Action:** Update manually when prices change

---

## Your Workflow Going Forward

### When You're Learning/Testing

```bash
# Work with original file (reads CSV automatically)
marimo run 04_Tools/pc_build_marimo.py

# Test changes locally
# All CSV updates work instantly
# No manual sync needed
```

### When You Want to Share Updates

```bash
# 1. Make changes in CSV (as usual)
# 2. Copy prices into WASM-SAFE file (manual step)
# 3. Export to HTML
# 4. Push to GitHub

marimo export html-wasm 04_Tools/pc_build_marimo_WASM_SAFE.py -o docs/planner.html
git add docs/planner.html
git commit -m "Update: prices from CSV"
git push origin main
```

---

## Why Two Files?

| File | For | CSV Sync | How It Works |
|------|-----|----------|--------------|
| `pc_build_marimo.py` | You (desktop) | Automatic | Reads CSV file |
| `pc_build_marimo_WASM_SAFE.py` | Dad (browser) | Manual | Embedded string |

**Example:**

You update prices in CSV → Open `pc_build_marimo.py` locally → Everything works instantly

Your dad needs new prices → You copy CSV into WASM-SAFE file → Export → Push → Dad reloads link

---

## The Manual Update Process

When you find new prices:

### Step 1: Update CSV (as usual)
```
02_PC_Builds/parts_options_seed.csv
│
└─ CPU_01_PL: 1349 PLN → 1299 PLN
```

### Step 2: Copy to Python File
```
04_Tools/pc_build_marimo_WASM_SAFE.py
│
└─ Find PARTS_CSV_DATA string
   └─ Find same CPU_01_PL line
   └─ Change price: 1349 → 1299
```

### Step 3: Re-export & Push
```bash
marimo export html-wasm 04_Tools/pc_build_marimo_WASM_SAFE.py -o docs/planner.html
git add docs/planner.html
git commit -m "Update: CPU price"
git push origin main
```

---

## Summary

✅ **Original file** — Leave alone, use for testing locally (reads CSV auto)  
✅ **WASM-Safe file** — Use for sharing, update manually (embed CSV in code)  
✅ **Your dad** — Always uses the deployed HTML link (single file, no setup)  

The original file works great on your desktop because it has file system access. The WASM version works in browsers because it has no dependencies on the file system.

Two files = best of both worlds.
