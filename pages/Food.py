import streamlit as st


st.image("phf01L.jpg")
st.header("RECIPE OF THE DAY")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Beef")
   st.markdown("Our Mongolian beef is incredibly quick and easy to make. In fact, it can be made in under 30 minutes making it a perfect weeknight dinner! Serve it with a little steamed rice and broccoli and you have a quick, delicious and flavor packed complete meal! We love making a double batch so we have plenty of leftovers to enjoy the next day.")
   st.write("[Beef Recipe](https://www.spoonforkbacon.com/mongolian-beef-over-steamed-rice/)")

with col2:
   st.header("Chicken")
   st.markdown(" This homemade chicken soup recipe is well worth making — it's good for the body and the soul. How is it that plain chicken and vegetables simmered together can taste so satisfying? You don't have to be sick to deserve to enjoy it!")
   st.write("[Chicken Soup](https://www.allrecipes.com/recipe/8814/homemade-chicken-soup/)")

with col3:
   st.header("Vegetable")
   st.markdown("A diet rich in vegetables and fruits can lower blood pressure, reduce the risk of heart disease and stroke, prevent some types of cancer, lower risk of eye and digestive problems, and have a positive effect upon blood sugar, which can help keep appetite in check. Eating non-starchy vegetables and fruits like apples, pears, and green leafy vegetables may even promote weight loss.")

   st.write("[Vegatables & Fruits](https://www.hsph.harvard.edu/nutritionsource/what-should-you-eat/vegetables-and-fruits/)")
   

st.image("veg01.jpg")
   

         