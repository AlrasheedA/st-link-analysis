import json
import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
from st_link_analysis.component.layouts import LAYOUTS

LAYOUT_NAMES = list(LAYOUTS.keys())

st.markdown("# Expand / Remove Nodes")
st.markdown(
    """
    The `node_actions` parameter allows for interactive expansion and removal of
    nodes in the graph. When used, the triggered events are sent back to the Streamlit
    app along with the selected node IDs, allowing developers to handle the necessary
    updates to the graph elements.
     - Removal is triggered by delete/backspace keydown or remove button click. 
     - Expansion is triggered by node double click or expand button click. 
     
     When any of these events are triggered the event is sent back along with selected
     node IDs to the Streamlit app as the component's return value. Users can then handle
    the necessary updates to the elements. 

    #### Example use with a callback 
    """
)

st.code(
    """
    def my_call_back() -> None:
        val = st.session_state["mygraph"]
        if val["action"] == "expand": 
            node_ids = val["data"]["node_ids"]
            # .. handle expand - currently only one node allowed
        elif val["action"] == "remove":
            node_ids = val["data"]["node_ids"]
            # .. handle remove 

    st_link_analysis(elements, node_actions=['remove', 'expand'], on_change=my_call_back, key="mygraph")
        """,
    language="python",
)

st.warning(
    """
    **Notes**
    - Ensure all edges have an existing source and target IDs to prevent errors.
    - This configuration is only initialized once. For changes to take effect, you need
    to remount the component.
    """,
    icon="⚠️",
)


class DummyGraph:
    def __init__(self):
        with open("./data/company.json", "r") as f:
            elements = json.load(f)
        self.all_nodes = elements["nodes"]
        self.all_edges = elements["edges"]
        self.nodes = set([n["data"]["id"] for n in elements["nodes"]])
        self.edges = set([e["data"]["id"] for e in elements["edges"]])

    def get_elements(self):
        return {
            "nodes": [n for n in self.all_nodes if n["data"]["id"] in self.nodes],
            "edges": [e for e in self.all_edges if e["data"]["id"] in self.edges],
        }

    def remove(self, node_ids):
        self.nodes -= set(node_ids)
        self._update_edges()

    def expand(self, node_ids):
        new_nodes = set()
        node_ids = set(node_ids)
        for e in self.all_edges:
            if e["data"]["source"] in node_ids:  # outbound
                new_nodes.add(e["data"]["target"])
            elif e["data"]["target"] in node_ids:  # inbound
                new_nodes.add(e["data"]["source"])
        self.nodes |= new_nodes
        self._update_edges()

    def _update_edges(self):
        self.edges = {
            e["data"]["id"]
            for e in self.all_edges
            if e["data"]["source"] in self.nodes and e["data"]["target"] in self.nodes
        }


COMPONENT_KEY = "NODE_ACTIONS"

if not hasattr(st.session_state, "graph"):
    st.session_state.graph = DummyGraph()

layout = st.selectbox("Try with different layouts", LAYOUT_NAMES, index=0)

node_styles = [
    NodeStyle("PERSON", "#FF7F3E", "email", "person"),
    NodeStyle("COMPANY", "#2A629A", "name", "business"),
]

edge_styles = [
    EdgeStyle("WORKS_AT", caption='label', directed=True),
    EdgeStyle("OWNED_BY", caption='label', directed=True),
]


def onchange_callback():
    val = st.session_state[COMPONENT_KEY]

    if val["action"] == "remove":
        st.session_state.graph.remove(val["data"]["node_ids"])

    elif val["action"] == "expand":
        st.session_state.graph.expand(val["data"]["node_ids"])


elements = st.session_state.graph.get_elements()
with st.container(border=True):
    vals = st_link_analysis(
        elements,
        layout=layout,
        node_styles=node_styles,
        key=COMPONENT_KEY,
        node_actions=['remove', 'expand'],
        on_change=onchange_callback,
    )
    st.markdown("#### Returned Value")
    st.json(vals or {}, expanded=True)


@st.cache_data
def get_source():
    with open(__file__, "r") as f:
        source = f.read()
    return source


source = get_source()
with st.expander("Source", expanded=False, icon="💻"):
    st.code(source, language="python")
