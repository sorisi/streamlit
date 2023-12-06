import streamlit as st


st.image("kmt01.jpg")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Politics")
   st.markdown("Democracy is arguably the greatest political buzzword of our time and is invoked by political leaders, corporations and citizens alike– but what does it mean? Can it be defined, measured, safeguarded? Can it be sold, bought, and transplanted? Can it grow? Can it die? What does it mean to people who can’t even talk about it? What does it mean to people who don’t believe in it?")
   st.write("[Why Democracy](https://www.thewhy.dk/docuseries/why-democracy?gad_source=1&gclid=EAIaIQobChMIktiqs7D3ggMV1ltHAR0q3wQuEAAYASAAEgJMdPD_BwE)")

with col2:
   st.header("World")
   st.markdown(" The order was part of mass evacuations Israel called for in southern Gaza, where tens of thousands of displaced Palestinians have sought refuge as Israel’s quest to route Hamas continues in the form of renewed bombardment and a widened ground offensive. With Israel’s negotiators summoned home over the weekend and Hamas insisting on a permanent cease-fire before releasing any more hostages, the onslaught was renewed ")
   st.write("[WHO Chief](https://www.yahoo.com/news/chief-begs-israel-rescind-order-212000523.html)")

with col3:
   st.header("Sports")
   st.markdown(" Nix was just as outstanding as Daniels was during the season. He had the Ducks on the verge of a College Football Playoff berth, but two losses to Penix’s Huskies put them out of contention. In 13 games, he had 4,145 passing yards and 40 touchdown passes. He transferred from Auburn after the 2021 season.  ")
   st.write("[Bo Nix](https://www.foxnews.com/sports/heisman-trophy-2023-jayden-daniels-bo-nix-michael-penix-jr-and-marvin-harrison-jr-named-finalists)")
   
st.image("kmt06.jpg")