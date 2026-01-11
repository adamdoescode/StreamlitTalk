"""
Access point for the streamlit app we will use to present
the talk.
"""

from pathlib import Path
import streamlit as st


FILE_DIR = Path(__file__).parent

if __name__ == "__main__":
    st.title("Streamlit is good! (for some things!)")
    # keeping markdown text in a .py is messy, so we keep snippets elsewhere and read them in
    st.markdown((FILE_DIR / "markdown_snippets" / "homepage.md").read_text())
