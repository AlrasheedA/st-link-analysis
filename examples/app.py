import streamlit as st

st.set_page_config(layout="wide")

# ------------ Home ------------
home = st.Page(
    "./docs/readme.py",
    title="README",
    default=True,
)
license = st.Page(
    "./docs/license.py",
    title="LICENSE",
)

# -------- Examples / Demos --------
node_style = st.Page(
    "./demos/node_style.py",
    title="Node Styles",
)
edge_style = st.Page(
    "./demos/edge_style.py",
    title="Edge Styles",
)
layout = st.Page(
    "./demos/layout.py",
    title="Layout Algorithms",
)

pg = st.navigation(
    {
        "Documentation": [home, license],
        "Demos": [node_style, edge_style, layout],
    }
)
pg.run()
