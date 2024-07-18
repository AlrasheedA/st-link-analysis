import streamlit as st
import re

with open("./../CHANGELOG.md") as f:
    changelog = f.read()

changelog = re.sub(r"(\n##) (.+)", r"\n---\n \1 :blue[\2]", changelog)
changelog = changelog.replace("##", "####").replace("# Changelog", "")

st.markdown("## Changelog")
st.markdown(changelog, unsafe_allow_html=False)
