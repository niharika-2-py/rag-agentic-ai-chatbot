# RAG-Based Agentic AI Chatbot

## Overview
This project implements a Retrieval-Augmented Generation (RAG) based AI chatbot using Python.
The chatbot answers questions strictly based on the Agentic AI eBook PDF.
No external data sources or no-code / low-code AI platforms are used.

This project was developed as part of an AI Engineer interview assignment.

---

## How the System Works
```text
1. Load the PDF document
2. Split text into smaller chunks
3. Convert chunks into embeddings
4. Store embeddings in FAISS
5. Retrieve relevant chunks for a query
6. Generate answer only from retrieved content
```

---

## Setup Instructions
```bash
git clone https://github.com/niharika-2-py/rag-agentic-ai-chatbot.git
cd rag-agentic-ai-chatbot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Running the Project

### Step 1: Create Text Chunks
```bash
python src/chunk_pdf.py
```

### Step 2: Generate Embeddings
```bash
python src/embed_chunks.py
```

### Step 3: Run Chatbot
```bash
python src/qa_faiss.py
```

---

## Example Questions
```text
What is Agentic AI?
How do AI agents differ from traditional AI systems?
What is autonomy in agentic systems?
What are applications of Agentic AI?
How do agents make decisions?
```

---

## Notes
```text
- The chatbot answers only from the PDF content.
- .pkl and .index files are binary artifacts.
- These files should not be opened manually.







