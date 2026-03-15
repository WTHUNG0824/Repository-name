
import streamlit as st, yfinance as yf

st.title("Market Dashboard")

codes = st.text_input("Stocks","2330.TW,2317.TW,2454.TW").split(",")

cols = st.columns(len(codes))

for i,c in enumerate(codes):
    c = c.strip()
    data = yf.Ticker(c).history(period="1mo")
    if len(data)>0:
        price = data["Close"].iloc[-1]
        with cols[i]:
            st.subheader(c)
            st.metric("Price", round(price,2))
            st.line_chart(data["Close"])
