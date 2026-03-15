
import streamlit as st, yfinance as yf

st.title("Investment Simulation")

stock = st.text_input("Stock","2330.TW")

data = yf.Ticker(stock).history(period="1d")

price = 0
if len(data)>0:
    price = data["Close"].iloc[-1]

if "cash" not in st.session_state:
    st.session_state.cash = 100000
    st.session_state.shares = 0

st.metric("Cash", st.session_state.cash)
st.metric("Shares", st.session_state.shares)

qty = st.number_input("Quantity",1)

if st.button("Buy"):
    cost = qty*price
    if st.session_state.cash >= cost:
        st.session_state.cash -= cost
        st.session_state.shares += qty

if st.button("Sell"):
    if st.session_state.shares >= qty:
        st.session_state.cash += qty*price
        st.session_state.shares -= qty
