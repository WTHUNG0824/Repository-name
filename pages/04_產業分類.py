
import streamlit as st
import pandas as pd

st.title("🏭 產業分類")

data={
"公司":["台積電","鴻海","聯發科","廣達","緯創"],
"產業":["半導體","電子代工","IC設計","AI伺服器","AI伺服器"]
}

df=pd.DataFrame(data)

ind=st.selectbox("選擇產業",df["產業"].unique())

st.dataframe(df[df["產業"]==ind])
