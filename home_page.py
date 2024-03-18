from PIL import Image
import streamlit as st
import os

base_path = os.getcwd()

# Define page content functions
def home():
    # st.markdown('<style>body{background-color: Yellow;}</style>',unsafe_allow_html=True)
    st.markdown(
        f"<h1 style='text-align: center; font-size: 85px; color: #FF0000'>Welcome to Spotilytics</h1>",
        unsafe_allow_html=True
    )
    st.title("What is Spotilytics, you ask?")
    
    ## Header section
    # st.title("Hi, This is our Home Page for Spotilytics")
    st.markdown(
        f'<h3 style="color: #F5F5F5;">Spotilytics is a comprehensive database management and analytics project designed to compute \
    essential business Key Performance Indicators (KPIs). It monitors metrics such as customer churn analysis, \
    monthly active users (MAU), Customer Lifetime Value (CLV), and Gross Revenue, providing valuable insights \
    for strategic decision-making and performance evaluation within the Spotify platform. Performed other analyses\
     like Geotargeting, Follower Count, and Regional Genre Analysis to gain deeper insights into user engagement, \
     demographic trends, and cultural preferences across different markets, ultimately enhancing content curation, \
     personalized recommendations, and platform optimization strategies.</h2>',
        unsafe_allow_html=True
    )
    # st.subheader("Spotilytics is a comprehensive database management and analytics project designed to compute \
    # essential business Key Performance Indicators (KPIs). It monitors metrics such as customer churn analysis, \
    # monthly active users (MAU), Customer Lifetime Value (CLV), and Gross Revenue, providing valuable insights \
    # for strategic decision-making and performance evaluation within the Spotify platform. Performed other analyses\
    #  like Geotargeting, Follower Count, and Regional Genre Analysis to gain deeper insights into user engagement, \
    #  demographic trends, and cultural preferences across different markets, ultimately enhancing content curation, \
    #  personalized recommendations, and platform optimization strategies.", className="gray-text")


    with st.container():
        st.title("")
        st.subheader("")
        st.subheader("")
        st.subheader("")
        st.subheader("")
        st.subheader("")
        st.subheader("")
        st.subheader("")
        st.markdown(
        f"<h1 style='text-align: center; font-size: 45px;'>Contributors of Spotilytics</h1>",    
        unsafe_allow_html=True
    )
    ## priya's container
    with st.container():
        st.title("Priya")
        left_col, right_col = st.columns(2)
        with left_col:
            st.subheader("I was incharge of creating and optimizing queries by studying execution plan, cost and \
                      applying appropriate indexing as well. I also created the Tableau Public Visualizations. I can't wait to apply all this learnt knowledge \
                       in real world.")
            
        with right_col:

            image_path = os.path.join(base_path, "images/priya.jpg")
            priya_image = Image.open(image_path)
            st.image(priya_image, use_column_width=True)


    ## jay's container
    with st.container():
        left_col, right_col = st.columns(2)
        with right_col:
            st.title("Sujay")
            st.subheader("I created fake dataset and integrated it to postgres.\
                      I was incharge of creating the self contained website and \
                      establishing a connection to the postgres. I also deployed this website.\
                       Additionally, I also helped Priya in optimization the query")

        with left_col:
            image_path = os.path.join(base_path, "images/jay.jpg")
            jay_image = Image.open(image_path)
            st.image(jay_image, use_column_width=True)

