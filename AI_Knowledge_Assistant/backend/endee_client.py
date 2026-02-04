from endee import EndeeClient

client = EndeeClient(api_key="YOUR_ENDEE_API_KEY")

def store_vectors(vectors, metadata):
    client.upsert(vectors=vectors, metadata=metadata)

def search_vectors(query_vector, top_k):
    return client.search(vector=query_vector, top_k=top_k)
