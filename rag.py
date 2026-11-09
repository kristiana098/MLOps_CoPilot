import os
import chromadb
from groq import Groq
from dotenv import load_dotenv

# 1. Load your Groq API key securely
load_dotenv()
llm_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 2. Connect to the local database we just built
chroma_client = chromadb.PersistentClient(path="./vector_store")
collection = chroma_client.get_collection(name="mlops_docs")

# 3. Define the question
user_question = "How do I build an image?"

# 4. Retrieval: Get the relevant document from ChromaDB
results = collection.query(query_texts=[user_question], n_results=1)
retrieved_info = results["documents"][0][0]
print(f"--- Found in Database: {retrieved_info} ---\n")

# 5. Generation: Force the LLM to use ONLY the retrieved info
prompt = f"""
You are an MLOps assistant. Answer the user's question using ONLY the provided context.

Context: {retrieved_info}

Question: {user_question}
"""

response = llm_client.chat.completions.create(
    messages=[{"role": "user", "content": prompt}],
    model="openai/gpt-oss-20b" # Swapped to the fast GPT-OSS model
)

print("🤖 AI Response:")
print(response.choices[0].message.content)