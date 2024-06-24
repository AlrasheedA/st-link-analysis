import streamlit as st

to_remove = [
    "# st-link-analysis",
    "![extended-example](demo.gif)",
]

with open("./../README.md") as f:
    readme = f.read()

for line in to_remove:
    readme = readme.replace(line, "")


st.markdown("## Streamlit Link Analysis")
st.markdown(readme)
