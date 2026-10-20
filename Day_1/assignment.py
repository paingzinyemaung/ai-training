# Student Performance Report

# Accept data for at least 5 students
students = [
    {"name": "Aung Aung", "age": 21, "study_hours": 4.5, "score": 85},
    {"name": "Su Su", "age": 20, "study_hours": 3.0, "score": 65},
    {"name": "Mg Mg", "age": 22, "study_hours": 2.0, "score": 35},
    {"name": "Hla Hla", "age": 19, "study_hours": 4.0, "score": 75},
    {"name": "Kyaw Kyaw", "age": 23, "study_hours": 5.0, "score": 90},
]

# Use a tuple to store fixed grade categories
GRADE_CATEGORIES = ("Excellent", "Good", "Pass", "Fail")

# Required Function: calculate_average(scores)
def calculate_average(scores):
  if len(scores) == 0:
    return 0
  return sum(scores) / len(scores)

# 4. Required Function: classify_grade(score)
def classify_grade(score):
  if score < 0 or score > 100:
    return "Invalid"
  elif score >= 80:
    return "Excellent"
  elif score >= 60:
    return "Good"
  elif score >= 40:
    return "Pass"
  else:
    return "Fail"

# Required Function: count_passed(students)
def count_passed(students):
  count = 0
  for student in students:
    if student["score"] >= 40:
      count += 1
  return count

# Calculate summary statistics using loops and functions
total_students = len(students)
scores_list = [s["score"] for s in students]
avg_score = calculate_average(scores_list)
highest_score = max(scores_list)
lowest_score = min(scores_list)
passed_count = count_passed(students)
failed_count = total_students - passed_count
top_student = max(students, key=lambda x: x["score"])

# top_student = students[0]

# for student in students:
#   if student["score"] > top_student["score"]:
#     top_student = student

# Display complete performance report
print("===== STUDENT PERFORMANCE REPORT =====\n")

for student in students:
  grade = classify_grade(student["score"])
  print(f"Name: {student['name']}")
  print(f"Age: {student['age']}")
  print(f"Study Hours: {student['study_hours']}")
  print(f"Score: {student['score']}")
  print(f"Grade: {grade}\n")

print("===== SUMMARY =====")
print(f"Total Students: {total_students}")
print(f"Average Score: {avg_score:.2f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passed Students: {passed_count}")
print(f"Failed Students: {failed_count}")
print(f"Top Student: {top_student['name']} ({top_student['score']})")