from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
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
embeddings = model.encode(chunks)
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print("Total chunks stored:", index.ntotal)
