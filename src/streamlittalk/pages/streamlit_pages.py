from pathlib import Path

import streamlit as st

FILE_DIR = Path(__file__)

# Actually, it's easier to have a single markdown with an obvious
# page seperate, e.g. `---` and just split that into a dict and then
# use it.
md_text = (FILE_DIR.parents[1] / "markdown_snippets" / "pages_1.md").read_text()
md_page_text = {page: content for page, content in enumerate(md_text.split("---"))}

st.title("Multi-page apps in Streamlit")
with st.expander("Implementing multiple pages", expanded=True):
    # we can use .get() so that we dont get an ugly error
    st.markdown(md_page_text.get(0, "No content found!"))
with st.expander("A Pages Directory", expanded=False):
    st.markdown(md_page_text.get(1, "No content found!"))
with st.expander("Configuration with `st.navigation` and `st.pages`", expanded=False):
    st.markdown(md_page_text.get(2, "No content found!"))
with st.expander("Configuration (my experience)", expanded=False):
    st.markdown(md_page_text.get(3, "No content found!"))
