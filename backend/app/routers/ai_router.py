from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.services.langgraph_agent import graph


router = APIRouter(
    prefix="/ai",
    tags=["AI Agent"]
)


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest, db: Session = Depends(get_db)):

    result = graph.invoke(
        {
            "user_input": request.message,
            "intent": "",
            "response": {},
            "db": db
        }
    )

    return result["response"]