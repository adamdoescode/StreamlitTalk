"""
Custom navigation requires a wrapper entry point page.
We launch our app from here.
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

# to illustrate the "thing on every page" feature/bug (its kinda both to my eyes)
# we'll comment this out. But look for it at the bottom of the page since it
# executes after (?) the page content.
# st.title("🐢🐢🐢 TURTLES FOR EVERY PAGE 🐢🐢🐢")
