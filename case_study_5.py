marks = [35, 45, 80, 95]
moderated = []

for mark in marks:
    new_mark = mark + 5

    if new_mark > 100:
        new_mark = 100

    moderated.append(new_mark)

print("Original marks:", marks)
print("Moderated marks:", moderated)

for mark in moderated:
    if mark >= 40:
        print(mark, "- Pass")
    else:
        print(mark, "- Fail")