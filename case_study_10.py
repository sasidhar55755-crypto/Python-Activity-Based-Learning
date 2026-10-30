courses = [
    ("Python", "Room A", 9),
    ("Java", "Room B", 9),
    ("Maths", "Room A", 9),
    ("English", "Room C", 10)
]

room_capacity = {
    "Room A": 40,
    "Room B": 30,
    "Room C": 50
}

students = {
    "Python": 35,
    "Java": 25,
    "Maths": 45,
    "English": 40
}

allocated = []

for course, room, period in courses:
    print("\nCourse:", course)
    print("Room:", room)
    print("Period:", period)

    if students[course] > room_capacity[room]:
        print("Room capacity exceeded")
    elif (room, period) in allocated:
        print("Timetable clash")
    else:
        allocated.append((room, period))
        print("Allocation successful")

print("\nTimetable allocation completed")