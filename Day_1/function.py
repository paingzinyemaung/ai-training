# parameterless
# def greet():
#     print("Welcome from Myanmar!")

# greet()

# function with parameter
# def greet_student(name):
#     print(f"Hello, I'm {name}!")

# greet_student("LiamPai")
# greet_student("MoMo")

# function with return value
# def calculate_average(scores):
#     if len(scores) == 0:
#         return 0
#     return sum(scores) / len(scores)

# print(calculate_average([70, 80, 90]))

# rule-based classification
# def classifiy_score(score):
#     if score < 0 or score > 100:
#         return "Invalid"
#     elif score >= 80:
#         return "Excellent"
#     elif score >= 60:
#         return "Good"
#     elif score >= 40:
#         return "Pass"
#     else:
#         return "Fail"

# print(classifiy_score(35))
# print(classifiy_score(85))
# print(classifiy_score(50))

# functions
# def calculate_total(scores):
#     total = 0
#     for score in scores:
#         total += score
#     return total

# print("Total: ", calculate_total([10, 20, 30]))
# print("Total: ", calculate_total([5, 15, 25, 35]))

# def calculate_average(scores):
#     if len(scores) == 0:
#         return 0
#     return sum(scores) / len(scores)

# print("Average: ", calculate_average([10, 20, 30]))
# print("Average: ", calculate_average([5, 15, 25, 35]))

# def classify_grade(score):
#     if score < 0 or score > 100:
#         return "Invalid score. Please enter a score between 0 and 100."
#     elif score >= 80:
#         return "Excellent"
#     elif score >= 60:
#         return "Good"
#     elif score >= 40:
#         return "Pass"
#     else:
#         return "Fail"

# print("Grade: ", classify_grade(47))
# print("Grade: ", classify_grade(32))

def count_passed(scores):
    passing = 0
    for score in scores:
        if score >= 40:
            passing += 1
    return passing

print("Passed: ", count_passed([45, 70, 85, 30, 90, 55]))
