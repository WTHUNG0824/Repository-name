
import streamlit as st

st.title("飆股雷達")

stocks=[
("3017","奇鋐"),
("3037","欣興"),
("2382","廣達")
]

for s in stocks:
    st.write("可能飆股",s[0],s[1])
