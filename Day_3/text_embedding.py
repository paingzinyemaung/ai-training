import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

embedding_1 = np.array([[0.8, 0.2, 0.5]])
embedding_2 = np.array([[0.7, 0.3, 0.6]])

score = cosine_similarity(embedding_1, embedding_2)

print(round(score[0][0], 3))