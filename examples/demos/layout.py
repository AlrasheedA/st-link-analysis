import json
import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle
from st_link_analysis.component.layouts import LAYOUTS

LAYOUT_NAMES = list(LAYOUTS.keys())

with open("./data/claims.json", "r") as f:
    elements = json.load(f)

sample = {
    "nodes": [
        {"data": {"id": "n1", "label": "PERSON"}},
        {"data": {"id": "n2", "label": "CAR"}},
        {"data": {"id": "n3", "label": "CLAIM"}},
    ],
    "edges": [
        {"data": {"id": "e1", "source": "n1", "target": "n2", "label": "DRIVES"}},
        {"data": {"id": "e2", "source": "n2", "target": "n3", "label": "INVOVLED_IN"}},
    ],
}

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
    NodeStyle("CLAIM", "#a87c2a", None, "description"),
    NodeStyle("CAR", "#028391", None, "directions_car"),
    NodeStyle("PERSON", "#01204E", None, "person"),
]

st_link_analysis(elements, layout, node_styles, key="xyz")


with st.expander("Snippet", expanded=False, icon="💻"):
    st.code(
        f"""
        from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle

        node_styles = [
            NodeStyle("CLAIM", "#a87c2a", None, "description"),
            NodeStyle("CAR", "#028391", None, "directions_car"),
            NodeStyle("PERSON", "#01204E", None, "person"),
        ]

        {layout=}

        elements = {json.dumps(sample)}

        st_link_analysis(elements, layout, node_styles, key="xyz")
    """,
        language="python",
    )
