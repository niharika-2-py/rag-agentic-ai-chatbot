# RAG-based AI Chatbot (Agentic AI eBook)

## 📌 Project Overview

This project is a **Retrieval-Augmented Generation (RAG) based AI Chatbot** built in **Python** as part of an AI Engineer interview assignment. The chatbot answers user questions **strictly based on the Agentic AI eBook** provided as the knowledge source.

📘 Knowledge Base: *Agentic AI eBook*
🔗 [https://konverge.ai/pdf/Ebook-Agentic-AI.pdf](https://konverge.ai/pdf/Ebook-Agentic-AI.pdf)

The system retrieves the most relevant content from the eBook and generates grounded answers using an LLM. The chatbot does **not hallucinate** and responds only when relevant information is found in the PDF.

---

## 🏗️ System Architecture (How It Works)

The chatbot follows a standard **RAG (Retrieval-Augmented Generation)** pipeline:

1. **PDF Ingestion**
   The Agentic AI eBook is loaded into the system.

2. **Text Chunking**
   The PDF text is split into smaller chunks to improve retrieval accuracy.

3. **Embedding Generation**
   Each chunk is converted into vector embeddings using a text embedding model.

4. **Vector Storage**
   All embeddings are stored in a Vector Database (Pinecone / local vector store).

5. **Retrieval (LangGraph)**
   When a question is asked, LangGraph retrieves the most relevant chunks based on similarity.

6. **Answer Generation**
   The LLM generates a final answer using **only the retrieved chunks**.
   
---

## 🛠️ Tech Stack Used

* **Python**
* **LangGraph** – RAG workflow orchestration
* **Vector Database** – Pinecone / Local Vector Store
* **Text Embeddings** – For semantic search
* **LLM** – For grounded response generation
* **GitHub** – Code hosting

---


## ▶️ How to Run the Chatbot

### Step 1: Clone the Repository

```bash
git clone <your-github-repo-link>
cd <repo-folder>
```

### Step 2: Create Virtual Environment

```bash
python -m venv rag-env
rag-env\Scripts\activate   # Windows
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Ingest PDF & Create Chunks

```bash
python data/chunk_pdf.py
```

### Step 5: Run the Chatbot

```bash
python src/chatbot.py
```
---

## 💬 Sample Queries

1. What is Agentic AI?
2. How do AI agents make decisions?
3. What are the components of an AI agent?
4. How is Agentic AI different from traditional AI systems?
5. What role do tools play in Agentic AI?
6. Explain autonomy in Agentic AI

---

## 🔐 Grounding & Safety

* The chatbot **only answers** if relevant context is found.
* If no matching content exists in the PDF, the chatbot responds accordingly.
* This ensures **zero hallucination**.

---

## 🎯 Key Design Decisions

* **Chunking** improves retrieval accuracy
* **Vector search** enables semantic similarity matching
* **LangGraph** ensures structured RAG flow
* **Binary storage (chunks.pkl)** improves performance

---

## 📌 Conclusion

This project demonstrates a complete end-to-end RAG-based chatbot implementation using Python and LangGraph. The system is modular, explainable, and strictly grounded in the provided knowledge source, fulfilling all assignment requirements.

---


