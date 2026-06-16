def show_purchase_with_fx_gain_loss(p_uah, r_order, r_pay, home_currency="HUF"):
    huf_order = p_uah / r_order
    huf_pay = p_uah / r_pay
    fx_gain_loss = huf_order - huf_pay

    print(f"Purchase amount: {p_uah} UAH")
    print(f"Rate at order: 1 {home_currency} = {r_order} UAH")
    print(f"Rate at payment: 1 {home_currency} = {r_pay} UAH")
    print(f"Expected cost: {huf_order:.2f} {home_currency}")
    print(f"Actual cost:   {huf_pay:.2f} {home_currency}")
    print(f"FX gain/loss:  {fx_gain_loss:+.2f} {home_currency}")
    if fx_gain_loss > 0:
        print("→ You gained (paid less than expected).")
    elif fx_gain_loss < 0:
        print("→ You lost (paid more than expected).")
    else:
        print("→ No FX effect.")