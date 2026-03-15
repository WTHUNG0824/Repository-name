
import streamlit as st

st.set_page_config(page_title="AI投資研究平台 V500",layout="wide",page_icon="📊")

st.title("📊 AI專業投資研究平台 V500")

st.markdown("""
本系統為 **完整投資研究平台架構**

主要模組

📈 市場總覽  
📉 K線技術分析  
🤖 AI投資評級  
🚀 AI自動選股  
🏭 產業分類  
🏦 籌碼分析  
📰 利多利空新聞  
📊 ETF完整資料庫  
💼 投資組合管理  
💰 模擬交易系統  
📚 投資教學  
""")

st.sidebar.title("🤖 AI投資助手")

if "chat" not in st.session_state:
    st.session_state.chat=[]

def ai_reply(q):
    q=q.lower()
    if "0050" in q:
        return "AI評級：🟢長期配置\n原因：大型權值股ETF、流動性高"
    if "00919" in q:
        return "AI評級：🟡收益型配置\n原因：高股息策略"
    return "AI建議：觀察產業趨勢、成交量與基本面。"

q=st.sidebar.chat_input("詢問股票 / ETF / 投資問題")

if q:
    r=ai_reply(q)
    st.session_state.chat.append(("你",q))
    st.session_state.chat.append(("AI",r))

for a,b in st.session_state.chat[-10:]:
    st.sidebar.write(f"**{a}:** {b}")
