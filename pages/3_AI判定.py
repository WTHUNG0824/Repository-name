
import streamlit as st

st.title("🤖 AI投資建議")

stock=st.text_input("股票","2330.TW")

st.subheader("AI模型分析")

c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric("OpenAI","偏多 📈")

with c2:
    st.metric("DeepSeek","偏多 📈")

with c3:
    st.metric("Claude","中性 ⚖️")

with c4:
    st.metric("Gemini","偏多 📈")

st.divider()

st.subheader("AI綜合建議")

st.table({
"判定":["🟢 建議買入","🟡 觀望","🔴 不建議"],
"說明":[
"趨勢強＋基本面良好",
"盤整或不明確",
"風險偏高"
]
})

st.success("AI建議：🟡 觀望等待回檔")
