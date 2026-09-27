from src.reranker import rerank_documents
from src.vectorstore import retrieve_documents, create_collection
from src.embeddings import embedding_model

from langchain_groq import ChatGroq

collection = create_collection()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

def build_context(results):
    context = "\n\n---\n\n".join(
        f"Report: {item['report']}\n"
        f"Page: {item['page_no']}\n"
        f"Content: {item['text']}"
        for item in results[:3]
    )

    return context

def create_prompt(question, context):
    return f"""
You are a financial research assistant.

Answer the user's question using ONLY the provided context.

IMPORTANT:
- Pay close attention to the financial year requested in the question.
- Financial tables may contain values for multiple years.
- Match the answer to the EXACT year requested by the user.
- Do not use a value from another year.
- If multiple years are present, identify the correct year before answering.
- If the requested year's value cannot be determined from the context, say:
"I don't know based on the provided documents."

Do not use outside knowledge.
Do not make up information.
Do not mention sources, page numbers, citations, or references in your answer.

Question:
{question}

Context:
{context}
"""

def generate_answer(question, context):
    prompt = create_prompt(question, context)
    response = llm.invoke(prompt)
    return response.content


def rag_answer(question):
    results = retrieve_documents(collection, embedding_model, question)
    reranked = rerank_documents(question, results)
    context = build_context(reranked)
    answer = generate_answer(question, context)

    return answer, reranked

def format_sources(sources):
    formatted = ["Sources:"]

    for source in sources[:3]:
        formatted.append(
            f"- Infosys Annual Report {source['report']} | Page {source['page_no']}"
        )

    return "\n".join(formatted)

def final_response(question):
    answer, sources = rag_answer(question)
    source_text = format_sources(sources)

    return f"{answer}\n\n{source_text}"