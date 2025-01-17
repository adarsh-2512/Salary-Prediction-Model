import streamlit as st

# Set Streamlit theme
st.set_page_config(
    page_title="Salary Prediction App",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="expanded",
)

from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
