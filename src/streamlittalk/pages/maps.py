from pathlib import Path

import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from utils.prettymapp_example import prettymaps_example
from utils.st_map import st_map


def geopandas_example() -> None:
    """
    Could use geopandas/plotly here?
    """
    pass


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
