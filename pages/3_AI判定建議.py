
import streamlit as st

st.title("AI判定建議")

ai_model = st.selectbox(
"選擇AI模型",
["OpenAI","DeepSeek","Claude","Gemini"]
)

stock = st.text_input("股票代碼","2330.TW")

if st.button("AI分析"):

    st.subheader("AI分析結果")

    st.write("AI模型:",ai_model)

    st.write("趨勢判定: 偏多")
    st.write("支撐區: 20日均線附近")
    st.write("壓力區: 前高")
    st.write("風險評估: 中等")
    st.write("操作建議: 回檔分批布局")
