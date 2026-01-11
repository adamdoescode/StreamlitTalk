from pathlib import Path
import streamlit as st

FILE_DIR = Path(__file__)

if __name__ == "__main__":
    st.title("Introduction")
    st.markdown((FILE_DIR.parents[1] / "markdown_snippets" / "intro.md").read_text())
