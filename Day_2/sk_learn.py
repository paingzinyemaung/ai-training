# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# import pandas as pd 

# import joblib

# df = pd.read_csv('data/student.csv')

# # split features and target
# X = df[['study_hours', 'attendance']]
# y = df['exam_score']

# X_train, X_test, y_train, y_test = train_test_split(X, y)

# print('Train set: ', len(X_train))
# print('Test set: ', len(X_test))

# model = LinearRegression()
# model.fit(X_train, y_train)

# print("Model training complete.")

# joblib.dump(model, "model/model.joblib")

# print("Model saved successfully.")


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import pandas as pd
import joblib

df = pd.read_csv('data/student.csv')

X = df[['study_hours', 'attendance']]
y = df['exam_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

print("Training records: ", len(X_train))
print("Testing records: ", len(X_test))

model = LinearRegression()

model.fit(X_train, y_train)

joblib.dump(model, 'model/model.joblib')

print("Model saved successfully")