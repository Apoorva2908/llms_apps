'''This file will be used to create a function which takes a text and returns its embeddings. 
Here the embeddings will be created text-embedding-small model of openAI hosted on Azure
-Apoorva S Shekhawat'''

#---------------------------------
# Importing required dependencies
#---------------------------------
import os
from openai import AzureOpenAI, OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

MODEL = "text-embedding-3-small"
BATCH = 64

def embed_chunks(chunks):
    vectors = []
    for i in range(0, len(chunks), BATCH_SIZE):
        batch = chunks[i:i+BATCH_SIZE]
        response = client.embeddings.create(
            model = MODEL,
            input = batch
        )
        vectors.extend([d.embedding for d in response.data])

    return vectors