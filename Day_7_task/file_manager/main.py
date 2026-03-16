from fastapi import FastAPI, File, UploadFile
import os
import shutil
from content_extracter import extract_text
from database import collection
from pydantic import BaseModel
from Rag_bot import answer_question
app = FastAPI()

upload_file_dir = "upload_file"
os.makedirs(upload_file_dir, exist_ok=True)

### endpoint to upload file
@app.post("/uploads")
async def upload_files(file: UploadFile = File(...)):
    try:
        filename = file.filename
        file_path = os.path.join(upload_file_dir, filename)

        ### save file in local folder
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        content = extract_text(file_path)

        file_type = file.filename.split(".")[-1]

        ### store in database
        collection.insert_one({"content": content,"filename": filename,"filetype": file_type})

        return {
            "content": content,
            "filename": filename,
            "filepath": file_path
        }

    except Exception as e:
        return {"error": str(e)}

### endpoints to view files
@app.get("/file/txt")
def get_txt_files():
    files = list(collection.find({"filetype": "txt"}, {"_id":0}))
    return files

@app.get("/file/pdf")
def get_pdf_files():
    files = list(collection.find({"filetype": "pdf"}, {"_id":0}))
    return files

@app.get("/file/audio")
def get_audio_files():
    files = list(collection.find({"filetype": {"$in": ["mp3","wav"]}}, {"_id":0}))
    return files

class Query(BaseModel):
    question: str

@app.post("/chat")
def chat(question: Query):
    return {"bot answer based on the uploaded doc ":answer_question(question)}
