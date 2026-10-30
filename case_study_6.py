units = [50, 150, 250]
rate1 = 2
rate2 = 3
rate3 = 5
fixed_charge = 50

for i in range(len(units)):
    u = units[i]

    if u <= 100:
        bill = u * rate1
    elif u <= 200:
        bill = 100 * rate1 + (u - 100) * rate2
    else:
        bill = 100 * rate1 + 100 * rate2 + (u - 200) * rate3

    bill = bill + fixed_charge

    print("Apartment", i + 1)
    print("Units:", u)
    print("Total bill: Rs.", bill)