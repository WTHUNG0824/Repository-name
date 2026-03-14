
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from prophet import Prophet

st.set_page_config(page_title="AI台股投資平台 V5", layout="wide")

st.title("AI台股投資平台 V5")

st.sidebar.header("功能選單")
menu = st.sidebar.radio(
    "選擇功能",
    [
        "股票搜尋",
        "股價走勢",
        "AI股價預測",
        "AI概念股",
        "低價潛力股",
        "投資教學"
    ]
)

def get_stock(code):
    ticker = yf.Ticker(code + ".TW")
    hist = ticker.history(period="1y")
    return ticker, hist

# 股票搜尋
if menu == "股票搜尋":
    code = st.text_input("輸入股票代碼", "2330")
    if code:
        ticker, hist = get_stock(code)

        if not hist.empty:
            price = hist["Close"].iloc[-1]
            st.metric("最新股價", round(price,2))

            hist["MA5"] = hist["Close"].rolling(5).mean()
            hist["MA20"] = hist["Close"].rolling(20).mean()
            hist["MA60"] = hist["Close"].rolling(60).mean()

            st.line_chart(hist[["Close","MA5","MA20","MA60"]])

# 股價K線
elif menu == "股價走勢":
    code = st.text_input("輸入股票代碼", "2330")
    ticker, hist = get_stock(code)

    if not hist.empty:
        fig = go.Figure(data=[go.Candlestick(
            x=hist.index,
            open=hist['Open'],
            high=hist['High'],
            low=hist['Low'],
            close=hist['Close']
        )])
        fig.update_layout(title="K線圖", height=600)
        st.plotly_chart(fig, use_container_width=True)

# AI股價預測
elif menu == "AI股價預測":
    code = st.text_input("輸入股票代碼", "2330")
    ticker, hist = get_stock(code)

    if not hist.empty:
        df = hist.reset_index()[["Date","Close"]]
        df.columns = ["ds","y"]

        model = Prophet()
        model.fit(df)

        future = model.make_future_dataframe(periods=30)
        forecast = model.predict(future)

        st.subheader("未來30天AI預測")
        st.line_chart(forecast.set_index("ds")["yhat"])

# AI概念股
elif menu == "AI概念股":

    ai_stocks = {
        "2330":"台積電",
        "2454":"聯發科",
        "3037":"欣興",
        "3443":"創意",
        "3661":"世芯",
        "6669":"緯穎"
    }

    st.subheader("AI概念股清單")

    for code,name in ai_stocks.items():
        st.write(code, name)

# 低價潛力股 (簡化版示範)
elif menu == "低價潛力股":

    watchlist = ["1101","1216","1301","1326","1402","2002","2105","2207","2303","2317"]

    results = []

    for code in watchlist:
        ticker = yf.Ticker(code + ".TW")
        hist = ticker.history(period="1d")

        if not hist.empty:
            price = hist["Close"].iloc[-1]

            if price < 20:
                results.append((code, price))

    st.subheader("20元以下潛力股")

    if results:
        df = pd.DataFrame(results, columns=["股票","價格"])
        st.dataframe(df)
    else:
        st.write("今天沒有符合條件股票")

# 投資教學
elif menu == "投資教學":

    st.header("股票新手教學")

    st.write("EPS = 每股盈餘，公司每股賺多少錢")
    st.write("PE = 本益比，股價 / EPS")
    st.write("MA5 / MA20 / MA60 = 移動平均線")
    st.write("K線 = 顯示股價每日變化")
