
import streamlit as st, yfinance as yf

st.title("ETF Analysis")

code = st.text_input("ETF","SPY")

data = yf.Ticker(code).history(period="1y")

if len(data)>0:
    st.line_chart(data["Close"])
