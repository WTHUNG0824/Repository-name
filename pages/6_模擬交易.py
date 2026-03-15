
import streamlit as st
import yfinance as yf

st.title("💰 投資模擬")

stock=st.text_input("股票","2330.TW")

data=yf.Ticker(stock).history(period="1d")

price=0
if len(data)>0:
    price=data["Close"].iloc[-1]

if "cash" not in st.session_state:
    st.session_state.cash=100000
    st.session_state.shares=0

st.metric("虛擬資金",st.session_state.cash)
st.metric("持股",st.session_state.shares)

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
