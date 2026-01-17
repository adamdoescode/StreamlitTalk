"""
Docstring for streamlittalk.pages.dataframes_and_plots

Streamlit has some great native ways to display dataframes interactively.
"""

from pathlib import Path

import pandas as pd
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

FILE_DIR = Path(__file__)

pm25_data = pd.read_csv(FILE_DIR.parents[1] / "internal_data/pm25.csv")
pm25_data.last_changed = pd.to_datetime(pm25_data.last_changed)
pm25_data["state"] = pd.to_numeric(pm25_data["state"].replace("unavailable", pd.NA))
pm25_data = (
    pm25_data.set_index("last_changed").drop(columns="entity_id").resample("4h").mean()
)


def static_dataframe() -> DeltaGenerator:
    """
    Extremely simple, nothing to screw up here.
    Not sure what a `DeltaGenerator` is but it lets us
    modify this "static" dataframe for some reason 🤷‍♀️
    """
    return st.dataframe(data=pm25_data)


def interactive_dataframe() -> pd.DataFrame:
    """
    Interactive dataframe, modifying this returns a new
    dataframe with the updated state.
    """
    return st.data_editor(
        data=pm25_data,
    )


INTERACTIVE_NOTES = """- We can modify the values in this and impact the graph below...
- this works because React will trigger a *rerun* each time we modify the dataframe."""

if __name__ == "__main__":
    st.title("Dataframes can be interactive")

    with st.expander(label="## Static dataframes"):
        st.markdown("## Static dataframes")
        static_dataframe()

    with st.expander(label="Interactive dataframes"):
        st.markdown("## *Interactive* dataframes")
        st.markdown(INTERACTIVE_NOTES)
        modified_df = interactive_dataframe()
        """
        A modification is best illustrated with a graph...
        """
        st.line_chart(modified_df)
