# Deep Search Prompt - PC Build Market Research

Use this prompt to research Roman's PC build across Hungary, Poland, and Ukraine.

The goal is not perfect data and not a final purchase decision. The goal is a useful, source-backed market map that gives Roman and Codex enough information to decide later.

## Research Mindset

- Search by requirements first, brand second.
- Be flexible if a site is blocked, incomplete, outdated, or hard to parse.
- Use exact prices when available.
- Use price ranges when exact prices are not reliable.
- State confidence for each important finding: high / medium / low.
- Prefer current local retailer and price-comparison pages, but use reputable fallback sources when needed.
- Separate "best technical choice" from "best buy at today's price."
- Do not get stuck trying to fill every table perfectly. If data is missing, write `not found` or `needs manual check` and continue.
- Do not assume MSI, Gigabyte, Kingston, Corsair, or any other brand is automatically best.
- Find the cheapest trusted option that satisfies the requirements. Do not chase the absolute cheapest no-name or suspicious listing.
- Do not make the final decision for Roman. Provide options, evidence, risks, tradeoffs, and questions for follow-up.

## Build Context

Roman is planning a PC for:

- database work
- SQL work
- finance work
- productivity
- many browser tabs / office workflow
- light gaming now
- stronger gaming later

Existing monitors:

- 4K 240Hz
- 4K 60Hz
- 1080p 144Hz

Buying plan:

- Build the main PC first, without the RTX 5080.
- Use Ryzen integrated graphics temporarily.
- Buy the RTX 5080 later when price, warranty, and availability make sense.

Future GPU target:

- RTX 5080 16GB
- prior observed target was around HUF 500,000, but this is not a limit. Use the actual current market.

## Budget Context

- First-stage build without GPU may land near HUF 700,000-1,000,000 depending CPU, cooling, case, and market prices.
- Future RTX 5080 purchase may be around HUF 500,000 or higher/lower depending actual market conditions.
- Eventual full build may be around HUF 1.2M-1.45M, but do not force the research into this range.

These are context bands, not thresholds. The researcher should find the cheapest trusted path that makes sense, then explain tradeoffs if the price is above or below these bands.

## Trusted-Cheapest Principle

For each category, search for the lowest sensible price among reputable brands, reputable models, and sellers with acceptable warranty/return conditions.

Trusted does not mean only the most famous brand. It means:

- known manufacturer or well-reviewed model line
- no obvious reliability red flags
- seller/retailer reputation is acceptable
- warranty/return route is understandable
- compatibility is clear

Examples of generally acceptable brand pools to consider:

- Motherboard/GPU: MSI, Gigabyte, ASUS, ASRock, Sapphire where relevant, Palit/Gainward/Zotac/PNY/Inno3D for GPU if reviews/warranty are acceptable.
- RAM: Kingston, G.Skill, Corsair, Crucial, TeamGroup, Lexar, Patriot if specs and EXPO support are good.
- SSD: Kingston, Samsung, WD, Crucial, Lexar, Solidigm, Seagate, SK hynix if model quality is good.
- PSU: be quiet!, Seasonic, Corsair, MSI, Thermaltake, FSP, Super Flower, Cooler Master, DeepCool if the exact model is reviewed and modern.
- Case/cooling: Corsair, NZXT, Fractal, Lian Li, Montech, Phanteks, DeepCool, be quiet!, Arctic, Thermalright, Noctua, Cooler Master if fit/value is good.

Avoid "cheap cheese" parts: unknown PSU platforms, no-name RAM/SSD, weak warranty, suspicious marketplace listings, or cases that look good but have bad airflow.

## Hard Constraints

These are the default non-negotiables unless the research finds an exceptional reason to challenge them.

- AM5 socket.
- ATX motherboard preferred; avoid mATX unless the value is exceptional and there is no practical downside.
- 2x32GB RAM preferred; do not recommend 4x16GB DDR5.
- DDR5-6000 CL30 or CL32 preferred.
- AMD EXPO preferred, not only XMP.
- Gen4 NVMe SSD minimum; Gen5 is not required.
- Avoid QLC SSDs for the main drive if better TLC options are reasonably priced.
- PSU should have native 12V-2x6 / PCIe 5.1 / ATX 3.1 support for the future RTX 5080.
- Case must fit large RTX 5080-class GPUs, preferably 360mm+ clearance.
- Case must have a black glass / visible-interior / clean aggressive aesthetic unless a much better value option appears.
- Cooling baseline: at least 3x120mm intake plus 1x120mm exhaust, or an equivalent airflow layout.

## Stop Conditions

Do not recommend buying if any of these apply:

- Seller rating/reputation is weak, unclear, or below roughly 4.0/5 where ratings are available.
- Return policy or warranty handling is unclear for an expensive part.
- Cross-border RTX 5080 price does not save enough money to justify warranty/return risk. A rough guide is 15-20% savings, but use judgment.
- RAM is 4x16GB DDR5, even if cheap, unless this is only mentioned as an avoid example.
- PSU lacks modern native GPU power support and is not a clearly excellent exception.
- Case cannot clearly fit the target GPU and cooling layout.

## Confidence Definitions

- High: verified current price from a reputable retailer, in stock, warranty/returns reasonably clear.
- Medium: price from an aggregator or reputable shop but not fully checked through, stock/warranty partly unclear, or price may be older than 7 days.
- Low: forum/marketplace listing, single obscure shop, unclear seller, non-local warranty risk, or data is incomplete.

## Price Freshness

- If a price is older than 14 days, mark it as `stale`.
- If stock appears very limited or uncertain, mark `low stock risk`.
- If prices differ strongly between sources, show the range and explain the likely reason.

## Markets To Compare

Primary markets:

- Hungary
- Poland
- Ukraine

Useful sources:

Hungary:

- Arukereso
- Argep
- iPon
- PCX
- Alza Hungary
- Aqua
- HardverApro for used/special GPU deals

Poland:

- Ceneo
- x-kom
- Morele
- Komputronik
- Proline
- Media Expert
- Allegro, with seller-risk check

Ukraine:

- Rozetka
- Hotline
- E-Katalog-style price comparison
- Telemart
- Brain
- other reputable PC shops if they appear

If one source is blocked or unclear, use another source and explain the limitation.

## Parts To Research

CPU options:

- Ryzen 7 9700X
- Ryzen 9 9900X
- Ryzen 7 9800X3D
- Ryzen 9 9900X3D
- Ryzen 9 9950X3D for context only, if easy to price

Motherboard:

- AM5
- good VRM/reliability
- Wi-Fi and Bluetooth preferred
- B850/B650E/X870 only if the price makes sense
- MSI MAG B850 Tomahawk MAX WiFi is the baseline, but compare alternatives

RAM:

- 64GB preferred
- 2x32GB preferred
- DDR5-6000 CL30 or CL32 preferred
- AMD EXPO preferred
- avoid 4-stick DDR5 unless there is a strong reason

SSD:

- 2TB Gen4 NVMe minimum
- Kingston KC3000 2TB is the baseline
- compare Samsung, WD, Lexar, Crucial, Solidigm, Seagate, and other reputable alternatives
- do not overpay for tiny benchmark differences
- avoid QLC drives for the main database/work SSD if good TLC drives are reasonably priced

PSU:

- 1000W ATX 3.1 / PCIe 5.1 preferred for future RTX 5080
- high-quality 850W ATX 3.1 acceptable if budget pressure is real
- native 12V-2x6 / modern GPU cable preferred
- avoid old models without modern GPU power support

Case and cooling:

- black case
- visible interior / glass / panoramic style preferred
- clean aggressive "Batman" look preferred
- must still have good airflow
- must fit large RTX 5080 cards
- compare Corsair 3500X RS-R ARGB as the visual baseline
- include similar Fractal, Lian Li, Montech, Phanteks, DeepCool, NZXT, be quiet!, and Corsair alternatives when price/value is strong
- include extra fan cost when a case has weak included cooling
- do not force a thick 360mm AIO into a case with risky radiator/GPU clearance
- minimum cooling target is 3x120mm intake plus 1x120mm exhaust, or equivalent airflow

CPU cooler:

- avoid overspending for Ryzen 7 9700X unless aesthetics/noise/future upgrade justify it
- stronger cooling is more reasonable for Ryzen 9 or X3D options
- compare strong air coolers, 240/280 AIOs, and 360 AIOs when relevant

GPU:

- RTX 5080 is for future purchase
- compare all major brands by actual market price and warranty, not brand loyalty
- include MSI, Gigabyte, ASUS, Palit, Gainward, Zotac, PNY, Inno3D, and others if available
- focus on watchlist candidates, not immediate purchase unless a deal is excellent

## Research Passes

If the task is too large for one clean answer, split the work into passes.

Pass 1 - CPU and motherboard:

- Compare CPU options across Hungary, Poland, and Ukraine.
- Compare B650/B850/X870 AM5 motherboard options across Hungary, Poland, and Ukraine.
- Verify exact model names, socket, form factor, Wi-Fi/Bluetooth, VRM quality, BIOS/firmware caveats, and price.

Pass 2 - RAM and SSD:

- Compare 64GB 2x32GB DDR5-6000 CL30/CL32 EXPO kits.
- Include a fallback 32GB discussion only as a budget/timing option.
- Compare 2TB Gen4 TLC SSDs for database/work use.
- Flag QLC and weak/no-name drives.

Pass 3 - PSU, case, cooling, fans:

- Compare 1000W ATX 3.1 / PCIe 5.1 PSUs and high-quality 850W fallbacks.
- Verify exact power connector names and avoid model confusion.
- Compare black glass / panoramic airflow cases.
- Count included fans and add extra fan cost where needed.
- Verify cooler, radiator, GPU, PSU, and cable clearance.

Pass 4 - RTX 5080 watchlist:

- Compare RTX 5080 cards across Hungary, Poland, and Ukraine.
- Focus on warranty-safe watchlist options.
- Check size, cooler/noise reputation, seller trust, and whether cross-border savings justify risk.

Each pass should produce:

- a short research summary
- a table of candidates
- source links
- confidence level
- open questions for the next pass

## Decision Logic

CPU:

- 9700X = value baseline
- 9900X = work/productivity upgrade
- 9800X3D = gaming-first option; do not recommend unless price is close or gaming priority rises
- 9900X3D = premium balanced option if the price is reasonable
- 9950X3D = likely overkill, price for context only

Budget logic:

- If first-stage build cost is closer to HUF 700,000: prioritize value and platform quality.
- If first-stage build cost is closer to HUF 900,000-1,000,000: consider CPU upgrade, better case/cooling, and stronger overall comfort.
- If the cheapest trusted build is outside these ranges, still report it and explain why.

Cross-border logic:

- Hungary is simplest for warranty and returns.
- Poland may be good for price hunting, especially smaller parts.
- Ukraine may be good if price is meaningfully better, but warranty and return practicality matter.
- For an expensive GPU, cross-border risk must be justified by a large saving.
- For RAM/SSD/CPU, cross-border buying is easier but still needs warranty/seller checks.

## Output Format

Start with a short answer-first research summary:

- strongest value patterns found
- strongest premium patterns found
- areas where the evidence is clear
- areas where more research or manual checking is needed
- parts that look promising
- parts that look risky

Then provide tables.

### Build Table

Create one table for a value build and one for a premium build.

Columns:

- Part
- Exact model or acceptable model range
- Tier, such as Best Value / Balanced / Premium / Watchlist
- Market/country
- Approximate price or price range
- HUF equivalent if available
- Why it fits
- Risk / caveat
- Confidence

### Component Market Table

Use this table for each component category when data is available.

Columns:

- Category
- Exact model
- Tier, such as Best Value / Balanced / Premium / Watchlist
- Country
- Retailer/source
- Price or range
- HUF equivalent if available
- Stock/warranty notes
- Compatibility notes
- Recommendation: buy / watch / avoid / needs manual check
- Confidence
- Source link
- Verification status: verified / aggregator only / needs click-through / manual check

Component categories:

- CPU
- motherboard
- RAM
- SSD
- PSU
- case
- CPU cooler
- case fans if needed
- future RTX 5080 options

## Scoring

Use a simple 1-5 score only when enough information exists. If not enough data exists, skip scoring and explain why.

Score categories:

- price/value
- compatibility
- quality/reliability
- warranty/seller confidence
- fit for Roman's use case

For cases, also score:

- airflow
- GPU clearance
- visual fit with black glass / visible-interior preference

For GPUs, also score:

- cooler/noise quality
- size/case fit
- warranty risk

## Important Flexibility Rules

- It is okay if the research cannot fully cover all three markets equally.
- It is okay to produce an initial shortlist first, then recommend a second pass for weak areas.
- It is okay to say "manual verification needed" for a seller, warranty, or stock status.
- Do not invent exact prices.
- Do not hide uncertainty.
- If price data is inconsistent, show the range and explain the likely reason.
- If one country's market is clearly worse for a category, say so and move on.

## After Research

After the market map is complete, produce:

- a candidate shopping list with exact models and likely retailers
- 2-3 backup alternatives per major category
- a list of parts that need manual verification before purchase
- a short "promising / watch / avoid / needs manual check" summary
- any compatibility checks that should be repeated in PCPartPicker before ordering
- open questions for Roman and Codex to decide in the next step

Important:

- Do not present the result as the final build.
- Present it as a research pack for the next decision conversation.
- Roman and Codex will make the final choices after reviewing the evidence.
