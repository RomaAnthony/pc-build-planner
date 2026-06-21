# SSD Decision Guide — Ryzen 9 9900X Build

For: Ryzen 9 9900X · MSI MAG B850 Tomahawk MAX WiFi (1x PCIe 5.0 M.2 + 3x PCIe 4.0 M.2)

---

## Bottom Line

**Target: Kingston KC3000 2TB (PCIe 4.0).** This is the best value SSD for this build — Intel 3D TLC NAND, DRAM-cached, sustained write speed ~6,000 MB/s, very reliable. PCIe 5.0 SSDs cost 2-3x more for 0-5% real-world gaming/loading improvement.

The B850 Tomahawk's PCIe 5.0 M.2 slot is future-proof for a PCIe 5.0 SSD upgrade in 2-3 years when prices drop. Today: KC3000 at PCIe 4.0 speeds is more than enough.

---

## PCIe 4.0 vs PCIe 5.0 — Real World Differences

| Metric | PCIe 4.0 | PCIe 5.0 | Real Impact |
|---|---|---|---|
| Sequential read | 7,000 MB/s | 10,000-14,500 MB/s | None for gaming/loading |
| Sequential write | 6,000 MB/s | 9,000-12,000 MB/s | Only large file transfers |
| Random 4K read | ~90 MB/s | ~100 MB/s | +5-10% (small visible diff) |
| Game load time (Cyberpunk) | 8.2s | 7.8s | 0.4s diff |
| Game load time (Starfield) | 6.5s | 6.1s | 0.4s diff |
| Windows boot | 12s | 11s | 1s diff |
| DirectStorage (future) | Good | Better | Potentially wider gap in future |
| Price 2TB | ~35-45k HUF | ~80-120k HUF | 2-3x more |
| Power draw | ~6W | ~10-12W | Higher, needs heatsink always |
| Thermal throttling | Rare | Common | PCIe 5.0 needs active cooling often |

**Conclusion**: PCIe 4.0 is the sweet spot. PCIe 5.0 gains are synthetic benchmarks, not real-world experience. Spend the extra money on RAM or GPU.

---

## DRAM vs DRAM-less — What Matters

| Feature | DRAM Cached | DRAM-less (HMB) |
|---|---|---|
| Random IO | Better at sustained writes | Acceptable for daily use |
| Write stability after SLC cache fills | Consistent ~1,000-2,000 MB/s | Drops to NAND raw speed (~100-500 MB/s) |
| OS drive performance | Better | Good enough |
| Price | Higher | Lower |
| Examples | KC3000, 990 PRO, SN850X | Lexar NM790, WD SN580 |

**For this build**: DRAM-cached (KC3000) is the right call. It's the OS drive and will see sustained writes (large file transfers, VM images, data analysis datasets). DRAM-less drives are fine as secondary storage later.

---

## TLC vs QLC

| NAND Type | Cells per Bit | Endurance | Speed | When Used |
|---|---|---|---|---|
| TLC | 3 | High | Fast | Mainstream SSDs, KC3000, SN850X |
| QLC | 4 | Lower | Slower after SLC cache | Budget SSDs (avoid for main drive) |

**Avoid QLC for the OS/main drive.** QLC falls to ~100 MB/s write speed after the SLC cache fills. Fine for bulk storage, bad for primary drive.

---

## Kingston KC3000 2TB — Why It's The Pick

| Spec | Value |
|---|---|
| NAND | Intel 3D TLC (176L) |
| DRAM | 2 GB DDR4 |
| Controller | Phison E18 |
| Seq Read | 7,000 MB/s |
| Seq Write | 7,000 MB/s |
| Endurance (TBW) | 1,600 TBW (2TB) — very high |
| Warranty | 5 years |
| DRAM Cache | Yes |
| HMB | Not needed |

The KC3000 competes with Samsung 990 PRO and WD SN850X at a lower price. Real-world performance is nearly identical. In Poland at ~78k HUF (939 PLN), it's significantly cheaper than the 990 PRO at ~122k HUF.

---

## Samsung 990 PRO 2TB — When Would It Be Worth?

- Only if the price gap is under 10% (it's currently 55% more)
- Samsung has slightly better random 4K (~95 vs ~90 MB/s)
- Samsung Magician software for firmware updates is better
- Better power efficiency at idle (~3W vs ~4W)

**Verdict**: Not worth the current premium. KC3000 is 95% of the performance at 65% of the price.

---

## FURY Renegade G5 (PCIe 5.0) — Why Skip

- 2TB: ~1,475 PLN / ~122k HUF in Poland
- PCIe 5.0: 10,000+ MB/s sequential
- Real gaming benefit: near zero
- Thermals: needs good airflow or active cooling
- Price premium: 57% over KC3000

**Skip.** Not worth the money for this build.

---

## Future Expansion

The B850 Tomahawk has 4 M.2 slots:
1. **PCIe 5.0 x4** (from CPU) — ideal for KC3000 now, PCIe 5.0 later
2. **PCIe 4.0 x4** (chipset) — for secondary storage later
3. **PCIe 4.0 x2** (chipset) — slower, fine for bulk storage
4. **PCIe 4.0 x4** (chipset) — secondary storage

When you need more storage later, slots 2-4 accept M.2 PCIe 4.0 drives. A Lexar NM790 or similar DRAM-less drive at 4,000-5,000 MB/s is fine for bulk.
