
import streamlit as st
import pandas as pd
import random

st.title("📈 市場總覽")

stocks = ["2330 台積電","2317 鴻海","2454 聯發科","3231 緯創","2382 廣達"]

cols = st.columns(len(stocks))

for i,s in enumerate(stocks):
    price = round(random.uniform(100,2000),2)
    change = round(random.uniform(-5,5),2)
    cols[i].metric(s, price, f"{change}%")
