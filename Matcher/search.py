import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

def find_matches(user_title, user_abstract, k=5):
    # Load data and index
    with open('data/abstracts.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    index = faiss.read_index('data/abstracts_index.faiss')
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    # Create embedding from user input
    query = model.encode([f"{user_title} {user_abstract}"], normalize_embeddings=True)

    # Search
    distances, indices = index.search(np.array(query), k)

    matches = []
    for i in range(k):
        match = data[indices[0][i]]
        match['score'] = float(distances[0][i])
        matches.append(match)

    return matches
