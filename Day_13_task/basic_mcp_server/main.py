from fastapi import FastAPI
from pydantic import BaseModel
from ai_agent import main

app = FastAPI(title="MCP AI Agent API")

class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
async def ask_question(request: QuestionRequest):
    result = await main(request.question)
    return result


@app.get("/")
def home():
    return {
        "message": "MCP AI Agent API is running"
    }