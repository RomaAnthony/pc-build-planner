# Case Decision Guide — Ryzen 9 9900X Build

For: ATX · 360mm AIO (front or top) · Full-size GPU (up to 340mm)

---

## Bottom Line

**Target: Lian Li Lancool 207 Digital Black (~32k HUF in Hungary).** Best airflow ATX case under 35k HUF. Comes with 4 fans (2x140mm front + 2x120mm bottom), mesh front, excellent GPU cooling. Buy in Hungary because glass case logistics make Poland/Ukraine painful.

If Lancool 207 is out of stock: Corsair 3500X ARGB at ~32k HUF is the backup — slightly less airflow but more visual appeal (glass front).

---

## Case Requirements

This build needs:

| Requirement | Why |
|---|---|
| ATX form factor | B850 Tomahawk is ATX |
| 360mm AIO support | Arctic Freezer III Pro 360 |
| 300mm+ GPU clearance | RTX 5080 Ventus is 303mm |
| 150mm+ PSU clearance | All PSU options are 150-180mm |
| Good airflow | 1440p gaming + 9900X produce heat |
| 2x HDD bay or 1x HDD + 2x SSD | Future bulk storage |

---

## Lian Li Lancool 207 Digital

| Spec | Value |
|---|---|
| Form factor | Mid-tower ATX |
| Motherboard support | ATX, mATX, ITX |
| GPU max length | 375mm (with front fan) |
| **PSU max with HDD cage** | **160mm** |
| **PSU max without HDD cage** | **210mm** |
| CPU cooler height | 175mm |
| 360mm AIO mount | Top or Front |
| Included fans | 2x140mm front + 2x120mm bottom (PWM) |
| Storage | 1x 3.5" + 2x 2.5" |
| Front I/O | USB-C, 2x USB 3.0 |
| Price (HU) | ~31,990 HUF |

### Key design notes:
- Bottom intake fans push air directly to GPU — best GPU cooling of any case in this price range
- PSU is front-mounted (unusual), which is why PSU length is critical
- Mesh front + mesh top = excellent airflow
- Cable management space: moderate (not the best, not the worst)
- Glass side panel (standard)

### The HDD Cage Trade-off

The PSU sits near the front, behind the HDD cage. With the cage installed:
- Max PSU = 160mm (Pure Power 13M fits ✅, RM1000x does NOT ❌)
- Without cage: max PSU = 210mm (everything fits)
- Cage removal loses the 3.5" HDD mount (use 2.5" SSDs or M.2 instead)

For this build: Pure Power 13M at 150mm means the cage stays. You keep the HDD option.

---

## Corsair 3500X ARGB

| Spec | Value |
|---|---|
| GPU max length | 365mm |
| PSU max length | 220mm |
| 360mm AIO mount | Top or side |
| Included fans | 3x120mm ARGB |
| Storage | 1x 3.5" + 2x 2.5" |
| Price | ~31,990 HUF (ARGB), ~21,326 HUF (plain) |

### vs Lancool 207

| Feature | Lancool 207 | Corsair 3500X |
|---|---|---|
| Airflow | 🥇 Excellent (mesh front) | 🥈 Good (mesh sides, glass front) |
| GPU cooling | 🥇 Bottom intake | 🥈 Standard |
| # Fans included | 4 | 3 |
| PSU layout | Front (be careful) | Bottom (standard) |
| Visual appeal | 🥈 Clean, simple | 🥇 Glass front looks premium |
| Cable management | 🥈 OK | 🥇 Better (standard layout) |

**Verdict**: Lancool 207 for performance. 3500X for looks. Both are priced similarly.

---

## Budget Alternatives

| Case | Price (HU) | Notes |
|---|---|---|
| Phanteks XT View TG | ~27,901 HUF | Cheap but good, D-RGB, decent airflow |
| Montech Air 903 Max | ~30,000 HUF | 4 fans, mesh, good value but harder to find in HU |
| NZXT H7 Flow | ~35,000 HUF | Excellent build quality, premium, slightly more expensive |

---

## Why Buy Locally (Hungary)

Cases are the one part where local purchase is strongly preferred:
- **Glass panel**: shipping glass across borders = risk of breakage
- **Size**: shipping a case box costs 5-10k HUF extra from Poland
- **No warranty concern**: cases rarely fail, but if the glass breaks in transit, local return is simpler
- **Price difference**: cases are priced similarly across HU/PL/UA (~10-15% max)

---

## Decision Flowchart

```
Need airflow?
├── Yes → Lancool 207 (4 fans, bottom GPU intake)
│           ├── PSU ≤ 160mm? → Keep HDD cage (Pure Power 13M)
│           └── PSU > 160mm? → Remove HDD cage (RM1000x)
│
└── Want looks?
    ├── Budget → Corsair 3500X ARGB
    └── Premium → NZXT H7 Flow
```
