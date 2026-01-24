"""
Access point for the streamlit app we will use to present
the talk.
"""

from pathlib import Path

import page_navigation
import streamlit as st

FILE_DIR = Path(__file__).parent

if __name__ == "__main__":
    st.title("Streamlit is good! (for some things!)")
    """But it's bad that it prints this line... since it is in a docstring."""
    st.markdown((FILE_DIR / "markdown_snippets" / "homepage.md").read_text())
    for page_obj in page_navigation.page_list:
        # st.page_link lets you just pass in the page object to generate a pretty link - neat!
        st.page_link(page_obj)
