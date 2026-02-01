from pathlib import Path
import streamlit as st

st.markdown(
    (Path(__file__).parents[1] / "markdown_snippets" / "credits.md").read_text()
)
