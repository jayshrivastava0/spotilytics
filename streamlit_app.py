from PIL import Image
import streamlit as st
from home_page import *
from insert_queries import *
from delete_query import *
from select_queries import *
from update_queries import *
from revenue_dashboard import *
from users_dashboard import *
import os


base_path = os.getcwd()

def ER_Diagram():
    st.title("ER Diagram of Spotilytics Database")
    image = Image.open(os.path.join(base_path, "images/ER.png"))
    st.image(image, use_column_width=True)



st.set_page_config(page_title="Spotilytics",\
                   page_icon = ":tada:",\
                    layout="wide")


st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Select Page", ["Home", "ER Diagram", \
                                                 "Insert Query", "Delete Query",\
                                                 "Select Query", "Update Query", \
                                                 "Revenue Dashboard", "Users Dashboard"])
showSidebarNavigation = True
# Display the selected page content
if selected_page == "Home":
    home()
elif selected_page == "ER Diagram":
    ER_Diagram()
elif selected_page == "Insert Query":
    page2()
elif selected_page == "Delete Query":
    delete_query_for_podcast()
elif selected_page == "Select Query":
    select_queries_select()
elif selected_page == "Update Query":
    update_query()
elif selected_page == "Revenue Dashboard":
    revenue_tableau_dashboard()
elif selected_page == "Users Dashboard":
    users_tableau_dashboard()