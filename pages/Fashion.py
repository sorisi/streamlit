import streamlit as st


st.image("toppf.png")

col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("Current")
   st.markdown(" Another year has come and gone, which means it’s time to start planning our vision boards for the year ahead. But first, let's talk about the 2023 style trends that experts predict will take over our closets.  ")
   st.image("https://img.kwcdn.com/garner-api/transfer/2023-9-22/88f1bdc6a4a58ac207142f980c9f22af.jpg?imageView2/2/w/800/q/70")
   st.write("[Current](https://www.glamour.com/story/2023-style-trends)")
   

with col2:
   st.subheader("Yesterday")
   st.markdown("All sorts of people, from doctors onwards, praised the new skirt, under the impression, apparently, that it had been prompted by the noblest of reasons. The woman of fashion was told that she had listened at last to the voice of hygiene, that in the interests of the public health she had ceased to sweep the germs of disease into the house. ")
   st.image("https://i.guim.co.uk/img/media/5b26f3109f485ae0ea8db7fa84de9a5b5286a822/0_196_3964_2378/master/3964.jpg?width=620&dpr=1&s=none")
   st.write("[Yesteryears](https://www.theguardian.com/fashion/2017/mar/14/skirts-fashion-archive-1906)")
   
with col3:
   st.subheader("Modern")
   st.markdown("Today, fashion is quite a phenomenon. In the olden days, clothing would help people show their societal status, and it would be fashion that helped to navigate in creating their style for the world to see. In our time, fashion is different: for clothes, makeup, books, hairstyles, and interior design.")
   st.image("https://www.fashiongonerogue.com/wp-content/uploads/2021/06/Model-Hijab-Head-Scarf-White-Outfit.jpg")
   st.write("[Modern](https://www.fashiongonerogue.com/what-know-fashion-modern-days/)")
   
   
st.image("kmt01.jpg")