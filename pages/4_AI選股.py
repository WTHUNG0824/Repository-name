
import streamlit as st

st.title("AI選股")

stocks=[
("2330","台積電"),
("2317","鴻海"),
("2454","聯發科"),
("2382","廣達")
]

for code,name in stocks:
    st.write("推薦:",code,name)
