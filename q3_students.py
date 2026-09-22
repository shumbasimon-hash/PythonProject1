students = {
    "John": 75,
    "Mary": 88,
    "Peter": 69,
    "Alice": 92,
    "David": 81
}

# Display all students and their marks
print("Students and Marks:")

for student, mark in students.items():
    print(student, ":", mark)

# Find the student with the highest mark
highest_student = max(students, key=students.get)

print("\nStudent with the highest mark:")
print(highest_student, ":", students[highest_student])