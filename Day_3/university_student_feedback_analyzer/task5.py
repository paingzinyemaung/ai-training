import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

df = pd.read_csv('student_feedback.csv')
X = df['feedback_text']
y = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
# print(X_test)

model = Pipeline(
    [
        ('tfidf', TfidfVectorizer()),
        ('classifier', MultinomialNB())
    ]

)

model.fit(X_train, y_train)

joblib.dump(model, 'model/sentiment_model.joblib')

print("Model Saved Successfully!")