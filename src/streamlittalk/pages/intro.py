# import Path from pathlib for files, yes, you should do this instead of whatever curses os and sys imports chatgpt is telling you to use
from pathlib import Path

# this is how we import streamlit
import streamlit as st

# get the filepath, mostly this avoids broken relative paths for the streamlit server
FILE_DIR = Path(__file__)
# and i put the markdown chunks in this folder...
SNIPPETS_DIR = FILE_DIR.parents[1] / "markdown_snippets"


def read_file(filename: str | Path = FILE_DIR) -> str:
    """Read this file!! Or another if non-default filename passed.
    Return as a string"""
    with open(filename) as f:
        return f.read()


if __name__ == "__main__":
    """Runs if we open this page in the streamlit server"""
    # st.title makes a title. Has some other arguments btw.
    st.title("Introduction")
    # st.expander creates a nice little expander for our content.
    # use it with `with` for maximum pythonic clarity (and whitespace)
    with st.expander("What is Streamlit?", expanded=True):
        # st.markdown supports markdown formatted text - very neat.
        st.markdown((SNIPPETS_DIR / "intro_1.md").read_text())

        st.markdown("- Enough already! What does it look like??")
        st.code(body=read_file(FILE_DIR.parents[1] / "pages" / "example.py"))
        # st.code prints strings formatted as code with syntax highlighting.
        st.markdown("- Here's the code for this page:")
        with st.expander("Page code"):
            st.code(
                body=read_file(),
                line_numbers=True,
            )
    with st.expander("Why tho?"):
        st.markdown("# Why tho?")
        # this must be relative to where we call streamlit run from
        st.image(image="media/ytho.jpg", width=300)
        st.markdown((SNIPPETS_DIR / "intro_2.md").read_text())

    with st.expander("Similar to..."):
        st.markdown("## Similar to...")
        st.markdown((SNIPPETS_DIR / "intro_3.md").read_text())
