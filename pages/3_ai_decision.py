
import streamlit as st

st.title("AI Investment Decision")

stock = st.text_input("Stock","2330.TW")

c1,c2,c3,c4 = st.columns(4)

c1.metric("OpenAI","BUY")
c2.metric("Claude","WATCH")
c3.metric("Gemini","BULLISH")
c4.metric("DeepSeek","CAUTION")

st.success("Combined AI Recommendation: Bullish")
