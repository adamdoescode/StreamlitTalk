"""
This demo is UGLY code.
So it gets relegated to its own .py so I don't have to look at it.
"""

import streamlit as st


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
