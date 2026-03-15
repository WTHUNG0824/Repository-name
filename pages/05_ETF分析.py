
import streamlit as st
import pandas as pd
import random

st.title("📊 ETF分析")

etf=st.selectbox("選擇ETF",["SPY","QQQ","VOO"])

data=pd.DataFrame({"價格":[random.uniform(300,500) for _ in range(60)]})

st.line_chart(data)
