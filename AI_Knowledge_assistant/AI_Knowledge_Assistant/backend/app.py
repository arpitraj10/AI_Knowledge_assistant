from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Knowledge Assistant Backend")

@app.get("/")
def health():
    return {"status": "Backend running with Endee"}
