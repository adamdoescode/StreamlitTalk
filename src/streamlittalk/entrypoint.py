"""
Custom navigation requires a wrapper entry point page.
Any styling or stuff we put on this page becomes shared across all pages.
Which can be a bit messy!
"""

import page_navigation
import streamlit as st
from streamlit.navigation.page import StreamlitPage

pg: StreamlitPage = st.navigation(
    pages=page_navigation.page_list,
    position="sidebar",
)
pg.run()
