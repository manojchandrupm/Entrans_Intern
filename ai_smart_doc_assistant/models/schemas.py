from pydantic import BaseModel
from typing import List

class HealthResponse(BaseModel):
    status: str
    app_name: str
    version: str

class UploadResponse(BaseModel):
    message: str
    filename: str
    total_chunks: int

class QueryRequest(BaseModel):
    question: str
    top_k: int = 3

class RetrievedMatch(BaseModel):
    chunk_id: str
    filename: str
    page: int
    chunk_index: int
    score: float
    text: str

class QueryResponse(BaseModel):
    question: str
    top_k: int
    matches: List[RetrievedMatch]

class QueryReply(BaseModel):
    answer : str
    sources : str