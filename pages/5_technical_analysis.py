
import streamlit as st, yfinance as yf, pandas as pd

st.title("Technical Analysis")

code = st.text_input("Stock","2330.TW")

data = yf.Ticker(code).history(period="6mo")

if len(data)>0:
    data["MA20"] = data["Close"].rolling(20).mean()
    data["MA60"] = data["Close"].rolling(60).mean()
    st.line_chart(data[["Close","MA20","MA60"]])
