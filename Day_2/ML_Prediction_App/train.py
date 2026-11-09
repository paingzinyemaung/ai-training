import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load the dataset
df = pd.read_csv('data/winequality-white.csv', sep=';')

# # identify missing values
# cols = [
#  'fixed acidity', 'volatile acidity'
# ]

# for col in cols:
#     df[col] = df[col].fillna(df[col].median())

# prepare features and target
X = df[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']]
# X = df.drop(columns=['quality']).values
y = df['quality']

# split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42
)

# train the model
model = LinearRegression()
model.fit(X_train, y_train)

# saved the model
joblib.dump(model, 'model/wine_model.joblib')
print("Wine quality model saved successfully!")