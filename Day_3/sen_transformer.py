from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

sentences = [
 "I want to buy a computer.",
 "I would like to purchase a laptop.",
 "The weather is sunny today."
]

embeddings = model.encode(sentences)

print("Embedding shape:", embeddings.shape)

print(embeddings)
