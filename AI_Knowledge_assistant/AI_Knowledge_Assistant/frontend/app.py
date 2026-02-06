import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL")

st.title("AI Knowledge Assistant (Endee + RAG)")

query = st.text_input("Ask a question")

if st.button("Ask"):
    response = requests.get(f"{BACKEND_URL}/")
    st.json(response.json())
