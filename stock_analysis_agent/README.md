# Stock Analysis Tool-Calling Agent (Azure GPT-4o)

An AI agent that performs **stock analysis using tool calling** with **Azure OpenAI GPT-4o**.
The agent can fetch stock data, compute technical indicators, and analyze fundamentals by calling external APIs such as **Yahoo Finance**.

This project demonstrates how to build **LLM agents with tool orchestration** using Azure-hosted models.

---

# Features

* Tool-calling agent using **Azure GPT-4o**
* Fetch stock price data via **Yahoo Finance API**
* Compute technical indicators
* Retrieve stock fundamentals
* Agent decides when to call tools automatically
* FastAPI endpoint for querying the agent
* Modular architecture

---

# Architecture

```
User Query
    │
    ▼
FastAPI API
    │
    ▼
Agent (GPT-4o)
    │
    ▼
Tool Selection
    │
    ├── get_stock_price
    ├── technical_analysis
    └── get_fundamentals
    │
    ▼
External APIs (Yahoo Finance)
    │
    ▼
Result returned to LLM
    │
    ▼
Final explanation
```

---

# Project Structure

```
stock-agent/
│
├── agent.py          # LLM agent loop and tool orchestration
├── tools.py          # Tool implementations (stock APIs)
├── api.py            # FastAPI server
├── config.py         # Environment configuration
├── requirements.txt  # Dependencies
└── .env              # Environment variables
```

---

# Tools Implemented

### get_stock_price

Fetches recent stock price data.

### technical_analysis

Computes simple technical indicators (moving averages).

### get_fundamentals

Fetches company fundamentals like:

* Market cap
* P/E ratio
* EPS
* Revenue growth

---

# Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/stock-agent.git
cd stock-agent
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Environment Setup

Create a `.env` file.

```
AZURE_OPENAI_ENDPOINT=https://YOUR_RESOURCE.openai.azure.com/
AZURE_OPENAI_KEY=YOUR_API_KEY
AZURE_DEPLOYMENT=gpt4o-agent
AZURE_API_VERSION=2024-02-15-preview
```

---

# Running the Agent
## Streamlit Web Interface

A Streamlit-based UI is included to interact with the AI stock analysis agent.

### Location

```
frontend/app.py
```

### Running the UI

1. Start the FastAPI backend:

```bash
uvicorn api:app --reload
```

2. Start the Streamlit app:

```bash
streamlit run frontend/app.py
```

3. Open the browser:

```
http://localhost:8501
```

# Example Queries

Open in browser or send request.

```
http://127.0.0.1:8000/analyze?query=Analyze Apple stock
```

Other examples:

```
Compare Tesla and Nvidia fundamentals
```

```
Is Microsoft stock bullish right now?
```

```
Analyze Amazon stock for long term investment
```

---

# Example Output

```
Apple stock is currently trading around $192.

Technical outlook:
The price remains above its 50-day moving average,
indicating a bullish trend.

Fundamentals:
Market Cap: $3.02T
PE Ratio: 31
Revenue growth remains stable.

Conclusion:
Apple remains fundamentally strong with moderate valuation.
```

---

# Technologies Used

* Azure OpenAI (GPT-4o)
* Python
* FastAPI
* Pandas
* Yahoo Finance API (yfinance)

---

# How Tool Calling Works

1. User asks a question.
2. GPT-4o decides if a tool is needed.
3. The model outputs a **tool call instruction**.
4. Backend executes the tool.
5. Tool result is returned to GPT-4o.
6. GPT-4o generates the final explanation.

---

# Example Agent Flow

```
User: Analyze Tesla stock

LLM decides:
→ call technical_analysis("TSLA")

Tool executes:
→ fetch stock history
→ compute moving average

Result returned to LLM

LLM explains trend and fundamentals
```

---

# Future Improvements

Possible extensions:

* Add stock **news sentiment analysis**
* Portfolio risk analyzer
* Chart generation with Plotly
* Multi-tool reasoning loop
* RAG over earnings call transcripts
* Support for multiple stock APIs

---

# Learning Goals

This project demonstrates:

* LLM tool calling
* AI agent orchestration
* External API integration
* Azure OpenAI usage
* Financial data pipelines

---


