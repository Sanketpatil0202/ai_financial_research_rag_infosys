from sentence_transformers import SentenceTransformer


embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(documents):
    texts = [doc.page_content for doc in documents]

    vectors = embedding_model.encode(texts)

    return vectors