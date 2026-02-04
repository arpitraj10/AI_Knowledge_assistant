from fastapi import FastAPI
from rag_pipeline import generate_answer

app = FastAPI()

@app.get("/ask")
def ask(query: str):
    answer = generate_answer(query)
    return {"answer": answer}
