import numpy as np

scores = np.array([45, 60, 72, 88, 95, 67])

print(scores)
print("Shape:", scores.shape)

print("Mean:", np.mean(scores))
print("Median:", np.median(scores))

print("Highest:", np.max(scores))
print("Lowest:", np.min(scores))

add_5_bonus = scores + 5

print("Add 5 bonus:", add_5_bonus)

# study hours and attendance for three students
students_data = np.array([
    [5, 80],
    [7, 85],
    [6, 90]
])