import streamlit as st

st.header("Home of Savings or Investment (SORI)")

st.image("logo031.png")


col1, col2, col3 = st.columns(3)

with col1:
   st.header("Bank")
   st.markdown("A majority of hard-working Americans have savings accounts with traditional “brick and mortar” banks that pay around 0.40% APY. Most local hometown credit unions don’t do much better. In fact, the FDIC national average savings account is hovering around 0.45% APY. ")

with col2:
   st.header("Stock")
   st.markdown("Investing in stocks is a great way to build wealth by harnessing the power of growing companies. Getting started can feel daunting for many beginners looking to get into the stock market despite the potential long-term gains, but you can start buying stock in minutes. ")

with col3:
   st.header("News")
   st.markdown("Cryptocurrency is a consistent headliner among alternative investments—both for being an opportunity for quick and dramatic gains, and for its vulnerabilities. Though cryptocurrency is still finding its footing with regulations and academically-substantiated valuation metrics, it continues to have sticking power with investors. ")
   
st.image("gain01.png")