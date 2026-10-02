# AI Financial Research & RAG Assistant

An AI-powered financial research assistant that uses Retrieval-Augmented Generation (RAG) to answer questions from Infosys annual reports.

Built with Python, LangChain, ChromaDB, Sentence Transformers, Groq LLMs, FastAPI, and Streamlit.

## Features

- Ask natural-language questions about Infosys annual reports
- Retrieval-Augmented Generation (RAG) pipeline
- Semantic search using Sentence Transformer embeddings
- Persistent ChromaDB vector database
- Cross-Encoder reranking for retrieved documents
- Query rewriting for improved retrieval
- Year-aware financial answer generation
- Source and page references in responses
- RAG evaluation using Answer Accuracy, Recall@3, and MRR@3
- FastAPI REST API for programmatic access
- Streamlit web interface for interactive research

## Architecture

```text
User Question
      ↓
Query Rewriting
      ↓
Sentence Transformer Embedding
      ↓
ChromaDB Semantic Retrieval
      ↓
Cross-Encoder Reranking
      ↓
Top Relevant Context
      ↓
Groq LLM
      ↓
Answer + Source References
```

## Tech Stack

- **Language:** Python
- **LLM:** Groq — `openai/gpt-oss-120b`
- **RAG Framework:** LangChain
- **Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`)
- **Vector Database:** ChromaDB
- **Reranking:** Cross-Encoder (`ms-marco-MiniLM-L-6-v2`)
- **API:** FastAPI
- **Frontend:** Streamlit
- **PDF Processing:** PyPDF
- **Environment & Package Management:** uv
- **Version Control:** Git & GitHub

## Project Structure

```text
ai_financial_research_rag_infosys/
│
├── app/
│   ├── api.py
│   └── streamlit_app.py
│
├── src/
│   ├── ingestion.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── reranker.py
│   └── rag.py
│
├── data/
│   └── raw/
│
├── tests/
│
├── notebooks/
│
├── .env
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

> **Note:** `.env` is used locally for API keys and should never contain a real API key in GitHub.

## How It Works

1. **Document Ingestion**  
   Infosys annual report PDFs are loaded and split into smaller chunks while preserving report year and page metadata.

2. **Embedding Generation**  
   Each document chunk is converted into a numerical vector using Sentence Transformers.

3. **Vector Storage**  
   The embeddings and document metadata are stored in a persistent ChromaDB collection.

4. **Query Rewriting**  
   The user's question is rewritten into a clearer financial research query before retrieval.

5. **Semantic Retrieval**  
   ChromaDB retrieves the most relevant document chunks based on semantic similarity.

6. **Reranking**  
   A Cross-Encoder reranks the retrieved chunks to improve the relevance of the final context.

7. **Answer Generation**  
   The Groq LLM generates an answer using only the retrieved context.

8. **Source References**  
   The application returns the relevant Infosys annual report and page numbers alongside the answer.

## Evaluation

The RAG pipeline was evaluated using financial question-answering test cases based on the Infosys annual reports.

| Metric | Result |
|---|---:|
| Answer Accuracy | 100% (5/5) |
| Recall@3 | 100% |
| MRR@3 | 53.33% |

The evaluation focused on retrieval quality and whether the generated answer corresponded to the correct financial year.

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/Sanketpatil0202/ai_financial_research_rag_infosys.git
cd ai_financial_research_rag_infosys
```

### 2. Create the environment

```bash
uv venv
```

### 3. Activate the environment on Windows

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
uv sync
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your real API key to GitHub.

### 6. Run the Streamlit application

```bash
uv run streamlit run app/streamlit_app.py
```

### 7. Run the FastAPI application

```bash
uv run uvicorn app.api:app --reload
```

The interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## API Usage

The project provides a FastAPI endpoint for querying the financial research assistant.

### Endpoint

```http
POST /ask
```

### Request

```json
{
  "question": "What was the consolidated revenue of Infosys in FY2024?"
}
```

### Response

```json
{
  "question": "What was the consolidated revenue of Infosys in FY2024?",
  "answer": "Infosys Ltd.’s consolidated revenue from operations for fiscal year 2024 was ₹1,53,670 crore.",
  "sources": [
    {
      "report": "2023-24",
      "page": 29
    },
    {
      "report": "2024-25",
      "page": 30
    },
    {
      "report": "2025-26",
      "page": 33
    }
  ]
}
```

## Git Workflow

The project uses Git for version control and GitHub for remote repository management.

Typical workflow:

```bash
git status
git add .
git commit -m "Describe the change"
git push origin main
```

- `git status` — Check modified and untracked files.
- `git add .` — Stage changes for the next commit.
- `git commit -m "..."` — Save a meaningful version of the changes.
- `git push origin main` — Upload commits to GitHub.

The project was developed using milestone-based commits so that major additions and improvements are tracked separately.

## Future Improvements

- Add hybrid search combining semantic and keyword retrieval
- Improve retrieval using metadata filtering by financial year
- Add automated evaluation with additional RAG metrics
- Add Docker support for easier deployment
- Deploy the Streamlit frontend and FastAPI backend
- Add authentication and request logging for production use

## Project Highlights

- Built an end-to-end RAG pipeline for financial research.
- Processed and indexed 4,742 document chunks from Infosys annual reports.
- Implemented semantic retrieval with Sentence Transformers and ChromaDB.
- Added Cross-Encoder reranking to improve retrieval relevance.
- Implemented query rewriting before document retrieval.
- Added year-aware prompting to reduce financial-year mismatches.
- Evaluated the system using Answer Accuracy, Recall@3, and MRR@3.
- Exposed the RAG pipeline through both Streamlit and FastAPI.
- Added persistent vector storage using ChromaDB.
- Managed development and version control using Git and GitHub.