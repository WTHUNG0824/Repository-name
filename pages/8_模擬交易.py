
import streamlit as st
import yfinance as yf

st.title("模擬交易")

stock=st.text_input("股票","2330.TW")

ticker=yf.Ticker(stock)
price_data=ticker.history(period="1d")

price=0
if len(price_data)>0:
    price=price_data["Close"].iloc[-1]

if "cash" not in st.session_state:
    st.session_state.cash=100000
    st.session_state.shares=0

st.write("現金",st.session_state.cash)
st.write("持股",st.session_state.shares)
st.write("股價",price)

qty=st.number_input("股數",1)

if st.button("買入"):
    cost=qty*price
    if st.session_state.cash>=cost:
        st.session_state.cash-=cost
        st.session_state.shares+=qty

if st.button("賣出"):
    if st.session_state.shares>=qty:
        st.session_state.cash+=qty*price
        st.session_state.shares-=qty
