'''This script will be used to generate final response given the query and the top k retrieved documents
-Apoorva S Shekhawat'''

import os
from openai import AzureOpenAI, OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

MODEL = os.getenv('DEPLOYMENT')
print(MODEL)

def generate_answer(query, contexts):

    context_text = "\n\n".join(contexts)

    prompt = f"""
You are a research assistant.

Answer the question using ONLY the context below.
If the answer is not present, say "Not found in the provided papers".

Context:
{context_text}

Question:
{query}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content

result = generate_answer("what is the name of the person", "Apoorva is a very smart girl, she is very hard working.")
print(result)