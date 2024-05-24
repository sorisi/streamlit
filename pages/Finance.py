import streamlit as st

st.header("Home of Savings or Investment (SORI)")

st.image("Finance01.png")


col1, col2, col3 = st.columns(3)

with col1:
   st.header("Bank")
   st.markdown(" Ms. Yellen’s comments came in the wake of Israel’s decision on Wednesday to withhold tax revenue from the Palestinian Authority in retaliation for three European countries’ unilaterally agreeing to recognize a Palestinian state. Ms. Yellen and other top economic officials from the Group of 7 nations are expected to discuss the matter and the humanitarian situation in Gaza during their summit in Stresa, Italy ")
   st.image("https://ichef.bbci.co.uk/news/1024/cpsprodpb/b822/live/64150340-18e9-11ef-b374-753f4dd92fb2.jpg.webp")
   st.write("[Bank](https://www.nytimes.com/2024/05/23/business/yellen-israel-gaza-palestinian-banks.html)")

with col2:
   st.header("Stock")
   st.markdown("What I found is summarized in the chart below. To construct it, I segregated all presidential elections since the Dow Jones Industrial Average DJIA was established in 1896 into four equal-sized groups based on its year-to-date return on Election Day. As you can see, the probabilities of the incumbent party retaining the White House grow in lockstep with year-to-date performance. ")
   st.image("https://s.yimg.com/ny/api/res/1.2/ybfgz5z9dKi9B.rR4ltpPA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTY2NztjZj13ZWJw/https://media.zenfs.com/en/marketwatch_hosted_869/b0e58d8f0deec9b7a754c379f2764a2c")
   st.write("[Stock](https://finance.yahoo.com/news/stock-market-already-chosen-winner-123000226.html)")

with col3:
   st.header("Real Estate")
   st.markdown(" Commercial real estate has been behind the eight ball for some time now, for all those pandemic-fallout-work-from-home reasons we’ve heard. But now there’s a really bad sign as to how deep the hole goes. For the first time since the financial crisis, investors in top-rated bonds backed by commercial real estate debt are getting hit with losses.")
   st.image("https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iPsvaKrGFG7c/v0/1200x800.jpg")
   st.write("[Real Estate](https://www.bloomberg.com/news/newsletters/2024-05-23/bloomberg-evening-briefing-a-really-bad-sign-for-commercial-real-estate)")
   
st.image("Finance02.png")