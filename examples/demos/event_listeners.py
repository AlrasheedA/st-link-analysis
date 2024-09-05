import json
import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle, Event

with open("./data/social.json", "r") as f:
    elements = json.load(f)

if hasattr(st.session_state, "counter"):
    st.session_state.counter += 1
else:
    st.session_state.counter = 1

st.markdown("# Events Listeners")
st.error(
    """
    With node actions feature added, the use case for this feature is no longer clear and may be removed in the future. If you have a use case for it please share via [Github](https://github.com/AlrasheedA/st-link-analysis). 
    """,
    icon="🚨",
)
st.markdown(
    """
    A list of events to listen to.  When any of these events are triggered,
    the event information is sent back to the Streamlit app as the component's
    return value. Each event can be defined using `Event` class which takes the
    following paramters:
     - **name:** User defined name which will be included in the return value to help identify the event
     - **event_type:** A space separated list of cytoscape.js events names to listen to (e.g.`click tap`). 
        For a full list of event types refer to [Cytoscape.js events](https://js.cytoscape.org/#events)
     - **selector:** A selector to specify elements for which the event handler runs (e.g. `node`). 
        For specification details refer to [Cytoscape.js selectors](https://js.cytoscape.org/#selectors)
    """
)

st.warning(
    "**NOTE:** event listners are only configured once. For changes in its configuration to take effect, you need to remount the componet."
)

st.markdown("The following example uses two events.")
st.code(
    """
    events = [
        Event("clicked_node", "click tap", "node"),
        Event("another_name", "dblclick dbltap", "*"),
    ]""",
    language="python",
)
st.markdown("**Total Number of runs:** %i" % st.session_state.counter)


node_styles = [
    NodeStyle("PERSON", "#FF7F3E", "email", "person"),
    NodeStyle("POST", "#2A629A", "created_at", "description"),
]

edge_styles = [
    EdgeStyle("FOLLOWS", caption="label", directed=True),
    EdgeStyle("POSTED", caption="label", directed=True),
    EdgeStyle("QUOTES", caption="label", directed=True),
]

events = [
    Event("clicked_node", "click tap", "node"),
    Event("another_name", "dblclick dbltap", "*"),
]

layout = "fcose"
with st.container(border=True):
    vals = st_link_analysis(
        elements, layout, node_styles, edge_styles, events=events, key="xyz"
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
