students = [
    ("Alice", 85),
    ("Bob", 75),
    ("Charlie", 95)
]

sorted_students = sorted(students, key=lambda x: x[0])

print(sorted_students)