
import streamlit as st
import yfinance as yf
import json
import plotly.graph_objects as go

st.title("📈 股票行情")

company=json.load(open("company_map.json",encoding="utf-8"))

code=st.text_input("股票代碼","2330.TW")

name=company.get(code,"")

if name:
    st.subheader(name)

data=yf.Ticker(code).history(period="6mo")

if len(data)>0:

    price=data["Close"].iloc[-1]

    st.metric("目前股價",round(price,2))

    fig=go.Figure()

    fig.add_trace(go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close']
    ))

    st.plotly_chart(fig,use_container_width=True)
