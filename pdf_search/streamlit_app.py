import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("📄 Research Paper RAG")

uploaded_file = st.file_uploader("Upload PDF", type = "pdf")

#Upload pdf
if uploaded_file:
    files = {
    "file": (uploaded_file.name, uploaded_file, "application/pdf")
}
    res = requests.post(f"{API_URL}/upload", files = files)
    if res.status_code == 200:
        st.success(res.json())
    else:
        st.error(f"Error {res.status_code}")
        st.text(res.text)

# Query
query = st.text_input("Ask a question")

if st.button("Search & Generate"):

    res = requests.get(
        f"{API_URL}/rag",
        params={"query": query, "k": 5}
    ).json()

    st.subheader("🧠 Answer")
    st.write(res["answer"])

    with st.expander("📚 Retrieved Context"):
        for c in res["contexts"]:
            st.write(c)
            st.write("----")