"""
Reinventing powerpoint slides in Streamlit:
    An introduction to how streamlit allows control of state
"""

from pathlib import Path

import streamlit as st


def read_markdown_content() -> dict[str, str]:
    markdown_content = {}
    for content in (
        (Path(__file__).parents[1] / "markdown_snippets" / "state.md")
        .read_text()
        .split("---")
    ):
        slide_name = content.strip("\n").split("\n")[0]
        markdown_content[slide_name] = "".join(
            content.strip("\n").split("\n", maxsplit=1)[1:]
        )
    return markdown_content


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


def state_demo() -> None:
    """
    On slide 2 we have two counter buttons,
    1. keeps it's state in a local variable
    2. holds it's state in st.session_state
    """
    st.divider()
    st.markdown("### Local variable")
    with st.expander("code", expanded=False):
        st.code(
            """local_count = 0
if st.button("Local counter (+1)"):
    local_count += 1
st.write(f"Local counter: **{local_count}**")"""
        )

    # local count code
    local_count = 0
    if st.button("Local counter (+1)"):
        local_count += 1
    st.write(f"Local counter: **{local_count}**")

    st.divider()
    st.markdown("### Session state")
    with st.expander("code", expanded=False):
        st.code(
            """if "session_count" not in st.session_state:
    st.session_state.session_count = 0
if st.button("Session counter (+1)"):
    st.session_state.session_count += 1
st.write(f"Session counter: **{st.session_state.session_count}**")

def reset_counter_state() -> None:
    # This is a callback function.
    st.session_state.session_count = 0

# using the `on_click` argument we can add the callback to our reset button
st.button("Reset session counter", on_click=reset_counter_state)"""
        )

    if "session_count" not in st.session_state:
        st.session_state.session_count = 0
    if st.button("Session counter (+1)"):
        st.session_state.session_count += 1
    st.write(f"Session counter: **{st.session_state.session_count}**")

    def reset_counter_state() -> None:
        """This is a callback function."""
        st.session_state.session_count = 0

    # using the `on_click` argument we can add the callback to our reset button
    st.button("Reset session counter", on_click=reset_counter_state)


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
        options=slides,
        key="slide_select",
        on_change=on_slide_change,
        index=0,
    )
    st.divider()
    st.markdown(markdown_content[str(st.session_state.slide)])
    if st.session_state.slide == 1:
        state_demo()
    if st.session_state.slide == 2:
        with st.expander("Whats in session_state right now?"):
            st.write(st.session_state)
    if st.session_state.slide == 4:
        if st.button("Try st.rerun!"):
            st.rerun()


if "slide" not in st.session_state:
    st.session_state["slide"] = 0

markdown_content = read_markdown_content()
slides = list(markdown_content.keys())

if "slide_select" not in st.session_state:
    st.session_state.slide_select = slides[st.session_state.slide]

slideshow()
