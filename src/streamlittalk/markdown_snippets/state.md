---
0
## Powerpoint slides in Streamlit!

- Welcome to a streamlit implementation of powerpoint slides!
- To pull this off we need to make use of the web-app's "memory"
  - as oppossed to just storing everything in python variables which are **NOT** stored between app refreshes!
- Thus we now need to discuss the concept of **state**:
$$
\text{state} = \text{memory (for web apps)}
$$
- In streamlit state is stored in a special variable which is basically a `dict`:
```python
st.session_state: MutableMapping[Key, Any]
```
- We'll talk a little about how session_state is implemented because its a nice dive into how to do class enum dict thingies.
- We'll also discuss that type hint `MutableMapping[Key, Any]` later!
---
1
## Why we need to use *state*

- A demonstration of why we want state...
- We have two counter buttons:
  1. button whose content is stored in a local variable `local_count`
  2. buttonw whose content is stored in `st.session_state`
- Let's see how each behaves and walk through the code

---
2
## (Screaming) Why is it stuck at 1??!

- The local counter is being reset *every time* the button is clicked, so that:
  - `local_count` is set to 0
  - we increment `local_count` by 1
  - it gets printed.
- Meanwhile, the chad `st.session_state.session_count` variable is not reset by the hidden page refresh that wipes clean our local python variables.

---
3
## Session state implementation

- Held in the streamlit `__init__.py` as:
```python
session_state = _SessionStateProxy()
```
- `_SessionStateProxy()` is a proxy for `SessionStateProxy()`:
```python
class SessionStateProxy(MutableMapping[Key, Any]):
```
- So its a `MutableMapping` with some custom dunder methods for streamlit's content
- **Mapping** == a data structure of key value pairs; think a `dict` (or hash table).
- **Mutable** == changeable - aka we can change the key - value pairs in this.

---
4
## The trouble with `st.rerun` and why you should use "callbacks"

- You saw a callback just before!
- It was this bad boi:
```python
def reset_counter_state() -> None:
    """This is a callback function."""
    st.session_state.session_count = 0

# using the `on_click` argument we can add the callback to our reset button
st.button("Reset session counter", on_click=reset_counter_state)
```
- Here, we run the function `reset_counter_state` when the user clicks the `st.button`.
- We can think of this as an "on demand function".
- The original chatGPT suggestion was this:
```python
if st.button("Reset session counter"):
    st.session_state.reset_counter_state = 0
    st.rerun()
```
- this is bad!
- although `st.rerun()` works in this case, it can often cause chaos when you have basically any level of complexity in your web app's state.
- Users should beware that LLMs will use the `st.rerun` pattern unless you tell it not to.
- Fortunately, since the slide tracking variable here `st.session_state.slide` is set as session state the `st.rerun()` does not reset our slide deck back to the start page.
