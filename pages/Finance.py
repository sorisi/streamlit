import streamlit as st

st.header("Home of Savings or Investment (SORI)")

st.image("Finance01.png")


col1, col2, col3 = st.columns(3)

with col1:
   st.header("Bank")
   st.markdown("Nearly 170 former employees of California's failed First Republic Bank have sued the U.S. Federal Deposit Insurance Corporation (FDIC), alleging that the regulator is improperly blocking their access to at least $150 million in retirement funds, a plaintiffs' attorney said on Monday.  ")
   st.write("[Bank](https://www.reuters.com/business/finance/former-first-republic-workers-sue-fdic-over-withheld-retirement-pay-2023-12-18/)")

with col2:
   st.header("Stock")
   st.markdown("I’ve talked about several companies employing the new AI technology in a variety of ways. But, there are also non-technology centric (at least not AI focused technology) ways to get in on the AI boom, that should have long term legs regardless of how AI is eventually employed.  ")
   st.write("[Stock](https://stocknews.com/news/vrt-nvda-hon-this-ai-backbone-stock-should-win-big-in-the-ai/)")

with col3:
   st.header("Real Estate")
   st.markdown("The housing in our neighborhoods should be homes for people, not profit centers for Wall Street,” said Merkley. “Yet, in every corner of the country, giant financial corporations are buying up housing and driving up both rents and home prices. It’s time for Congress to put in place commonsense guardrails that ensure all families have a fair chance to buy or rent a decent home in their community at a price they can  ")
   st.write("[Real Estate](https://wrenews.com/new-bill-would-ban-hedge-funds-from-owning-single-family-homes/)")
   
st.image("Finance02.png")