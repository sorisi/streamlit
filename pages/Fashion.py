import streamlit as st


st.image("Fashion05.png")

col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("Current")
   st.markdown(" British department store retailer John Lewis has introduced a selection of menswear brands to its rental offering in response to heightened demand from consumers on its e-commerce site.  ")
   st.image("https://fashionunited.com/r/fit=cover,format=auto,gravity=center,height=463,quality=70,width=694/https://fashionunited.com/img/upload/2024/05/23/menswear-rental-hugo-boss-lloxlpkr-2024-05-23.jpeg")
   st.write("[Current](https://fashionunited.com/news/fashion/john-lewis-launches-mens-rental-service-responding-to-significant-demand/2024052360015)")
   

with col2:
   st.subheader("Yesteryear")
   st.markdown("The noughties enthusiast has built an online following from her comedic takedowns of yesteryear's trends. The creator has once again gone viral after poking fun at images of herself from 2009, in which she is rocking the hottest styles of that year. ")
   st.image("https://d.newsweek.com/en/full/2396609/jenna-barclay.webp?w=790&f=a1b4452c39a9f4929d9945331a937533")
   st.write("[Yesteryears](https://www.newsweek.com/woman-social-media-noughties-fashion-1902900)")
   
with col3:
   st.subheader("Modern")
   st.markdown(" Turner wheeled a silver Rimowa cabin case decked out with a smorgasbord of luggage stickers. From afar, the pair could have been mistaken for travelers from the 1960s (though Lipa’s cherry Coke-colored tresses and Puma sneakers slightly give the game away), wistfully accruing mementos and keepsakes from trips abroad. ")
   st.image("https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-2114886211.jpg?q=w_2000,c_fill/f_webp")
   st.write("[Modern](https://www.cnn.com/2024/03/29/style/dua-lipa-callum-turner-lotw/index.html)")
   
   
st.image("Fashion04.png")