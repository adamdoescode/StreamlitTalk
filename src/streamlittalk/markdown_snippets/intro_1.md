
## About me
- Environmental scientist at a small air quality consultancy
- Former medical biologist
- I like:
  - python (and have no formal training in it)
  - R (and have some formal training in it)
  - I also like birds
---
## What is streamlit?
- Another python web app platform
- Web apps for data scientists without time to learn React
- Looks :grey[(objectively)] *nice* by default
- Easy to install and run
---
## Y tho?
- Web stuff is confusing and scary
- Python is nice because I already know it
- What if I just write my web app in python?
- Surely there will be no consequences for this.
---
## Similar to...
- Other solutions to :blue["make web dev easy for data scientists"] exist.
- Dash
  - VERY similar use case to streamlit.
  - The [minimal dash app](https://dash.plotly.com/minimal-app) was far too complex and scary for me.
  - last time I tried `conda install` on dash it broke so I never even tried it tbh.
  - It did, however, install in this repo with `uv add dash`...
- Shiny
  - R framework designed for R data scientists scared of React (and possibly Python?)
  - I have used this and liked it. Impressed my boss at the time with a demo. Once saw some HORRIFIC academic code using this for a rather user friendly personal genomics website (sadly taken down now).
- Jupyter widgets
  - I use these, and like them. But man, they are *not* performant or reproducible!
  - Mind you, streamlit widgets with plotly can chug too.
- [Textual](https://textual.textualize.io/)
  - Terminal GUI apps, with easy web app deploys (on localhost anyway).
  - Amazing, so cool. Wish I had a good excuse to use it more.
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
  - there is no escape from handling state once you are in web interface world...
