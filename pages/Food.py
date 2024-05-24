import streamlit as st


st.image("Food04.png")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Meat")
   st.markdown("Ground meat products, particularly ground beef and chicken, are items I would avoid purchasing from grocery store butcher counters. The bulk of these products come pre-ground from large meat processing facilities, where the risk of contamination is significantly higher.")
   st.image("https://img.huffingtonpost.com/asset/663d17b126000034008bcaab.jpeg?ops=scalefit_720_noupscale&format=webp")
   st.write("[MEAT](https://www.huffpost.com/entry/worst-meat-to-buy_l_66353524e4b05f96b0185689)")

with col2:
   st.header("Pasta")
   st.markdown(" While the fresh cheese can be enjoyed in any seat in the house, the restaurant said the wheel pasta bar makes for a unique experience as guests are able to see up-and-personal the chef’s working to plate the creamy pasta dishes. ")
   st.image("https://www.eatingwell.com/thmb/poitmxoMCGphCW4uId5XvfNiqkw=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/6691966-235e96dcfaaf4d098b4d217c4e6b9f73.jpg")
   st.write("[PASTA](https://fox5sandiego.com/news/business/san-diegos-first-cheese-wheel-pasta-bar-opens-in-little-italy/)")

with col3:
   st.header("Vegetable")
   st.markdown("While all vegetables are healthy and can help lower the risk of cancer, if you aren’t used to eating vegetables regularly, it can be helpful to start by focusing on incorporating one into your meals regularly. ")
   st.image("https://parade.com/.image/c_limit%2Ccs_srgb%2Cq_auto:good%2Cw_700/MjA2NTczNTczMTU2OTA2MTg4/best-vegetable-for-cancer-prevention-according-to-oncologists.webp")
   st.write("[VEGETABLE / FRUITS](https://parade.com/health/best-vegetable-for-cancer-prevention-according-to-oncologists)")
   
   
   
st.image("Food01.png")


         
