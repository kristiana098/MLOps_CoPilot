import chromadb

# 1. Create a local folder called 'vector_store' to hold the database
client = chromadb.PersistentClient(path="./vector_store")

# 2. Create a collection (like a table) for our documentation
collection = client.get_or_create_collection(name="mlops_docs")

# 3. Add a single test document to ensure it works
collection.upsert(
    documents=["Docker uses a Dockerfile to build container images."],
    ids=["test_doc_1"]
)

print("Database initialized!")
print(f"Total documents stored: {collection.count()}")

# 4. Search the database to see retrieval in action
results = collection.query(
    query_texts=["How do I build an image?"],
    n_results=1
)

print("\nSearch Results:")
print(results["documents"])