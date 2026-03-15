import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="AI股票分析系統", layout="wide")

st.title("📈 AI股票分析系統 V11")

stock = st.text_input("輸入股票代碼", "2330.TW")

if stock:

    ticker = yf.Ticker(stock)

    data = ticker.history(period="6mo")

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

    st.plotly_chart(fig, use_container_width=True)
