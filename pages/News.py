import streamlit as st


st.image("News01.png")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Politics")
   st.markdown("The sudden burst of support for an industry with a relatively small base of users is the culmination of a yearslong effort to win legitimacy — and lighter-touch regulatory treatment — in Washington. The push, which is now backed by tens of millions of dollars in political spending funded by crypto executives and investors, is proving to be resilient in the face of major scandals that have sent industry leaders to prison and highlighted risks in what critics deride as the “Wild West” of finance.")
   st.write("[POLITICS](https://www.politico.com/news/2024/05/23/crypto-2024-election-impact-00159506)")

with col2:
   st.header("World")
   st.markdown("sraeli Prime Minister Benjamin Netanyahu and his government are finding themselves increasingly boxed into a corner. Netanyahu is waging a devastating war in the Gaza Strip that has riled global public opinion and placed him and his government before two of the world’s most significant courts. ")
   st.write("[WORLD](https://www.washingtonpost.com/world/2024/05/23/israel-isolation-icj-ruling-gaza/)")

with col3:
   st.header("Sports")
   st.markdown("The deal still must be approved by the federal judge overseeing the case and challenges could arise, but if the agreement stands it will mark the beginning of a new era in college sports where athletes are compensated more like professionals and schools can compete for talent using direct payments. ")
   st.write("[SPORT](https://www.baltimoresun.com/2024/05/23/ncaa-leagues-back-2-8-billion-settlement-setting-stage-for-dramatic-change-across-college-sports/)")
   
st.image("news02.png")
