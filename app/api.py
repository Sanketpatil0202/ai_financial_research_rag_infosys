from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel
from src.rag import final_response
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
    response = final_response(request.question)

    return {
        "question": request.question,
        "response": response
    }