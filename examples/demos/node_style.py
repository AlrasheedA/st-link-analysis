import json
import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
from st_link_analysis.component.icons import SUPPORTED_ICONS

with open("./data/social.json", "r") as f:
    elements = json.load(f)

PERSON_ATTRS = list(elements["nodes"][0]["data"].keys()) + [None]

st.markdown("# Node Styles")
st.markdown(
    """
    A unique node style can be applied to each group of nodes (grouped by `label` 
    data element). Here is an example of modifying `PERSON` nodes styles
    """
)

left, middle, right = st.columns(3)
label = "PERSON"
icon = left.selectbox("Icon", SUPPORTED_ICONS, index=2)
caption = middle.selectbox("Caption", PERSON_ATTRS, index=3)
color = right.color_picker("Color", value="#FF7F3E")

node_styles = [
    NodeStyle(label, color, caption, icon),
    NodeStyle("POST", "#2A629A", "created_at", "description"),
]

edge_styles = [
    EdgeStyle("FOLLOWS", caption="label", directed=True),
    EdgeStyle("POSTED", caption="label", directed=True),
    EdgeStyle("QUOTES", caption="label", directed=True),
]

layout = {"name": "cose", "animate": "end", "nodeDimensionsIncludeLabels": False}

st_link_analysis(
    elements, node_styles=node_styles, edge_styles=edge_styles, layout=layout, key="xyz"
)

with st.expander("Snippet", expanded=False, icon="💻"):
    st.code(
        f"""
        from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
        
        node_styles = [
            NodeStyle({label=}, {color=}, {caption=}, {icon=}),
            NodeStyle(label="POST", color="#2A629A", caption="created_at", icon="description")
        ]

        edge_styles = [
            EdgeStyle("FOLLOWS", caption='label', directed=True),
            EdgeStyle("POSTED", caption='label', directed=True),
            EdgeStyle("QUOTES", caption='label', directed=True),
        ]

        layout = {{"name": "cose", "animate": "end", "nodeDimensionsIncludeLabels": False}}

        elements = {json.dumps(elements)}

        st_link_analysis(elements, layout, node_styles, edge_styles, key="xyz")
    """,
        language="python",
    )
