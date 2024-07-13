import streamlit as st
import re

with open("./../CHANGELOG.md") as f:
    changelog = f.read()

changelog = re.sub(r"(\n##) (.+)", r"\n---\n \1 :blue[\2]", changelog)

changelog = changelog.replace("##", "####")

st.markdown(changelog, unsafe_allow_html=True)
