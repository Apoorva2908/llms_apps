'''This script contains the code for the api which receives query from the user and returns agent response
-Apoorva S Shekhawat'''

from fastapi import FastAPI
from agent import run_agent

app = FastAPI()

@app.get("/analyze")
def analyze_stock(query: str):

    response = run_agent(query)

    return {"analysis": response}