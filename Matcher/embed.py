import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

def main():
    print("🔍 Loading model...")
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    print("📦 Loading abstracts...")
    with open('data/abstracts.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("🔢 Generating embeddings...")
    texts = [item['abstract_content'] for item in data]
    embeddings = model.encode(texts, normalize_embeddings=True)

    print("📥 Saving FAISS index...")
    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(np.array(embeddings))
    faiss.write_index(index, 'data/abstracts_index.faiss')

    print("✅ Index saved. Ready for matching!")

if __name__ == "__main__":
    main()
