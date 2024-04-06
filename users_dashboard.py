import streamlit as st
import streamlit.components.v1 as components

def users_tableau_dashboard():
    st.title("[Tableau Users' Insights Dashboard](https://public.tableau.com/views/Spotilytics-Users/Users?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link)")
    html_code = """
    <div class='tableauPlaceholder' id='viz1712365791020' style='position: relative'>
        <noscript>
            <a href='#'>
                <img alt='Users ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sp&#47;Spotilytics-Users&#47;Users&#47;1_rss.png' style='border: none' />
            </a>
        </noscript>
        <object class='tableauViz'  style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='Spotilytics-Users&#47;Users' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sp&#47;Spotilytics-Users&#47;Users&#47;1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
        </object>
    </div>
    <script type='text/javascript'>
        var divElement = document.getElementById('viz1712365791020');
        var vizElement = divElement.getElementsByTagName('object')[0];
        if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} 
        else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} 
        else { vizElement.style.width='100%';vizElement.style.height='1277px';} 
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>
    """
    components.html(html_code, height=800, scrolling=True)

