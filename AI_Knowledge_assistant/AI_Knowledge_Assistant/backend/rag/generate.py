def generate_answer(contexts, query):
    context_text = "\n".join(contexts)
    return f"Answer based on context:\n{context_text}\n\nQuestion: {query}"
