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
import streamlit.components.v1 as components
def embed_tableau_dashboard():
    st.title("Tableau Public Dashboard")
    st.markdown("Here's the embedded Tableau Public Dashboard:")
    


    components.iframe("<div class='tableauPlaceholder' id='viz1712349261627' style='position: relative'><noscript><a href='#'><img alt='Revenue ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sp&#47;Spotilytics&#47;Revenue&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Spotilytics&#47;Revenue' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sp&#47;Spotilytics&#47;Revenue&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1712349261627');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='1277px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>",height=200)
    # Replace the URL below with the URL of your Tableau Public dashboard
    # tableau_url = "<div class='tableauPlaceholder' id='viz1712349261627' style='position: relative'><noscript><a href='#'><img alt='Revenue ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sp&#47;Spotilytics&#47;Revenue&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Spotilytics&#47;Revenue' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sp&#47;Spotilytics&#47;Revenue&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1712349261627');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='1277px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    
    # Use an iframe to embed the Tableau dashboard
    # st.components.v1.html(f'<iframe src="{tableau_url}" width="1000" height="600" frameborder="0"></iframe>', height=700)


    


st.set_page_config(page_title="Spotilytics",\
                   page_icon = ":tada:",\
                    layout="wide")

# Define pages
# pages = {
#     "Home": home,
#     "ER_Diagram": ER_Diagram,
#     "Insert Query": page2,
#     "Delete Query" : delete_query_for_podcast,
#     "Select Query" : select_queries_select,
#     "Update Query" : update_query,
#     "Dashboard": embed_tableau_dashboard# Add more pages as needed
# }

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