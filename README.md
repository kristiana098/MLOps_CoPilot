# 🐳 MLOps & Infrastructure Co-Pilot (RAG System)

An interactive, local Retrieval-Augmented Generation (RAG) assistant built to retrieve and synthesize technical documentation for infrastructure tools like Docker, Kubernetes, and GitHub Actions.

## 🚀 Project Overview
This is a mini project created to test how a chat application can answer specific questions using a local Retrieval-Augmented Generation (RAG) system. I built this to experiment with vector databases, embedding models, and Streamlit, creating a custom chat interface that answers questions based purely on the text files uploaded to its memory.

### Key Features
* **Local Vector Storage:** Uses ChromaDB to store and retrieve document embeddings entirely locally.
* **Dynamic Ingestion:** A sidebar UI that allows users to upload `.txt` files, which are automatically chunked and indexed into the vector database in real-time.
* **Strict Semantic Retrieval:** Leverages the Groq API (`openai/gpt-oss-20b`) to answer complex infrastructure queries using *only* the retrieved context.
* **Interactive UI:** Built a clean, session-state chat interface using Streamlit.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Vector Database:** ChromaDB (Local SQLite-based)
* **LLM / Inference:** Groq API (GPT-OSS-20b)
* **Embeddings:** Sentence-Transformers (`all-MiniLM-L6-v2`)
* **Frontend:** Streamlit

## 💻 Local Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/MLOps_CoPilot.git](https://github.com/kristiana098/MLOps_CoPilot.git)
   cd MLOps_CoPilot