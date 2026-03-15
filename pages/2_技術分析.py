
import streamlit as st
import yfinance as yf
import pandas as pd

st.title("技術分析")

stock = st.text_input("股票代碼","2330.TW")

ticker = yf.Ticker(stock)
data = ticker.history(period="1y")

if len(data)>0:

    data["MA20"]=data["Close"].rolling(20).mean()
    data["MA60"]=data["Close"].rolling(60).mean()

    st.line_chart(data[["Close","MA20","MA60"]])
