import pandas as pd
import re

# task 1 - dataset preparation
# load dataset
df = pd.read_csv("student_feedback.csv")

# task 2 - text preprocessing
data = df['feedback_text']

for text in data:
    text = text.lower() # 1. convert to lowercase
    text = re.sub(r"[^\w\s]", "", text) # 2. puncuation
    text = re.sub(r"\s+", " ", text).strip() # remove extra whitespace
    text = text.split() # 3. tokenization

    stop_words = {'a', 'an', 'the', 'is', 'on', 'and', 'at', 'are', 'for', 'has', 'have', 'in', 'to', 'of','me'}

    filtered = [word for word in text if word not in stop_words] # stop-words removal
    print(filtered)

