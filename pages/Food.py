import streamlit as st


st.image("phf01L.jpg")
st.header("RECIPE OF THE DAY")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Beef")
   st.markdown("Chunks of well-marbled beef are seared in a hot pan, then gently braised with garlic and onions in a rich wine-based broth. After a few hours in the oven, the meat becomes meltingly tender and enveloped in a deeply flavorful sauce.")
   st.write("[BEEF](https://www.onceuponachef.com/recipes/beef-stew-with-carrots-potatoes.html)")

with col2:
   st.header("Chicken")
   st.markdown(" One of the reasons we love chicken, and likely why it’s so popular, is just how adaptable this poultry can be. You can make a super simple chicken recipe in just thirty minutes, without sacrificing flavor, or you can use chicken to make a show-stopping main dish. ")
   st.write("[CHICKEN](https://www.foodandwine.com/meat-poultry/chicken)")

with col3:
   st.header("Vegetable")
   st.markdown("At least nine different families of fruits and vegetables exist, each with potentially hundreds of different plant compounds that are beneficial to health. Eat a variety of types and colors of produce in order to give your body the mix of nutrients it needs. This not only ensures a greater diversity of beneficial plant chemicals but also creates eye-appealing meals.")

   st.write("[VEGETABLE / FRUITS](https://www.hsph.harvard.edu/nutritionsource/what-should-you-eat/vegetables-and-fruits/)")
   
   
   
#st.image("kmt05.jpg")


         
