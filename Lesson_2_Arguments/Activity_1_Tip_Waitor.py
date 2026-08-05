def total_cal(bill_amount, tip_perc):
    tip = bill_amount * tip_perc / 100
    final_bill = round(bill_amount + tip)
    print(f"Please pay {final_bill}$")
total_cal(150, 5)