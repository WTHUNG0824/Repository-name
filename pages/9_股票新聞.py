
import streamlit as st

st.title("股票新聞")

news=[
"AI需求帶動半導體",
"台股成交量創高",
"ETF資金持續流入"
]

for n in news:
    st.write(n)
