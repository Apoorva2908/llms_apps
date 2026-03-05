import os
from dotenv import load_dotenv

load_dotenv()

AZURE_OPENAI_ENDPOINT = os.getenv("API_BASE")
AZURE_OPENAI_KEY = os.getenv("OPENAI_API_KEY")
AZURE_DEPLOYMENT = os.getenv("DEPLOYMENT")
# AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")