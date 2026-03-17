from sentence_transformers import SentenceTransformer
import numpy as np
from transformers import pipeline
from database import collection

model = SentenceTransformer("all-MiniLM-L6-v2")

docs = collection.find()

for doc in docs:
    content = doc["content"]

    embedding = model.encode(content).tolist()

    collection.update_one(
        {"_id": doc["_id"]},
        {"$set": {"embedding": embedding}}
    )

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve_docs(query):

    query_embedding = model.encode(query)

    docs = collection.find()

    scores = []

    for doc in docs:
        doc_embedding = np.array(doc["embedding"])
        score = cosine_similarity(query_embedding, doc_embedding)

        scores.append((score, doc["content"]))

    scores.sort(reverse=True)

    top_docs = [doc for _, doc in scores[:3]]

    return top_docs

generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_answer(query):

    docs = retrieve_docs(query)

    context = "\n".join(docs)

    prompt = f"""
    Answer the question based on the context.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """
    result = generator(prompt, max_length=200)

    return result[0]["generated_text"]

# print(generate_answer("what AI"))