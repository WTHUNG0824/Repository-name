
import streamlit as st
import pandas as pd

st.title("🚀 AI自動選股")

data={
"股票":["緯創","技嘉","奇鋐","廣達","台燿"],
"AI評分":[88,84,80,77,75],
"建議":["🟢買入","🟢關注","🟡觀察","🟡觀察","🟡觀察"]
}

df=pd.DataFrame(data)

st.dataframe(df,use_container_width=True)
