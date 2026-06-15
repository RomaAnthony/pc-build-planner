# Your Workflow — Two Files, One Vision

## Day-to-Day: Work With the Original File

This reads your CSV automatically. Use this for learning and testing.

```bash
# Always use this when you're working locally
marimo run 04_Tools/pc_build_marimo.py
```

✅ Changes in CSV show up instantly
✅ No manual copying needed
✅ Fast to test and experiment
✅ This is your real working file

---

## Share With Dad: Update the WASM File

When your dad needs new prices, you update the shared version.

```bash
# 1. Make changes in your CSV (as usual)
# 2. Open the WASM-SAFE file
# 3. Find the PARTS_CSV_DATA string at the top
# 4. Copy-paste the new CSV content there
# 5. Save and export

marimo export html-wasm 04_Tools/pc_build_marimo_WASM_SAFE.py -o docs/planner.html
git add docs/planner.html
git commit -m "Update: new prices"
git push origin main
```

✅ Your dad's link updates automatically (takes 30 seconds)
✅ He doesn't need to do anything
✅ He always has the latest prices

---

## The Two-File Strategy

### Original: `pc_build_marimo.py`
```python
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS_CSV = ROOT / "02_PC_Builds" / "parts_options_seed.csv"
parts = pd.read_csv(PARTS_CSV)  # ← Reads your CSV file automatically
```

**For you:**
- Fast to test
- CSV updates instantly
- No manual sync
- Use for development

---

### WASM-Safe: `pc_build_marimo_WASM_SAFE.py`
```python
from io import StringIO

PARTS_CSV_DATA = """ID,Part,Priority,...
CPU_01_HU,CPU,1,...
..."""  # ← CSV content embedded as string

parts = pd.read_csv(StringIO(PARTS_CSV_DATA))  # ← Parses the string
```

**For your dad:**
- Works in browser
- Single HTML file
- No dependencies
- Manual update from CSV

---

## Simple Update Checklist

When you find better prices:

1. **Edit CSV**
   ```
   02_PC_Builds/parts_options_seed.csv
   ```
   Change: `CPU_01_PL,CPU,1,...,1349,PLN,...`  
   To: `CPU_01_PL,CPU,1,...,1299,PLN,...`

2. **Test locally** (with original file)
   ```bash
   marimo run 04_Tools/pc_build_marimo.py
   ```
   ✅ New prices showing? Good!

3. **Update WASM file**
   ```
   Open: 04_Tools/pc_build_marimo_WASM_SAFE.py
   Find: PARTS_CSV_DATA = """...
   Paste: New CSV content with same changes
   ```

4. **Export & push**
   ```bash
   marimo export html-wasm 04_Tools/pc_build_marimo_WASM_SAFE.py -o docs/planner.html
   git add docs/planner.html
   git commit -m "Update: new prices"
   git push origin main
   ```

5. **Your dad reloads**
   ```
   https://romaanthony.github.io/pc-build-planner/planner.html
   ```
   ✅ New prices live!

---

## Why This Works

| Need | Use File | Why |
|------|----------|-----|
| Fast testing | `pc_build_marimo.py` | Reads CSV automatically |
| Share with dad | `pc_build_marimo_WASM_SAFE.py` | Works in browser |
| Your workflow | Both | Original for dev, WASM for deploy |

---

## Future: Automate This

Later, if you want, I can help you:
- **Auto-sync** CSV to Python file (no manual copy-paste)
- **Auto-export** when you push to GitHub
- **Auto-update** your dad's link

For now? Manual is fine. You're learning. ✅

---

## Files to Keep

```
04_Tools/
├── pc_build_marimo.py             ← Your working file (auto CSV)
├── pc_build_marimo_WASM_SAFE.py   ← Dad's shared file (embedded CSV)
├── WASM_MIGRATION_GUIDE.md        ← Why WASM version exists
└── HOW_TO_UPDATE_PRICES.md        ← How to update manually

02_PC_Builds/
└── parts_options_seed.csv         ← Your source of truth

docs/
└── planner.html                   ← Live version for dad
```

Everything is set up. You can work naturally with CSV, and manually sync when dad needs updates.
