scores = [
    [20, 30, 25],
    [35, 40, 30],
    [15, 20, 18]
]

for i in range(len(scores)):
    total = sum(scores[i])
    average = total / len(scores[i])

    print("Player", i + 1)
    print("Total score:", total)
    print("Average score:", average)

    if total > 100:
        print("Excellent performance")