
import streamlit as st

st.title("台股排行榜")

stocks=[
("2330","台積電"),
("2317","鴻海"),
("2454","聯發科"),
("2303","聯電"),
("2603","長榮")
]

for s in stocks:
    st.write(s[0],s[1])
