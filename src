from pypdf import PdfReader
import pickle

pdf_path = "data/Ebook-Agentic-AI.pdf"

reader = PdfReader(pdf_path)

all_text = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        all_text += text + "\n"

chunk_size = 500
chunks = []

for i in range(0, len(all_text), chunk_size):
    chunks.append(all_text[i:i + chunk_size])

with open("data/chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("Chunks created:", len(chunks))


