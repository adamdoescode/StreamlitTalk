
## About me
- Environmental scientist at a small air quality consultancy
  - [ETA - Environmental Technologies & Analytics](https://envanalytics.com.au/)
- Former medical biologist
- I like:
  - python (and have no formal training in it)
  - R (and have some formal training in it)
  - I also like birds
- I do:
  - Air quality modelling
  - Data analysis (small datasets of 5 to 5 million rows)
  - Map making (for fun and profit)
  - Birdwatching

---
## What is streamlit?
- (Another) python web app platform
  - Let's you build web applications
  - Simple declarative interface with minimal LOC for a working app
- Web apps for data scientists and the impatient
- Looks :grey[(objectively)] *nice* by default
- Easy to install and run
---
## Y tho?
> *A faster way to build and share data apps*

:grey[- streamlit.io official splash page]

- **Serious answer**:
  - Viable web app in a minimal amount of time and effort
  - Batteries included (*if* the batteries are standard)
  - Easy deployment of simple data science dashboard and forms
  - Great for internal tooling using web forms for a front end
- **Emotive answer**:
  - I find NPM packaging alarming
  - React takes more than five minutes to learn and I have no time.
  - Python is nice because I already know it
  - It worked when I tried `conda install streamlit`
    - and worked again when I tried `streamlit run main.py`.
---
## :red[What it's NOT]
- I have been told by multiple experienced (and very tired) developers to tell you this:
  - :red[**Streamlit is NOT a drop-in replacement for React**]
- It will not let you build the fancy and complex SPA webapp of your dreams or resume
- You *will* find yourself deep in the technical debt mines whipping chatGPT to generate custom React components for streamlit.
- You *will* weep in despair and ask:
  - why didn't I just use React? 😭😭😭😭
- That said;
  - it's pretty nice for a quick web form with fast feedback
  - and neat dashboards 😊
---
## Similar to...
- Other solutions to :blue["make web dev easy for data scientists"] exist.
- Dash
  - VERY similar use case to streamlit.
  - The [minimal dash app](https://dash.plotly.com/minimal-app) was complex enough to scare me off.
  - last time I tried `conda install` on dash it broke so I never even tried it again.
  - It did, however, install in this repo with `uv add dash`...
- Shiny:
  - R framework designed for R data scientists/statisticians/economists.
  - I have used this and liked it. Impressed my boss at the time with a demo.
  - Similar declarative style API.
  - Apparently available in Python now.
- Jupyter widgets:
  - I use these, and like them. But man, they are *not* performant or reproducible!
  - Mind you, streamlit widgets with plotly can chug too.
- [Textual](https://textual.textualize.io/)
  - Terminal TUI app framework.
  - Has an in browser version that is a perfect 1:1 with the terminal TUI.
  - Amazing, so cool. Wish I had a good excuse to use it more.
  - Relatively complex but much more flexible than Streamlit.
---
## Pros
- Pros:
  - easy to install and get started with.
  - the beginner example is very simple and not scary.
  - the offical docs are good!!
  - **short development loop**:
    - live updates to streamlit pages 
    - no compiling
    - launch time for a vanilla app is imperceptable.
  - Decent support for markdown (not perfect)
    - most of this talk is actually *.md files read into streamlit
  - Good support for the python data toolkit (pandas, plotly, etc)
  - LLMs know about it:
    - enough community surrounds it that you can get help from your preferred clanker.
    - LLMs will also happily write working streamlit code, but beware the usual BS with LLMs.
  - :green[looks] :orange[pretty] :red[nice] :blue[by default]:
    - Approachable rounded corners out of the box (and on every box)
    - Nice friendly forms and data drag and drops
---
## Cons
- Cons:
  - Using python to build typescript components means inevitably building a house of cards
  - multiline comments get printed! Awful!
```python
"""
Insane rambling comment here over multiple lines 
will be put in your demo when you present it to your bosses
"""
```
  - hidden footguns once you start doing more complex stuff
  - difficult to implement anything that isn't supported out of the box
  - there is no escape from handling state once you are in web interface world...
