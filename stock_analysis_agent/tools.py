'''This script contains functions which will be used by the llm for function calling
-Apoorva S Shekhawat'''
#Importing dependencies
import yfinance as yf
import pandas as pd

#Defining functions
def get_stock_price(ticker: str):

    stock = yf.Ticker(ticker)
    hist = stock.history(period = "6mo")

    latest_price = hist["Close"].iloc[-1]

    return {
        "ticker": ticker,
        "latest_price": float(latest_price),
        "history_points": len(hist)
    }

def get_fundamentals(ticker: str):

    stock = yf.Ticker(ticker)
    info = stock.info

    return {
        "ticker":ticker,
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "eps": info.get("trailingEps"),
        "revenue_growth": info.get("revenueGrowth")
    }

def technical_analysis(ticker: str):

    stock = yf.Ticker(ticker)
    df = stock.history(period = "3mo")

    df["MA50"] = df["Close"].rolling(50).mean()

    trend = "bullish" if df['Close'].iloc[-1] > df['MA50'].iloc[-1] else "bearish"

    return {
        "ticker": ticker,
        "trend":trend,
        "latest_price": float(df["Close"].iloc[-1]),
        "moving_average": float(df["MA50"].iloc[-1])
    }