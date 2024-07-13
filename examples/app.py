import streamlit as st

st.set_page_config(layout="wide")

# ------------- Home -------------
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
)  #TODO: use multi-edge graph example for edge styles
layout = st.Page(
    "./demos/layout.py",
    title="Layout Algorithms",
)

#TODO: Return Selection

# --------- Advanced Usage ---------
event_listeners = st.Page(
    "./demos/event_listeners.py",
    title="Events Listeners",
)

#TODO: Further Styling
#TODO: Customized Layouts

pg = st.navigation(
    {
        "Documentation": [home, license],
        "Demos": [node_style, edge_style, layout],
        "Advanced Usage": [event_listeners],
    }
)
pg.run()
