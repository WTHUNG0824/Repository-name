
import streamlit as st
import yfinance as yf

st.title("ETF分析")

etf=st.text_input("ETF代碼","0050.TW")

ticker=yf.Ticker(etf)
data=ticker.history(period="1y")

if len(data)>0:
    st.line_chart(data["Close"])
