import chromadb


client = chromadb.Client()


def create_collection(collection_name="infosys_financial_rag"):
    collection = client.get_or_create_collection(
        name=collection_name
    )

    return collection

def add_documents(collection, documents, vectors):
    ids = [f"chunk_{i}" for i in range(len(documents))]

    collection.add(
        ids=ids,
        documents=[doc.page_content for doc in documents],
        embeddings=vectors.tolist(),
        metadatas=[doc.metadata for doc in documents]
    )

def retrieve_documents(collection, embedding_model, question, k=5):
    query_vector = embedding_model.encode(question).tolist()

    result = collection.query(
        query_embeddings=[query_vector],
        n_results=k
    )

    retrieved = []

    for i in range(len(result["documents"][0])):
        retrieved.append({
            "text": result["documents"][0][i],
            "page_no": result["metadatas"][0][i]["page_no"],
            "source": result["metadatas"][0][i]["source"],
            "report": result["metadatas"][0][i]["report"],
            "distance": result["distances"][0][i]
        })

    return retrieved