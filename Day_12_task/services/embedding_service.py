import requests

def generate_embedding(text):
    """
    Generate embedding using Ollama embeddings API.
    """
    response = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": "nomic-embed-text",
            "input": text
        },
        timeout=60
    )

    response.raise_for_status()
    data = response.json()

    return data["embeddings"][0]
