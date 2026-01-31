# import Path from pathlib for files, yes, you should do this instead of whatever curses os and sys imports chatgpt is telling you to use
from pathlib import Path

# this is how we import streamlit
import streamlit as st

# get the filepath, mostly this avoids broken relative paths for the streamlit server
# using Pathlib means we get the handy `.read_text()` method too!
FILE_DIR = Path(__file__)
# and i put the markdown chunks in this folder...
SNIPPETS_DIR = FILE_DIR.parents[1] / "markdown_snippets"

# read in markdown snippets and split by a known seperator `---`
# use level 2 titles as keys so we dont have to worry about order so much!
markdown_content: dict[str, str] = {
    content.split("\n")[1].replace("## ", "").strip(): content
    for content in (SNIPPETS_DIR / "intro_1.md").read_text().split("---")
}

if __name__ == "__main__":
    # Runs if we open this page in the streamlit server
    # st.title makes a title. Has some other arguments btw.
    st.title("Introduction")
    # st.expander creates a nice little expander for our content.
    # use it with `with` for maximum pythonic clarity (and whitespace)
    with st.expander("About Me", expanded=True):
        st.markdown(markdown_content.get("About me", "No content found!"))
    with st.expander("What is Streamlit?"):
        # st.markdown supports markdown formatted text - very neat.
        st.markdown(markdown_content.get("What is streamlit?", "No content found!"))

        st.image(image="media/streamlit_gh.png", width=300)

        st.markdown("- Enough already! What does the code look like??")
        st.code(body=(FILE_DIR.parents[1] / "pages" / "example.py").read_text())
        # st.code prints strings formatted as code with syntax highlighting.
        st.markdown("- Here's the code for this page:")
        with st.expander("Page code"):
            st.code(
                body=FILE_DIR.read_text(),
                line_numbers=True,
            )
    with st.expander("Y tho?"):
        # streamlit can't handle markdown linked images so we have to have that line seperately.
        st.image(image="media/ytho.jpg", width=300)
        st.markdown(markdown_content.get("Why tho?", "No content found!"))
    with st.expander("Similar to..."):
        st.markdown(markdown_content.get("Similar to...", "No content found!"))
    with st.expander("Pros"):
        st.markdown(markdown_content.get("Pros", "No content found!"))
        dummy_upload = st.file_uploader(label="Upload example widget")
        if dummy_upload:
            st.write(f"Uploaded: {dummy_upload.name}")
    with st.expander("Cons"):
        st.markdown(markdown_content.get("Cons", "No content found!"))
