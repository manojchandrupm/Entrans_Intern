from fastapi import FastAPI
from pydantic import BaseModel
from summarizer import generate_summary
import uuid
from Db_store import collection
from datetime import datetime
from fastapi import HTTPException

app = FastAPI()

current_time = datetime.utcnow()

class MeetingText(BaseModel):
    text: str

@app.post("/summarize")
def text_summary(data: MeetingText):

    summary_text,tokens_count = generate_summary(data.text)

    summary_id = str(uuid.uuid4())
    formatted_time = current_time.strftime("%B %d, %Y %I:%M %p")
    document = {"summary_id":summary_id,"summary_text": summary_text, "tokens_count": tokens_count,"created_at": formatted_time}
    collection.insert_one(document)

    return {"summary_id": summary_id, "summary_text": summary_text}

@app.get("/tokens/{summary_id}")
def tokens_used(summary_id: str):
    result = collection.find_one({"summary_id":summary_id})
    if not result:
        raise HTTPException(
            status_code=404,
            detail="Summary ID not found"
        )

    return {
        "summary_id": summary_id,
        "summary_text": result["summary_text"],
        "tokens_used": result["tokens_count"],
        "created_at": result["created_at"]
    }

