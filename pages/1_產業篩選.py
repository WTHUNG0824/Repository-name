
import streamlit as st
import json

st.title("🏭 產業股票篩選")

industry_map=json.load(open("industry_map.json",encoding="utf-8"))
company_map=json.load(open("company_map.json",encoding="utf-8"))

inds=list(industry_map.keys())
inds.insert(0,"全部產業")

sel=st.selectbox("選擇產業",inds)

stocks=[]

if sel=="全部產業":
    for v in industry_map.values():
        stocks+=v
else:
    stocks=industry_map[sel]

for s in stocks:
    st.write(f"{s}  {company_map.get(s,'')}")
