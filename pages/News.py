import streamlit as st


st.image("News01.png")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Politics")
   st.markdown("Democracy is arguably the greatest political buzzword of our time and is invoked by political leaders, corporations and citizens alike– but what does it mean? Can it be defined, measured, safeguarded? Can it be sold, bought, and transplanted? Can it grow? Can it die? What does it mean to people who can’t even talk about it? What does it mean to people who don’t believe in it?")
   st.write("[POLITICS](https://www.thewhy.dk/docuseries/why-democracy?gad_source=1&gclid=EAIaIQobChMI4JuRptr0gwMVjElHAR1hKQHjEAAYAiAAEgKZfvD_BwE)")

with col2:
   st.header("World")
   st.markdown("Lawmakers ratified Sweden’s accession protocol 287 to 55, with ruling party members saying the Nordic country’s tougher stance on Kurdish militants was key to winning approval. President Recep Tayyip Erdogan also previously has linked the ratification to Turkey’s desire to buy fighter jets from the U.S. ")
   st.write("[WORLD](https://apnews.com/article/turkey-sweden-nato-kurdish-militants-quran-ff81aa2d36160428d766579963f97fce)")

with col3:
   st.header("Sports")
   st.markdown(" Japan coach Hajime Moriyasu said he was ashamed and appalled to see his goalkeeper Zion Suzuki subjected to racial abuse on social media after they lost their second Asian Cup group game against Iraq last week.")
   st.write("[SPORT](https://www.reuters.com/sports/soccer/japan-coach-moriyasu-appalled-by-racist-abuse-directed-keeper-suzuki-2024-01-23/)")
   
st.image("News02.png")