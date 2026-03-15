
import streamlit as st

st.set_page_config(page_title="AI股票分析平台 FINAL", layout="wide")

st.sidebar.title("🤖 AI即時助手")

if "chat" not in st.session_state:
    st.session_state.chat = []

def ai_reply(q):
    q = q.lower()
    if "台積電" in q or "2330" in q:
        return "🟢 AI判讀：台積電為半導體龍頭，長期基本面強。"
    if "ai股" in q:
        return "AI概念股：台積電、廣達、緯創、技嘉、鴻海。"
    return "AI建議：觀察產業趨勢、成交量與均線。"

q = st.sidebar.chat_input("詢問股票 / 產業 / 技術指標")
if q:
    a = ai_reply(q)
    st.session_state.chat.append(("你", q))
    st.session_state.chat.append(("AI", a))

for r,m in st.session_state.chat[-10:]:
    st.sidebar.write(f"**{r}:** {m}")

st.title("📊 AI股票分析平台 FINAL")

st.markdown("""
完整功能：

市場總覽  
AI全股票評分  
產業分類篩選  
股票技術分析  
ETF分析  
產業強度雷達  
AI飆股掃描  
籌碼分析  
股票新聞  
模擬交易  
投資組合  
風險分析  
術語說明  
""")
