
import streamlit as st

st.title("💰 模擬交易")

price=500

if "cash" not in st.session_state:
    st.session_state.cash=100000

if "stock" not in st.session_state:
    st.session_state.stock=0

if st.button("買進"):
    if st.session_state.cash>=price:
        st.session_state.cash-=price
        st.session_state.stock+=1

if st.button("賣出"):
    if st.session_state.stock>0:
        st.session_state.cash+=price
        st.session_state.stock-=1

st.write("現金:",st.session_state.cash)
st.write("持股:",st.session_state.stock)
