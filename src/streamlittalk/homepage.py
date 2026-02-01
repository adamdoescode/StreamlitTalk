"""
Access point for the streamlit app we will use to present
the talk.
"""

from pathlib import Path

import page_navigation
import streamlit as st

FILE_DIR = Path(__file__).parent

if __name__ == "__main__":
    st.markdown("# Streamlit is good!")
    st.markdown("## :grey[(for some things!)]")
    st.divider()
    col1, col2 = st.columns(spec=[1, 1])
    with col1:
        st.markdown("#### :orange[By Adam Graham]")
    with col2:
        st.markdown("#### :blue[PythonWA Talk]")
        st.markdown("#### :red[February 2026]")
    st.divider()
    """## Page Links"""
    for page_name, page_obj in page_navigation.page_list.items():
        # st.page_link lets you just pass in the page object to generate a pretty link - neat!
        st.page_link(page_obj)
