
import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="AI台股投資平台", layout="wide")

# -----------------------------
# Mock stock database
# -----------------------------
data = [
    {"code":"2330","name":"台積電","price":600,"eps":32,"sector":"半導體","ai":"AI晶片"},
    {"code":"2382","name":"廣達","price":250,"eps":12,"sector":"電子","ai":"AI伺服器"},
    {"code":"3231","name":"緯創","price":115,"eps":6,"sector":"電子","ai":"AI伺服器"},
    {"code":"2376","name":"技嘉","price":300,"eps":15,"sector":"電子","ai":"AI GPU"},
    {"code":"1513","name":"中興電","price":9.8,"eps":1.2,"sector":"電機","ai":"無"},
    {"code":"2406","name":"國碩","price":8.3,"eps":0.9,"sector":"電子","ai":"無"},
]

df = pd.DataFrame(data)

# -----------------------------
# Beginner explanations
# -----------------------------
def explain_eps():
    st.info("EPS（每股盈餘）：代表公司每一股賺多少錢。EPS越高通常代表公司越賺錢。")

def explain_pe(price, eps):
    if eps > 0:
        pe = price / eps
        st.info(f"本益比 PE = 股價 / EPS → {price}/{eps} = {round(pe,2)}")
    else:
        st.info("公司目前沒有獲利，無法計算本益比")

# -----------------------------
# AI prediction mock
# -----------------------------
def ai_prediction(price):
    future7 = round(price * random.uniform(0.95,1.05),2)
    future30 = round(price * random.uniform(0.9,1.1),2)
    confidence = random.randint(60,90)

    st.subheader("AI股價預測")
    st.write("AI根據歷史資料模擬預測未來價格（示範功能）")

    st.table({
        "時間":["7天","30天"],
        "預測價格":[future7,future30]
    })

    st.success(f"AI信心度：{confidence}%")
    st.caption("AI預測僅供參考，投資仍需自行判斷")

# -----------------------------
# Stock health check
# -----------------------------
def stock_health(price, eps):
    score = random.randint(60,95)

    if eps > 5:
        growth = "高"
    elif eps > 1:
        growth = "中"
    else:
        growth = "低"

    risk = random.choice(["低","中","高"])

    st.subheader("股票健檢報告")
    st.table({
        "項目":["AI評分","成長性","風險"],
        "結果":[f"{score}分",growth,risk]
    })

# -----------------------------
# Simulated trading state
# -----------------------------
if "cash" not in st.session_state:
    st.session_state.cash = 1000000
if "portfolio" not in st.session_state:
    st.session_state.portfolio = []

# -----------------------------
# Sidebar feature selection
# -----------------------------
st.sidebar.title("功能選單")

feature = st.sidebar.radio(
    "選擇功能",
    [
        "股票搜尋",
        "AI預測中心",
        "AI概念股",
        "低價股雷達",
        "股票健檢",
        "模擬交易",
        "投資教學"
    ]
)

st.title("AI台股投資平台（新手版）")

# -----------------------------
# Stock search
# -----------------------------
if feature == "股票搜尋":

    code = st.text_input("輸入股票代碼")

    if code:
        result = df[df["code"]==code]

        if len(result)>0:

            stock = result.iloc[0]

            st.table(result)

            explain_eps()
            explain_pe(stock.price, stock.eps)

        else:
            st.warning("查無資料")

# -----------------------------
# AI prediction
# -----------------------------
elif feature == "AI預測中心":

    code = st.selectbox("選擇股票", df["code"])

    stock = df[df["code"]==code].iloc[0]

    st.write("目前股價:", stock.price)

    ai_prediction(stock.price)

# -----------------------------
# AI stocks
# -----------------------------
elif feature == "AI概念股":

    ai_df = df[df["ai"]!="無"]

    st.subheader("AI概念股")
    st.dataframe(ai_df)

# -----------------------------
# Low price radar
# -----------------------------
elif feature == "低價股雷達":

    low = df[df["price"]<20]

    st.subheader("低價股 (<20元)")
    st.dataframe(low)

# -----------------------------
# Stock health
# -----------------------------
elif feature == "股票健檢":

    code = st.selectbox("選擇股票", df["code"])

    stock = df[df["code"]==code].iloc[0]

    st.write("股票:", stock.name)
    st.write("股價:", stock.price)
    st.write("EPS:", stock.eps)

    stock_health(stock.price, stock.eps)

# -----------------------------
# Simulated trading
# -----------------------------
elif feature == "模擬交易":

    st.write("目前資金:", st.session_state.cash)

    code = st.selectbox("股票", df["code"])
    qty = st.number_input("股數",1,1000,1)

    stock = df[df["code"]==code].iloc[0]
    cost = stock.price * qty

    if st.button("買入"):
        if st.session_state.cash >= cost:

            st.session_state.cash -= cost

            st.session_state.portfolio.append({
                "code":code,
                "price":stock.price,
                "qty":qty
            })

            st.success("模擬買入成功")

        else:
            st.error("資金不足")

    st.subheader("投資組合")

    if st.session_state.portfolio:

        port = pd.DataFrame(st.session_state.portfolio)
        st.dataframe(port)

    else:
        st.write("尚未持有股票")

# -----------------------------
# Education
# -----------------------------
elif feature == "投資教學":

    st.subheader("股票基礎知識")

    st.markdown("**EPS（每股盈餘）**：公司每一股賺多少錢")

    st.markdown("**本益比（PE）**：股價 / EPS，用來判斷股票估值")

    st.markdown("**營收YoY**：今年營收與去年相比的成長率")

    st.info("新手建議：先用模擬交易熟悉市場")
