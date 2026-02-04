from sentence_transformers import SentenceTransformer
from pathlib import Path
from endee_client import store_vectors

model = SentenceTransformer("all-MiniLM-L6-v2")

docs_path = Path("data/documents")

for file in docs_path.iterdir():
    text = file.read_text()
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    
    embeddings = model.encode(chunks).tolist()
    metadata = [{"source": file.name} for _ in chunks]
    
    store_vectors(embeddings, metadata)

print("Documents ingested successfully")
