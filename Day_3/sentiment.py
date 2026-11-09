from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

texts = [
    'I love this product',
    'The service is excellent',
    'This is a wonderful experience',
    'I am very happy with the purchase',
    'The product is funtastic',
    'I really like the service',
    'I hate this product',
    'The service is terrible',
    'This is a bad experience',
    'I am very disappointed',
    'The product is awful',
    'I do not like this service'
]

labels = [
    'Positive',
    'Positive',
    'Positive',
    'Positive',
    'Positive',
    'Positive',
    'Negative',
    'Negative',
    'Negative',
    'Negative',
    'Negative',
    'Negative',
]

X_train, X_test, y_train, y_test = train_test_split(
    texts,
    labels,
    test_size = 0.25,
    random_state = 0,
    stratify = labels
)

model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(y_test)

print(predictions)

print("Accuracy: ", accuracy_score(y_test, predictions))

print(classification_report(y_test, predictions, zero_division = 0))

new_reviews = [
    'I love the excellent service',
    'This product is terrible'
]

print(model.predict(new_reviews))

# predicting new text
while True:
    review = input("Enter a review (or type exit): ")

    if review.lower() == 'exit':
        break

    prediction = model.predict([review])[0]

    print("Printed sentiment: ", prediction)