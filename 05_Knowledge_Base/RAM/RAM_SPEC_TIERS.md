# RAM Spec Tiers — What the Numbers Mean

For: Ryzen 9 9900X · AM5 · DDR5

---

## Bottom Line

**DDR5-6000 CL30 1.35V EXPO is the performance target. The real differentiator between kits is not the primary timings — it's the IC (Hynix A-die vs M-die vs Samsung) and the sub-timing headroom.**

At the same DDR5-6000 CL30 spec, two kits can perform 5-10% differently because of sub-timings (tRFC, tFAW, tWR) and which IC they use. This guide explains what matters beyond the big numbers on the box.

---

## Speed Tier Guide (for AM5)

| Speed | 1:1 Mode | Latency (CL30) | Verdict |
|---|---:|---:|---:|
| DDR5-4800 | Always stable | 12.5 ns | JEDEC boot default, too slow |
| DDR5-5200 | Always stable | 11.5 ns | Entry level, avoid |
| DDR5-5600 | Almost always stable | 10.7 ns | Acceptable fallback |
| **DDR5-6000** | **Safe target** | **10.0 ns** | **SWEET SPOT** |
| DDR5-6200 | ~60% of chips | 9.7 ns | Silicon lottery |
| DDR5-6400 | ~30% of chips | 9.4 ns | Not worth gamble |
| DDR5-6800+ | Mandatory 2:1 | ~8.8 ns but 2:1 penalty | Higher bandwidth, higher latency |

The key number is **UCLK = MCLK = 3000 MHz** at DDR5-6000. Going to 6400 gives 6.7% more bandwidth but forces UCLK=3200 which many chips can't do stable. Losing 1:1 mode adds ~10ns penalty that wipes out the speed gain.

---

## Timing Components (Primary)

DDR5 primary timings: **CL-tRCD-tRP-tRAS** (commonly shown as CL30-38-38-96 or similar)

| Timing | What It Controls | Good Value | OK Value | Poor |
|---|---|---|---|---|
| **CL** (CAS Latency) | Cycles before data from a column | 30 | 32-34 | 36+ |
| **tRCD** (Row to Column Delay) | Cycles to open a row and read | 36-38 | 38-40 | 40+ |
| **tRP** (Row Precharge) | Cycles to close a row | 36-38 | 38-40 | 40+ |
| **tRAS** (Row Active Time) | Min cycles a row stays open | 84-96 | 96 | 96+ |

*Numbers given are at DDR5-6000. Convert for other speeds proportionally.*

**Primary timings are NOT the whole story.** Two kits with identical CL30-38-38-96 can have wildly different sub-timings.

---

## Sub-Timings (Critical for Real Performance)

| Timing | What It Controls | Good Stock | Tuned Target | Impact |
|---|---|---|---|---|
| **tRFC** (Refresh Cycle) | Time between refresh cycles | 500-630 | 350-400 | 🟢 Big latency impact |
| **tFAW** (Four Activate Window) | How fast rows can activate | 32-40 | 24-28 | 🟢 Medium bandwidth impact |
| **tWR** (Write Recovery) | Time between write and precharge | 48-64 | 40-48 | 🟡 Small-medium |
| **tCWL** (CAS Write Latency) | Write equivalent of CL | auto = CL | CL-2 to CL | 🟡 Small |
| **tRDRD** (Read-to-Read) | Same bank group delay | 8-10 | 6-8 | 🟢 Medium |

**Why this matters**: Most DDR5-6000 CL30 kits come with tRFC around 500-630. Dropping tRFC to 350 can reduce latency by 3-5ns — equivalent to going from CL30 to CL22. Hynix A-die handles low tRFC best.

---

## IC (Integrated Circuit / Die) Hierarchy

This is the single most important spec that isn't on the box.

| IC | Density | Speed Ceiling | Sub-timing Headroom | Used In |
|---|---|---|---|---|
| **Hynix A-die** 🥇 | 16Gb | 8000+ MT/s | Best | Early high-bin kits, G.Skill Trident Z5 |
| **Hynix M-die** 🥈 | 24Gb (newer) | 7200+ MT/s | Very Good | Most 2024+ 64GB kits, Patriot Viper Venom, Kingston Fury |
| **Hynix A-die 24Gb** 🥇 | 24Gb | 8000+ | Excellent | Latest 2x24GB/2x48GB premium kits |
| **Samsung** 🥉 | 16Gb | 6800 MT/s | Moderate | Corsair Vengeance, some Kingston OEM |
| **Micron** 🥉 | 16Gb | 6400 MT/s | Limited | Budget kits, OEM, Crucial |

### For 64GB (2x32GB) at DDR5-6000 CL30

You will almost certainly get **Hynix M-die** (24Gb density) or possibly Hynix A-die depending on the revision. This is fine — both easily handle 6000 CL30 and have plenty of headroom for sub-timing tightening.

**How to identify**: Look at the version number on the physical stick label:
- Hynix: usually `H5` or `HMC` prefix
- Samsung: `SEC` or `S5` prefix  
- Micron: `MT` prefix

On Patriot Viper Venom specifically: version `V4.51` = Hynix, version `V4.47` = Hynix.

---

## Voltage Guide

| Voltage | Range | Notes |
|---|---|---|
| **VSOC** (CPU SoC) | **1.20-1.25V safe daily** | MSI B850 Tomahawk Auto is fine. Max 1.30V for daily, 1.35V+ risks degradation on AM5 |
| **VDD** (DRAM) | 1.35V (EXPO), 1.40-1.45V safe daily | 6000 CL30 EXPO typically = 1.35V. 1.40V for tighter timings is fine with airflow |
| **VDDQ** (DRAM termination) | Same as VDD typically | EXPO sets this automatically within margin |
| **VDDIO** (Memory controller I/O) | 1.20-1.30V safe | Set to match VSOC roughly |

**Do not go over 1.30V VSOC on AM5 for daily use.** The safe limit is well-documented after the Ryzen 7000 degradation issues in 2023. MSI B850 Tomahawk BIOS tends to set VSOC conservatively (1.20-1.25V) which is ideal.

---

## Memory Context Restore (MCR) & Power Down

Two BIOS settings that matter for boot time and stability:

- **Memory Context Restore**: ON = faster boot (skips re-training), OFF = more stable (re-trains each boot). For EXPO kits verified to work, keep ON. If unstable, toggle OFF.
- **Power Down Enable**: ON = power saving (idle voltage drop), can cause instability at tight timings. OFF = more stable.

---

## Heat & Temperatures

DDR5 runs hotter than DDR4. DDR5-6000 CL30 at 1.35V:

- Idle: 35-40°C
- Under load: 45-55°C (with case airflow)
- Throttle: 85°C+ (won't happen in normal use)

**Dual-rank (2x32GB) runs 3-5°C hotter** than single-rank (2x16GB) because more ICs per stick.

**RGB adds 1-3°C** from the LED controller on the stick. Not meaningful.

**Heatspreaders matter**: Metal heatspreaders help. Plastic "gamer" shrouds don't. Patriot Viper Venom has metal. Kingston Fury Beast has metal. G.Skill Trident Z5 has metal.

---

## Rank Configuration (Performance Impact)

| Config | Ranks per Channel | Performance vs Single-Rank |
|---|---|---|
| 2x16GB (1 rank per stick) | 1 rank/ch | Baseline |
| 2x32GB (2 ranks per stick) | 2 ranks/ch | +3-5% bandwidth (rank interleave) |
| 4x16GB (1 rank per stick) | 2 ranks/ch | +3-5% bandwidth BUT lower max speed |

Dual-rank advantage comes from rank interleaving: while one rank refreshes, the other answers requests. This is a genuine ~5% performance lift in bandwidth-sensitive workloads (compression, large data sets).

## Final Tier Classification

For this build:

| Tier | Spec | Makes Sense For |
|---|---:|---|
| 🥇 **Target** | DDR5-6000 CL30 2x32GB EXPO | Perfect for 9900X, heavy multitasking, data analysis |
| 🥈 **Acceptable** | DDR5-6000 CL32-CL34 2x32GB EXPO | If CL30 is 20%+ more expensive |
| 🥉 **Budget-down** | DDR5-6000 CL30 2x16GB EXPO | Dropping capacity, not quality |
| ❌ **Skip** | Anything DDR5-5600, CL36+, 4-stick, no-name, Intel XMP only | Will leave performance on table or cause headaches |
