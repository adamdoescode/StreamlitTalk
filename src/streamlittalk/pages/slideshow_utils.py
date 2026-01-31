import streamlit as st


def header_setup(n_slides: int, session_slide_key: str = "slide") -> None:
    # streamlit allows for column (flexbox) syntax:
    # our list into st.columns defines width
    col1, col2, col3 = st.columns(spec=[1, 2, 1])

    with col1:
        if st.button("⬅️ Previous", disabled=st.session_state[session_slide_key] == 0):
            st.session_state[session_slide_key] -= 1
            st.rerun()

    with col2:
        st.markdown(
            f"#### Slide {st.session_state[session_slide_key] + 1}",
            text_alignment="center",
        )

    with col3:
        if st.button(
            "Next ➡️", disabled=st.session_state[session_slide_key] == n_slides - 1
        ):
            st.session_state[session_slide_key] += 1
            st.rerun()
