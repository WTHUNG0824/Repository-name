
import streamlit as st

st.title("💰 模擬交易")

price=500

if "cash" not in st.session_state:
    st.session_state.cash=100000
if "shares" not in st.session_state:
    st.session_state.shares=0

c1,c2=st.columns(2)

with c1:
    if st.button("買進"):
        if st.session_state.cash>=price:
            st.session_state.cash-=price
            st.session_state.shares+=1

with c2:
    if st.button("賣出"):
        if st.session_state.shares>0:
            st.session_state.cash+=price
            st.session_state.shares-=1

st.write("現金:",st.session_state.cash)
st.write("持股:",st.session_state.shares)
