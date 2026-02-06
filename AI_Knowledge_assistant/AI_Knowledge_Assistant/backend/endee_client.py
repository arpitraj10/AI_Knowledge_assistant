import os
import requests

ENDEE_API_KEY = os.getenv("ENDEE_API_KEY")
ENDEE_BASE_URL = os.getenv("ENDEE_BASE_URL")

HEADERS = {
    "Authorization": f"Bearer {ENDEE_API_KEY}",
    "Content-Type": "application/json"
}

def add_vectors(vectors):
    response = requests.post(
        f"{ENDEE_BASE_URL}/vectors",
        headers=HEADERS,
        json=vectors
    )
    response.raise_for_status()
    return response.json()

def search_vectors(query_vector, top_k=5):
    response = requests.post(
        f"{ENDEE_BASE_URL}/search",
        headers=HEADERS,
        json={
            "vector": query_vector,
            "top_k": top_k
        }
    )
    response.raise_for_status()
    return response.json()
