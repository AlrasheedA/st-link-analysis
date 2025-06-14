import os
import streamlit as st

st.set_page_config(layout="wide")

# ------------- Docs -------------
home = st.Page(
    "./docs/readme.py",
    title="Readme",
    default=True,
)
license = st.Page(
    "./docs/license.py",
    title="License",
)

changelog = st.Page(
    "./docs/changelog.py",
    title="Changelog",
)

icons = st.Page(
    "./docs/supported_icons.py",
    title="Supported Icons",
)

# -------- Examples / Demos --------
node_style = st.Page(
    "./demos/node_style.py",
    title="Node Styles",
)
edge_style = st.Page(
    "./demos/edge_style.py",
    title="Edge Styles",
)  # TODO: use multi-edge graph example for edge styles
layout = st.Page(
    "./demos/layout.py",
    title="Layout Algorithms",
)

# --------- Advanced Usage ---------
event_listeners = st.Page(
    "./demos/event_listeners.py",
    title="Events Listeners",
)

node_actions = st.Page(
    "./demos/node_actions.py",
    title="Node Actions",
)

# TODO: Further Styling
# TODO: Customized Layouts


# --------- Navigation ---------
menu = {
    "Documentation": [home, changelog, license, icons],
    "Demos": [node_style, edge_style, layout],
    "Advanced Usage": [event_listeners, node_actions],
}

# --------- Debugging ---------
debug_pages = [
    st.Page(f"./debug/{file}", title=file.replace(".py", ""))
    for file in os.listdir("./debug")
    if file.endswith(".py")
]

if debug_pages:
    menu["Debugging"] = debug_pages

pg = st.navigation(menu)
pg.run()
