# Cooling Decision Guide — Ryzen 9 9900X Build

For: Ryzen 9 9900X · Lian Li Lancool 207 / Corsair 3500X

---

## Bottom Line

**Target: Arctic Liquid Freezer III Pro 360 A-RGB Black (BP028EU).** Best price/performance 360mm AIO. ~31,500 HUF in Hungary. Excellent AM5 mounting (offset bracket for better performance on Ryzen), thicker radiator (38mm vs standard 27mm) for better cooling, quiet pump. Buy in Hungary unless Poland has a deal.

---

## Why 360mm AIO for Ryzen 9 9900X?

| Cooler Type | 9900X Gaming Temp | 9900X All-Core Load | Noise |
|---|---|---|---|
| Stock AMD cooler | 85-90°C | Throttles | Loud |
| Good air cooler (NH-D15, PA120) | 65-70°C | 80-85°C | Quiet |
| **240mm AIO** | 60-65°C | 75-80°C | Quiet |
| **280mm AIO** | 55-60°C | 70-75°C | Quiet |
| **360mm AIO** | 50-55°C | 65-70°C | Very quiet |
| 420mm AIO | 48-52°C | 60-65°C | Very quiet |

The 9900X has a 120W TDP that can burst to 170-200W under all-core load. A 360mm AIO keeps it at 65-70°C under sustained load with quiet fan speeds. An air cooler works but runs 10-15°C hotter and louder under load.

For this build (data analysis, compiling, VM work that can sustain CPU load): 360mm AIO is justified.

---

## Arctic Liquid Freezer III Pro 360 — Why It's The Pick

| Feature | Value |
|---|---|
| Radiator | 38mm thick (beats most 27mm) |
| Fans | 3x 120mm P12 PWM PST (daisy chain) |
| Pump | VRM fan integrated in pump housing |
| AM5 compatibility | Offset mounting bracket (improves hotspot temps by 3-5°C) |
| RAM clearance | Excellent — pump doesn't overhang RAM |
| Noise | 0.3 sone pump (quiet even at full) |
| Tube length | 450mm (fits top mount easily) |
| Warranty | 6 years |
| Price | ~31,500 HUF HU |

The **Pro** version adds A-RGB fans over the standard version. The standard (non-RGB) is ~29,200 HUF. Both use the same radiator and pump — only fan lighting differs.

### The VRM Fan

Arctic includes a small fan on the pump block that blows air over the motherboard VRM area. In the Lancool 207 with a top-mounted 360mm AIO, VRM airflow is otherwise limited. This fan helps keep the 9900X's VRM cool even under sustained load.

---

## Competitor Comparison

| AIO | HU Price | Radiator | Pump | Fans | Performance | Noise |
|---|---|---|---|---|---|---|
| **Arctic LF III Pro 360** 🥇 | 31,500 HUF | 38mm | VRM fan | P12 PST | Excellent | Very quiet |
| DeepCool LE360 V2 | 22,500 HUF | 27mm | Standard | Standard | Good | Moderate |
| MSI MAG CoreLiquid A13 360 | 27,777 HUF | 27mm | Standard | Standard | Good | Moderate |
| Gigabyte GME 360 | 31,800 HUF | 27mm | Standard | Standard | Good | Moderate |
| be quiet! Pure Loop 3 360 | 34,800 HUF | 27mm | Standard | Silent Wings | Very good | Quietest |
| Arctic LF III 360 (no RGB) | 29,200 HUF | 38mm | VRM fan | P12 (no RGB) | Excellent | Very quiet |

**Arctic wins on value** — 38mm rad gives 10-15% better cooling than 27mm competitors at the same or lower price. DeepCool is cheaper but the thinner rad and worse fans mean higher noise for same temps.

---

## Top Mount vs Front Mount

In Lancool 207 or Corsair 3500X:

| Mount | Pros | Cons |
|---|---|---|
| **Top** 🥇 | Better GPU airflow (no rad blocking front), hot air exhausts naturally | CPU gets pre-heated case air |
| Front | CPU gets fresh cool air (better CPU temps by 1-3°C) | GPU airflow restricted, rad in front is more dust-prone |

**For this build: top mount.** The Lancool 207's GPU cooling depends on front/bottom intake. Blocking the front with a rad reduces GPU airflow significantly. Top mount with the 9900X in exhaust gives balanced temps.

---

## Arctic — RAM Clearance

The Arctic LF III Pro pump is compact and does NOT overhang RAM slots on AM5. All standard DDR5 modules clear it, including tall RGB ones like G.Skill Trident Z5 (44mm).

This is a significant advantage over some other AIOs (Corsair H150i, NZXT Kraken) whose pump blocks can overhang the first RAM slot on certain motherboards.

---

## Case Fitment

| Case | Top 360 Mount | Clearance |
|---|---|---|
| Lian Li Lancool 207 | ✅ Yes | 50mm+ from motherboard to top |
| Corsair 3500X | ✅ Yes | Standard ATX clearance |
| NZXT H7 Flow | ✅ Yes | Ample |

The Arctic LF III Pro 360 (38mm rad + 25mm fans = 63mm total) fits in all three cases' top mounts.

---

## Fan Configurations

| Config | Fans | Orientation | Best For |
|---|---|---|---|
| **Top AIO exhaust** | 3x rad fans top, 2x140mm front intake, 2x120mm bottom intake | Balanced | Lancool 207 standard setup |
| Top AIO + front intake | 3x rad fans top, 3x120mm front intake | Better CPU, worse GPU | If not using bottom fans |

Lancool 207 Recommended: top AIO exhaust + 2x140mm front intake + 2x120mm bottom intake. The bottom fans feed the GPU directly, which is the case's design strength.
