import streamlit as st
import requests
import uuid

API_URL = "http://localhost:8000/chat"

st.set_page_config(page_title = "Travel Planner")

st.title("🌍 AI Travel Planner")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.chat_input('Plan your trip..')

if user_input:
    st.session_state.chat.append(('user', user_input))
    response = requests.post(
        API_URL,
        json = {
            "session_id": st.session_state.session_id,
            "message": user_input
        }
    ).json()["response"]

    st.session_state.chat.append(('assistant', response))

for role, msg in st.session_state.chat:
    with st.chat_message(role):
        st.write(msg)