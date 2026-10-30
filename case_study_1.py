marks = [85, 35, 60]
attendance = [90, 55, 80]
lab_scores = [80, 30, 65]

for i in range(len(marks)):
    print("Student", i + 1)

    if marks[i] < 40 or attendance[i] < 75 or lab_scores[i] < 40:
        print("High Risk")
    elif marks[i] < 60:
        print("Medium Risk")
    else:
        print("Low Risk")