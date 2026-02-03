
## Mapping in Streamlit

- The *best* data analytics involves maps
- Streamlit, knowing this, has a few built-in ways to display static and interactive maps
- We'll explore a couple of them here:
  - `st.map`
  - Roll your own with `geopandas` and `matplotlib`
  - Using the very pretty `prettymap`

---
## Using `st.map`

- The simplest approach in streamlit is to use the built-in `st.map`.
- Uses `pydeck` under the hood.
- I am still trying to understand how `pydeck` works...

---
## Roll your own with `matplotlib` and `geopandas`

- Streamlit offers `st.pyplot` which we can leverage with a form to create regenerating static plots and maps

---
## Prettymapp

- [Github link](https://github.com/chrieke/prettymapp)
- [Streamlit App link](https://prettymapp.streamlit.app/)
- An excellent example of exactly what Streamlit is good for:
  - a simple form + image generation app
