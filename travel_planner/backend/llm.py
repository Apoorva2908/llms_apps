#---------------------------------
# Importing required dependencies
#---------------------------------
import os
from openai import AzureOpenAI, OpenAI
from dotenv import load_dotenv

load_dotenv()

DEPLOYMENT = os.getenv("DEPLOYMENT")
client = OpenAI(
    base_url=os.getenv("API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

SYSTEM_PROMPT = """
You are a travel planning expert.

Rules:
- Only answer travel-related queries
- If not travel → politely refuse
- Ask follow-up questions if details are missing

Trip requirements:
source, destination, dates, budget, travelers, interests
"""

def get_response(messages):
    response = client.chat.completions.create(
        model = DEPLOYMENT,
        messages = messages,
        temperature = 0.7
    )
    return response.choices[0].message.content