import streamlit as st


st.image("Food04.png")
st.header("RECIPE OF THE DAY")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Meat")
   st.markdown("The highly coveted “Extreme Croquettes” are one of four types of Kobe beef croquettes available at Asahiya. Can’t wait nearly four decades? The shop’s Premier Kobe Beef Croquettes currently have a more palatable four-year waitlist.")
   st.write("[MEAT](https://www.cnn.com/travel/japanese-kobe-beef-croquettes-43-year-wait-list-intl-hnk/index.html)")

with col2:
   st.header("Pasta")
   st.markdown(" Shrimp and pasta are an incredibly versatile pairing and a winning dinner solution. So, when you want a light dinner with protein, vegetables, and some pasta to fill you up, these shrimp pasta recipes are the way to go. Shrimp can handle spices from all around the world­; ­­­­they're equally as delicious with olive oil, parsley, and lemon as they are with mango,")
   st.write("[PASTA](https://www.marthastewart.com/shrimp-pasta-recipes-8547437)")

with col3:
   st.header("Vegetable")
   st.markdown("In a world grappling with challenges like population growth, climate change and food security, a new approach to agriculture is on the horizon. Vertical farming is growing crops on vertically stacked layers in a controlled environment.")

   st.write("[VEGETABLE / FRUITS](https://www.farmprogress.com/vegetables/1218f1-3407-slideshow)")
   
   
   
st.image("Food01.png")


         
