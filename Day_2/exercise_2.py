import pandas as pd 

df = pd.read_csv("data/next_student.csv")

# top 5 rows
print(df.head())

# dataset dimensions (rows, columns)
print(df.shape)

# check for missing values
print(df.isnull().sum())

X = df[['study_hours', 'attendance', 'previous_score']]
y = df['exam_score']

print(X.head())
print(y.head())

