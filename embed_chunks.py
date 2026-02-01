from sentence_transformers import SentenceTransformer
import pickle
import numpy as np
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

embeddings = model.encode(chunks)
embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

faiss.write_index(index, "data/faiss.index")

print("FAISS index created with", index.ntotal, "vectors")

