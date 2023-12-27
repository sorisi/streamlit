import streamlit as st


st.image("kmt01.jpg")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Politics")
   st.markdown("Civil rights organizations are asking the full 8th U.S. Circuit Court of Appeals to review a ruling by a three-judge panel that threatens to make it harder to enforce the Voting Rights Act's protections against racial discrimination in the election process.")
   st.write("[POLITICS](https://www.npr.org/2023/12/11/1218306963/voting-rights-act-section-2-private-right-of-action)")

with col2:
   st.header("World")
   st.markdown("A lot has been said in this context about central bank digital currencies (CBDCs), covering issues including data security and what separates them from other digital currencies. See below for a series of explainers on CBDCs and what they mean for people and economies. ")
   st.write("[WORLD](https://www.weforum.org/agenda/2023/12/economy-news-2023-inflation-banking-jobs/)")

with col3:
   st.header("Sports")
   st.markdown(" These historic shirts are not only a tangible reminder of one of the most important moments in the history of sports, but are principally connected to the pinnacle moment in the career of the most decorated football player in history ")
   st.write("[SPORT](https://sports.yahoo.com/lionel-messis-2022-world-cup-jerseys-sell-for-78-million-at-auction-180211598.html)")
   
st.image("kmt06.jpg")