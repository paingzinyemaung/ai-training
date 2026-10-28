import pandas as pd 

df = pd.DataFrame({
    "study_hours": [2, 4, None, 6],
    "attendance": [60, 75, 80, None],
    "exam_score": [45, 65, 72, 85]
})

print("Missing values:")
print(df.isnull().sum())

df["study_hours"] = df["study_hours"].fillna(
    df["study_hours"].median()
)

df["attendance"] = df["attendance"].fillna(
    df["attendance"].median()
)

print(df)
