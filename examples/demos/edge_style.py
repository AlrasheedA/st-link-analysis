import json
import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle

with open("./examples/sample_data.json", "r") as f:
    elements = json.load(f)

PERSON_ATTRS = list(elements["edges"][0]["data"].keys()) + [None]
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

cols = st.columns((4, 1, 2, 5))
label = "FOLLOWS"
curve_style = cols[0].selectbox("Curve Style", CURVE_STYLES, index=0)
color = cols[1].color_picker("Line Color", value="#808080")
labeled = cols[2].checkbox("Labeled", value=False)
directed = cols[2].checkbox("Directed", value=False)

node_styles = [
    NodeStyle("PERSON", "#FF7F3E", "name", "person"),
    NodeStyle("POST", "#2A629A", "created_at", "description"),
]

edge_styles = [
    EdgeStyle(label, color, labeled, directed, curve_style),
    EdgeStyle("POSTED", labeled=True, directed=True),
    EdgeStyle("QUOTES", labeled=True, directed=True),
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
            EdgeStyle({label=}, {color=}, {labeled=}, {directed=}, {curve_style=}),
            EdgeStyle("POSTED", labeled=True, directed=True),
            EdgeStyle("QUOTES", labeled=True, directed=True),
        ]

        node_styles = [
            NodeStyle("PERSON", "#FF7F3E", "name", "person"),
            NodeStyle("POST", "#2A629A", "created_at", "description")
        ]

        layout = {{"name": "cose", "animate": "end", "nodeDimensionsIncludeLabels": False}}

        elements = {json.dumps(elements)}

        st_link_analysis(elements, layout, node_styles, edge_styles)
    """,
        language="python",
    )
