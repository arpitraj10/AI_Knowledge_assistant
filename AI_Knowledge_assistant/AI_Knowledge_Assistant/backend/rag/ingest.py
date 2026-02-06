from endee_client import add_vectors

def ingest_documents(docs, embeddings):
    vectors = []
    for i, emb in enumerate(embeddings):
        vectors.append({
            "id": f"doc_{i}",
            "values": emb,
            "metadata": {"text": docs[i]}
        })

    add_vectors(vectors)
