# Share This Link With Your Dad ✅

## The Link
```
https://romaanthony.github.io/pc-build-planner/planner.html
```

**Copy & send this to your dad.** He can:**
- Open it in any browser (Chrome, Safari, Firefox, Edge)
- No installation needed
- No login needed
- Click dropdowns to change parts
- See prices in HUF and UAH instantly
- Works offline too (once loaded)

---

## What He'll See

1. **Choose a build** — dropdown at the top
   - Main 64GB, GPU later
   - Budget 32GB, GPU later  
   - Full build with RTX 5080

2. **Change parts** (optional) — 8 dropdowns for CPU, RAM, SSD, etc.

3. **See totals** — prices in HUF, EUR, and UAH

4. **Compare markets** — Polish vs Hungarian prices

---

## If He Has Questions

**Q: "Will it work on my phone?"**
A: Yes! Works on phone, tablet, desktop.

**Q: "Do I need internet?"**
A: Once it loads, no. It works offline.

**Q: "Can I save or export?"**
A: Not yet—but you can take a screenshot or send him updated links.

**Q: "Why does it say 'offline fallback' for exchange rates?"**
A: The app is using last-known good rates. They're accurate enough for PC shopping.

---

## If Something Breaks

Tell me and I'll fix it immediately. Just say what went wrong:
- "Dropdown doesn't work"
- "Prices look wrong"
- "Page won't load"

---

## How to Update It Later

When you change parts or prices in the CSV:

1. Edit the CSV in `02_PC_Builds/parts_options_seed.csv`
2. Update the embedded copy in `04_Tools/pc_build_marimo_WASM_SAFE.py`
3. Re-export: `marimo export html-wasm 04_Tools/pc_build_marimo_WASM_SAFE.py -o docs/planner.html`
4. Push to GitHub: `git add docs/planner.html && git commit -m "Update: new prices" && git push`
5. Done! The link automatically has new data (might take 30 seconds for cache)

---

## Summary

✅ **File is live**: https://romaanthony.github.io/pc-build-planner/planner.html  
✅ **Shared with dad**: Works anywhere, no setup  
✅ **Static data**: You control it, no API surprises  
✅ **Easy to update**: Edit CSV, re-export, push  

---

**Send him the link. He can use it right now.**
