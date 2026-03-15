
import streamlit as st
import yfinance as yf

st.title("📊 ETF分析")

code=st.text_input("ETF","0050.TW")

data=yf.Ticker(code).history(period="1y")

if len(data)>0:
    st.line_chart(data["Close"])
