import streamlit as st
import requests 
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)
local_css(r"C:\Users\navee\Desktop\Python\style.css")

lottie_coding = load_lottieurl("https://lottie.host/d2043e88-85dc-4684-90ba-1a59be0262e9/nHrmaPwGwE.json")
img_contact_form = (r'C:\Users\navee\Desktop\Python\images.png')

#Header of Who I Am
with st.container():
    st.subheader("Hi, I am Naveen Indraj")
    st.title("A Senior in High School")
    st.write("")
    st.write("[Learn More >](https://docs.google.com/document/d/1apzeYNn_quBYJQJXLRdFRJcN_oil2nPzbMhWnSHLKac/edit?usp=sharing)")

#Header with Info 
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
    """_summary_
    """
        )
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")

with st.container():
    st.write("---")
    st.header("My Work")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        file_path = r"C:\Users\navee\Desktop\Python\images.png"
        with open(file_path, "w") as file:
            new_content = img_contact_form
            file.write(new_content)
        print("File content modified successfully!")
    with text_column:
        st.write(""" """)
        st.write(""" """)

with st.container():
    st.write("---")
    st.header("Email Submission")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/indnav33@gmail.com" method="POST">
        <input type="hidden" name="_capthca" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email"required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()