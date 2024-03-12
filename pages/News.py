import streamlit as st


st.image("News01.png")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Politics")
   st.markdown("Every week political cartoonists throughout the country and across the political spectrum apply their ink-stained skills to capture the foibles, memes, hypocrisies and other head-slapping events in the world of politics. The fruits of these labors are hundreds of cartoons that entertain and enrage readers of all political stripes. Here's an offering of the best of this week's crop, picked fresh off the Toonosphere")
   st.write("[POLITICS](https://www.politico.com/gallery/2024/03/08/the-nations-cartoonists-on-the-week-in-politics-00145777?slide=0)")

with col2:
   st.header("World")
   st.markdown("It's become a bit of addiction - the world is so big and beautiful and a bike is fast enough that you can get from A to B, but slow enough - as I am only doing 80-100km a day that you get an opportunity to see the world properly and spend time with the people who inhabit it ")
   st.write("[WORLD](https://www.bbc.com/news/articles/cn04gyg2k86o)")

with col3:
   st.header("Sports")
   st.markdown("She's now the all-time leader for 3-point field goals made in a single NCAA season, a record that she'd previously tied, in company with Golden State Warriors legend and former Davidson star Stephen Curry and former Liberty guard Darius McGhee at 162. ")
   st.write("[SPORT](https://sports.yahoo.com/caitlin-clark-surpasses-stephen-curry-to-break-ncaa-record-for-3-pointers-in-a-season-011451636.html)")
   
st.image("news02.png")
