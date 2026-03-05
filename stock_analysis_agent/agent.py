import json
from openai import OpenAI
from config import *
from tools import *

client = OpenAI(
    base_url=os.getenv("API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

TOOLS = [
    {
        "type":"function",
        "function":{
            "name":"get_stock_price",
            "description":"Get latest stock price",
            "parameters":{
                "type":"object",
                "properties":{
                    "ticker":{"type":"string"}
                },
                "required": ["ticker"]
            }
        }
    },
    {
        "type":"function",
        "function":{
            "name":"get_fundamentals",
            "description": "Get stock fundamentals",
            "parameters":{
                "type":"object",
                "properties":{
                    "ticker": {"type":"string"}
                },
            "required": ["ticker"]
            }
        }
    },
    {
        "type":"function",
        "function": {
            "name":"technical_analysis",
            "description": "Compute technical indicators",
            "parameters":{
                "type":"object",
                "properties":{
                    "ticker":{"type":"string"}
                },
                "required":["ticker"]
            }
        }

    }
]

TOOL_MAP = {
    "get_stock_price": get_stock_price,
    "get_fundamentals": get_fundamentals,
    "technical_analysis":technical_analysis
}

def run_agent(user_query):

    messages = [
        {
            "role":"system",
            "content": "You are a financial stock analyst AI. Use tools whenever needed before answering."
        },
        {"role":"user", "content":user_query}
    ]

    response = client.chat.completions.create(
        model = AZURE_DEPLOYMENT,
        messages = messages,
        tools = TOOLS,
        tool_choice = "auto"
    )

    message = response.choices[0].message

    if message.tool_calls:

        messages.append(message)

        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            result = TOOL_MAP[tool_name](**args)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })

        final_response = client.chat.completions.create(
            model=AZURE_DEPLOYMENT,
            messages=messages
        )

        return final_response.choices[0].message.content
    
    return message.content