from sentence_transformers import SentenceTransformer
from endee_client import search_vectors
import openai

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_answer(query):
    query_embedding = model.encode([query])[0].tolist()
    results = search_vectors(query_embedding, top_k=5)

    context = " ".join([r["metadata"]["text"] for r in results])

    prompt = f"""
    Answer the question using the context below.
    Context: {context}
    Question: {query}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
