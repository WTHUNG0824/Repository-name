
import streamlit as st

st.title("模擬交易")

if "cash" not in st.session_state:
    st.session_state.cash=1000000

st.write("虛擬資金:",st.session_state.cash)

stock=st.text_input("股票")
price=st.number_input("價格")
qty=st.number_input("數量")

if st.button("買入"):
    cost=price*qty

    if st.session_state.cash>=cost:
        st.session_state.cash-=cost
        st.success("買入成功")
    else:
        st.error("資金不足")
