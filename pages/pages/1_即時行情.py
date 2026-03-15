
import streamlit as st
from modules.realtime import get_realtime_price

st.title("台股即時行情")

stock=st.text_input("輸入股票代號","2330")

if stock:
    data=get_realtime_price(stock)

    if data:
        st.metric("即時價格",data["price"])
        st.write("買價:",data["bid"])
        st.write("賣價:",data["ask"])
        st.write("成交量:",data["volume"])
    else:
        st.warning("查無資料")
