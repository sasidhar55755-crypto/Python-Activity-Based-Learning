before = [100, 200, 150]
after = [80, 120, 90]

for i in range(len(before)):
    saving = before[i] - after[i]
    percentage = saving / before[i] * 100

    print("Appliance", i + 1)
    print("Energy saved:", saving)
    print("Saving percentage:", percentage, "%")