# Streamlit is good! (for some things!)

## Talk Blurb

Join Adam as he attempts to explain what Streamlit is while using an ill-advised re-invention of Powerpoint in... Streamlit, actually. Learn why Streamlit is pretty good for the *right* things, how you can make a web form with a pandas dataframe, discover that interactive maps are really easy (but also hard), why you should NEVER use `st.rerun()`, and why using Python to write a highly constrained Typescript webapp is bad for maintainability.

[View this site here!](https://adamdoescodetalk.streamlit.app/)

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

- [ ] improved state explainer
- [ ] maps demos:
  - [ ] prettymaps
  - [ ] basic map embedding tricks
  - [ ] could consider using the wheatbelt birds stuff here!
- [ ] it may be expedient to live demo the creation of a new page
  - I think it's enough to have a prompt for this at the end of the talk and then get some audience feedback on what to make :)
- [ ] the async generation of resource intensive matplotlib is quite nice, find a way to demo this!
  - We may be able to do this with something as simple as a `time.sleep()` call...
- [ ] deployment:
  - [x] try using the free streamlit deploy service
  - Got this working BUT did have to use python 3.13.
  - This required two commits because I am still learing the basics of `uv`.
  - [ ] maybe a slide on this? Describing my experience and opinion on it would be nice.
  - Keep in mind there's no guarantee of web access for the talk
- [ ] how normal forms work
  - [ ] I think we can just straight up use prettymap for this since it looks fantastic
  - EXCEPT: talk is local only, which may complicate matters
- [ ] Under the hood:
  - Let's spend some time understanding the implementation
  - I know its translating python to typescript, but that's about all I know at this point.
  - [ ] explore this

## TODONE

- [x] make the page styling more in-line with a powerpoint
- [x] acknowledgements!
- [x] in intro "Y tho" I need to:
  - [x] what problem this solves:
    - Simple and easy to implement web apps with a DS focus or a friendly form
  - [x] what problem it doesn't solve
  - [x] **why** is it not as good a solution as using React or TS
    - Streamlit implements a subset of React
    - It is not easy to access the full functionality available in React
- [x] `st.rerun` is bad (some of the time)
- [x] cursed reinvention of powerpoint slides:
  - We can use these slides to cover the concept of *state* here
  - Since refreshing the contents on the page requires use of state we can explain it while on these slides
- [x] dataframe example:
  - [x] it would be *funny* if the interactive dataframe changed results in a timeseries
    - Oh lol I did this. It's pretty good actually.
  - [x] dataframe as a web-form!
    - web-form for what content tho?
    - I'll do a simple text injection for now
    - done, uninspired but illustrative.
- [x] add pre-commit for consistent ruff formatting checks
- [x] how pages work (since its simple and neat)
  - hahahah yeah, simple and neat if you use the basic `pages` dir. A bit more of a headache when doing it via config. But still, the result is quite nice once you can avoid the footguns!
- [x] page ordering config in streamlit? I would like to fix this up for the sidebar.
  - [page docs](https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation)
  - this ended up being a bit of a journey
  - I think this deserves its own section for me to gripe about!
  - [x] page on pages in streamlit
- [x] consolidate intro mds into a single md file using `---` to split
- [x] things I like about streamlit:
  - Add this to the intro slides I think
  - [x] ease of install
  - [x] ease of use
  - [x] very short development loop
  - [x] LLMs like streamlit (double edged sword)
  - [x] Looks *nice enough* by default
- [x] things I dislike about streamlit:
  - [x] multiline comments get printed! Awful!
    - this is because they are just strings and streamlit defaults to burping them out.


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
