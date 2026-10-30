electricity = [100, 150, 200]
water = [500, 600, 800]

for i in range(len(electricity)):
    print("Floor", i + 1)
    print("Electricity usage:", electricity[i])
    print("Water usage:", water[i])

    if electricity[i] > 150 or water[i] > 700:
        print("Usage exceeds limit")