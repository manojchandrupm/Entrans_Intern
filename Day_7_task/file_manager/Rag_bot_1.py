from langchain_text_splitters import CharacterTextSplitter
from database import collection
from langchain.embeddings import HuggingFaceEmbeddings
import numpy as np
from transformers import pipeline

def chunk_documents():
    docs = collection.find()
    text_chunks = []

    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    for doc in docs:
        content = doc["content"]
        chunks = splitter.split_text(content)
        for chunk in chunks:
            text_chunks.append({
                "filename": doc["filename"],
                "chunk": chunk
            })
    return text_chunks

print(chunk_documents())

# Use Olamma embeddings model
embeddings_model = HuggingFaceEmbeddings(model_name="olamma/embedding-model")  # example

def get_embedding(text):
    return embeddings_model.embed_query(text)

text_chunks = chunk_documents()

for chunk in text_chunks:
    vector = get_embedding(chunk['chunk'])
    collection.insert_one({
        "chunk_id": chunk['filename'],
        "text": chunk['chunk'],
        "embedding": vector
    })

def search(query, k=3):
    q_emb = get_embedding(query)
    # Compute cosine similarity manually
    results = []
    for doc in collection.find():
        vec = np.array(doc['embedding'])
        sim = np.dot(q_emb, vec) / (np.linalg.norm(q_emb) * np.linalg.norm(vec))
        results.append((sim, doc['text']))
    results.sort(key=lambda x: x[0], reverse=True)
    return [text for _, text in results[:k]]

# HuggingFace Olamma model for text generation
pipe = pipeline("text-generation", model="olamma/your-olamma-model")
def answer(query):
    context = "\n".join(search(query, k=3))
    prompt = f"Use the following context to answer the question:\n\n{context}\n\nQuestion: {query}\nAnswer:"
    output = pipe(prompt, max_length=512, do_sample=True)
    return output[0]['generated_text']

print(answer("What is the content of the uploaded PDF?"))