from pathlib import Path
import streamlit as st

FILE_DIR = Path(__file__)
SNIPPETS_DIR = FILE_DIR.parents[1] / "markdown_snippets"

if __name__ == "__main__":
    st.title("Introduction")
    st.markdown((SNIPPETS_DIR / "intro_1.md").read_text(), unsafe_allow_html=True)
    # this must be relative to where we call streamlit run from
    st.image(image="media/ytho.jpg", width=300)
    st.markdown((SNIPPETS_DIR / "intro_2.md").read_text())
