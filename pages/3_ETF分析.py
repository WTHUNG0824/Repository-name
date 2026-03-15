
import streamlit as st
import pandas as pd

st.title("ETF分析")

data={
"ETF":["0050","0056","00878","00919"],
"配息":["半年","季","季","月"],
"殖利率":[3.2,6.5,6.1,7.0]
}

st.dataframe(pd.DataFrame(data),use_container_width=True)
