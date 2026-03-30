from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from config import env


qdrant_client = QdrantClient(
    url=env.QDRANT_URL,
    api_key=env.QDRANT_API_KEY,
)


def store_chunks_in_qdrant(chunks: list):
    if not chunks:
        return

    points = []
    vector_size = len(chunks[0]["embedding"])
    for idx, chunk in enumerate(chunks):
        points.append(
            PointStruct(
                id=idx + 1,
                vector=chunk["embedding"],
                payload={
                    "chunk_id": chunk["chunk_id"],
                    "filename": chunk["filename"],
                    "page": chunk["page"],
                    "chunk_index": chunk["chunk_index"],
                    "text": chunk["text"]
                }
            )
        )

    qdrant_client.create_collection(
        collection_name="doc_assistant_collection",
        vectors_config=VectorParams(
            size=vector_size,
            distance=Distance.COSINE
        )
    )
    qdrant_client.upsert(
        collection_name="doc_assistant_collection",
        points=points
    )