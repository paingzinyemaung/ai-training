import pandas as pd

data = {
 "study_hours": [2, 4, 6, 3, 7],
 "attendance": [60, 75, 90, 65, 95],
 "exam_score": [45, 65, 85, 55, 92]
}

df = pd.DataFrame(data)

print(df)

# explore dataset
print(df.head())
print("Shape")
print(df.shape)
print("Columns")
print(df.columns)
print("Info")
print(df.info())
print("Describe")
print(df.describe())

# split feature and label(target)
X = df[["study_hours", "attendance"]]
y = df["exam_score"]

print("Features: ")
print(X)

print("Target: ")
print(y)