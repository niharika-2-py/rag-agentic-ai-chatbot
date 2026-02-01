from pypdf import PdfReader

reader = PdfReader("data/Ebook-Agentic-AI.pdf")

print("Total pages:", len(reader.pages))

text = reader.pages[0].extract_text()
print(text)
