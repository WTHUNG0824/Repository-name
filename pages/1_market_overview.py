
import streamlit as st, yfinance as yf
st.title("Market Overview")

symbols = ["2330.TW","2317.TW","2454.TW","SPY","QQQ"]
cols = st.columns(len(symbols))

for i,s in enumerate(symbols):
    data = yf.Ticker(s).history(period="5d")
    if len(data)>0:
        price = data["Close"].iloc[-1]
        with cols[i]:
            st.subheader(s)
            st.metric("Price", round(price,2))
            st.line_chart(data["Close"])
