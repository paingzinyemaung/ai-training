from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    'AI improves learning',
    'AI improves business'
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())
print(X.toarray().round(3))