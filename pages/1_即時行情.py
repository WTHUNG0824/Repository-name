
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.title("即時行情")

stock = st.text_input("股票代碼","2330.TW")

ticker = yf.Ticker(stock)
data = ticker.history(period="6mo")

if len(data)>0:

    price = data["Close"].iloc[-1]
    st.metric("最新股價", round(price,2))

    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close']
    ))

    st.plotly_chart(fig,use_container_width=True)
