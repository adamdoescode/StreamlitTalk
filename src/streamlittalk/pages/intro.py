# import Path from pathlib for files, yes, you should do this instead of whatever curses os and sys imports chatgpt is telling you to use
from pathlib import Path

# this is how we import streamlit
import streamlit as st
from pages.slideshow_utils import header_setup

# get the filepath, mostly this avoids broken relative paths for the streamlit server
# using Pathlib means we get the handy `.read_text()` method too!
FILE_DIR = Path(__file__)

# read in markdown snippets and split by a known seperator `---`
# use level 2 titles as keys so we dont have to worry about order so much!
markdown_content: dict[str, str] = {
    content.split("\n")[1].replace("## ", "").strip(): content
    for content in (FILE_DIR.parents[1] / "markdown_snippets" / "intro_1.md")
    .read_text()
    .split("---")
}


def on_slide_change():
    """
    The selectbox needs a *second* item in state
    otherwise we are recursively modifying the slide state...
    """
    st.session_state["slide"] = st.session_state.slide_select


def slideshow():
    # st.title makes a title.
    st.title("Introduction")
    slides: dict[int, str] = {i: x for i, x in enumerate(markdown_content.keys())}
    if "slide" not in st.session_state:
        st.session_state["slide"] = 0
    header_setup(n_slides=len(slides))
    st.selectbox(
        label="Page",
        # options=slides,
        options=[i for i, _ in enumerate(slides)],
        key="slide_select",
        on_change=on_slide_change,
        format_func=lambda x: slides[x],
    )
    st.divider()

    st.markdown(markdown_content[slides[st.session_state.slide]])
    if slides[st.session_state.slide].lower() == "what is streamlit?":
        st.image(image="media/streamlit_gh.png", width=300)
        st.markdown("- Enough already! What does the code look like??")
        st.code(body=(FILE_DIR.parents[1] / "pages" / "example.py").read_text())
        # st.code prints strings formatted as code with syntax highlighting.
        st.markdown("- Here's the code for this page:")
        with st.expander("Page code"):
            st.code(
                body=FILE_DIR.read_text(),
                line_numbers=True,
            )
    if slides[st.session_state.slide].lower() == "y tho?":
        st.image(image="media/ytho.jpg", width=300)
    if slides[st.session_state.slide].lower() == "similar to...":
        with st.expander("Minimal dash app code:"):
            st.markdown(
                (
                    FILE_DIR.parents[1] / "markdown_snippets" / "minimal_dash_app.md"
                ).read_text()
            )
    if slides[st.session_state.slide].lower() == "pros":
        dummy_upload = st.file_uploader(label="Upload example widget")
        if dummy_upload:
            st.write(f"Uploaded: {dummy_upload.name}")
    if slides[st.session_state.slide].lower() == "cons":
        st.markdown("- Here's the code for this page:")
        with st.expander("Page code"):
            st.code(
                body=FILE_DIR.read_text(),
                line_numbers=True,
            )


if "slide_select" not in st.session_state:
    st.session_state.slide_select = 0

slideshow()
