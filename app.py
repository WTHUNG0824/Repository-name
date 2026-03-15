
import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI台股投資系統 V10", layout="wide")

st.title("AI台股投資系統 V10")
st.info("提供即時行情、AI選股、ETF分析、模擬交易與新手教學")

st.header("系統功能")
st.markdown("""
- 即時台股行情
- AI選股與飆股雷達
- ETF分析
- 股票新聞
- 模擬交易
- 投資教學
""")

st.header("熱門ETF")
data = {
"ETF":["0050","0056","00878","00919","00713","00929"],
"名稱":["元大台灣50","元大高股息","國泰永續高股息","群益高股息","元大高息低波","復華台灣科技優息"],
"殖利率":[3.2,6.5,6.1,7.0,5.8,6.4]
}
st.dataframe(pd.DataFrame(data),use_container_width=True)
