# Deploy to GitHub Pages — Action Steps

## Right Now (5 minutes)

### 1. Test the Fixed Version
```bash
cd ~/OneDrive/Files_Roman/06_Personal/Personal_Projects/Hungarian_PC_Parts_Market
marimo run 04_Tools/pc_build_marimo_WASM_SAFE.py
```
✅ All dropdowns work? All tables update? → Continue to step 2

### 2. Export to HTML-WASM
```bash
marimo export html-wasm 04_Tools/pc_build_marimo_WASM_SAFE.py -o docs/planner.html
```
✅ No errors? File created at `docs/planner.html`? → Continue to step 3

### 3. Open in Browser (Test Locally)
```bash
open docs/planner.html
```
✅ No "An internal error occurred"? All UI works? → Continue to step 4

### 4. Commit & Push
```bash
cd /Users/romaantonyak/OneDrive/Files_Roman/06_Personal/Personal_Projects/Hungarian_PC_Parts_Market

git add docs/planner.html
git commit -m "Fix: WASM-safe marimo export to HTML"
git push origin main
```

### 5. Verify on GitHub Pages
Visit your GitHub Pages URL:
```
https://romaanthony.github.io/pc-build-planner/planner.html
```
✅ Works? Done!

---

## If Something Goes Wrong

| Problem | Fix |
|---------|-----|
| `marimo: command not found` | `pip install marimo` |
| Export produces no file | Check file permissions in `docs/` |
| "Internal error" in browser | Reload hard: `Cmd+Shift+R` (macOS) |
| Exchange rates show "offline fallback" | That's OK—API is blocked by CORS (fallback works) |
| GitHub Pages not enabled | Settings → Pages → Source = `main` → `docs/` folder |

---

## Files You Need to Know

| File | Purpose |
|------|---------|
| `04_Tools/pc_build_marimo_WASM_SAFE.py` | **Use THIS for export** |
| `04_Tools/pc_build_marimo.py` | Original (desktop use only) |
| `04_Tools/WASM_MIGRATION_GUIDE.md` | Technical details |
| `04_Tools/BROWSER_SANDBOX_EXPLAINED.md` | Why the fix works |
| `docs/planner.html` | **Generated output—commit this** |

---

## Reference: What Changed

### Before
```python
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]      # ❌ Fails in browser
PARTS_CSV = ROOT / "02_PC_Builds" / "parts_options_seed.csv"
parts = pd.read_csv(PARTS_CSV)                  # ❌ No filesystem
```

### After
```python
from io import StringIO
PARTS_CSV_DATA = """ID,Part,Priority,...     # ✅ Embedded string
CSV_01_HU,CPU,1,..."""
parts = pd.read_csv(StringIO(PARTS_CSV_DATA))  # ✅ Works everywhere
```

---

Done! You now have a browser-safe export that works on GitHub Pages.
