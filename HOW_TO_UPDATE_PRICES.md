# How to Update Prices (Simple 3-Step Guide)

## When You Find a Better Price

1. **Update the CSV** (`02_PC_Builds/parts_options_seed.csv`)
2. **Update the Python file** (`04_Tools/pc_build_marimo_WASM_SAFE.py`)
3. **Push to GitHub** (makes it live instantly)

---

## Step 1: Update the CSV

Open: `02_PC_Builds/parts_options_seed.csv`

Find the row you want to change. Example:
```
CPU_01_PL,CPU,1,AMD Ryzen 9 9900X Box,Poland,x-kom.pl,1349,PLN,112061,Compare,Medium,...
```

Change just the **Price column** (column 7):
```
CPU_01_PL,CPU,1,AMD Ryzen 9 9900X Box,Poland,x-kom.pl,1299,PLN,112061,Compare,Medium,...
                                                    ↑
                                              Changed: 1349 → 1299
```

**Save the file.**

---

## Step 2: Update the Python File

Open: `04_Tools/pc_build_marimo_WASM_SAFE.py`

Find the same line in the `PARTS_CSV_DATA` string (around line 20).

Change the **Price value** to match:
```python
PARTS_CSV_DATA = """ID,Part,Priority,...
CPU_01_PL,CPU,1,AMD Ryzen 9 9900X Box,Poland,x-kom.pl,1299,PLN,112061,Compare,Medium,...
                                                    ↑
                                              Change here too
...
```

**Save the file.**

---

## Step 3: Push to GitHub

```bash
cd ~/OneDrive/Files_Roman/06_Personal/Personal_Projects/Hungarian_PC_Parts_Market

git add 02_PC_Builds/parts_options_seed.csv 04_Tools/pc_build_marimo_WASM_SAFE.py

git commit -m "Update: new prices for CPU/RAM/GPU"

git push origin main
```

**Wait 30 seconds.** Then reload the link in your browser:
```
https://romaanthony.github.io/pc-build-planner/planner.html
```

✅ **New prices are live!**

---

## Automatic (The Easy Way — Future)

Once you're comfortable, I can help you:
- **Sync CSV to Python automatically** (no manual copy-paste)
- **Auto-generate the HTML** when you push
- **Alert you when prices change**

For now, manual works fine. Just 2 files to edit.

---

## Checklist

- [ ] Edit CSV
- [ ] Edit Python file (same change)
- [ ] `git add` both files
- [ ] `git commit -m "..."`
- [ ] `git push origin main`
- [ ] Wait 30 seconds
- [ ] Reload browser → see new prices

Done!
