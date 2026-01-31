"""
Reinventing powerpoint slides in Streamlit:
    An introduction to how streamlit allows control of state
"""

from pathlib import Path

import streamlit as st

from pages.counter_state import state_demo
from pages.slideshow_utils import header_setup


def on_slide_change():
    """
    The selectbox needs a *second* item in state
    otherwise we are recursively modifying the slide state...
    """
    st.session_state["state_slide"] = st.session_state.slide_select


def slideshow() -> None:
    """
    Orchestrator function for our powerpoint slides.
    """
    header_setup(n_slides=len(slides), session_slide_key="state_slide")
    st.selectbox(
        label="Page",
        # options=slides,
        options=[i for i, _ in enumerate(slides)],
        key="slide_select",
        on_change=on_slide_change,
    )
    st.divider()
    st.markdown(markdown_content[slides[st.session_state["state_slide"]]])

    # this approach is fragile and crude. I would like to improve it...
    if st.session_state["state_slide"] == 1:
        state_demo()
    if st.session_state["state_slide"] == 2:
        with st.expander("Whats in session_state right now?"):
            st.write(st.session_state)
    if st.session_state["state_slide"] == 4:
        if st.button("Try st.rerun!"):
            st.rerun()


markdown_content: dict[str, str] = {
    content.split("\n")[1].replace("## ", "").strip(): content
    for content in (Path(__file__).parents[1] / "markdown_snippets" / "state.md")
    .read_text()
    .split("---")
}

slides: dict[int, str] = {i: x for i, x in enumerate(markdown_content.keys())}
if "state_slide" not in st.session_state:
    st.session_state["state_slide"] = 0


if "slide_select" not in st.session_state:
    st.session_state.slide_select = 0

slideshow()
