"""
Form using prettymapp
https://github.com/chrieke/prettymapp
"""

from pathlib import Path
import streamlit as st
from prettymapp.geo import get_aoi
from prettymapp.osm import get_osm_geometries
from prettymapp.plotting import Plot
from prettymapp.settings import STYLES

shape_options = {False: "circle", True: "rectangle"}


def generate_prettymapp(
    address: str = "Praça Ferreira do Amaral, Macau",
    radius: int = 500,
    rectangular: bool = False,
    name: str = "",
) -> None:
    aoi = get_aoi(address=address, radius=radius, rectangular=rectangular)
    df = get_osm_geometries(aoi=aoi)
    fig = Plot(
        df=df,
        aoi_bounds=aoi.bounds,
        draw_settings=STYLES["Peach"],
        shape=shape_options[rectangular],
        name_on=False if name == "" else True,
        name=name,
        text_x=40,
        text_y=-40,
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
        st.session_state["address"] = "Bankwest Place"
        st.session_state["radius"] = 500
        st.session_state["rectangular"] = False
        st.session_state["name"] = ""

    with st.form("Prettymapp form"):
        columns: list = st.columns(spec=[1, 1])
        columns[0].text_input(
            "Location address",
            key="address",
        )
        columns[0].slider(
            "Radius (meter)",
            100,
            1000,
            key="radius",
        )
        st.text_input(
            label="Title name for map",
            value="",
            key="name",
        )
        columns[1].radio(
            "Map Shape",
            options=[False, True],
            key="rectangular",
            format_func=lambda key: shape_options[key],
        )
        columns[1].form_submit_button("Update map")

    with st.expander("Code"):
        st.code(Path(__file__).read_text(), line_numbers=True)

    generate_prettymapp(
        address=st.session_state["address"],
        radius=st.session_state["radius"],
        rectangular=st.session_state["rectangular"],
        name=st.session_state["name"],
    )
