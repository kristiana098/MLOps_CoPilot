# 🐳 MLOps & Infrastructure Co-Pilot (RAG System)

An interactive, local Retrieval-Augmented Generation (RAG) assistant built to retrieve and synthesize technical documentation for infrastructure tools like Docker, Kubernetes, and GitHub Actions.

## 🚀 Project Overview
Building machine learning models is only half the battle; deploying and maintaining them requires deep infrastructure knowledge. I built this tool to bridge the gap between Data Science and MLOps. Instead of relying on generalized LLM knowledge, this Co-Pilot grounds its answers strictly in the official technical documentation I ingest into its local vector memory, preventing hallucinations and providing exact configuration commands.

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
   git clone [https://github.com/yourusername/MLOps_CoPilot.git](https://github.com/yourusername/MLOps_CoPilot.git)
   cd MLOps_CoPilot