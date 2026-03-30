from fastapi import APIRouter, HTTPException
from pymupdf import message

from models.schemas import QueryRequest, QueryResponse, RetrievedMatch,QueryReply
from services.retrieval_service import retrieve_similar_chunks
from services.user_query_response_service import generate_query_response

router = APIRouter(prefix="/query", tags=["Query"])

@router.post("/", response_model=QueryReply)
async def query_document(payload: QueryRequest):
    question = payload.question.strip()

    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    try:
        matches = retrieve_similar_chunks(question=question, top_k=payload.top_k)

        query_reply = QueryResponse(
            question=question,
            top_k=payload.top_k,
            matches=[RetrievedMatch(**match) for match in matches]
        )

        answer = await generate_query_response(query_reply.model_dump())

        return QueryReply(
            bot=answer
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query pipeline failed: {str(e)}")