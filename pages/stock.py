import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import requests
from bs4 import BeautifulSoup

st.set_page_config( page_title="Multipage App")

st.header("Home of Savings or Investment (SORI)")

st.image("stock01.png")
col1, col2, col3 = st.columns(3)

with col1:
   st.image("phs01.jpg")

with col2:
   st.image("graffiti.jpg")

with col3:
   st.image("phws01.jpg")
with col1:
   st.image("Home04.png")

with col2:
   st.image("ph10.jpg")

with col3:
   st.image("Home03.png")
with col1:
   st.image("lon02.jpg")

with col2:
   st.image("snow.jpg")

with col3:
   st.image("lon01.jpg")
   
st.image("Home01.png")
st.image("stock02.png")