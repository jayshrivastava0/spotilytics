from PIL import Image
import streamlit as st
import os

base_path = os.getcwd()

# Define page content functions
def home():
    # st.markdown('<style>body{background-color: Yellow;}</style>',unsafe_allow_html=True)
    st.title("Welcome to the Home Page")
    
    ## Header section
    st.title("Hi, This is our deployed website for group project of Spotilytics")
    st.subheader("We are group of aspiring Data Science Students")

    ## priya's container
    with st.container():
        st.title("Priya")
        left_col, right_col = st.columns(2)
        with left_col:
            st.header("I was incharge of creating and optimizing queries by studying execution plan, cost and \
                      applying appropriate indexing as well. I can't wait to apply all this learnt knowledge \
                       in real world.")
            
        with right_col:

            image_path = os.path.join(base_path, "images/priya.jpg")
            priya_image = Image.open(image_path)
            st.image(priya_image, use_column_width=True)


    ## sanju's container
    with st.container():
        left_col, right_col = st.columns(2)
        with right_col:
            st.title("Sanju")
            st.header("I was heavily invested in creating the report and data integration part of intial stages")

        with left_col:
            image_path = os.path.join(base_path, "images/sanjukta.jpg")
            priya_image = Image.open(image_path)
            st.image(priya_image, use_column_width=True)

    # Jay's container
    with st.container():
        left_col, right_col = st.columns(2)
        with left_col:
            st.title("Sujay")
            st.header("I created fake dataset and integrated it to postgres.\
                      I was incharge of creating the self contained website and \
                      establishing a connection to the postgres. I also helped Priya in optimization")

        with right_col:
            image_path = os.path.join(base_path, "images/jay.jpg")
            priya_image = Image.open(image_path)
            st.image(priya_image, use_column_width=True)
