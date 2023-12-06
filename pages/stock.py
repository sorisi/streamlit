import streamlit as st
#import yfinance as yf
import pandas as pd
import numpy as np
import datetime
#import appdirs as ad
#ad.user_cache_dir = lambda *args: "/tmp"

st.header("Home of Savings or Investment (SORI)")
st.image("nov2023.png")

tickers = ('TSLA', 'AAPL', 'AMZN', 'SQ', 'COIN','BRK-B','BIT-USD', 'MSTR')

dropdown = st.multiselect('Pick your assets', 
                          tickers)

start = st.date_input('Start', value = pd.to_datetime('2021-11-01'))
end = st.date_input('End', value = pd.to_datetime('today'))

def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() -1
    cumret = cumret.fillna(0)
    return cumret

if len(dropdown) > 0:
    #df = yf.download(dropdown,start,end)['Adj Close']
    df = relativeret(yf.download(dropdown,start,end)['Adj Close'])
    st.header('*Returns of {}*'.format(dropdown))
    st.line_chart(df)

tab1, tab2, tab3, tab4, tab5 = st.sidebar.tabs(["AAPL", "TSLA", "SQ", "AMZN", "BRK-A"])

with tab1:
   st.header("AAPL")
   st.image("https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png?201609051049", width=50)

with tab2:
   st.header("TSLA")
   st.image("https://upload.wikimedia.org/wikipedia/commons/e/e8/Tesla_logo.png", width=50)

with tab3:
   st.header("SQ")
   st.image("https://upload.wikimedia.org/wikipedia/en/thumb/3/33/Block%2C_Inc_logo.png/170px-Block%2C_Inc_logo.png", width=50)
   
with tab4:
   st.header("AMZN")
   st.image("https://1000logos.net/wp-content/uploads/2016/10/Amazon-Logo.png", width=50)

with tab5:
   st.header("BRK-A")
   st.image("https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/vsnwi4ppyv3n8p3u9y9o", width=200)
   
st.image("kmt04.jpg")

