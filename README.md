# Streamlit is good! (for some things!)

## Talk Blurb

Join Adam as he attempts to explain what Streamlit is while using an ill-advised re-invention of Powerpoint in... Streamlit, actually. Learn why Streamlit is pretty good for the *right* things, how you can make a web form with a pandas dataframe, discover that interactive maps are really easy (but also hard), why you should NEVER use `st.rerun()`, and why using Python to write a highly constrained Typescript webapp is bad for maintainability.

## Quick notes

- Use `uv` for my env here

## TODO

- [ ] add pre-commit for consistent ruff formatting checks
- [ ] dataframe example:
  - [ ] it would be *funny* if the interactive dataframe changed results in a timeseries

### How?

- We should do a presentation in streamlit!
- What better demo than to use it as a slideshow :)

### What?

- Things I want to explore/discuss:
  - how streamlit works (React*-style* frontend with python scripting?)
  - basics of what you can do with it:
    - quick prototyping
    - great for simple, easy on the eyes, GUIs
    - how pages work
    - simple API:
      - widgets
      - other stuff?
    - Good integrations for:
      - dataframes
      - plotting and plotly
      - maps
  - It's limits;
    - limited ability to handle deep complexity
    - see if we can find some footguns
  - caching and session state are messy topics worth touching on.
    - st.rerun is cursed ☠️
    - `st.session_state`

- [Prettymap](https://github.com/marceloprates/prettymaps)

## About Me

Adam is an air quality data scientist with Environmental Technologies and Analytics. He uses Python for fun and profit and has a Graduate Diploma in Biostatistics. His credentials for discussing streamlit come from the trial-by-fire search for the holy grail of "user uptake" by his coworkers. He is still not sure what Spas have to do with Apps and Components but he would absolutely download a Spa if he could. In a past life he was a research biologist and science communicator. He remains a committed bird nerd and maintains a neobrutalist website at https://adamdoescode.github.io/.
