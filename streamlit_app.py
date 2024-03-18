from PIL import Image
import streamlit as st
from home_page import *
from insert_queries import *
from delete_query import *
from select_queries import *
from update_queries import *
import os


base_path = os.getcwd()

def ER_diagram():
    st.title("ER Diagram of Spotilytics Database")
    image = Image.open(os.path.join(base_path, "images/ER.png"))
    st.image(image, use_column_width=True)





st.set_page_config(page_title="Spotilytics",\
                   page_icon = ":tada:",\
                    layout="wide")

# Define pages
pages = {
    "Home": home,
    "ER Diagram": ER_diagram,
    "Insert Query": page2,
    "Delete Query" : delete_query_for_podcast,
    "Select Query" : select_queries_select,
    "Update Query" : update_query
    # Add more pages as needed
}

st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Select Page", ["Home", "ER Diagram", "Insert Query", "Delete Query", "Select Query", "Update Query"])
showSidebarNavigation = True
# Display the selected page content
if selected_page == "Home":
    home()
elif selected_page == "ER_diagram":
    ER_diagram()
elif selected_page == "Insert Query":
    page2()
elif selected_page == "Delete Query":
    delete_query_for_podcast()
elif selected_page == "Select Query":
    select_queries_select()
elif selected_page == "Update Query":
    update_query()