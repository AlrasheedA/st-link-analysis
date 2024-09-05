import json
import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle

with open("./data/social.json", "r") as f:
    elements = json.load(f)

EDGE_ATTRS = ["id", "source", "target", "label", None]
CURVE_STYLES = [
    "bezier",
    "haystack",
    "straight",
    "unbundled-bezier",
    "round-segments",
    "segments",
    "round-taxi",
    "taxi",
]

st.markdown("# Edge Styles")
st.markdown(
    """
    A unique edge style can be applied to each group of edges (grouped by `label` 
    data element). Here is an example of modifying `FOLLOWS` edges style
    """
)

c1, c2, c3, c4 = st.columns(4)
label = "FOLLOWS"
curve_style = c1.selectbox("Curve Style", CURVE_STYLES, index=0)
caption = c2.selectbox("Caption", EDGE_ATTRS, index=3)
directed = c3.selectbox("Directed", [True, False], index=0)
color = c4.color_picker("Line Color", value="#808080")


node_styles = [
    NodeStyle("PERSON", "#FF7F3E", "name", "person"),
    NodeStyle("POST", "#2A629A", "created_at", "description"),
]

edge_styles = [
    EdgeStyle(label, color, caption, directed=directed, curve_style=curve_style),
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
        
        edge_styles = [
            EdgeStyle({label=}, {color=}, {caption=}, {directed=}, {curve_style=}),
            EdgeStyle("POSTED", caption='label', directed=True),
            EdgeStyle("QUOTES", caption='label', directed=True),
        ]

        node_styles = [
            NodeStyle("PERSON", "#FF7F3E", "name", "person"),
            NodeStyle("POST", "#2A629A", "created_at", "description")
        ]

        layout = {{"name": "cose", "animate": "end", "nodeDimensionsIncludeLabels": False}}

        elements = {json.dumps(elements)}

        st_link_analysis(elements, layout, node_styles, edge_styles, key="xyz")
    """,
        language="python",
    )
