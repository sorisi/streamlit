import streamlit as st

st.header("Home of Savings or Investment (SORI)")

st.image("Finance01.png")


col1, col2, col3 = st.columns(3)

with col1:
   st.header("Bank")
   st.markdown("The rate-cut-mania-inspired plunge in longer-term yields at the end of Q4, now partially reverse, had a salubrious effect on the balance sheets of commercial banks, according to the FDIC’s quarterly bank data released on Thursday.  ")
   st.write("[Bank](https://wolfstreet.com/2024/03/10/the-banks-unrealized-losses-securities-held-by-banks-bank-failures-and-the-dropping-bank-count/)")

with col2:
   st.header("Stock")
   st.markdown("The stock has soared over the past decade, and while e-commerce remains the company's largest source of revenue, its other segments are making notable contributions to its profits and success. ")
   st.write("[Stock](https://finance.yahoo.com/news/buying-super-stock-59-could-092600615.html)")

with col3:
   st.header("Real Estate")
   st.markdown("Chinese investors, once among the most active buyers of commercial property in the United States, sold US$31.7 billion of US commercial real estate between 2019 and last year, 15 times more than what they acquired during the same period, according to MSCI Real Assets, a real estate and infrastructure data provider. ")
   st.write("[Real Estate](https://www.scmp.com/property/article/3254787/chinese-investors-offloaded-us317-billion-us-commercial-real-estate-over-last-five-years-driven)")
   
st.image("Finance02.png")