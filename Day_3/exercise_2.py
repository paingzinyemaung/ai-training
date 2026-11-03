from sklearn.feature_extraction.text import CountVectorizer

documents = [
    'Python is easy',
    'Python is powerful',
    'AI is powerful'
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())
print(X.toarray())