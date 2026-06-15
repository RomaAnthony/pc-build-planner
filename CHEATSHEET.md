# PC Build Planner — Cheatsheet

## In One Sentence

**Original file = your work. WASM file = dad's link. Update WASM file when prices change.**

---

## The Three Facts

| Fact | Explanation |
|------|-------------|
| **Original problem** | Marimo notebook tried to read from disk + call APIs. Browsers can't do that. |
| **The solution** | Embedded CSV in code. No disk I/O needed. Works in browser. |
| **Your setup** | Two files: one for you (auto CSV), one for dad (manual CSV). |

---

## Your Daily Workflow

### Morning: Work on Prices
```bash
# Edit your CSV (as normal)
nano 02_PC_Builds/parts_options_seed.csv

# Test locally (reads CSV auto)
marimo run 04_Tools/pc_build_marimo.py

# See new prices instantly ✅
```

**Important:** Leave `pc_build_marimo_WASM_SAFE.py` alone. It updates manually.

---

### Evening: Dad Needs Update
```bash
# 1. Copy new CSV
cat 02_PC_Builds/parts_options_seed.csv

# 2. Open WASM file
nano 04_Tools/pc_build_marimo_WASM_SAFE.py

# 3. Find PARTS_CSV_DATA = """...
# 4. Replace old CSV with new CSV
# 5. Save

# 3. Export to HTML
marimo export html-wasm 04_Tools/pc_build_marimo_WASM_SAFE.py -o docs/planner.html

# 4. Push to GitHub
git add docs/planner.html
git commit -m "Update: new prices"
git push origin main

# Dad's link updates automatically ✅
```

---

## Two Files

```
pc_build_marimo.py
├─ Your working file
├─ Reads CSV automatically
├─ Use: marimo run 04_Tools/pc_build_marimo.py
└─ Fast feedback loop

pc_build_marimo_WASM_SAFE.py
├─ Dad's shared file
├─ Has CSV embedded (string)
├─ Use: Export to HTML when updating
└─ Works in browser, no setup
```

---

## The Original Problem (Why Two Files Exist)

```python
# BROKEN (original)
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]     # ❌ No __file__ in browser
PARTS_CSV = ROOT / "02_PC_Builds" / "parts.csv"
parts = pd.read_csv(PARTS_CSV)                 # ❌ No disk access in browser

# FIXED (WASM-safe)
from io import StringIO
PARTS_CSV_DATA = """ID,Part,...                 # ✅ String embedded in code
CSV_01,..."""
parts = pd.read_csv(StringIO(PARTS_CSV_DATA))  # ✅ Works in browser
```

---

## Dad's Link

```
https://romaanthony.github.io/pc-build-planner/planner.html
```

Send him this. He opens it in any browser. Done.

---

## Files to Remember

| File | What It Is | What To Do |
|------|-----------|-----------|
| `02_PC_Builds/parts_options_seed.csv` | Your CSV | Edit freely, test with original file |
| `04_Tools/pc_build_marimo.py` | Your working file | Use daily, reads CSV auto |
| `04_Tools/pc_build_marimo_WASM_SAFE.py` | Dad's shared file | Update when copying CSV changes |
| `docs/planner.html` | Live for dad | Auto-generated, don't edit by hand |

---

## When Something Goes Wrong

| Problem | Fix |
|---------|-----|
| Original file doesn't read CSV | Check CSV path, file permissions |
| WASM file has old prices | Copy new CSV into PARTS_CSV_DATA |
| Dad's link shows old prices | Re-export HTML and push to GitHub |
| marimo: command not found | Activate venv: `source .venv_marimo/bin/activate` |

---

## Bottom Line

✅ **You:** Edit CSV, test with original file  
✅ **Dad:** Clicks link, sees live prices  
✅ **Update:** Copy CSV to WASM file, export, push  
✅ **Learning:** Two files show why browsers are different  

Done.
