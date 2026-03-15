
import streamlit as st
import pandas as pd
import random

st.title("📡 產業強度雷達")

industries=["AI","半導體","電動車","伺服器","光通訊"]
strength=[random.randint(50,100) for _ in industries]

df=pd.DataFrame({"產業":industries,"強度":strength})
st.bar_chart(df.set_index("產業"))
