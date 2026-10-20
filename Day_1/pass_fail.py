scores = [45, 70, 85, 30, 90, 55]

total = 0

for score in scores:
    total += score

average = total / len(scores)

print(f"Total Score: {total}")
print(f"Average Score: {average}")

# number of passing scroes and failing scores | 40 or above is pass
passing = 0
failing = 0

for score in scores:
    if score >= 40:
        passing += 1
    else:
        failing += 1

print(f"Passing Scores: {passing}")
print(f"Failing Scores: {failing}")
