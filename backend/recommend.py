# recommend.py
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load catalog
df = pd.read_csv("catalog.csv")
texts = df['name'].tolist()

# Embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(texts, convert_to_tensor=True)

def recommend_assessments(query, top_k=10):
    query_emb = model.encode([query], convert_to_tensor=True)
    similarities = cosine_similarity(query_emb, embeddings)[0]
    top_idx = np.argsort(similarities)[::-1][:top_k]
    recommendations = []
    for idx in top_idx:
        recommendations.append({
            "name": df.iloc[idx]['name'],
            "url": df.iloc[idx]['url'],
            "category": df.iloc[idx]['category'],
            "test_type": df.iloc[idx]['test_type']
        })
    return recommendations

# Test standalone
if __name__ == "__main__":
    query = "Hiring a Python developer with analytical skills"
    recs = recommend_assessments(query, top_k=5)
    for r in recs:
        print(r)
