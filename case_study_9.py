received = [100, 150, 200]
distributed = [80, 120, 180]
damaged = [5, 10, 5]

minimum_stock = 20

for i in range(len(received)):
    remaining = received[i] - distributed[i] - damaged[i]

    print("Location", i + 1)
    print("Remaining stock:", remaining)

    if remaining < minimum_stock:
        print("Replenishment required")
    else:
        print("Stock is sufficient")