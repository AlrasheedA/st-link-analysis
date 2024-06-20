import json
import streamlit as st
import pandas as pd
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
from st_link_analysis.component.icons import SUPPORTED_ICONS

# -------- Constants & defaults --------
CAPTIONS = {
    "PERSON": ["id", "label", "name", None],
    "POST": ["id", "label", "content", None],
}
ICONS_DEFAULT = {"PERSON": 2, "POST": 35}

st.set_page_config(layout="centered")

# -------- Data --------
nodes = [
    {"data": {"id": 1, "label": "PERSON", "name": "Streamlit"}},
    {"data": {"id": 2, "label": "PERSON", "name": "Hello"}},
    {"data": {"id": 3, "label": "PERSON", "name": "World"}},
    {"data": {"id": 4, "label": "POST", "content": "x"}},
    {"data": {"id": 5, "label": "POST", "content": "y"}},
]

edges = [
    {"id": 6, "label": "FOLLOWS", "source": 1, "target": 2},
    {"id": 7, "label": "FOLLOWS", "source": 2, "target": 3},
    {"id": 8, "label": "POSTED", "source": 3, "target": 4},
    {"id": 9, "label": "POSTED", "source": 1, "target": 5},
    {"id": 10, "label": "QUOTES", "source": 5, "target": 4},
]

edge_styles = [
    EdgeStyle("FOLLOWS", labeled=True, directed=True),
    EdgeStyle("POSTED", labeled=True, directed=True),
    EdgeStyle("QUOTES", labeled=True, directed=True),
]

layout = {
    "name": "cose",
    "nodeRepulsion": 2024,
    "animate": "end",
    "animationDuration": 500,
    "nodeDimensionsIncludeLabels": True,
    "padding": 20,
}


# -------- Helpers --------
def display_node_style_form(label: str) -> NodeStyle:
    st.markdown(f"**{label}**")
    left, middle, right = st.columns(3)
    icon = left.selectbox(
        "Icon", SUPPORTED_ICONS, key=label + "1", index=ICONS_DEFAULT[label]
    )
    cap = middle.selectbox("Caption", CAPTIONS[label], key=label + "2")
    color = right.color_picker("Color", key=label + "3")
    return NodeStyle(label, color, cap, icon)


def display_edges_editor(edges: dict) -> dict:
    edges = st.data_editor(
        data=edges,
        use_container_width=True,
        hide_index=True,
        column_config={
            "id": st.column_config.NumberColumn(disabled=True),
            "label": st.column_config.SelectboxColumn(
                required=True,
                options=["FOLLOWS", "POSTED", "QUOTES"],
                default="POSTED",
            ),
            "source": st.column_config.NumberColumn(
                required=True, min_value=1, max_value=5
            ),
            "target": st.column_config.NumberColumn(
                required=True, min_value=1, max_value=5
            ),
        },
    )
    return [{"data": e} for e in edges]


def display_layout_editor(layout: dict) -> dict:
    layout = st.text_area(
        label="Layout options",
        value=json.dumps(layout, indent=2),
        height=200,
    )
    try:
        return json.loads(layout)
    except json.JSONDecodeError:
        st.warning("Invalid JSON format", icon="⚠️")


# -------- App --------
st_example = st.container(border=True)
st_example.markdown("### st-link-analysis: Extended Example")
tabs = st_example.tabs(["Elements", "Styles", "Layout"])

with tabs[0]:
    st.markdown("##### Modifying Elements (edges as example)")
    edges = display_edges_editor(edges)

with tabs[1]:
    st.markdown("##### Modifying Styles (nodes as example) ")
    person_style = display_node_style_form("PERSON")
    post_style = display_node_style_form("POST")

with tabs[2]:
    st.markdown("##### Modifying layout")
    st.caption(
        "No available JSON editor, so please ensure entered text is a valid JSON"
    )
    layout = display_layout_editor(layout)
    height = st.slider("Height", 250, 750, 400)


elements = {"nodes": nodes, "edges": edges}
node_styles = [person_style, post_style]

with st_example:
    st_link_analysis(
        elements=elements,
        layout=layout,
        node_styles=node_styles,
        edge_styles=edge_styles,
        height=height,
        key="xyz",
    )
