"""
Reinventing powerpoint slides in Streamlit:
    An introduction to how streamlit allows control of state
"""

from pathlib import Path

import streamlit as st

from pages.counter_state import state_demo


markdown_content: dict[str, str] = {
    content.split("\n")[1].replace("## ", "").strip(): content
    for content in (Path(__file__).parents[1] / "markdown_snippets" / "state.md")
    .read_text()
    .split("---")
}


def header_setup(slides: list[str]) -> None:
    n_slides = len(slides)
    # streamlit allows for column (flexbox) syntax:
    # our list into st.columns defines width
    col1, col2, col3 = st.columns(spec=[1, 2, 1])

    with col1:
        if st.button("⬅️ Previous", disabled=st.session_state.slide == 0):
            st.session_state.slide -= 1
            st.rerun()

    with col2:
        st.markdown(f"#### Slide {st.session_state.slide + 1}", text_alignment="center")

    with col3:
        if st.button("Next ➡️", disabled=st.session_state.slide == n_slides - 1):
            st.session_state.slide += 1
            st.rerun()


def on_slide_change():
    """
    The selectbox needs a *second* item in state
    otherwise we are recursively modifying the slide state...
    """
    st.session_state.slide = slides.index(st.session_state.slide_select)


def slideshow() -> None:
    """
    Orchestrator function for our powerpoint slides.
    """
    header_setup(slides=slides)
    # horizontal rule to split our header from the body
    st.selectbox(
        label="Page",
        # options=slides,
        options=[i for i, _ in enumerate(slides)],
        key="slide_select",
        on_change=on_slide_change,
    )
    st.divider()
    st.markdown(markdown_content[slides[st.session_state.slide]])
    if st.session_state.slide == 1:
        state_demo()
    if st.session_state.slide == 2:
        with st.expander("Whats in session_state right now?"):
            st.write(st.session_state)
    if st.session_state.slide == 4:
        if st.button("Try st.rerun!"):
            st.rerun()


slides = list(markdown_content.keys())
if "slide" not in st.session_state:
    st.session_state["slide"] = 0


if "slide_select" not in st.session_state:
    st.session_state.slide_select = 0

slideshow()
