import streamlit as st


st.image("Fashion05.png")

col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("Current")
   st.markdown("Goodbye, lumpy puffers and salt-caked boots. Hello, spring 2024 fashion trends! If your wardrobe is starting to feel a bit tired after months of gray skies and howling winds, you’re in luck—a new season is on the way, bringing plenty of fresh inspiration from the spring runways along with it.  ")
   st.image("https://media.glamour.com/photos/65cce0375ea0c25e5b06764f/master/w_1920,c_limit/spring%202024%20fashion%20trends.jpg")
   st.write("[Current](https://www.glamour.com/story/2024-fashion-trends)")
   

with col2:
   st.subheader("Yesterday")
   st.markdown(" Remakes are everywhere right now – from TV shows to movies to music – even history tends to repeat itself. And fashion is no different. Styles have a tendency to show up again every few decades. As teens of the ‘90s, some of us wish we had held on to our clothing from that decade. Let’s take a look at what’s as trendy now as it was years ago.")
   st.image("https://www.mycitymag.com/wp-content/uploads/2022/08/Style-082022-00-702x336.jpg")
   st.write("[Yesteryears](https://www.mycitymag.com/summer-trends-from-yesteryear/)")
   
with col3:
   st.subheader("Modern")
   st.markdown(" Today, fashion is quite a phenomenon. In the olden days, clothing would help people show their societal status, and it would be fashion that helped to navigate in creating their style for the world to see. In our time, fashion is different: for clothes, makeup, books, hairstyles, and interior design. ")
   st.image("https://www.fashiongonerogue.com/wp-content/uploads/2021/06/Model-Hijab-Head-Scarf-White-Outfit.jpg")
   st.write("[Modern](https://www.fashiongonerogue.com/what-know-fashion-modern-days/)")
   
   
st.image("Fashion04.png")