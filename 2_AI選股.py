
import streamlit as st
import pandas as pd

st.title("AI推薦股票")

data={
"股票":["2382 廣達","3017 奇鋐","2376 技嘉"],
"AI評分":[91,88,87],
"理由":[
"AI伺服器需求爆發",
"散熱需求成長",
"AI PC 與 GPU 需求"
]
}

st.dataframe(pd.DataFrame(data),use_container_width=True)
