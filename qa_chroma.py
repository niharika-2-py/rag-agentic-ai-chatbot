from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read PDF
reader = PdfReader("data/Ebook-Agentic-AI.pdf")

all_text = ""
for page in reader.pages:
    if page.extract_text():
        all_text += page.extract_text() + "\n"

# Chunk text
chunk_size = 500
chunks = []
for i in range(0, len(all_text), chunk_size):
    chunks.append(all_text[i:i + chunk_size])

# Create embeddings
embeddings = model.encode(chunks).astype("float32")

# Setup ChromaDB
client = chromadb.Client()
collection = client.create_collection(name="agentic_ai")

collection.add(
    documents=chunks,
    embeddings=embeddings.tolist(),
    ids=[str(i) for i in range(len(chunks))]
)

print("Total chunks stored:", len(chunks))

# ---- QUESTION LOOP ----
while True:
    query = input("\nAsk a question (type 'exit' to quit): ")
    if query.lower() == "exit":
        break

    query_embedding = model.encode([query]).tolist()
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    print("\nAnswer context:\n")
    for doc in results["documents"][0]:
        print(doc)
        print("-" * 40)


