"""
Form using prettymapp
https://github.com/chrieke/prettymapp
"""

import streamlit as st
from prettymapp.geo import get_aoi
from prettymapp.osm import get_osm_geometries
from prettymapp.plotting import Plot
from prettymapp.settings import STYLES

shape_options = {False: "circle", True: "rectangle"}


def generate_prettymapp(
    address: str = "Praça Ferreira do Amaral, Macau",
    radius: int = 1100,
    rectangular: bool = False,
) -> None:
    aoi = get_aoi(address=address, radius=radius, rectangular=rectangular)
    df = get_osm_geometries(aoi=aoi)

    with st.spinner("Generating Plot", show_time=True):
        fig = Plot(
            df=df,
            aoi_bounds=aoi.bounds,
            draw_settings=STYLES["Peach"],
            shape=shape_options[rectangular],
        ).plot_all()
    st.pyplot(fig, width=1000)


def prettymaps_example() -> None:
    """
    Prettymaps seems interesting, a quick example could be nice, and a bit of wowser to kick off with!
    The form for the streamlit example has been pilfered to create this cut down
    example for the talk.
    See here: https://github.com/chrieke/prettymapp/blob/main/streamlit-prettymapp/app.py
    """

    if "address" not in st.session_state:
        st.session_state["address"] = "Praça Ferreira do Amaral, Macau"
        st.session_state["radius"] = 1100
        st.session_state["rectangular"] = False

    with st.form("Prettymapp form"):
        st.text_input(
            "Location address",
            key="address",
        )
        st.slider(
            "Radius (meter)",
            100,
            1500,
            key="radius",
        )
        st.radio(
            "Map Shape",
            options=[False, True],
            key="rectangular",
            format_func=lambda key: shape_options[key],
        )
        st.form_submit_button("Update map")

    generate_prettymapp(
        address=st.session_state["address"],
        radius=st.session_state["radius"],
        rectangular=st.session_state["rectangular"],
    )
