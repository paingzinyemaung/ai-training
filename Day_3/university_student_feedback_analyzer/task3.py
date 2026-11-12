# task 3 - text representation
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv('student_feedback.csv')

data = df['feedback_text']

# CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data)

print(vectorizer.get_feature_names_out())
print(X.toarray())

# TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
X2 = tfidf_vectorizer.fit_transform(data)

print(tfidf_vectorizer.get_feature_names_out())
print(X2.toarray().round(3))
