# RAG-based Agentic AI Chatbot

## Overview
This project implements a Retrieval-Augmented Generation (RAG) chatbot that answers user queries strictly based on a provided knowledge source.

The knowledge base used is the **Agentic AI eBook (PDF)**.  
The chatbot retrieves relevant content from the document using vector similarity search and returns responses grounded only in the PDF.

---

## Tech Stack
- Python
- PyPDF
- Sentence-Transformers (all-MiniLM-L6-v2)
- FAISS (Vector Database)
- NumPy

---

## Architecture / Flow
1. Load and read the PDF file
2. Split text into fixed-size chunks
3. Generate embeddings for each chunk
4. Store embeddings in a FAISS vector index
5. Retrieve top relevant chunks based on user query
6. Display answers strictly from retrieved document context

---

## How to Run

### Step 1: Create chunks
```bash
python data/chunk_pdf.py
```

### Step 2: Build FAISS index
```bash
python data/embed_chunks.py
```

### Step 3: Ask questions
```bash
python data/src/qa_faiss.py
```

Type `exit` to quit the chatbot.

---

## Sample Queries
- What is Agentic AI?
- What are the key characteristics of agentic systems?
- How does Agentic AI differ from traditional AI?
- What are examples of agent-based workflows?

---

## Notes
- The chatbot answers strictly from the PDF content
- No external knowledge or hallucination is used
