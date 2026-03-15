
import streamlit as st
import json
import pandas as pd

st.title("📊 ETF完整資料庫")

with open("data/etf_database.json","r",encoding="utf-8") as f:
    data=json.load(f)

df=pd.DataFrame(data)

etf=st.selectbox("選擇ETF",df["code"]+" "+df["name"])

row=df[df["code"]==etf.split()[0]].iloc[0]

st.subheader(row["name"])

st.write("ETF代碼:",row["code"])
st.write("ETF類型:",row["category"])
st.write("投資主題:",row["focus"])
st.write("風險等級:",row["risk"])
st.write("說明:",row["desc"])

st.dataframe(df,use_container_width=True)
