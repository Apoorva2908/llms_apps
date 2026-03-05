import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(page_title="Stock Analysis Agent", layout="centered")

st.title("📈 AI Stock Analysis Agent")
st.write(
    "Ask questions about stocks. The AI agent will fetch price data, "
    "fundamentals, and technical indicators before answering."
)

query = st.text_input(
    "Enter your query",
    placeholder="Example: Analyze Tesla stock"
)

if st.button("Analyze"):

    if query.strip() == "":
        st.warning("Please enter a query.")
    else:

        with st.spinner("Analyzing stock..."):

            response = requests.get(API_URL, params={"query": query})

            if response.status_code == 200:
                result = response.json()["analysis"]

                st.success("Analysis Complete")
                st.write(result)

            else:
                st.error("Failed to get response from backend.")