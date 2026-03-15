
import streamlit as st, yfinance as yf, plotly.graph_objects as go, json

st.title("Stock Analysis")
company=json.load(open("company_map.json",encoding="utf-8"))

code = st.text_input("Stock Code","2330.TW")

if code:
    data = yf.Ticker(code).history(period="6mo")
    if len(data)>0:
        price = data["Close"].iloc[-1]
        st.metric("Current Price", round(price,2))

        fig = go.Figure()
        fig.add_trace(go.Candlestick(x=data.index,open=data['Open'],high=data['High'],low=data['Low'],close=data['Close']))
        st.plotly_chart(fig, use_container_width=True)

        st.write("Company:", company.get(code,"Unknown"))
