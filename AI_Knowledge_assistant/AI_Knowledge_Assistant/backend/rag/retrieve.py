from endee_client import search_vectors

def retrieve_context(query_embedding):
    results = search_vectors(query_embedding)
    contexts = [r["metadata"]["text"] for r in results["matches"]]
    return contexts
