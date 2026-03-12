from fastapi import FastAPI
from pydantic import BaseModel
from summarizer import generate_summary
import uuid

app = FastAPI()

class MeetingText(BaseModel):
    text: str

summary_store = {}

@app.post("/summarize")
def text_summary(data: MeetingText):

    summary_text,tokens_count = generate_summary(data.text)

    summary_id = str(uuid.uuid4())

    summary_store[summary_id] = {"summary_id":summary_id,"summary_text": summary_text, "tokens_count": tokens_count}

    return {"summary_id": summary_id, "summary_text": summary_text}

@app.get("/tokens/{summary_id}")
def tokens_used(summary_id: str):
    if summary_id not in summary_store:
        return {"Summary_id NOT FOUND"}
    return {"summary_id": summary_id,"tokens_used":summary_store[summary_id]["tokens_count"]}

