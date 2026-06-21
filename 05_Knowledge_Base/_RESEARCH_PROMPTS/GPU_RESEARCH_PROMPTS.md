# GPU Research Prompts — AI-Ready

Paste these into ChatGPT / Claude / Gemini one at a time. Each prompt includes full context so the AI knows exactly what to deliver. **No price analysis needed** — prices are already captured in the market snapshots.

---

## PROMPT 1: RTX 5080 Manufacturer Model Binning

===BEGIN PROMPT===
I need a complete breakdown of every RTX 5080 manufacturer model tier, from cheapest (value) to most expensive (premium), for all major AIB partners.

## CONTEXT
- **GPU**: RTX 5080 16GB GDDR7
- **Target build**: Ryzen 9 9900X + MSI B850 Tomahawk MAX WiFi + 1440p 165Hz
- **Case**: Lian Li Lancool 207 (GPU max 375mm)
- **Use case**: Gaming with ray tracing, Python data analysis, potential ML/AI
- **Need is**: Phase 1 = no GPU (integrated graphics), Phase 2 = add RTX 5080 later
- **NO price analysis needed** — I already have market prices. I need SPECS and QUALITY comparison.

## WHAT I NEED (structured output)

### Section 1: Manufacturer Model Hierarchy
For each manufacturer (MSI, ASUS, Gigabyte, ASRock, Palit, Inno3D, PNY, Zotac, Gainward):

**Products table with:**
| Manufacturer | Tier Name | SKU suffix | Cooler Type (fans/heatpipes/fins) | Length (mm) | Slots | Noise Level (subjective) | Typical Temp under Load | Build Quality Notes |
|---|---|---|---|---|---|---|---|---|

Tiers should be clearly classified as:
- **Value** (entry level, basic cooler, e.g. Ventus, Windforce, Palit Dual)
- **Mid** (better cooler, dual BIOS, mild RGB, e.g. Gaming Trio, TUF, Gaming OC)
- **Premium** (overbuilt, LCD screens, AORUS Master, ROG Strix, Suprim)
- **Liquid** (AIO-cooled, Suprim Liquid, AORUS Waterforce)

**For each model tier, I need to know:**
- What physically changes between tiers (more heatpipes? bigger heatsink? better fans?)
- Which tier actually has a meaningfully different PCB (not just different cooler on same PCB)
- Does the value tier compromise anything important (louder fans, coil whine, worse VRM cooling)?

### Section 2: Cooling Performance Range
- Typical GPU temps under 1440p gaming load for value vs mid vs premium air coolers
- Power draw range: 300-400W, what models run hottest
- Which models have known coil whine issues or thermal problems (hotspot deltas)
- Fan noise at load: dB estimates or subjective ranks

### Section 3: Size Constraints Check
- Which models WON'T fit Lancool 207 (375mm max) — list exact lengths
- Which models are too tall for standard ATX cases (>3 slots)
- Which models need the 12V-2x6 cable clearance (any minimum bend radius issues with side panel?)

### Section 4: Physical Build Quality
- Does the value tier use a metal backplate or plastic?
- Are there RGB versions vs non-RGB? Which have physical RGB switch vs need software?
- Dual BIOS switch availability per tier

### Section 5: Bottom Line
- Best value pick for this build (price + quality + size balance)
- Best quiet pick if budget allows more
- Which models to avoid and why (specific issues)
- Is the cheapest tier (Ventus/Windforce) actually fine, or is there a real reason to step up?

## ANTI-PATTERNS
- Do NOT say "it depends" without clear guidance
- Do NOT give USA-centric info — I need global/EU product naming
- Do NOT quote prices — I have those
- Do NOT recommend a tier without explaining WHY it's better (not just "it's higher end")
===END PROMPT===

---

## PROMPT 2: RTX 5080 vs RTX 5070 Ti vs RTX 4080 Super — Real Performance Comparison

===BEGIN PROMPT===
I need a detailed performance comparison between RTX 5080, RTX 5070 Ti (16GB version), and RTX 4080 Super for a specific build context.

## CONTEXT
- **Build**: Ryzen 9 9900X + MSI B850 Tomahawk + 64GB DDR5-6000
- **Display**: 1440p 165Hz gaming monitor
- **Use cases**: 1440p gaming (including RT/path tracing), Python data analysis, potential light ML/AI
- **GPU will be bought later** (phase 2), so this comparison is for decision-making, not purchase timing
- **NO price analysis needed** — I already have market prices. I need PERFORMANCE %, not cost.

## WHAT I NEED (structured)

### 1. Performance Table — 1440p Gaming (No Ray Tracing)
20+ modern game titles (2023-2026 releases). For each:
| Game | RTX 5080 FPS | RTX 5070 Ti FPS | RTX 4080S FPS | 5080 vs 5070 Ti % | 5080 vs 4080S % | Setting |
Average and median across all games.

### 2. Performance Table — 1440p With Ray Tracing
Same games where RT is available:
| Game | RT ON | RTX 5080 FPS | RTX 5070 Ti FPS | RTX 4080S FPS | 5080 vs 5070 Ti % |
Cyberpunk 2077 path tracing at 1440p **must** be included. Show with and without DLSS and frame gen.

### 3. DLSS and Frame Gen Comparison
- Which DLSS transformer model each card supports
- Which frame gen each supports (single vs multi 3x/4x)
- Real FPS uplift in Cyberpunk path tracing 1440p with frame gen on all 3
- Image quality differences between frame gen implementations (any artifacting?)

### 4. Productivity / Compute Comparison
- CUDA compute performance (Geekbench Compute, Blender, V-Ray)
- Local LLM inference (LLaMA 7B/13B token/s if known)
- Stable Diffusion image gen speed (steps/s)
- Video encoding quality (NVENC AV1 support)

### 5. Percentage Summary Table

| Metric | RTX 5080 (baseline 100%) | RTX 5070 Ti (%) | RTX 4080 Super (%) |
|---|---|---|---|
| 1440p raster (avg FPS) | 100% | ? | ? |
| 1440p RT (avg FPS) | 100% | ? | ? |
| 1440p PT + DLSS + FG | 100% | ? | ? |
| Productivity compute | 100% | ? | ? |

### 6. VRAM Analysis
- VRAM usage in 1440p ultra (2025-2026 titles) — does 16 GB hit limits in any scenario?
- Which card runs out of VRAM first, and in which specific games/workloads?
- Future projection: will 16 GB be enough in 2028 for 1440p?

### 7. Clear Recommendation
- Which GPU is the right pick for this build and why
- At what performance% gap would you step down to 5070 Ti?
- Is the 4080 Super still worth considering if found used/cheap, or skip entirely?

## ANTI-PATTERNS
- Do NOT say "it depends" — make a clear recommendation
- Do NOT compare against hypothetical cards ("wait for next gen")
- Do NOT focus on 4K — this build is 1440p
- Do NOT use synthetic benchmarks alone — game benchmarks are primary
===END PROMPT===

---

## PROMPT 3: Manufacturer and Model Reputation Analysis

===BEGIN PROMPT===
I need a reputation and reliability analysis of all RTX 5080 AIB manufacturers for a long-term personal build.

## CONTEXT
- GPU: RTX 5080 (any model)
- Build lifecycle: 5+ years, high personal standards
- Markets: Hungary, Poland, Ukraine (need EU warranty support)
- Not interested in RGB software ecosystems
- Value quiet operation, build quality, and reliability over flashy features

## WHAT I NEED

### 1. Manufacturer Reputation Table
| Manufacturer | Overall Reliability Rank (1-10) | Cooler Quality | Build Quality | Common Issues | Warranty (years) | RMA Experience (EU) |
|---|---|---|---|---|---|---|

For: MSI, ASUS, Gigabyte, ASRock, Palit, Inno3D, PNY, Zotac, Gainward

### 2. EU Warranty Reality
- Which manufacturers honor EU-wide warranty (buy in Poland, RMA in Hungary)?
- Which require registration in country of purchase?
- Which have service centers in Hungary vs Poland vs neither?
- Real RMA anecdotes: who is actually good to deal with, who fights claims?

### 3. Known Issues Per Model (RTX 5080 Generation)
- Any model with known coil whine (specific SKUs if reported widely)
- Any model with thermal pad issues (hotspot delta >15°C)
- Any model with fan bearing failures early on
- Any model with 12V-2x6 connector issues (melting, poor seating)
- Which of these are widespread vs isolated incidents

### 4. BIOS / Software
- Which manufacturers have good software (fan curve, OC, monitoring) — rate 1-10
- Which have bad software (bloat, forced login, ads, crashes)?
- Dual BIOS availability per manufacturer (silent/performance switch)
- Can you fully control the card without running their software? (fan control via Afterburner, voltage via BIOS)

### 5. Bottom Line
- Safest manufacturer for a 5+ year EU build
- Best value vs reliability combination
- Which manufacturers to actively avoid and why
===END PROMPT===

---

## PROMPT 4: RTX 5080 vs AMD RX 9070 XT — NVIDIA vs AMD at High End

===BEGIN PROMPT===
I need a comparison between RTX 5080 and RX 9070 XT to confirm whether NVIDIA is the right choice for this specific build.

## CONTEXT
- Build: Ryzen 9 9900X + 1440p 165Hz
- Primary use: gaming with ray tracing, Python data analysis, potential ML/AI
- Current assumption: RTX 5080 is the target
- Not brand-loyal — just want the best tool
- **NO price analysis needed** — I have market prices. I need PERFORMANCE and CAPABILITY comparison.

## WHAT I NEED

### 1. Gaming Performance Comparison
- 1440p raster (no RT): which wins? By how much (%)?
- 1440p RT: which wins? By how much (%)?
- Can RX 9070 XT do playable path tracing at 1440p? (Cyberpunk benchmark expected)
- Upscaling quality: DLSS 4 vs FSR 3.1 at 1440p quality mode — side by side comparison

### 2. Productivity Comparison
- CUDA vs ROCm: for Python data analysis (Pandas, Numpy — does GPU even matter here?)
- Local LLM inference (7B, 13B): which is better? Any limitations with AMD ROCm?
- Stable Diffusion: which is faster? Which has better compatibility?
- Video encoding: NVENC vs AMD encoder quality/speed for recording/streaming

### 3. Feature Comparison
- DLSS 4 multi-frame gen vs AMD Fluid Motion Frames — real quality difference?
- Ray tracing hardware: NVIDIA 4th gen RT vs AMD 2nd gen — core architectural difference?
- Power draw under load: which card draws less?
- VRAM advantage: both are 16 GB — is that a wash?

### 4. Future-Proofing
- Which card will age better over 5 years? (considering RT demands increasing, DLSS vs FSR ecosystem growth)
- For ML/AI specifically: will AMD ever catch up on CUDA lock-in, or is NVIDIA permanently ahead for this use case?

### 5. Specific Verdict
- Should I buy RTX 5080 or RX 9070 XT for this specific build?
- Is there any scenario where RX 9070 XT is the better choice?
- Is the answer different if I don't actually end up doing ML/AI work?
===END PROMPT===

---

## PROMPT 5: No GPU First — Integrated Graphics Reality Check

===BEGIN PROMPT===
I need a reality check on using the Ryzen 9 9900X's integrated graphics as a placeholder for 1-6 months before buying a discrete GPU.

## CONTEXT
- Ryzen 9 9900X has 2 RDNA 2 compute units on the I/O die (iGPU)
- Monitor: 1440p 165Hz (will run at lower resolution if needed)
- Phase 1: building the PC now with no discrete GPU
- Phase 2: adding RTX 5080 later (1-6 months)
- Tasks during phase 1: web browsing, Excel/data analysis, coding (VS Code, Python), video playback, Windows desktop

## WHAT I NEED

### 1. What the iGPU Can Actually Do
- Display output resolution: max via HDMI and via DP (motherboard outputs on B850 Tomahawk)
- Can it drive 1440p 60Hz on desktop? Any issues with refresh rate?
- Can it decode YouTube 1440p/4K video? Which codecs supported (AV1, HEVC, H.264)?
- Can it drive 2 monitors? Yes/no, any conditions?

### 2. What It CANNOT Do
- Any modern gaming — specific examples of what's impossible
- GPU acceleration in content creation
- ML/AI inference at usable speed

### 3. Practical Daily Experience
- Will Windows feel laggy/slow on desktop with animations?
- Will VS Code, Excel, Firefox/Chrome work normally?
- Will Python data analysis (Pandas, basic matplotlib plotting) work without GPU?
- Will compiling code work fine?
- Any jank or stutter in normal desktop use?

### 4. Recommendations
- Any BIOS settings to check for motherboard video output
- Whether to get a cheap placeholder GPU ($50-100 used) or just use iGPU
- Is there any case where the iGPU is unusably bad for desktop work?
===END PROMPT===
