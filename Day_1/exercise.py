students = [
    {"name": "Aung Aung", "score": 85},
    {"name": "Su Su", "score": 92},
    {"name": "Mg Mg", "score": 35}
]

# 1. Display each student's name and score
for student in students:
    print(f"Name: {student['name']}, Score: {student['score']}")

# 2. Classify each student's grade using a function
def classify_grade(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"

for student in students:
    grade = classify_grade(student["score"])
    print(f"{student['name']}: {grade}")

# 3. Display only passing students
for student in students:
    if 40 <= student["score"] <= 100:
        print(f"{student['name']}: {student['score']}")

# 4. Add a fourth student
students.append({"name": "Mo Mo", "score": 75})

for student in students:
    print(f"Name: {student['name']}, Score: {student['score']}")

# 5. Create a tuple of three subject names and display them
subjects = ("Python", "Database", "Web Development")

for subject in subjects:
    print(subject)
