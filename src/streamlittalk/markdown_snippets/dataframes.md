- Interactive dataframes use a different method: `st.data_editor`.
- We can modify the values in this and impact the graph below...
- this works because Streamlit will trigger a *rerun* each time we modify the dataframe.
- since st.data_editor returns a new Dataframe it just passes the updated df to line_chart.
```python
modified_df: pd.DataFrame = st.data_editor(data=pm25_data)
st.line_chart(modified_df)
```
---
- We can also use dataframes for non date-ry tasks.
- Likely, this is *ill-advised* but its neat that you can do it!
