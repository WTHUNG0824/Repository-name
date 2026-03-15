
import streamlit as st
import pandas as pd
import random

st.title("📊 股票技術分析")

code=st.text_input("輸入股票代碼","2330")

data=pd.DataFrame({
"價格":[500+random.uniform(-20,20) for _ in range(60)]
})

st.line_chart(data)

st.markdown("技術指標說明")
st.write("MA20：20日均線")
st.write("MA60：60日均線")
st.write("RSI：超買超賣指標")
