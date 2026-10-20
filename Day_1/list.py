# student_scores = [70, 85, 90, 65, 78]

# print("Student Scores: ", student_scores)
# print("First Student Score: ", student_scores[0])
# print("Third Student Score: ", student_scores[2])

# scores = [70, 85, 90]

# scores.append(95)
# print(scores)

# scores[0] = 75
# print(scores)

# scores.remove(85)
# print(scores)

# print("Count: ", len(scores))
# print("Highest: ", max(scores))
# print("Lowest: ", min(scores))

# scores = [55, 80, 35, 90, 65]

# for score in scores:
#     if score >= 80:
#         print(score)

scores = [55, 80, 35, 90, 65]

scores.append(75)
scores[1] = 85

print(scores)
print(max(scores))
print(min(scores))

def average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)
print(average(scores))

for score in scores:
    if score >= 80:
        print(score)
