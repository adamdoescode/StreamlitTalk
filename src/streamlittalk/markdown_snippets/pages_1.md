- Streamlit supports 'multipage' apps.
- This talk is implemented in such a multipage app.
- There are two approaches:
  1. a `pages` directory
  2. using `st.navigation` and `st.pages`
---
- the pages directory is a simple approach
- "convention over configuration"
- just need a directory called "pages" setup relative to the entry point file (see below)
- Pros:
  - very simple!
  - I have had this work for me every time I've tried it in Streamlit
- Cons:
  - filename is title
  - no control over order of pages
  - no easy way to make things ✨pretty✨

```bash
src/streamlittalk/
├── entrypoint.py
└── pages
    ├── dataframes_and_plots.py
    ├── example.py
    ├── intro.py
    ├── maps.py
    ├── state_and_caching.py
    └── streamlit_pages.py
```
---
- If you want to get 🐢fancy🐢 you need to do some configuration.
- *Theoretically* this is easy:
  - you define each page in a list:
    - where each list item is an `st.Page` object
  - then you instantiate the `StreamlitPage` object with `st.navigation`.
  - and `.run()` it. Which you can do exactly once.
```python
page_list: list[StreamlitPage] = [
    # since this is the first page listed, it is treated as our homepage when we
    # start the app up.
    st.Page(page="./homepage.py", title="Start!", icon="🏡"),
    # this is a seperate page we have to link to. It will show with this title
    # and icon, which is a bit nicer than just showing "intro".
    st.Page(page="./pages/intro.py", title="Introduction", icon="📖"),
]
# create the navigation object
pg: StreamlitPage = st.navigation(
    pages=page_navigation.page_list,
    position="sidebar",
)
# and run it - you can only do this once!
pg.run()
```
---
```bash
commit 88e7118aa7d59dc38440b0f83ca5c05d68a40389 (origin/main)
Author: AdamG <EMAIL>
Date:   Sat Jan 24 10:43:37 2026 +0800

wrestle with page navigation setup. Turns out this has a few footguns which are not 'easy' to solve
```
- While this seems simple enough, I found it rather fragile in practice.
- Firstly how streamlit interprets your entry-point script changes compared to the `pages` directory approach:
  - It's no longer just a homepage - the content of this page *executes on every page*
  - Adam, this is the bit where you un-comment line 21(-ish) on the `entrypoint.py` script!
- Second, the `st.Page` and `st.navigation` elements really can only be exeucted once!
  - I wanted to use the st.Page elements on two seperate scripts: `homepage.py` and `entrypoint.py`.
  - If you define this in `entrypoint.py` and then imported the `page_list` into `homepage.py` the app will double print the contents of `homepage.py` because it reinitialises the page_list and thus homepage.py! Recursion!
  - So my start page requires **three** .py scripts:
    - `page_navigation` which inits my list of `st.Page` objects
    - `homepage.py` which has the content of my starting page including links to other pages by importing the list of `st.Page` objections.
    - `entrypoint.py` which handles app initialisation including `st.navigation`. BUT this does not have any actual content because that will be put on every other page too.
  - this is a lot of complexity for something a tired and web-naive data scientist is putting together 10 minutes before a meeting!
