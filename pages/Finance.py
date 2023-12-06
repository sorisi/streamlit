import streamlit as st

st.header("Home of Savings or Investment (SORI)")

st.image("logo031.png")


col1, col2, col3 = st.columns(3)

with col1:
   st.header("Bank")
   st.markdown("When managing your personal finances, we understand the convenience you need—and the attention you deserve. That’s why at International Finance Bank, we believe in going the extra mile to simplify your big financial decisions along with your everyday tasks. ")
   st.write("[Bank](https://www.ifbbank.com/)")

with col2:
   st.header("Stock")
   st.markdown(" Stocks were on a rocket last month. Now they’re coming down to Earth somewhat. The three major indices were mixed Tuesday, with the Dow falling for a second straight day, the S&P 500 sliding a touch and the Nasdaq posting a slight gain.")
   st.write("[Stock](https://www.cnbc.com/2023/12/06/5-things-to-know-before-the-stock-market-opens-wednesday-december-6.html)")

with col3:
   st.header("Real Estate")
   st.markdown(" Industry economists with the real estate listings website determined the top 10 housing markets that are expected to fare well in 2024 in terms of sales growth. Home sales are expected to rise slightly over the coming year nationwide, but Realtor.com expects markets in the Northeast, Midwest and Southern California.")
   st.write("[Real Estate](https://www.foxbusiness.com/lifestyle/top-housing-markets-for-2024)")
   
st.image("HM01.jpg")