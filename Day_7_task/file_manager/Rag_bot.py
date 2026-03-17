from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import numpy as np
from database import collection

###### --- Embedding Model (all-MiniLM-L6-v2) ---
embed_model = SentenceTransformer("D:/Entrans_intern/models/all-MiniLM-L6-v2/models--sentence-transformers--all-MiniLM-L6-v2/snapshots/c9745ed1d9f207416be6d2e6f8de32d1f16199bf")

###### --- Text Generation Model (flan-t5-large) ---
model_path = "D:/Entrans_intern/models/flan-t5-large/models--google--flan-t5-large/snapshots/0613663d0d48ea86ba8cb3d7a44f0f65dc596a2a"
tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path, local_files_only=True)

###### ---- Store Document Embeddings ----
docs = collection.find()
for doc in docs:
    content = doc["content"]

    embedding = embed_model.encode(content).tolist()

    collection.update_one(
        {"_id": doc["_id"]},
        {"$set": {"embedding": embedding}}
    )

###### ---- Similarity Function ----
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

###### ---- Retrieve Relevant Documents ----
def retrieve_docs(query):
    query_embedding = embed_model.encode(query)

    docs = collection.find()

    scores = []

    for doc in docs:
        doc_embedding = np.array(doc["embedding"])
        score = cosine_similarity(query_embedding, doc_embedding)
        scores.append((score, doc["content"]))
    scores.sort(reverse=True)
    top_docs = [doc for _, doc in scores[:3]]

    return top_docs




###### ---- Generate Answer using flan-t5-large ----
def generate_answer(query):
    docs = retrieve_docs(query)
    context = "\n".join(docs)
    prompt = f"""
    You are an AI assistant. Answer only using the given context.
    If the answer is not present, say "I don't know".

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_length=300
    )
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer

print(generate_answer("what happned in the graybridge city?"))