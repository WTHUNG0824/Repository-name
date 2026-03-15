
import streamlit as st
import pandas as pd
import random

st.title("📈 市場總覽")

stocks=["2330 台積電","2317 鴻海","2454 聯發科","2382 廣達","3231 緯創"]

data={
"股票":stocks,
"價格":[random.randint(80,900) for _ in stocks],
"漲跌%":[round(random.uniform(-3,3),2) for _ in stocks]
}

df=pd.DataFrame(data)

st.dataframe(df,use_container_width=True)
st.bar_chart(df.set_index("股票")["漲跌%"])
