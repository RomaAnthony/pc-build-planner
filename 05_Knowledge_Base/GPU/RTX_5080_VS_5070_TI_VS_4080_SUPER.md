# RTX 5080 vs 5070 Ti vs 4080 Super — Direct Comparison

For: Ryzen 9 9900X · 1440p 165Hz

---

## Bottom Line

**RTX 5080 > RTX 4080 Super > RTX 5070 Ti.** The 5080 is ~30% faster than the 4080 Super in ray tracing and ~25% in raster at roughly the same launch price (adjusted for inflation). The 5070 Ti's 12 GB VRAM would have been a hard limit for this build; the 16 GB version (late 2025) fixes VRAM but is still 25-30% slower than 5080 for ~15% less money.

---

## Performance Comparison

| Metric | RTX 5080 16GB | RTX 5070 Ti 16GB | RTX 4080 Super 16GB | Unit |
|---|---|---|---:|---:|
| **1440p raster** (avg 10 games) | ~150 | ~115 | ~120 | FPS |
| **1440p RT** (avg 10 games) | ~95 | ~68 | ~72 | FPS |
| **4K raster** (avg) | ~85 | ~65 | ~68 | FPS |
| **Cyberpunk 2077 Path Tracing 1440p** | ~55 (with FG: ~110) | ~38 (with FG: ~75) | ~40 (with FG: ~78) | FPS |
| **Power draw** | ~360W | ~300W | ~320W | TDP |
| **Price in HU (MSRP+)** | ~499k HUF | ~430k HUF | ~450k HUF | HUF |
| **Price in PL** | ~4,899 PLN | ~4,000 PLN | ~4,200 PLN | PLN |
| **CUDA cores** | 10,752 | 8,960 | 10,240 | count |
| **Memory bandwidth** | ~960 GB/s | ~896 GB/s | ~736 GB/s | GDDR7 vs GDDR6X |
| **Frame Gen** | Multi (3x/4x) | Single | Single | |

---

## DLSS / Upgrading Path

- **RTX 5080**: DLSS 4 transformer model as default, multi-frame generation (3x/4x). This means Cyberpunk at 1440p path-traced can hit 130+ FPS with frame gen, vs 75-80 FPS on 5070 Ti.
- **RTX 5070 Ti**: DLSS 4 but single-frame gen only (same as 4000 series).
- **RTX 4080 Super**: DLSS 3.5, no multi-frame gen.

---

## VRAM Analysis

**All three have 16 GB VRAM now** (5070 Ti was released with 12 GB but late 2025+ units are 16 GB). For this build:

| Workload | VRAM Usage | Safe? |
|---|---|---|
| 1440p gaming (2025-2026 titles) | 8-14 GB | Yes, all 3 |
| 1440p path tracing | 10-14 GB | Yes, all 3 |
| 4K gaming | 12-16 GB | 5080/4080S borderline comfortable, 5070 Ti scrapes by |
| Local LLM 7B (6-bit) | ~8 GB | All fine |
| Local LLM 13B (4-bit) | ~10 GB | All fine |
| Stable Diffusion XL | ~8-12 GB | All fine |
| Local LLM 30B (4-bit) | ~20 GB | None — need >16 GB or offload to CPU |

16 GB is acceptable for 2026 but not future-proof. If NVIDIA had offered a 20 GB 5080, it would be worth the premium. But since they didn't, 16 GB is what we have.

---

## Price/Value Calculation (at Poland prices)

| GPU | Performance Index | Price (PLN) | Cost per Frame | Value Rank |
|---|---|---|---:|---:|---:|
| RTX 5080 | 100 | 4,899 | 49 | 🥇 Best at top end |
| RTX 5070 Ti | 75 | 4,000 | 53 | 🥈 Worse value |
| RTX 4080 Super | 78 | 4,200 | 54 | 🥉 Worst value |

The 5080 is paradoxically the best value because it offers more performance per frame than the step-down cards. This is unusual — usually the flagship has worse value. The 5070 Ti/4080 Super prices haven't adjusted enough since the 5080 launched.

---

## Recommendation

**Buy RTX 5080 or don't buy a GPU yet.** There's no compelling reason to spend 80% of a 5080's price on a 5070 Ti that performs 25% worse. Wait for a GPU deal or price drop, then get the 5080.
