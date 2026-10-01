from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel
from src.rag import final_response
from src.rag import rag_answer


app = FastAPI(
    title="AI Financial Research API",
    description="API for querying Infosys annual reports",
    version="1.0.0"
)



from pydantic import BaseModel, Field,field_validator


class QuestionRequest(BaseModel):
    question: str = Field(..., min_length=1)

    @field_validator("question")
    @classmethod
    def validate_question(cls, value):
        if not value.strip():
            raise ValueError("Question cannot be empty")
        return value.strip() 

@app.post("/ask")
def ask_question(request: QuestionRequest):
    answer, sources = rag_answer(request.question)

    formatted_sources = [
        {
            "report": source["report"],
            "page": source["page_no"]
        }
        for source in sources[:3]
    ]

    return {
        "question": request.question,
        "answer": answer,
        "sources": formatted_sources
    }