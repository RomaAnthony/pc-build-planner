# RAM Research Prompts — AI-Ready

Paste these into ChatGPT / Claude / Gemini one at a time. Each prompt includes full context so the AI knows exactly what to deliver. **No price analysis needed** — prices are already captured in the market snapshots.

---

## PROMPT 1: DDR5 RAM Manufacturer and Model Binning

===BEGIN PROMPT===
I need a complete breakdown of every DDR5 manufacturer's model tiers for 64GB (2x32GB) DDR5-6000 CL30 kits. I need to understand who makes what, which ICs they use, and which model gives best value.

## CONTEXT
- **Target spec**: DDR5-6000 CL30 64GB (2x32GB) — EXPO preferred for AM5
- **CPU**: Ryzen 9 9900X (AM5)
- **Motherboard**: MSI MAG B850 Tomahawk MAX WiFi
- **Use cases**: 1440p gaming, Python data analysis, VM work, heavy coding, multitasking
- **Markets**: Hungary, Poland, Ukraine
- **NO price analysis needed** — I have market prices. I need SPECS and QUALITY comparison.

## WHAT I NEED (structured output)

### Section 1: Manufacturer Tier Matrix
For each major DDR5 manufacturer (Patriot, Kingston, G.Skill, Corsair, GOODRAM, TeamGroup, ADATA/XPG, Silicon Power):

**Products table with:**
| Manufacturer | Value Tier Name | Mid Tier Name | Premium Tier Name | Typical IC Used (Hynix A/M, Samsung, Micron) | Heatspreader Type (metal vs plastic) | Height (mm) | RGB Option? | EXPO Support? |
|---|---|---|---|---|---|---|---|---|

Specifically for 64GB (2x32GB) DDR5-6000 CL30 kits:
- **Patriot**: Viper Venom (value), Viper Elite 5 (mid), Viper Xtreme 5 (premium)
- **Kingston**: Fury Beast (value), Fury Renegade (premium)
- **G.Skill**: Flare X5 (value), Trident Z5 Neo (mid), Trident Z5 Royal (premium)
- **Corsair**: Vengeance (value), Dominator Titanium (premium)
- **GOODRAM**: IRDM (value)
- **ADATA/XPG**: Lancer (value), Lancer Blade (mid)
- **TeamGroup**: Vulcan (value), T-Force Delta (mid), T-Force Xtreem (premium)

### Section 2: IC (Die) Deep Dive
Which IC does each kit actually use at 6000 CL30 64GB?
- Hynix A-die vs M-die vs Samsung vs Micron — which is in which kit
- For kits that change IC over time (revision-based), how to identify by version number on the stick
- Which IC gives best sub-timing headroom (tRFC, tFAW, tWR)?
- Any known IC issues (Samsung unstable at 6000 CL30? Micron bad sub-timings?)
- Is there a meaningful difference between Hynix A-die and M-die at 6000 CL30? (speed ceiling, latency, voltage tolerance)

### Section 3: Physical Build Quality
- Heatspreader: which are real metal vs painted aluminum vs plastic with metal cap?
- PCB color options (for white/black build aesthetics)
- Which kits have thermal pads between IC and heatspreader (vs just thermal tape)?
- Height comparison: Patriot Viper Venom (~33mm) vs Kingston Fury Beast (~35mm) vs G.Skill Trident Z5 (~44mm) vs Corsair Vengeance RGB (~51mm) — are there clearance issues with AIO pump blocks?

### Section 4: What Changes Between Tiers (Same Manufacturer)
For each manufacturer: what physically changes from value to premium tier?
- Example: Patriot Viper Venom vs Viper Xtreme 5 — different PCB? Different IC binning? Just heatsink?
- Example: Kingston Fury Beast vs Fury Renegade — same PCB or different?
- Example: G.Skill Flare X5 vs Trident Z5 Neo vs Royal — same ICs, just different heatsink?
- Is the premium tier actually worth it for same speed/timing spec, or is it purely cosmetic?

### Section 5: Bottom Line
- Top 3 recommendations for this build (ranked by spec quality + reliability)
- Which kits are the same thing rebranded? (Tell me if I'm paying for branding vs actual better hardware)
- Which manufacturers to avoid and why
- For the Patriot Viper Venom at 64GB CL30: is this actually good, or cutting corners?

## ANTI-PATTERNS
- Do NOT say "it depends" without clear guidance
- Do NOT give USA-centric information
- Do NOT include prices — I have those
- Do NOT recommend without explaining WHY the product is good
===END PROMPT===

---

## PROMPT 2: DDR5 Specifications Deep Dive — What Actually Matters

===BEGIN PROMPT===
I need a deep technical explanation of what matters in DDR5 RAM specifications, specifically for an AM5 Ryzen 9 9900X build. Not general "more frequency better" — I need the actual engineering trade-offs.

## CONTEXT
- CPU: Ryzen 9 9900X (Zen 5, AM5, dual-channel memory controller on I/O die)
- Target: 64GB (2x32GB) DDR5
- Use: gaming + data analysis + productivity

## WHAT I NEED (detailed)

### 1. AM5 Memory Controller Deep Dive
- How the I/O die's memory controller works (UCLK, MCLK, FCLK relationship)
- Why DDR5-6000 in 1:1 mode (UCLK=MCLK) is the sweet spot — explain the Infinity Fabric ratio
- What happens at DDR5-6200/6400 — does 1:1 still work on Ryzen 9000? (success rate %)
- What happens at DDR5-6800+ (forced 2:1 mode) — what latency penalty in nanoseconds?
- How does this compare to Intel's approach (gear 1/gear 2)?

### 2. Timing Breakdown — What Each Number Actually Means
| Timing | Full Name | What It Controls (in English) | Good Value at DDR5-6000 | OK Value | Poor | Real Performance Impact |
|---|---|---|---|---|---|---|
| CL | CAS Latency | ... | 30 | 32-34 | 36+ | ... |
| tRCD | Row to Column Delay | ... | 36-38 | 38-40 | 40+ | ... |
| tRP | Row Precharge Time | ... | 36-38 | 38-40 | 40+ | ... |
| tRAS | Row Active Time | ... | 84-96 | 96 | 96+ | ... |

Explain each in plain English — what physically happens in the memory chip during each step.

### 3. Sub-Timings That Matter for Real Performance
| Sub-Timing | What It Does | Typical Stock at 6000 CL30 | Can Be Tuned To (Hynix) | Est. Performance Gain |
|---|---|---|---|---|
| tRFC | Refresh cycle time | 500-630 | 350-400 | ... |
| tFAW | Four activate window | 32-40 | 24-28 | ... |
| tWR | Write recovery | 48-64 | 40-48 | ... |

Is the sub-timing headroom difference between Hynix A-die and M-die meaningful at 6000 CL30?

### 4. Rank Configuration Explained
- What does dual-rank vs single-rank mean physically? (two banks of chips on one stick)
- 2x32GB sticks = typically dual-rank = 2 ranks per channel
- 2x16GB sticks = typically single-rank = 1 rank per channel
- 4x16GB = 2 ranks per channel BUT electrical penalty
- Rank interleaving: explain what happens when the controller switches between ranks during refresh
- Performance benefit: measured ~3-5% in bandwidth, does it help latency too?

### 5. EXPO vs XMP vs Manual
- What EXPO sets beyond just frequency (sub-timings, voltages)
- Can XMP kits work on AM5? Any issues with stability?
- Manual tuning: how much can you gain over EXPO on Hynix-based 6000 CL30 kits? (e.g. tRFC reduction)
- Is manual tuning worth it for a daily use machine?

### 6. Voltage Limits (Crucial for AM5 Safety)
- VSOC max safe for daily use on AM5 — what's the hard limit?
- VDD (DRAM voltage) safe daily range for 6000 CL30
- What happens above safe limits? (degradation over time vs immediate crash?)
- Does the MSI B850 Tomahawk handle voltages conservatively or aggressively at default?

### 7. Bottom Line
- One paragraph: what RAM spec to buy and why nothing else makes sense for this build
- Is there any scenario where DDR5-6400 CL32 beats 6000 CL30 for this build? (exact trade-off)
- Is CL30 worth paying for over CL32? Where is the line?

## ANTI-PATTERNS
- Do NOT skip the WHY — "6000 CL30 is the sweet spot" needs explanation
- Do NOT overhype 1-2% gains as worth paying 20% more
- Do NOT recommend unsafe tuning
- Do NOT use synthetic benchmarks as the only evidence — connect to real workloads
===END PROMPT===

---

## PROMPT 3: AM5 RAM Compatibility & Known Issues

===BEGIN PROMPT===
I need a compatibility analysis of DDR5 RAM specifically for MSI MAG B850 Tomahawk MAX WiFi with Ryzen 9 9900X.

## CONTEXT
- Motherboard: MSI MAG B850 Tomahawk MAX WiFi (AGESA 1.2.x+)
- CPU: Ryzen 9 9900X (Zen 5)
- Cooler: Arctic Liquid Freezer III Pro 360 A-RGB
- Case: Lian Li Lancool 207
- Target RAM: 64GB (2x32GB) DDR5-6000 CL30

## WHAT I NEED

### 1. QVL Reality
- Is the MSI QVL exhaustive or just a small tested subset?
- Which specific 64GB (2x32) DDR5-6000 CL30 kits ARE on the QVL?
- Which known-good kits are NOT on QVL but work fine?

### 2. Known AM5 RAM Issues — Status Check (2025/2026)
For each historical issue:
- Long boot times (30+s with MCR disabled) — RESOLVED or still present?
- EXPO instability at 6000 — RESOLVED or still motherboard-specific?
- VSOC overvoltage damaging CPUs — FIXED in BIOS or still a risk?
- 4-DIMM 6000 impossible — still a limitation or improved?

### 3. Specific Kit Compatibility
| Kit | QVL Listed? | Reported Issues | Known Working BIOS | Notes |
|---|---|---|---|---|
| Patriot Viper Venom 64GB CL30 PVV564G600C30K | | | | |
| Kingston Fury Beast EXPO 64GB CL30 | | | | |
| GOODRAM IRDM 64GB CL30 | | | | |
| G.Skill Trident Z5 Neo 64GB CL30 | | | | |
| Corsair Vengeance 64GB CL30 | | | | |

### 4. Cooler Clearance Check
Will Arctic Liquid Freezer III Pro pump block clear each kit?
- Height of each kit (Patriot ~33mm, Kingston ~35mm, G.Skill ~44mm, Corsair RGB ~51mm)
- Does the Arctic pump overhang the RAM slots? (it uses an offset mount on AM5)
- Any known conflict with tall RGB RAM?

### 5. BIOS Settings for Optimal Stability
- Memory Context Restore: ON for fast boot? Any stability risk?
- Power Down Enable: ON for power saving? Does it cause instability at 6000 CL30?
- EXPO I vs EXPO II vs Memory Try It — which to use on MSI board?
- Any specific MSI B850 Tomahawk BIOS tricks for 64GB 6000?

### 6. Bottom Line
- Safest 64GB kit for this exact motherboard (zero headache guarantee)
- Best value kit that's also known-good
- Any kits to absolutely avoid on this board
===END PROMPT===

---

## PROMPT 4: Dual-Rank vs Single-Rank — Real-World Performance

===BEGIN PROMPT===
I need to understand the real-world performance difference between dual-rank and single-rank DDR5, specifically for a Ryzen 9 9900X build with 64GB total.

## CONTEXT
- CPU: Ryzen 9 9900X (Zen 5, dual-channel)
- Configurations being compared:
  - Option A: 2x32GB (dual-rank sticks) = 64GB, 2 ranks per channel
  - Option B: 2x16GB (single-rank sticks) = 32GB, 1 rank per channel
  - Option C: 4x16GB (single-rank sticks) = 64GB, 2 ranks per channel BUT 4-DIMM
- All at DDR5-6000 CL30

## WHAT I NEED

### 1. Bandwidth Comparison
- Real measured bandwidth in AIDA64 for each config (if known)
- Memory-sensitive benchmarks: 7-Zip compression, Y-Cruncher, Handbrake
- FPS difference in games — which games show a measurable benefit from rank interleave?

### 2. Latency Comparison
- Real measured latency in AIDA64 for each config
- Gaming responsiveness: does lower latency give smoother frame times or just lower numbers?

### 3. 4-DIMM vs 2-DIMM Stability
- Can 4x16GB actually run DDR5-6000 stable on AM5? (real reported success rate)
- What's the highest stable speed with 4 DIMMs on B850 Tomahawk?
- Does daisy-chain topology penalize 4-DIMM specifically on this board?

### 4. Real-World Scenarios
- Gaming: Cyberpunk, Starfield, Baldur's Gate 3 — FPS difference
- Data analysis: Python Pandas on large dataframes — time difference
- Compilation: large C++ project — time difference
- Is any of this noticeable outside of synthetic benchmarks?

### 5. Power and Heat
- Temperature difference: dual-rank sticks run hotter — how much (°C)?
- Power difference: idle and under load

### 6. Bottom Line
- Clear recommendation: 2x32GB vs 2x16GB vs 4x16GB for this build
- At what specific workload does dual-rank matter?
- Is 64GB (2x32GB) better for performance than 32GB (2x16GB) even at same speed? (rank interleave bonus)
===END PROMPT===
