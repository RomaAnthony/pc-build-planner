# PSU Decision Guide — Ryzen 9 9900X Build

For: Ryzen 9 9900X · RTX 5080 (future) · Lian Li Lancool 207 / Corsair 3500X

---

## Bottom Line

**Target: be quiet! Pure Power 13 M 1000W (BP028EU).** ATX 3.1, 150mm compact, Gold efficiency, native 12V-2x6 cable for RTX 5080, ~48k HUF in Hungary. Fits Lancool 207 with HDD cage installed (max 160mm, this is 150mm).

If you want Corsair: RM1000x ATX 3.1 at 647 PLN in Poland is excellent and cheaper than Hungary. But it's 180mm — needs HDD cage removed in Lancool 207.

---

## 850W vs 1000W — Do You Need 1000W?

| Component | Typical Power Draw |
|---|---|
| Ryzen 9 9900X (gaming) | ~100-130W |
| Ryzen 9 9900X (all-core) | ~170-200W |
| RTX 5080 (gaming) | ~300-360W |
| RTX 5080 (transient spikes) | ~450W+ for 1-100ms |
| System (fans, RAM, SSD) | ~50-80W |
| **Total (gaming)** | **~450-550W** |
| **Total (stress test)** | **~650-700W** |

**1000W is the right choice** because:
- ATX 3.1 standards recommend 200W+ headroom for transient spikes
- RTX 5080 can draw >400W peaks
- PSUs operate most efficiently at 40-70% load (500-700W on a 1000W)
- 850W would be at 80-90% load under stress — no headroom for future upgrades
- Price difference between 850W and 1000W Gold ATX 3.1 is ~10-15k HUF — small

---

## ATX 3.1 vs ATX 3.0 vs Older

| Feature | ATX 3.1 | ATX 3.0 | ATX 2.x |
|---|---|---|---|
| Native 12V-2x6 | ✅ Latest | ✅ (12VHPWR) | ❌ (needs adapter) |
| Transient handling | 200% rated for 100µs | 200% rated | No spec |
| PCIe 5 GPU ready | ✅ | ✅ | ❌ |
| Cable safety | 12V-2x6 (improved sense pins) | 12VHPWR (older, melting risk) | Adapters |
| CPU support | ✅ | ✅ | ✅ |

**Get ATX 3.1.** The improvements from 3.0 to 3.1 are small but meaningful: better 12+4 pin connector (12V-2x6 instead of 12VHPWR) with deeper sense pins that detect incomplete seating and shut down before melting. The be quiet! Pure Power 13 M and Corsair RM1000x are both ATX 3.1.

---

## Gold vs Platinum Efficiency

| Tier | Efficiency at 50% load | 1000W Yearly Cost (HU avg, 6h/day) | Difference |
|---|---|---|---|
| Gold | 87-90% | ~28,000 HUF | Baseline |
| Platinum | 89-92% | ~26,000 HUF | ~2,000 HUF/yr savings |
| Titanium | 90-94% | ~24,500 HUF | ~3,500 HUF/yr |

**Gold is good enough.** The difference between Gold and Platinum is ~3% efficiency, which saves about 2,000 HUF per year. The Pure Power 13M is Gold at 48k HUF. The Power Zone 2 is Platinum at 58k HUF. It would take 5 years to recoup the price difference in electricity savings.

---

## Cable Management Comparison

| PSU | Wires | 12V-2x6 Cable | Sleeving | Length | Bendable |
|---|---|---|---|---|---|
| **be quiet! Pure Power 13M** | Full modular | ✅ Native | Sleeved | Standard | Good |
| **be quiet! Power Zone 2** | Full modular | ✅ Native | Sleeved | Standard | Good |
| **Corsair RM1000x ATX 3.1** | Full modular | ✅ Type 5 (micro-fit) | Sleeved | Long | Very good (Type 5 is more flexible) |
| **Seasonic Focus GX-1000** | Full modular | ✅ (most variants) | Sleeved | Standard | Good |

Corsair's Type 5 cables (RM1000x ATX 3.1) are slightly more flexible than standard, making routing easier in tight cases. But all are fully modular with native 12V-2x6 — no real cable management concern with any of these.

---

## Physical Size (Length) — Case Fitment

Lian Li Lancool 207:
- **PSU max with HDD cage**: 160mm
- **PSU max without HDD cage**: 210mm

| PSU | Length | Fits Lancool 207 |
|---|---|---|
| **be quiet! Pure Power 13M 1000W** | 150mm | ✅ With cage |
| **be quiet! Power Zone 2 1000W** | 150mm | ✅ With cage |
| **be quiet! Dark Power 14 1000W** | 175mm | ❌ Need cage removed |
| **Corsair RM1000x ATX 3.1** | **180mm** | ❌ Need cage removed |
| **Seasonic Focus GX-1000** | 150mm | ✅ With cage |
| **Corsair RM1000e 2025** | 160mm | ✅ With cage (tight) |

If you want the RM1000x in Lancool 207, the HDD cage must be removed. You lose the 3.5" drive mount. For most builds this is fine (use M.2 SSD).

---

## Final Comparison (Target Models)

| Model | HU Price | PL Price | UA Price | UAH Best | Length | Efficiency |
|---|---|---|---|---|---:|---:|---:|
| Pure Power 13M 1000W | 48,240 HUF | ~640 PLN | 7,013 UAH | 7,013 | 150mm | Gold |
| RM1000x ATX 3.1 | 66,200 HUF | 647 PLN | 8,804 UAH | 7,957 | 180mm | Gold |
| Power Zone 2 1000W Plat | 57,836 HUF | ~640 PLN | 8,630 UAH | 7,868 | 150mm | Platinum |
| Seasonic Focus GX-1000 | 57,070 HUF | 687 PLN | 8,620 UAH | 8,469 | 150mm | Gold |
| CHIEFTEC Stealth 1000W Plat | 45,000 HUF | — | 6,453 UAH | 6,453 | — | Platinum |

**Recommendation**:
- **Best value HU**: Pure Power 13M — 48,240 HUF, compact, reliable
- **Best value PL**: RM1000x — 647 PLN, proven platform
- **Best value UA**: Pure Power 13M — 7,013 UAH (cheapest among quality options)
