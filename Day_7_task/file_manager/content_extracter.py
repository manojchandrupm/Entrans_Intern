from pypdf import PdfReader
import whisper
import os

model = whisper.load_model("base")

def extract_text(filepath):

    file_ext = os.path.splitext(filepath)[1].lower()
    if file_ext == ".txt":
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    elif file_ext == ".pdf":
        reader = PdfReader(filepath)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

        return text

    elif file_ext in [".mp3", ".wav", ".m4a", ".ogg"]:
        result = model.transcribe(filepath)
        return result["text"]

    return "no file content"