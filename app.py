
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

try:
    from prophet import Prophet
    PROPHET=True
except:
    PROPHET=False

st.set_page_config(page_title="AI台股投資平台 V7", layout="wide")
st.title("AI台股投資平台 V7")

menu = st.sidebar.radio("功能選單",[
"股票搜尋","技術分析","AI預測","公司新聞",
"AI概念股","低價股掃描","模擬交易",
"股利計算器","投資教學"
])

if "cash" not in st.session_state:
    st.session_state.cash=100000
    st.session_state.portfolio={}

def get_stock(code):
    t=yf.Ticker(code+".TW")
    hist=t.history(period="1y")
    try:
        info=t.info
    except:
        info={}
    return t,hist,info

# 股票搜尋
if menu=="股票搜尋":
    code=st.text_input("股票代碼","2330")
    if code:
        t,hist,info=get_stock(code)
        if not hist.empty:
            price=hist["Close"].iloc[-1]
            st.metric("最新股價",round(price,2))
            st.write("公司:",info.get("longName"))
            st.write("產業:",info.get("industry"))
            st.write("EPS:",info.get("trailingEps"))
            st.write("本益比:",info.get("trailingPE"))
            st.write(info.get("longBusinessSummary",""))

# 技術分析
elif menu=="技術分析":
    code=st.text_input("股票代碼","2330")
    t,hist,info=get_stock(code)
    if not hist.empty:
        hist["MA5"]=hist["Close"].rolling(5).mean()
        hist["MA20"]=hist["Close"].rolling(20).mean()
        hist["MA60"]=hist["Close"].rolling(60).mean()

        st.subheader("均線")
        st.line_chart(hist[["Close","MA5","MA20","MA60"]])

        delta=hist["Close"].diff()
        gain=(delta.where(delta>0,0)).rolling(14).mean()
        loss=(-delta.where(delta<0,0)).rolling(14).mean()
        rs=gain/loss
        hist["RSI"]=100-(100/(1+rs))

        st.subheader("RSI")
        st.line_chart(hist["RSI"])

# AI預測
elif menu=="AI預測":
    code=st.text_input("股票代碼","2330")
    t,hist,info=get_stock(code)

    if PROPHET and not hist.empty:
        df=hist.reset_index()[["Date","Close"]]
        df.columns=["ds","y"]
        model=Prophet()
        model.fit(df)
        future=model.make_future_dataframe(periods=30)
        forecast=model.predict(future)
        st.line_chart(forecast.set_index("ds")["yhat"])
    else:
        st.warning("AI預測無法使用")

# 公司新聞
elif menu=="公司新聞":
    code=st.text_input("股票代碼","2330")
    t=yf.Ticker(code+".TW")
    try:
        news=t.news
        for n in news[:10]:
            st.write(n["title"])
            st.write(n.get("publisher",""))
            st.write(n.get("link",""))
            st.write("---")
    except:
        st.write("沒有新聞")

# AI概念股
elif menu=="AI概念股":
    ai={
    "2330":"台積電",
    "2454":"聯發科",
    "3443":"創意",
    "3661":"世芯",
    "6669":"緯穎"
    }
    for c,n in ai.items():
        st.write(c,n)

# 低價股掃描
elif menu=="低價股掃描":
    watch=["1101","1216","1301","2303","2317","2603","2882"]
    res=[]
    for c in watch:
        t=yf.Ticker(c+".TW")
        h=t.history(period="1d")
        if not h.empty:
            p=h["Close"].iloc[-1]
            if p<20:
                res.append((c,p))
    if res:
        st.dataframe(pd.DataFrame(res,columns=["股票","價格"]))
    else:
        st.write("沒有符合條件股票")

# 模擬交易
elif menu=="模擬交易":
    st.write("現金",st.session_state.cash)
    code=st.text_input("股票","2330")
    qty=st.number_input("股數",1)
    if st.button("買入"):
        t=yf.Ticker(code+".TW")
        h=t.history(period="1d")
        if not h.empty:
            price=h["Close"].iloc[-1]
            cost=price*qty
            if st.session_state.cash>=cost:
                st.session_state.cash-=cost
                st.session_state.portfolio[code]=st.session_state.portfolio.get(code,0)+qty
                st.success("買入成功")
            else:
                st.error("資金不足")
    if st.button("查看持股"):
        st.write(st.session_state.portfolio)

# 股利計算
elif menu=="股利計算器":
    price=st.number_input("股價",100.0)
    yield_rate=st.number_input("殖利率 %",5.0)
    shares=st.number_input("股數",1000)
    dividend=price*(yield_rate/100)*shares
    st.write("預估股利",dividend)

elif menu=="投資教學":
    st.write("EPS=每股盈餘")
    st.write("PE=本益比")
    st.write("RSI=動能指標")
