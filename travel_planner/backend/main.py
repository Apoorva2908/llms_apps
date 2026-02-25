'''
This is the main file for backend
'''

from fastapi import FastAPI
from pydantic import BaseModel
from llm import get_response, SYSTEM_PROMPT
from state import get_messages, update_messages

app = FastAPI()

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    
    #Initialize the memory with session id using system prompt
    #if not present already else retreives the history of the given sessions
    messages = get_messages(req.session_id, SYSTEM_PROMPT)

    #updates the user prompt
    update_messages(req.session_id, "user", req.message)

    #receives system reply
    reply = get_response(messages)

    #updates system reply in memory
    update_messages(req.session_id, "assistant", reply)

    return {"response": reply}

@app.get("/")
def root():
    return {"message": "Travel Planner API is running"}

