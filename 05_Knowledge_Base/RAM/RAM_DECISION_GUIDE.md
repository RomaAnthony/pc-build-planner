# RAM Decision Guide — Ryzen 9 9900X Build

For: MSI MAG B850 Tomahawk MAX WiFi · AM5 · Ryzen 9 9900X

---

## Bottom Line

**Target: DDR5-6000 CL30 64GB (2x32GB) — EXPO certified for AMD.**

This is the AM5 sweet spot. The Ryzen 9 9900X's memory controller (IOD) is most stable at DDR5-6000 with a 1:1 UCLK:MCLK ratio. CL30 gives genuine latency benefit over CL36/CL40 for 64GB kits. 64GB (2x32GB dual-rank) is the right call for data analysis, heavy multitasking, and future-proofing without sacrificing speed.

If budget forces a reduction: drop to 32GB (2x16GB) before you drop to slower timings.

---

## Why DDR5-6000 CL30?

On AM5, the memory controller (IOD on the CPU die) has a preferred operating range. Three things matter:

### 1. Fabric Clock Ratio (1:1 vs 2:1)

AM5 runs best with UCLK = MCLK (memory controller clock = memory clock ratio 1:1). This mode works reliably up to about DDR5-6000 (3000 MHz actual clock). Beyond that, the controller switches to 2:1 mode (UCLK = MCLK/2), which adds latency penalty that often outweighs the raw speed gain.

- **DDR5-6000**: 1:1 mode works on almost all Ryzen 9000 chips
- **DDR5-6200/6400**: 1:1 is possible on good chips but not guaranteed
- **DDR5-6800+**: forced 2:1 mode, latency actually increases

Result: DDR5-6000 is the safe maximum for 1:1 operation on AM5.

### 2. What CL Numbers Actually Mean

CAS latency in nanoseconds = (CL × 2000) / speed

| Kit | Formula | Nanoseconds |
|---|---:|---:|
| 6000 CL30 | (30 × 2000) / 6000 | 10.0 ns |
| 6000 CL32 | (32 × 2000) / 6000 | 10.67 ns |
| 6000 CL34 | (34 × 2000) / 6000 | 11.33 ns |
| 6000 CL36 | (36 × 2000) / 6000 | 12.0 ns |
| 6000 CL40 | (40 × 2000) / 6000 | 13.33 ns |

Real-world impact at 1440p gaming: CL30 to CL36 is roughly 1-3% FPS difference. CL30 to CL40 is about 3-5%. Not massive, but CL30 kits cost minimally more than CL36 — so there's no reason to settle for worse timings.

**The real value of CL30 is in tighter sub-timings.** Kits binned as CL30 tend to have better ICs (Hynix A/M-die) that can run tighter tRFC, tFAW, and tWR, which improves system responsiveness beyond just the CAS number.

### 3. Sub-Timings Matter More Than CAS

Most DDR5-6000 CL30 kits can reduce tRFC (Refresh Cycle) from 630 to 350-400, and tFAW from 40 to 24-28. These adjustments improve latency by 10-15% more than the CAS number alone suggests. A CL30 kit with good ICs is a better starting point for this.

---

## 2x32GB (Dual-Rank) vs 4x16GB (Single-Rank)

For 64GB total:

| Config | Pros | Cons |
|---|---|---|
| **2x32GB dual-rank** | Easier on memory controller, 2-DIMM topology is faster, up to 6000+ stable, rank interleaving gives ~5% speed bonus | Slightly less common, slightly more expensive per GB |
| 4x16GB single-rank | Uses common 16GB sticks | 4-DIMM populate drops max stable speed by ~200-400 MHz, harder on IMC, no rank interleave benefit |

**Recommendation: 2x32GB.** The B850 Tomahawk has daisy-chain topology optimized for 2 DIMMs. Populating all 4 slots will likely cap you at DDR5-5600 or DDR5-5200 stable. 2x32GB dual-rank actually outperforms 4x16GB because of rank interleaving — the system treats each dual-rank stick as "2 ranks" just like having 2 single-rank sticks per channel, giving the same parallelism without the electrical penalty.

---

## Dual-Rank Performance Bonus

Dual-rank memory (2x32GB) gives about 3-5% more bandwidth than single-rank at the same speed because of rank interleaving — the memory controller can switch between ranks while one is on refresh. This is a free performance lift. You don't get this with 2x16GB single-rank or 4x16GB (which is 2 ranks per channel but at the cost of signal integrity).

**Practical takeaway**: 2x32GB CL30 is both "more RAM" AND "faster RAM" vs 2x16GB CL30 — not just more capacity.

---

## EXPO vs XMP

AMD EXPO (Extended Profiles for Overclocking) is native to AM5. Intel XMP works too on most boards, but EXPO gives better-tuned sub-timings for Ryzen.

- **Prefer EXPO kits** — they're tuned for AMD
- **XMP kits work** — the B850 Tomahawk reads XMP profiles fine
- **Manual tuning** — you can always set speed/timing manually without either

Most Patriot, G.Skill, and Kingston DDR5 kits list both EXPO and XMP support on their spec sheets.

---

## Key Brands Evaluated

Based on parts_options_seed.csv + market data + DDR5 reliability research:

| Brand | DDR5 Verdict | IC Used | Notes |
|---|---|---|---|
| **Patriot** | ✅ Good value | Hynix M-die (most kits) | Viper Venom is clean, no RGB bloat, good EU RMA through distributors |
| **Kingston** | ✅ Safe choice | Hynix A/M-die rotating | Fury Beast = solid, better RMA in HU/PL/UA, slightly more expensive |
| **GOODRAM** | ✅ EU reliable | Hynix OEM | Polish brand, easy warranty in PL, good IC quality |
| **G.Skill** | ⚠️ Premium price | Hynix A-die | Trident Z5 is great but 20-40% more for same specs |
| **Corsair** | ⚠️ Overpriced | Samsung/Micron rotating | Vengeance is 30-50% more than Patriot for same spec, weaker sub-timings |
| **Silicon Power** | ⚠️ Suspicious | Mixed/unknown | XPower Zenith at 225k HUF in HU is suspiciously cheap — verify authenticity |

---

## Recommended Finalists (from market data)

### 64GB Route
1. **Patriot Viper Venom 64GB 2x32 DDR5-6000 CL30 (PVV564G600C30K)** — Best value, ~39k UAH from Poland
2. **Kingston Fury Beast EXPO 64GB 2x32 DDR5-6000 CL30** — Safest brand, ~42k UAH from Poland
3. **GOODRAM IRDM 64GB 2x32 DDR5-6000 CL30** — Solid backup, ~41k UAH from Poland

### 32GB Route (budget-down)
1. **Patriot Viper Venom 32GB 2x16 DDR5-6000 CL30** — ~20k UAH from Poland/Ukraine
2. **Lexar Ares 32GB 2x16 DDR5-6000 CL30** — ~20.5k UAH from Poland

---

## What to Avoid

- **4x16GB kits** — will struggle to reach 6000 CL30 on AM5, potential stability headache
- **DDR5-6400+ without proof it works in 1:1** — silicon lottery
- **CL36+ at similar price to CL30** — free performance left on the table
- **No-name brands** (LogicPower, no-name OEM) — can use wrong ICs, no EXPO, no support
- **RGB versions unless you want the look** — 5-10% price premium, no performance gain, software bloat

---

## Decision Checklist

When you find a candidate kit, verify:

1. [ ] DDR5-6000 (not 5600, not 6400+)
2. [ ] CL30 (CL32 acceptable, CL34+ skip)
3. [ ] 2x32GB for 64GB target, 2x16GB for 32GB
4. [ ] EXPO certified (ideally)
5. [ ] Brand: Patriot / Kingston / GOODRAM / G.Skill (avoid no-name)
6. [ ] Price competitive with current market snapshot
7. [ ] Seller has real warranty (not marketplace rando)
