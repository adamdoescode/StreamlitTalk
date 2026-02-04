"""
Docstring for streamlittalk.pages.dataframes_and_plots

Streamlit has some great native ways to display dataframes interactively.
"""

from pathlib import Path

import pandas as pd
import streamlit as st

FILE_DIR = Path(__file__)

pm25_data = pd.read_csv(FILE_DIR.parents[1] / "internal_data/pm25.csv")
pm25_data.last_changed = pd.to_datetime(pm25_data.last_changed)
pm25_data["state"] = pd.to_numeric(pm25_data["state"].replace("unavailable", pd.NA))
pm25_data = (
    pm25_data.set_index("last_changed").drop(columns="entity_id").resample("4h").mean()
)


# read in markdown snippets and split by a known seperator `---`
markdown_content = {
    page: content
    for page, content in enumerate(
        (FILE_DIR.parents[1] / "markdown_snippets" / "dataframes.md")
        .read_text()
        .split("---")
    )
}


def df_form() -> None:
    """
    Function for the dataframe form tab
    """
    st.markdown(markdown_content.get(1, "AAHHHHHH NO CONTENT"))
    table_for_form = pd.DataFrame(
        {
            "Favourite Animal": ["Turtle"],
            "Best Emoji": ["🐢"],
            "Your Name": ["Sir Turtlemas"],
            "Pronoun": ["They"],
        },
        index=pd.Series(["Answers"]),
    )

    table_for_form = st.data_editor(data=table_for_form)
    table_dict = table_for_form.to_dict(orient="list")

    st.markdown("### Result")
    st.markdown(
        "##### "
        f":blue[{table_dict.get('Your Name', 'MISSING')[0]}]'s favourite animal is a "
        f":red[{table_dict.get('Favourite Animal', 'MISSING')[0]}]. "
        f":green[{table_dict.get('Pronoun', 'MISSING')[0]}] like the "
        f"{table_dict.get('Best Emoji', 'MISSING')[0]} emoji."
    )


if __name__ == "__main__":
    st.title("Dataframes can be interactive")

    tab_labels = [
        "## Static dataframes",
        "Interactive dataframes",
        "Dataframe as a form?!",
    ]
    tabs = st.tabs(tabs=tab_labels)
    tab_dict = dict(zip(tab_labels, tabs))

    with tab_dict["## Static dataframes"]:
        st.markdown("## Static dataframes")
        st.markdown("- static dataframes use `st.dataframe`")
        st.markdown("- the below uses this:")
        st.code("static_df = st.dataframe(data=pm25_data)")
        static_df = st.dataframe(data=pm25_data)

    with tab_dict["Interactive dataframes"]:
        st.markdown("## *Interactive* dataframes")
        st.markdown(markdown_content[0])
        modified_df: pd.DataFrame = st.data_editor(
            data=pm25_data,
        )
        """
        A modification is best illustrated with a graph...
        """
        st.line_chart(modified_df)

    with tab_dict["Dataframe as a form?!"]:
        df_form()
