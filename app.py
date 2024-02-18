pip install streamlit-lottie

import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/Best-sites-and-practices-for-monitoring-hotel-reviews (1).png")
img_lottie_animation = Image.open("images/Opiod stock photo.jpg")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Sakthi Jaisankar :wave:")
    st.title("A Data Scientist")
    st.write(
        "Motivated and results-driven Mathematics graduate, Offering a strong foundation in Machine Learning models, data analysis, and SQL, with a proven ability to predict future data, deliver successful outcomes and collaborate within cross-functional teams.."
    )
    st.write("[Learn More >](https://www.linkedin.com/in/sakthijaisankar)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            As a data scientist with six months of experience: 
            - I primarily focus on tasks such as cleaning and preprocessing data, 
            - Conducting exploratory data analysis (EDA), 
            - Building and evaluating machine learning models,
            - Communicating insights through data visualization. 
            
            Collaboration with team members and effective communication of findings are also essential aspects 
            of my role."
            """
        )
        st.write("[Git >](https://github.com/sakthijaisankar)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Drug Satisfaction predictor")
        st.write(
            """
            Conducted Exploratory Data Analysis (EDA) and Regression modeling, achieving 85percent accuracy in predicting drug satisfaction rates for various diseases.
            Developed and deployed a Drug Satisfaction Rate predictor with a 70percent confidence level, accessible via an HTML website, aiding in treatment decisions for specific diseases.
            Enabled 60percent of hospitals to predict drug satisfaction, facilitating informed treatment selection and management.
            """
        )
        st.markdown("[Explore Our Project...](https://drive.google.com/drive/folders/1iaGzfPeO6OsmcFUq7MizDa7jMPvefQjv?usp=drive_link)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Hotel Reviews Analysis")
        st.write(
            """
            Conducted text analysis on over 20,000 hotel reviews to extract insights.
            Identified key trends and sentiments within the reviews to gauge customer satisfaction.
            Provided actionable recommendations based on the analysis to improve overall hotel experience and customer satisfaction.
            """
        )
        st.markdown("[Explore Our Project...](https://drive.google.com/drive/folders/172jz77fmAaD2BJp1mT3ohHcPxwDWuUyM?usp=drive_link)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/sakthineg007@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
