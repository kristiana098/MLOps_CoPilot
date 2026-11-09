import os
import streamlit as st
import chromadb
from groq import Groq
from dotenv import load_dotenv

# 1. Initialize API and Database connections
load_dotenv()
llm_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
chroma_client = chromadb.PersistentClient(path="./vector_store")
collection = chroma_client.get_or_create_collection(name="mlops_docs")

# 2. Configure the Streamlit Interface
st.set_page_config(page_title="MLOps Co-Pilot", page_icon="🐳")
st.title("🐳 MLOps Co-Pilot")
st.caption("Your RAG-powered infrastructure assistant.")

# --- NEW: Sidebar with Live Counter ---
with st.sidebar:
    st.header("📚 Knowledge Base")
    
    # 1. Live Document Counter
    doc_count = collection.count()
    st.metric(label="🧠 Chunks in Memory", value=doc_count)
    
    st.divider()
    
    st.write("Upload `.txt` documentation to expand my memory.")
    uploaded_file = st.file_uploader("Choose a file", type=["txt"])
    
    if uploaded_file is not None:
        if st.button("Process & Save to Database"):
            content = uploaded_file.read().decode("utf-8")
            chunks = [chunk.strip() for chunk in content.split("\n\n") if chunk.strip()]
            
            if chunks:
                ids = [f"{uploaded_file.name}_chunk_{i}" for i in range(len(chunks))]
                collection.upsert(documents=chunks, ids=ids)
                st.success(f"✅ Successfully memorized {len(chunks)} chunks!")
                # Force app to refresh so the counter updates instantly
                st.rerun() 
    
    st.divider()
    
    st.header("⚠️ Danger Zone")
    if st.button("🗑️ Clear Database"):
        chroma_client.delete_collection(name="mlops_docs")
        collection = chroma_client.get_or_create_collection(name="mlops_docs")
        st.success("Database wiped clean!")
        # Force app to refresh so the counter drops to 0 instantly
        st.rerun()


# 3. Setup Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 4. Handle New User Input
if user_question := st.chat_input("Ask a question about your infrastructure..."):
    
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    # Retrieve context from ChromaDB
    results = collection.query(query_texts=[user_question], n_results=1)
    
    if results["documents"] and results["documents"][0]:
        retrieved_info = results["documents"][0][0]
    else:
        retrieved_info = "No relevant context found in database."

    # Generate answer with Groq
    prompt = f"""
    You are an MLOps assistant. Answer the user's question using ONLY the provided context.
    If the context doesn't contain the answer, say "I don't have that in my documentation."
    
    Context: {retrieved_info}
    
    Question: {user_question}
    """

    with st.chat_message("assistant"):
        response = llm_client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="openai/gpt-oss-20b"
        )
        answer = response.choices[0].message.content
        
        st.markdown(answer)
        st.caption(f"🔍 **Retrieved from database:** {retrieved_info}")
        
    # Save assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": answer})