# Book1 Workbook Map

Updated: 2026-06-15

Source workbook:
- `00_Hub/Book1.xlsx`

## Sheets

| Sheet | Used range | Purpose |
|---|---|---|
| `Sheet2` | `A1` only | Empty / unused sheet. Good place to paste or import the future `Builds` sheet. |
| `Parts` | `A1:M47` | Current parts database. One row = one exact offer/market option. |

## Parts Sheet Structure

Title:
- `Parts!A1` = `Data Sheet`

Headers:
- Header row is `Parts!A2:M2`.
- Data starts at `Parts!A3`.
- Data currently ends at `Parts!M47`.

Columns:

| Column | Header | Meaning | Formula lookup use |
|---|---|---|---|
| `A` | `ID` | Stable option ID, like `RAM_01_PL` | Main lookup key |
| `B` | `Part` | Category, like CPU/RAM/GPU | Filtering/grouping |
| `C` | `Priority` | Rank inside category | Sorting |
| `D` | `Option` | Product/model name | Pull to Builds sheet |
| `E` | `Market` | Hungary/Poland/etc. | Pull to Builds sheet |
| `F` | `Store` | Store or market lead | Pull to Builds sheet |
| `G` | `Price` | Original local price | Source price |
| `H` | `Currency` | HUF/PLN/etc. | Source currency |
| `I` | `HUF_Est` | Converted HUF estimate | Main total formula source |
| `J` | `Status` | Pick/Backup/Watch/Compare/Avoid | Optional display |
| `K` | `Risk` | Low/Medium/High | Optional display |
| `L` | `Note` | Short human comment | Pull to Builds sheet |
| `M` | `Source` | Local capture/note reference | Audit trail |

## Current Formula Strategy

The `Builds` sheet should only require manual selection of:
- `Selected_ID`
- optional `HU_Compare_ID`

Everything else can be pulled from `Parts`.

Recommended lookup formulas:

```excel
Part:
=IF($E7="","",XLOOKUP($E7,Parts!$A:$A,Parts!$D:$D,""))

Market:
=IF($E7="","",XLOOKUP($E7,Parts!$A:$A,Parts!$E:$E,""))

Store:
=IF($E7="","",XLOOKUP($E7,Parts!$A:$A,Parts!$F:$F,""))

HUF:
=IF($E7="","",XLOOKUP($E7,Parts!$A:$A,Parts!$I:$I,""))

Comment:
=IF($E7="","",XLOOKUP($E7,Parts!$A:$A,Parts!$L:$L,""))
```

If exchange rates are placed in the build sheet:
- `B3` = HUF per EUR
- `B4` = HUF per UAH

Then:

```excel
EUR:
=IF($J7="","",$J7/$B$3)

UAH:
=IF($J7="","",$J7/$B$4)
```

For savings versus a Hungary comparison row:

```excel
=IF($F7="","",MAX(0,XLOOKUP($F7,Parts!$A:$A,Parts!$I:$I,0)-$J7))
```

Example:
- `Selected_ID` = `RAM_01_PL`
- `HU_Compare_ID` = `RAM_01_HU`
- Saving formula compares `RAM_01_HU` HUF price against `RAM_01_PL` HUF price.

## Files Created For This Step

- `parts_options_seed.csv`: plain source database seed.
- `builds_seed.csv`: hardcoded readable build summary from earlier.
- `builds_formula_template.csv`: formula-based build sheet template that pulls from `Parts`.

Use `builds_formula_template.csv` for learning formulas and for the real build sheet.
