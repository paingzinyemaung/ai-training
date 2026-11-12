import pandas as pd 
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the pretrained sentence embedding model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

df = pd.read_csv('student_feedback.csv')

data = df['feedback_text'].iloc[:5].tolist() # five sentences

# print(data)

embeddings = model.encode(data)

print(embeddings)

score = cosine_similarity([embeddings[0]],[embeddings[1]])

print(score)



