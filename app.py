import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI台股投資系統", layout="wide")

st.title("AI台股投資系統 V10")
st.info("提供即時行情、AI選股、ETF分析、模擬交易與新手教學")

# 側邊選單
menu = st.sidebar.selectbox(
    "功能選單",
    [
        "首頁",
        "即時行情",
        "AI選股",
        "ETF分析",
        "模擬交易",
        "投資教學"
    ]
)

# 首頁
if menu == "首頁":
    st.header("系統功能")

    st.write("""
    - 即時台股行情
    - AI選股與飆股雷達
    - ETF分析
    - 股票新聞
    - 模擬交易
    - 投資教學
    """)

# 即時行情
elif menu == "即時行情":
    st.header("即時行情")

    stock = st.text_input("輸入股票代號", "2330")

    st.write("即時行情功能示範")
    st.write("股票:", stock)

# AI選股
elif menu == "AI選股":
    st.header("AI推薦股票")

    data = {
        "股票": ["2382", "3231", "3017"],
        "公司": ["廣達", "緯創", "奇鋐"],
        "AI評分": [91, 88, 85],
        "推薦原因": [
            "AI伺服器需求爆發",
            "輝達供應鏈",
            "散熱需求增加"
        ]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)

# ETF分析
elif menu == "ETF分析":

    st.header("熱門ETF")

    data = {
        "ETF": ["0050", "0056", "00878", "00919", "00713", "00929"],
        "名稱": [
            "元大台灣50",
            "元大高股息",
            "國泰永續高股息",
            "群益高股息",
            "元大高息低波",
            "復華科技優息"
        ],
        "殖利率": [3.2, 6.5, 6.1, 7.0, 5.8, 6.4]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)

# 模擬交易
elif menu == "模擬交易":

    st.header("模擬交易")

    money = 1000000

    stock = st.text_input("股票代號")

    qty = st.number_input("買入股數", 0)

    if st.button("模擬買入"):
        st.success("模擬買入成功")

# 投資教學
elif menu == "投資教學":

    st.header("新手投資教學")

    st.subheader("什麼是EPS")
    st.write("EPS代表公司每股賺多少錢")

    st.subheader("什麼是ETF")
    st.write("ETF是一次投資一籃子股票")
