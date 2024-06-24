import streamlit as st

to_remove = []

with open("./../LICENSE") as f:
    license = f.read()

for line in to_remove:
    license = license.replace(line, "")


st.markdown("## License")
st.markdown(license)
