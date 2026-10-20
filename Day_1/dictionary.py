# student = {
#     "name": "LiamPai",
#     "age": 21,
#     "score": 89,
#     "passed": True
# }

# print("Student Name: ", student["name"])
# print("Student Score: ", student["score"])

# update student information
# student = {
#     "name": "Eaint",
#     "score": 85
# }

# student["course"] = "Python"
# student["score"] = 90

# print(student.get("name"))
# print(student.get("grade", "Not Found"))
# print(student)

# list of dictionaries
students = [
    {"name": "LiamPai", "score": 85},
    {"name": "May", "score": 45},
    {"name": "Hmue", "score": 55}
]

print("Student List: ", students)
for student in students:
    print("Name: ", student["name"], ", Score: ", student["score"])

