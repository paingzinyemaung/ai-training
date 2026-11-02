import numpy as np 
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. load the dataset
df = pd.read_csv('data/students.csv')

# 2. select features and target
X = df[['study_hours', 'attendance']]
y = df['exam_score']

# 3. split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.25,
    random_state = 42
)

# 4. create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. save the trained model
joblib.dump(model, 'model/exam_model.joblib')

print('Model saved as exam_model.joblib')