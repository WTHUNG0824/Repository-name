
import streamlit as st, random, json

st.title("AI Market Scan")

stocks=["2330.TW","2317.TW","2454.TW","2382.TW","3231.TW"]
company=json.load(open("company_map.json",encoding="utf-8"))

st.write("Trending Stocks")

for s in random.sample(stocks,3):
    st.write(s, company.get(s,""))
