# 📄 AI Smart Document Assistant

A backend-focused AI application that allows users to upload PDF documents and ask questions based on their content.
The system uses a Retrieval-Augmented Generation (RAG) approach to fetch relevant information from the document and will later generate answers with proper source references.

## 🚀 Project Overview

This project is designed to simulate how modern AI systems like ChatGPT work on private documents.

Instead of relying on external knowledge, the system:

Reads your PDF
Breaks it into smaller chunks
Converts them into embeddings
Stores them in a vector database
Retrieves the most relevant content when a question is asked

The goal is to build everything step by step, focusing mainly on backend clarity rather than using frameworks as a black box.

## 🧠 Current Features

- 📥 Upload PDF files
- 📄 Extract text page by page
- ✂️ Split content into chunks with overlap
- 🔢 Generate embeddings using Ollama
- 🗄️ Store vectors in Qdrant with metadata
- 🔍 Retrieve top-k relevant chunks based on user query
- 📍 Includes page number and chunk-level details in results

## 🏗️ Tech Stack
### Backend: FastAPI
LLM / Embeddings: Ollama (local models)
Vector Database: Qdrant
PDF Processing: PyMuPDF
Frontend: Basic HTML (for testing)
⚙️ How It Works
### 1. Document Ingestion
Upload a PDF
Extract text page by page
Split into chunks (with overlap)
Generate embeddings
Store in Qdrant
### 2. Retrieval Pipeline
User asks a question
Convert question into embedding
Perform similarity search in Qdrant
Return top matching chunks with metadata

## 📂 Project Structure
```
ai-smart-doc-assistant/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── routes/
│   │   ├── upload.py
│   │   └── query.py
│   ├── services/
│   │   ├── pdf_service.py
│   │   ├── chunk_service.py
│   │   ├── embedding_service.py
│   │   ├── qdrant_service.py
│   │   └── retrieval_service.py
│   └── models/
│       └── schemas.py
│
├── data/uploads/
├── requirements.txt
└── .env
```

## ▶️ How to Run

##### 1. Clone the repository
```
git clone https://github.com/your-username/ai-smart-doc-assistant.git
cd ai-smart-doc-assistant
```
##### 2. Create virtual environment
```
python -m venv venv
venv\Scripts\activate   # Windows
```
##### 3. Install dependencies
```
pip install -r requirements.txt
```
##### 4. Start Ollama
```
ollama serve
```
###### Pull embedding model:
```
ollama pull nomic-embed-text
```
##### 5. Start Qdrant (Docker)
```
docker run -p 6333:6333 qdrant/qdrant
```
##### 6. Run FastAPI server
```
uvicorn app.main:app --reload
```
Open:
```
http://127.0.0.1:8000/docs
```
## 🧪 API Endpoints
Upload PDF
POST /upload/
Query Document
POST /query/

#### Example request:
{
  "question": "What is this document about?",
  "top_k": 3
}

## 📌 Future Improvements
💬 Answer generation using Ollama (LLM)
📚 Source-aware responses (page/chunk references)
⚡ Streaming responses
🧠 Chat memory
📂 Multi-document support
🐳 Docker & deployment
🎯 Learning Focus

This project is built with a strong focus on understanding:

How RAG systems work internally
How embeddings and vector search operate
How retrieval and generation are connected
Avoiding heavy abstraction frameworks

## 🙌 Author
Manoj Chandru P M

## ⭐ Note
This project is being developed step by step as part of an internship learning process, focusing on backend architecture and real-world AI system design.
