# PCIe 4.0 vs PCIe 5.0 SSD — Real-World Performance

For: Ryzen 9 9900X · MSI B850 Tomahawk (PCIe 5.0 M.2 slot available)

---

## Bottom Line

**PCIe 4.0 is sufficient for 2026.** PCIe 5.0 SSDs cost 2-3x more with 0-5% real-world gaming improvement. The main PCIe 5.0 use case is: 8K video editing, large dataset transfers, or professional content creation with massive files.

For this build (data analysis, coding, 1440p gaming): KC3000 PCIe 4.0 is correct. The slot is future-proof for when PCIe 5.0 prices drop.

---

## Benchmark Comparison

| Benchmark | KC3000 PCIe 4.0 | FURY Renegade G5 PCIe 5.0 | Delta |
|---|---|---|---|
| Sequential read | 7,000 MB/s | 14,500 MB/s | +107% |
| Sequential write | 7,000 MB/s | 12,000 MB/s | +71% |
| Random 4K Q1T1 read | 85 MB/s | 95 MB/s | +12% |
| Random 4K Q1T1 write | 300 MB/s | 350 MB/s | +17% |
| PCMark 10 Storage Score | 3,800 | 4,100 | +8% |
| Game load (Cyberpunk) | 8.2s | 7.8s | +5% |
| Game load (Starfield) | 6.5s | 6.1s | +6% |
| Windows boot | 12s | 11s | +8% |
| Price 2TB | ~35,000 HUF | ~122,000 HUF | +248% |

---

## When PCIe 5.0 Actually Matters

- **Large file transfers (>100 GB):** PCIe 5.0 finishes in 10s vs 20s
- **DirectStorage games (future):** Could improve asset streaming if games use it properly
- **Pro video editing:** Multiple streams of 8K RAW
- **VM/container workloads:** Rapidly spinning up large disk images

**None of these are your primary use case.**

---

## DirectStorage — The Wild Card

DirectStorage (Microsoft's API for GPU-driven asset streaming) could make PCIe 5.0 SSDs more beneficial in future games. But:
- Only a handful of games support it as of 2026
- Most games still load through CPU/system RAM
- Even with DirectStorage, the difference between PCIe 4.0 and 5.0 is small (GPU decompression speed matters more)

**Verdict**: Not worth paying 2-3x for. By the time DirectStorage is widespread, PCIe 5.0 SSDs will be cheaper.

---

## Thermal Considerations

| Metric | PCIe 4.0 | PCIe 5.0 |
|---|---|---|
| Peak power draw | ~6-8W | ~10-14W |
| Idle temp (case airflow) | 35-40°C | 40-50°C |
| Load temp (passive heatsink) | 50-60°C | 65-85°C |
| Throttling temp | 80°C | 85°C |
| Heatsink needed? | Motherboard heatsink is fine | Motherboard heatsink + good airflow, or active fan |

PCIe 5.0 SSDs run hot. In a 360 AIO front-mounted case, the VRM/M.2 area gets less airflow. A PCIe 4.0 SSD is safer thermally.

---

## Price Trajectory

| Year | PCIe 4.0 2TB | PCIe 5.0 2TB |
|---|---|---|
| 2024 | ~25-35k HUF | ~60-80k HUF |
| 2025 | ~30-40k HUF | ~80-120k HUF |
| 2026 | ~35-45k HUF | ~80-150k HUF |

PCIe 5.0 prices are dropping slowly because real-world demand is low. Most users don't need the speed, so manufacturers price for the workstation market.

---

## Recommendation

**Buy KC3000 PCIe 4.0 now. Use the PCIe 5.0 slot for a future upgrade.** In 2-3 years, a 4TB PCIe 5.0 SSD might cost what KC3000 costs today. The slot is there for exactly that reason.
