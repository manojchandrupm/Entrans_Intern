from sentence_transformers import SentenceTransformer
import numpy as np

##### document loading
with open("Rag_doc.txt", "r", encoding="utf-8") as file:
    text = file.read()

##### splitting into chunks
# chunk_size = 100
chunks = text.split("\n")
# for i in range(0, len(text), chunk_size):
#     chunk = text[i:i + chunk_size]
#     chunks.append(chunk)

##### embedding the chunks using the pretrained model
##this model wil convert the chunks into tokens(single words) -> provide token ids -> provide dense vector based on ids in the embedding layer.
model = SentenceTransformer("all-MiniLM-L6-v2")
chunk_embeddings = model.encode(chunks)

query = input("Ask a question: ")
query_embedding = model.encode([query])

# formula to find the cosine similarity
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)

similarity = []
for chunk in chunk_embeddings:
    similarity.append(cosine_similarity(query_embedding[0],chunk))

# similarities = np.array(similarity, dtype=float)

#### the below line sort the similarity list values and return the index based on the sorted values
sorted_indices = np.argsort(similarity)

reversed_indices = []
for i in range(len(sorted_indices)-1,-1,-1):
    reversed_indices.append(sorted_indices[i])
print("Reversed indices (high to low):", reversed_indices)

top_indices = []
for i in range(0,3):
    top_indices.append(reversed_indices[i])

for idx in top_indices:
    print(chunks[idx])


