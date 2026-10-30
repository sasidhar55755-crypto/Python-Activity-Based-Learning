seats = [
    [101, 102, 103],
    [104, None, 106],
    [107, 102, 109]
]

tickets = [101, 102, 103, 104, 106, 107, 109]

registered = []

for row in seats:
    for seat in row:
        if seat is None:
            print("Empty seat")
        elif seat in registered:
            print("Duplicate seat number:", seat)
        else:
            registered.append(seat)

for ticket in tickets:
    if ticket not in registered:
        print("Invalid ticket:", ticket)

print("Seating validation completed")