
import streamlit as st

st.title("投資教學")

topic=st.selectbox("選擇主題",[
"股票是什麼",
"ETF是什麼",
"EPS是什麼",
"本益比是什麼"
])

content={
"股票是什麼":"股票代表公司所有權的一部分",
"ETF是什麼":"ETF是一籃子股票，例如0050",
"EPS是什麼":"EPS為每股盈餘，代表公司賺錢能力",
"本益比是什麼":"本益比 = 股價 ÷ EPS"
}

st.write(content[topic])
