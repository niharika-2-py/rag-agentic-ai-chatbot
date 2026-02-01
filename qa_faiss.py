from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import pickle

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load chunks
with open("data/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# Load FAISS index
index = faiss.read_index("data/faiss.index")

print("FAISS index ready with", index.ntotal, "chunks")

# Ask questions
while True:
    query = input("\nAsk a question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    query_embedding = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, 3)

    print("\nAnswer from PDF:\n")
    for i in indices[0]:
        print(chunks[i][:400])
        print("-" * 40)
