# Dictionary containing students and their marks
students = {
    "John": 75,
    "Mary": 82,
    "Peter": 68,
    "Sarah": 91,
    "david": 79,
}

#Display all students and their marks
print("students and their marks:")

for student, mark in students.items():
    print(student, ":", mark)

# Find the student with the highest mark
highest_student = max(students,key=students.get)
print("\nStudent with the highest mark:")
print(highest_student, ":", students[highest_student])