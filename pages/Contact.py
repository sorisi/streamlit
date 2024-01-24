import streamlit as st

contact_form = """
<form action="https://formsubmit.co/tfcasa@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.header("Home of Savings or Investment (SORI)")
st.image("Contact03.png")
st.subheader(":mailbox: Get in Touch")

st.container()
st.markdown(contact_form, unsafe_allow_html=True)
def local_css(file_name):
  with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
local_css("style/style.css")

st.image("Contact04.png")