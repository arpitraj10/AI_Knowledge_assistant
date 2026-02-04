import streamlit as st
import requests

st.set_page_config(page_title="AI Knowledge Assistant")

st.title("AI Knowledge Assistant")

query = st.text_input("Ask a question from your documents")

if st.button("Ask"):
    response = requests.get(
        "http://localhost:8000/ask",
        params={"query": query}
    )
    st.success(response.json()["answer"])
