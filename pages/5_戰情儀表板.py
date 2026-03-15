
import streamlit as st
import yfinance as yf
import json

st.title("🖥 股票戰情儀表板")

company=json.load(open("company_map.json",encoding="utf-8"))

codes=st.text_input("輸入股票 (逗號分隔)","2330.TW,2317.TW,2454.TW").split(",")

cols=st.columns(len(codes))

for i,c in enumerate(codes):

    c=c.strip()

    data=yf.Ticker(c).history(period="1mo")

    if len(data)>0:

        price=data["Close"].iloc[-1]

        with cols[i]:

            st.subheader(c)
            st.caption(company.get(c,""))

            st.metric("股價",round(price,2))

            st.line_chart(data["Close"])
