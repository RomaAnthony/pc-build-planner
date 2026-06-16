# FX Gain/Loss Logic for Purchases in Foreign Currency

**Log ID:** `FX-PURCHASE-20260615-001`  
**Date:** 2026-06-15  
**Context:** Hungary (HUF) vs. Ukraine (UAH) – impact of exchange rate strength on purchase profit/loss

---

## 1. Objective

When you buy something priced in a foreign currency (e.g., UAH) but pay in your home currency (e.g., HUF), exchange rate movements between the order date and the settlement date create an FX gain or loss.

This document shows:
- How to **display** the purchase in the foreign currency.
- How to **calculate the FX gain/loss** in your home currency.
- Whether a **stronger HUF + weaker UAH** leads to a worse outcome – and if that actually makes sense.

---

## 2. Basic Setup

Let:
- **Home currency** = HUF (forint) – what you pay with.
- **Foreign currency** = UAH (hryvnia) – the price of the purchased item.
- **Purchase price** = `P_UAH` (in UAH).
- **Exchange rate** = amount of UAH you get for 1 HUF.  
  Example: `1 HUF = 1.25 UAH` means HUF is strong (you get many UAH per HUF).

### 2.1 Exchange rate notation

We define the **rate** as: