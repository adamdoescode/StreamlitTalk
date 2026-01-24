# Streamlit is good! (for some things!)

## Talk Blurb

Join Adam as he attempts to explain what Streamlit is while using an ill-advised re-invention of Powerpoint in... Streamlit, actually. Learn why Streamlit is pretty good for the *right* things, how you can make a web form with a pandas dataframe, discover that interactive maps are really easy (but also hard), why you should NEVER use `st.rerun()`, and why using Python to write a highly constrained Typescript webapp is bad for maintainability.

## How to run

1. Install uv [from here](https://docs.astral.sh/uv/getting-started/installation/).
2. Setup uv env:  
```bash
uv sync
```
3. Start the streamlit app:  
```bash
uv run streamlit run src/streamlittalk/homepage.py
```

## TODO

- [x] add pre-commit for consistent ruff formatting checks
- [ ] page ordering config in streamlit? I would like to fix this up for the sidebar.
  - [page docs](https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation)
- [ ] things I like about streamlit:
  - Add this to the intro slides I think
  - [ ] ease of install
  - [ ] ease of use
  - [ ] very short development loop
  - [ ] LLMs like streamlit (double edged sword)
  - [ ] Looks *nice enough* by default
- [ ] dataframe example:
  - [x] it would be *funny* if the interactive dataframe changed results in a timeseries
    - Oh lol I did this. It's pretty good actually.
  - [ ] dataframe as a web-form!
- [ ] deployment:
  - [x] try using the free streamlit deploy service
  - Got this working BUT did have to use python 3.13.
  - This required two commits because I am still learing the basics of `uv`.
  - [ ] maybe a slide on this? Describing my experience and opinion on it would be nice.
  - Keep in mind there's no guarantee of web access for the talk
- [ ] how normal forms work
  - [ ] I think we can just straight up use prettymap for this since it looks fantastic
  - EXCEPT: talk is local only, which may complicate matters
- [ ] how pages work (since its simple and neat)
- [ ] cursed reinvention of powerpoint slides:
  - We can use these slides to cover the concept of *state* here
  - Since refreshing the contents on the page requires use of state we can explain it while on these slides
- [ ] Under the hood:
  - Let's spend some time understanding the implementation
  - I know its translating python to typescript, but that's about all I know at this point.
  - [ ] explore this

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
