import os
import streamlit.components.v1 as components
from typing import Optional, Union

from st_link_analysis.component.layouts import LAYOUTS
from st_link_analysis.component.styles import NodeStyle, EdgeStyle
from st_link_analysis.component.events import Event

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "st_link_analysis",
        url="http://localhost:3001",  # For development
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "../frontend/build")
    _component_func = components.declare_component(
        "st_link_analysis",
        path=build_dir,  # For distribution
    )


def st_link_analysis(
    elements: dict,
    layout: Union[str, dict] = "cose",
    node_styles: list[NodeStyle] = [],
    edge_styles: list[EdgeStyle] = [],
    height: int = 500,
    key: Optional[str] = None,
    events: list[Event] = [],
) -> None:
    """
    Renders a link analysis graph using Cytoscape in Streamlit.

    Parameters
    ----------
    elements : dict
        Graph elements data including nodes and edges. Each node should have
        an 'id', and 'name'. Each edge should have an 'id', 'source', 'target',
        and 'label'.
    layout : str or dict, default 'cose'
        Layout configuration for Cytoscape. If a string is provided, it
        specifies the layout name. If a dictionary is provided, it should
        contain layout options. Default is "cose". A list of support layouts and
        default settings is available in `st_link_analysis.component.layout`
    node_styles : list[NodeStyle], optional
        A list of custom NodeStyle instances to apply styles to node groups in the graph
    edge_styles : list[EdgeStyle], optional
        A list of custom EdgeStyle instances to apply styles to edge groups in the graph
    height: int, default 500
        Component's height in pixels.
    key : str, optional
        A unique key for the component. If provided, this key allows multiple
        instances of the component to exist in the same Streamlit app without
        conflicts. Setting this parameter is also important to avoid unnecessary
        re-rendering of the component.
    events: list[Event]
        For advanced usage only. A list of events to listen to.  When any of these
        events are triggered, the event information is sent back to the Streamlit
        app as the component's return value. NOTE: only defined once. Changing the
        list of events requires remounting the component.

    Returns
    -------
    None
        This function does not return anything. It renders the Cytoscape component in the
        Streamlit app.
    """
    node_styles = [n.dump() for n in node_styles]
    edge_styles = [e.dump() for e in edge_styles]
    style = node_styles + edge_styles

    height = str(height) + "px"

    if isinstance(layout, str):
        layout = LAYOUTS[layout]

    events = [e.dump() for e in events]

    return _component_func(
        elements=elements,
        style=style,
        layout=layout,
        height=height,
        key=key,
        events=events,
    )
