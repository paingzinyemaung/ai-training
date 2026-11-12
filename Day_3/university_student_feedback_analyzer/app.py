# ============================================================
# AI-Powered University Student Feedback Analyzer
# ============================================================

# -------------------- Required libraries --------------------

import re
import pandas as pd
import gradio as gr

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics.pairwise import cosine_similarity

from sentence_transformers import SentenceTransformer


# -------------------- Task 1: Dataset preparation --------------------

# Read the CSV file.
# Keep student_feedback.csv in the same folder as this app.py file.

df = pd.read_csv("student_feedback.csv")

# Show the first five feedback records.
print("STUDENT FEEDBACK DATASET")
print(df.head())

# Show how many feedback messages are in the dataset.
print("\nTotal feedback messages:", len(df))


# -------------------- Task 2: Text preprocessing --------------------

# Select one feedback message to demonstrate preprocessing.
# The original feedback_text in the CSV is not changed.

text = df["feedback_text"][0]

print("\nTASK 2: TEXT PREPROCESSING")
print("Original text:")
print(text)

# Step 1: Convert text to lowercase.
text = text.lower()

# Step 2: Remove punctuation.
# This follows the re.sub() example in the lecture.
text = re.sub(r"[^\w\s]", "", text)

# Step 3: Remove extra spaces.
# \s+ means one or more whitespace characters.
text = re.sub(r"\s+", " ", text).strip()

print("\nProcessed text:")
print(text)

# Step 4: Tokenization.
# split() separates the sentence into words.
tokens = text.split()

print("\nTokens:")
print(tokens)

# Step 5: Stop-word removal.
# These are the same example stop words used in the lecture.
stop_words = {"the", "is", "and"}

filtered_tokens = [
    word for word in tokens if word not in stop_words
]

print("\nTokens after stop-word removal:")
print(filtered_tokens)


# -------------------- Task 3: Text representation --------------------

# Use the feedback messages from the CSV as documents.
documents = df["feedback_text"].tolist()


# Part A: Bag of Words (CountVectorizer)

print("\nTASK 3A: BAG OF WORDS")

# CountVectorizer learns the vocabulary and counts each word.
bow_vectorizer = CountVectorizer()

# fit_transform() learns the vocabulary and converts documents to numbers.
bow_features = bow_vectorizer.fit_transform(documents)

print("\nBag of Words vocabulary:")
print(bow_vectorizer.get_feature_names_out())

print("\nBag of Words numerical features (first 5 feedback messages):")
print(bow_features.toarray()[:5])


# Part B: TF-IDF (TfidfVectorizer)

print("\nTASK 3B: TF-IDF")

# TfidfVectorizer converts documents into TF-IDF numerical features.
tfidf_vectorizer = TfidfVectorizer()

tfidf_features = tfidf_vectorizer.fit_transform(documents)

print("\nTF-IDF vocabulary:")
print(tfidf_vectorizer.get_feature_names_out())

print("\nTF-IDF numerical features (first 5 feedback messages):")
print(tfidf_features.toarray()[:5].round(3))


# -------------------- Task 4: Text embeddings --------------------

print("\nTASK 4: TEXT EMBEDDINGS")

# Select five feedback messages from the dataset.
sentences = documents[:5]

# Load the pretrained sentence embedding model from the lecture.
embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# Convert the five sentences into numerical vectors.
embeddings = embedding_model.encode(sentences)

print("\nNumber of feedback messages:", len(sentences))
print("Embedding shape:", embeddings.shape)

# Calculate cosine similarity between the first two messages.
similarity = cosine_similarity(
    [embeddings[0]],
    [embeddings[1]]
)

print("\nMessage 1:")
print(sentences[0])

print("\nMessage 2:")
print(sentences[1])

print("\nCosine similarity:")
print(round(similarity[0][0], 3))


# -------------------- Task 5: Build the classification model --------------------

print("\nTASK 5: SENTIMENT CLASSIFICATION")

# X contains the feedback text.
# y contains the correct sentiment labels.
X = df["feedback_text"]
y = df["sentiment"]

# Split the dataset into training data and testing data.
# 25% is used for testing and 75% for training.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=0,
    stratify=y
)

# Create a Pipeline.
# First, TF-IDF converts text into numerical features.
# Second, MultinomialNB learns to classify the sentiment.
sentiment_model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# Train the model using the training data.
sentiment_model.fit(X_train, y_train)

# Predict the sentiment of the testing data.
predictions = sentiment_model.predict(X_test)

# Evaluate the model.
print("\nSentiment accuracy:")
print(accuracy_score(y_test, predictions))

print("\nSentiment classification report:")
print(classification_report(y_test, predictions, zero_division=0))


# The assignment also asks the interface to show a category.
# Therefore, train a second model to predict the feedback category.

print("\nCATEGORY CLASSIFICATION")

X_category = df["feedback_text"]
y_category = df["category"]

X_train_category, X_test_category, y_train_category, y_test_category = train_test_split(
    X_category,
    y_category,
    test_size=0.25,
    random_state=0,
    stratify=y_category
)

category_model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

category_model.fit(X_train_category, y_train_category)

category_predictions = category_model.predict(X_test_category)

print("\nCategory accuracy:")
print(accuracy_score(y_test_category, category_predictions))

print("\nCategory classification report:")
print(classification_report(
    y_test_category,
    category_predictions,
    zero_division=0
))


# -------------------- Task 6: Gradio application interface --------------------

print("\nTASK 6: GRADIO INTERFACE")


# This function receives the feedback typed by the user in Gradio.
def analyze_feedback(feedback):

    # Check whether the user entered any text.
    if feedback.strip() == "":
        return "Please enter student feedback.", "", ""

    # Predict the sentiment.
    predicted_sentiment = sentiment_model.predict([feedback])[0]

    # Predict the feedback category.
    predicted_category = category_model.predict([feedback])[0]

    # Process the input text for the summary.
    processed_text = feedback.lower()
    processed_text = re.sub(r"[^\w\s]", "", processed_text)
    processed_text = re.sub(r"\s+", " ", processed_text).strip()

    # Split the processed text into tokens.
    tokens = processed_text.split()

    # Remove the example stop words from the lecture.
    filtered_tokens = [
        word for word in tokens if word not in stop_words
    ]

    # Prepare the text summary to show in Gradio.
    summary = (
        "Original feedback:\n"
        + feedback
        + "\n\nProcessed text:\n"
        + processed_text
        + "\n\nTokens:\n"
        + str(tokens)
        + "\n\nAfter stop-word removal:\n"
        + str(filtered_tokens)
    )

    return predicted_sentiment, predicted_category, summary


# Create the Gradio interface.
interface = gr.Interface(
    fn=analyze_feedback,

    inputs=gr.Textbox(
        lines=5,
        label="Enter student feedback"
    ),

    outputs=[
        gr.Textbox(label="Predicted sentiment"),
        gr.Textbox(label="Predicted category"),
        gr.Textbox(label="Processed text summary", lines=10)
    ],

    title="AI-Powered University Student Feedback Analyzer",

    description=(
        "Enter a student feedback message. "
        "The application predicts its sentiment and category "
        "and displays the text preprocessing results."
    )
)


# Start the Gradio application.
interface.launch()
