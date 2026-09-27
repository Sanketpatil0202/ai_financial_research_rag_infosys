from sentence_transformers import CrossEncoder


reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank_documents(question, documents):
    pairs = [(question, item["text"]) for item in documents]

    scores = reranker.predict(pairs)

    reranked = []

    for item, score in zip(documents, scores):
        reranked.append({
            "text": item["text"],
            "page_no": item["page_no"],
            "source": item["source"],
            "report": item["report"],
            "distance": item["distance"],
            "rerank_score": float(score)
        })

    reranked = sorted(
        reranked,
        key=lambda x: x["rerank_score"],
        reverse=True
    )

    return reranked