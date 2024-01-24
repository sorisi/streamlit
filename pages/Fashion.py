import streamlit as st


st.image("Fashion05.png")

col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("Current")
   st.markdown(" Being a mob wife is a full-time job. Not only are you probably privy to unsavoury information and sworn to some kind of life-altering secrecy, but you must also always look fabulous. How does one embody this all-encompassing attitude? By curating the perfect mob wife outfit.")
   st.image("https://fashionmagazine.com/wp-content/uploads/2024/01/HORIZONTAL-FEATURE-IMAGE-TEMPLATE-1200x800-c-top.png")
   st.write("[Current](https://fashionmagazine.com/style/shopping/mob-wife-outfit/)")
   

with col2:
   st.subheader("Yesterday")
   st.markdown(" When Christian Dior’s “New Look” appeared in February 1947, it became an instant success and the nipped-in waist and full-skirted silhouette remained the leading style until the mid-1950s. As the decade progressed, the dominant silhouette became progressively straighter and slimmer, and as fashion began to look to the new “teenager” for inspiration, the elegance and formality of the early part of the decade began to lessen.")
   st.image("https://fashionhistory.fitnyc.edu/wp-content/uploads/2017/08/1950-fashionc-1280x640.jpg")
   st.write("[Yesteryears](https://fashionhistory.fitnyc.edu/1950-1959/)")
   
with col3:
   st.subheader("Modern")
   st.markdown("While modern and classic fashion style are two very different movements, they also have many similarities that allow fashionistas to experiment with both. Creating clothing combinations of neutral wardrobe essentials and bold modern garments could be quite successful. ")
   st.image("https://d2line.com/thatlook/wp-content/uploads/sites/4/2022/08/mediterranean-style-d2line-modern-fashion.png")
   st.write("[Modern](https://d2line.com/thatlook/modern-vs-classic-fashion-style/)")
   
   
st.image("Fashion04.png")