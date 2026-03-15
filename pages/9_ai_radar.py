
import streamlit as st, random, json

st.title("AI Momentum Radar")

stocks=["2382.TW","3231.TW","2454.TW","2330.TW"]
company=json.load(open("company_map.json",encoding="utf-8"))

for s in random.sample(stocks,2):
    st.success("Potential stock: "+s+" "+company.get(s,""))
