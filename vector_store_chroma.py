from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read PDF
reader = PdfReader("data/Ebook-Agentic-AI.pdf")

all_text = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        all_text += text + "\n"

# Chunk text
chunk_size = 500
chunks = []

for i in range(0, len(all_text), chunk_size):
    chunks.append(all_text[i:i + chunk_size])

# Create embeddings
embeddings = model.encode(chunks)

# Create Chroma collection
client = chromadb.Client()
collection = client.create_collection(name="agentic_ai")

# Store chunks
for i, chunk in enumerate(chunks):
    collection.add(
        documents=[chunk],
        embeddings=[embeddings[i].tolist()],
        ids=[str(i)]
    )

print("Total chunks stored:", collection.count())
