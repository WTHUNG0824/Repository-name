
import streamlit as st
import pandas as pd
import numpy as np

st.title("📉 技術分析")

code=st.text_input("股票代碼","2330")

price=np.cumsum(np.random.normal(0,1,250))+100

df=pd.DataFrame({"價格":price})

st.line_chart(df)

st.markdown("技術指標: MA / RSI / MACD / KD")
