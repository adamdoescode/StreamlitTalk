"""
Streamlit only allows us to define each st.Page object once.
So we set them up in this little .py as we want to import them
into two different locations: homepage.py and entrypoint.py.
If you just defined this in entrypoint.py and then imported
the page_list in homepage.py the app will double print the
contents of homepage.py because it reinitialises the page_list
and thus homepage.py! Recursion!
"""

import streamlit as st
from streamlit.navigation.page import StreamlitPage

page_list: list[StreamlitPage] = [
    st.Page(page="./homepage.py", title="Start!", icon="🏡"),
    st.Page(page="./pages/intro.py", title="Introduction", icon="📖"),
    st.Page(
        page="./pages/dataframes_and_plots.py", title="Dataframes and plots", icon="🍴"
    ),
    st.Page(page="./pages/streamlit_pages.py", title="Multi-page apps", icon="🗒️"),
    st.Page(page="./pages/maps.py", title="Maps", icon="🗺️"),
    st.Page(page="./pages/state_and_caching.py", title="State and caching", icon="🇦🇺"),
    st.Page(page="./pages/example.py", title="Simple Example", icon="🎈"),
    st.Page(page="./pages/credits.py", title="Credits (thanks)", icon="❤️"),
]
