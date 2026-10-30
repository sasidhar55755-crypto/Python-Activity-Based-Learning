passengers = [
    [35, 40, 45],
    [20, 25, 30],
    [50, 55, 60]
]

capacity = 40
fuel = [30, 25, 40]

for i in range(len(passengers)):
    total = sum(passengers[i])
    average = total / len(passengers)

    print("Route", i + 1)
    print("Total passengers:", total)
    print("Average passengers:", average)
    print("Fuel used:", fuel[i])

    if max(passengers[i]) > capacity:
        print("Overloaded route")
    else:
        print("Route within capacity")