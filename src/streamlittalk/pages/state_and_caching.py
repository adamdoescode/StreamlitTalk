"""
Reinventing powerpoint slides in Streamlit:
    An introduction to how streamlit allows control of state
"""

from pathlib import Path

import numpy as np
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
        options=[i for i, _ in enumerate(slides)],
        key="slide_select",
        on_change=on_slide_change,
        format_func=lambda x: slides[x],
    )
    st.divider()
    slide_key: str = slides[st.session_state["state_slide"]]
    st.markdown(markdown_content[slide_key])

    # this approach is fragile and crude. I would like to improve it...
    if slide_key == "Why we need to use *state*":
        state_demo()
    if slide_key in [
        "Powerpoint slides in Streamlit!",
        "What is State?",
        "(Screaming) Why is it stuck at 1??!",
    ]:
        with st.expander("Whats in session_state right now?"):
            st.write(st.session_state)
    if slide_key == "The trouble with `st.rerun`":
        if st.button("Try st.rerun!"):
            st.rerun()


if "rng" not in st.session_state:
    st.session_state["rng"] = np.random.randint(0, 100)

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
