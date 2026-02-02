from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def st_map() -> None:
    """
    Can you show a mapbox example.
    """
    if "df" not in st.session_state:
        st.session_state["df"] = pd.DataFrame(
            np.random.randn(200, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
        )
        st.session_state["df"]["colour"] = "#f244b5"

    st.map(st.session_state["df"], color="colour")
    with st.expander("data"):
        st.session_state["df"] = st.data_editor(st.session_state["df"])


def geopandas_example() -> None:
    """
    Could use geopandas/plotly here?
    """
    pass


def prettymaps_example() -> None:
    """
    Prettymaps seems interesting, a quick example could be nice, and a bit of wowser to kick off with!
    """
    from prettymapp.geo import get_aoi
    from prettymapp.osm import get_osm_geometries
    from prettymapp.plotting import Plot
    from prettymapp.settings import STYLES

    aoi = get_aoi(
        address="Praça Ferreira do Amaral, Macau", radius=1100, rectangular=False
    )
    df = get_osm_geometries(aoi=aoi)

    with st.spinner("Generating Plot", show_time=True):
        fig = Plot(
            df=df,
            aoi_bounds=aoi.bounds,
            draw_settings=STYLES["Peach"],
        ).plot_all()
    st.pyplot(fig)


if __name__ == "__main__":
    # get the filepath, mostly this avoids broken relative paths for the streamlit server
    # using Pathlib means we get the handy `.read_text()` method too!
    FILE_DIR = Path(__file__)

    # read in markdown snippets and split by a known seperator `---`
    # use level 2 titles as keys so we dont have to worry about order so much!
    markdown_content: dict[str, str] = {
        content.split("\n")[1].replace("## ", "").strip(): content
        for content in (FILE_DIR.parents[1] / "markdown_snippets" / "maps.md")
        .read_text()
        .split("---")
    }

    st.title("Maps in Streamlit")
    tab_names = ["Explainer", "Using `st.map`", "Geopandas with form", "Prettymapp"]
    tabs: dict[str, DeltaGenerator] = {
        tabname: tab_obj for tabname, tab_obj in zip(tab_names, st.tabs(tab_names))
    }

    with tabs["Explainer"]:
        st.markdown(markdown_content["Mapping in Streamlit"])

    with tabs["Using `st.map`"]:
        st.markdown(markdown_content["Using `st.map`"])
        st_map()

    with tabs["Geopandas with form"]:
        st.markdown(markdown_content["Roll your own with `matplotlib` and `geopandas`"])
        geopandas_example()

    with tabs["Prettymapp"]:
        st.markdown(markdown_content["Prettymapp"])
        prettymaps_example()
