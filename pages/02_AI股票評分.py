
import streamlit as st
import pandas as pd
import random

st.title("🤖 AI股票評分")

stocks=[
"2330 台積電","2317 鴻海","2454 聯發科","3231 緯創",
"2382 廣達","2376 技嘉","3661 世芯"
]

scores=[random.randint(50,95) for _ in stocks]

icons=[]
for s in scores:
    if s>=80:
        icons.append("🟢 建議關注")
    elif s>=65:
        icons.append("🟡 中性")
    else:
        icons.append("🔴 風險")

df=pd.DataFrame({"股票":stocks,"AI評分":scores,"AI判讀":icons})
st.dataframe(df.sort_values("AI評分",ascending=False))
