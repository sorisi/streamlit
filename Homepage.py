import streamlit as st
import numpy as np

st.set_page_config( page_title="Multipage App")
#st.title("Welcome to SORI")

st.header("Home of Savings or Investment (SORI)")
#st.sidebar.header("Homepage")
#st.image("banner02.png")
#st.sidebar.latex(r'''  a+b x^2+c''')

#st.sidebar.image("phd012.jpg")
#st.sidebar.checkbox("Login")
#st.sidebar.button("Login")

col1, col2, col3 = st.columns(3)

with col1:
   st.image("phs01.jpg")

with col2:
   st.image("graffiti.jpg")

with col3:
   st.image("phws01.jpg")
with col1:
   st.image("phf02.jpg")

with col2:
   st.image("ph10.jpg")

with col3:
   st.image("phf01.jpg")
with col1:
   st.image("lon02.jpg")

with col2:
   st.image("snow.jpg")

with col3:
   st.image("lon01.jpg")
   
st.image("kmt10.jpg")