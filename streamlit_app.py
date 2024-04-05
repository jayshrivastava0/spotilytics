from PIL import Image
import streamlit as st
from home_page import *
from insert_queries import *
from delete_query import *
from select_queries import *
from update_queries import *
import os


base_path = os.getcwd()

def ER_Diagram():
    st.title("ER Diagram of Spotilytics Database")
    image = Image.open(os.path.join(base_path, "images/ER.png"))
    st.image(image, use_column_width=True)



import streamlit as st

def embed_tableau_dashboard():
    st.title("Tableau Public Dashboard")
    st.markdown("Here's the embedded Tableau Public Dashboard:")
    
    # Replace the URL below with the URL of your Tableau Public dashboard
    tableau_url = "https://public.tableau.com/app/profile/priyadarshini.raghavendra/viz/Spotilytics/Revenue"
    
    # Use an iframe to embed the Tableau dashboard
    st.components.v1.html(f'<iframe src="{tableau_url}" width="1000" height="600" frameborder="0"></iframe>', height=700)


    


st.set_page_config(page_title="Spotilytics",\
                   page_icon = ":tada:",\
                    layout="wide")

# Define pages
pages = {
    "Home": home,
    "ER_Diagram": ER_Diagram,
    "Insert Query": page2,
    "Delete Query" : delete_query_for_podcast,
    "Select Query" : select_queries_select,
    "Update Query" : update_query
    "Dashboard": embed_tableau_dashboard# Add more pages as needed
}

st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Select Page", ["Home", "ER Diagram", "Insert Query", "Delete Query", "Select Query", "Update Query", "Dashboard"])
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
elif selected_page == "Dashboard":
    embed_tableau_dashboard()