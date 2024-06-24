import json
import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
from st_link_analysis.component.layouts import LAYOUTS

LAYOUT_NAMES = list(LAYOUTS.keys())

with open("./examples/sample_data.json", "r") as f:
    elements = json.load(f)

st.markdown("# Layout Algorithms")
st.markdown(
    """
    You can select from different layout options which determines how elements 
    positions are calculated in the graph. Refer to 
    [Cytoscape JS](https://js.cytoscape.org/#layouts) for full options.
    """
)

layout = st.selectbox("Layout Name", LAYOUT_NAMES, index=0)

node_styles = [
    NodeStyle("PERSON", "#FF7F3E", None, "person"),
    NodeStyle("POST", "#2A629A", None, "description"),
]

edge_styles = [
    EdgeStyle("FOLLOWS", labeled=True, directed=True),
    EdgeStyle("POSTED", labeled=True, directed=True),
    EdgeStyle("QUOTES", labeled=True, directed=True),
]

st_link_analysis(elements, layout, node_styles, edge_styles, key="xyz")

with st.expander("Snippet", expanded=False, icon="💻"):
    st.code(
        f"""
        from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
        
        edge_styles = [
            EdgeStyle("FOLLOWS", labeled=True, directed=True),
            EdgeStyle("POSTED", labeled=True, directed=True),
            EdgeStyle("QUOTES", labeled=True, directed=True),
        ]

        node_styles = [
            NodeStyle("PERSON", "#FF7F3E", None, "person"),
            NodeStyle("POST", "#2A629A", None, "description"),
        ]

        {layout=}

        elements = {json.dumps(elements)}

        st_link_analysis(elements, layout, node_styles, edge_styles)
    """,
        language="python",
    )
