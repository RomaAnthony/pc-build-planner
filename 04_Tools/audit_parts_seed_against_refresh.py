#!/usr/bin/env python3
"""Find captured planner options that are not yet in parts_options_seed.csv.

Run from the project root:

    python3 04_Tools/audit_parts_seed_against_refresh.py
    python3 04_Tools/audit_parts_seed_against_refresh.py --check-wasm

The script reads the active refresh CSVs only. It does not read raw captures and
does not edit files. Treat the output as a review queue, not an auto-merge.
The WASM sync check is opt-in so local Marimo surgery can happen without
touching the hosted export.
"""

from __future__ import annotations

import csv
import ast
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / "02_PC_Builds" / "parts_options_seed.csv"
REFRESH = ROOT / "02_PC_Builds" / "01_Price_Refresh" / "2026-06-21"
LOCAL_APP = ROOT / "04_Tools" / "pc_build_marimo.py"
WASM_APP = ROOT / "04_Tools" / "pc_build_marimo_WASM_SAFE.py"
CHECK_WASM = "--check-wasm" in sys.argv
COMPARE_OPTIONAL_PARTS = {"Fan", "Thermal paste"}

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


def read_seed_rows() -> list[dict[str, str]]:
    with SEED.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def norm_exact(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def extract_app_dicts(path: Path) -> dict[str, dict]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    found = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in {"builds", "compare_ids"}:
                found[target.id] = ast.literal_eval(node.value)
    return found


def planner_integrity_errors() -> list[str]:
    rows = read_seed_rows()
    by_id = {row["ID"]: row for row in rows}
    errors: list[str] = []
    duplicate_ids = sorted({row["ID"] for row in rows if [r["ID"] for r in rows].count(row["ID"]) > 1})
    if duplicate_ids:
        errors.append(f"Duplicate seed IDs: {', '.join(duplicate_ids)}")

    local = extract_app_dicts(LOCAL_APP)
    if CHECK_WASM:
        wasm = extract_app_dicts(WASM_APP)
        if local.get("builds") != wasm.get("builds"):
            errors.append("Local and WASM build dictionaries differ.")
        if local.get("compare_ids") != wasm.get("compare_ids"):
            errors.append("Local and WASM compare_ids dictionaries differ.")

    builds = local.get("builds", {})
    compare_ids = local.get("compare_ids", {})
    for build_name, build_parts in builds.items():
        for part_label, item_id in build_parts.items():
            if item_id not in by_id:
                errors.append(f"Build {build_name!r} references missing {part_label}: {item_id}")
            elif (
                by_id[item_id]["Market"] in {"Poland", "Ukraine"}
                and by_id[item_id]["Part"] not in COMPARE_OPTIONAL_PARTS
                and item_id not in compare_ids
            ):
                errors.append(
                    f"Build {build_name!r} uses {item_id} without a Hungarian savings reference."
                )

    for source_id, ref_id in compare_ids.items():
        if source_id not in by_id:
            errors.append(f"compare_ids key is missing from seed: {source_id}")
            continue
        if ref_id not in by_id:
            errors.append(f"compare_ids value is missing from seed: {source_id} -> {ref_id}")
            continue
        if by_id[source_id]["Part"] != by_id[ref_id]["Part"]:
            errors.append(
                f"compare_ids part mismatch: {source_id} ({by_id[source_id]['Part']}) -> "
                f"{ref_id} ({by_id[ref_id]['Part']})"
            )

    active_or_mapped_ids = {
        item_id
        for build_parts in builds.values()
        for item_id in build_parts.values()
        if item_id in by_id
    } | {item_id for item_id in compare_ids if item_id in by_id}

    by_model: dict[tuple[str, str], dict[str, dict[str, str]]] = defaultdict(dict)
    for row in rows:
        by_model[(row["Part"], norm_exact(row["Option"]))][row["Market"]] = row
    for (_part, _model), markets in by_model.items():
        hu_row = markets.get("Hungary")
        if not hu_row:
            continue
        for market in ("Poland", "Ukraine"):
            row = markets.get(market)
            if not row:
                continue
            if row["ID"] not in active_or_mapped_ids:
                continue
            mapped = compare_ids.get(row["ID"])
            if mapped != hu_row["ID"]:
                errors.append(
                    f"Exact HU reference missing/wrong: {row['ID']} should map to {hu_row['ID']}"
                )

    return errors


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
    errors = planner_integrity_errors()
    if errors:
        print("Planner integrity errors:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    print("Planner integrity: OK")

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
