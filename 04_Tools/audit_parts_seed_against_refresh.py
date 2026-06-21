#!/usr/bin/env python3
"""Find captured planner options that are not yet in parts_options_seed.csv.

Run from the project root:

    python3 04_Tools/audit_parts_seed_against_refresh.py

The script reads the active refresh CSVs only. It does not read raw captures and
does not edit files. Treat the output as a review queue, not an auto-merge.
"""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "02_PC_Builds" / "parts_options_seed.csv"
REFRESH = ROOT / "02_PC_Builds" / "01_Price_Refresh" / "2026-06-21"

SKIP_DECISION_WORDS = {
    "reject",
    "verify_price",
}


def norm(value: str) -> str:
    value = value.lower()
    value = value.split(" - ")[0]
    value = value.replace("(", " ").replace(")", " ")
    value = value.replace("geforce", " ")
    value = value.replace("16g ", "16gb ")
    value = re.sub(r"\b(exact|broad|lead|row|sku)\b", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def price_key(row: dict[str, str]) -> tuple[str, str, str, str]:
    price = row.get("Price") or row.get("EU_Price") or ""
    try:
        price = f"{float(price):.2f}"
    except ValueError:
        price = str(price).strip()
    return (
        row.get("Part", ""),
        row.get("Market") or row.get("Country") or "",
        price,
        (row.get("Currency") or "").upper(),
    )


def read_seed_keys() -> tuple[set[tuple[str, str, str]], set[tuple[str, str, str, str]]]:
    with SEED.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
        name_keys = {
            (row["Part"], row["Market"], norm(row["Option"]))
            for row in rows
        }
        price_keys = {price_key(row) for row in rows}
        return name_keys, price_keys


def part_from_filename(path: Path) -> str:
    name = path.name
    if name.startswith("gpu_"):
        return "GPU"
    if name.startswith("motherboard_"):
        return "Motherboard"
    return ""


def is_usable(row: dict[str, str]) -> bool:
    price = (row.get("Price") or "").strip()
    decision = (row.get("Decision") or "").lower()
    if not price or price.upper() in {"NA", "NEED_PRICE"}:
        return False
    if any(word in decision for word in SKIP_DECISION_WORDS):
        return False
    try:
        float(price)
    except ValueError:
        return False
    return True


def main() -> None:
    seed_keys, seed_price_keys = read_seed_keys()
    missing: dict[tuple[str, str], list[tuple[str, dict[str, str]]]] = defaultdict(list)

    files = sorted(REFRESH.glob("*_reviewed_options.csv")) + sorted(
        REFRESH.glob("*_market_snapshot.csv")
    )
    for path in files:
        with path.open(newline="", encoding="utf-8-sig") as handle:
            for row in csv.DictReader(handle):
                if not is_usable(row):
                    continue
                part = row.get("Part") or part_from_filename(path)
                country = row.get("Country") or row.get("Market") or ""
                product = row.get("Product") or row.get("Option") or ""
                if not part or not country or not product:
                    continue
                key = (part, country, norm(product))
                row_for_price = {
                    "Part": part,
                    "Country": country,
                    "Price": row.get("Price") or "",
                    "Currency": row.get("Currency") or "",
                }
                if key not in seed_keys and price_key(row_for_price) not in seed_price_keys:
                    missing[(part, country)].append((path.name, row))

    for (part, country), rows in sorted(missing.items()):
        print(f"\n{part} / {country}: {len(rows)} possible seed additions")
        for filename, row in rows:
            product = row.get("Product") or row.get("Option") or ""
            price = row.get("Price") or ""
            currency = row.get("Currency") or ""
            decision = row.get("Decision") or ""
            match = row.get("Match_Quality") or row.get("Evidence") or ""
            print(f"  - [{filename}] {decision}/{match}: {product} | {price} {currency}")


if __name__ == "__main__":
    main()
