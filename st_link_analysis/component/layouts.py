"""
For full options see https://js.cytoscape.org/#layouts
"""

DEFAULT_ATTRS = {
    "padding": 20,
    "animationDuration": 500,
    "fit": True,
    "animate": True,
    "nodeDimensionsIncludeLabels": True,
}

LAYOUTS = {
    "cose": {
        **DEFAULT_ATTRS,
        "name": "cose",
        "nodeRepulsion": 2024,
        "animate": "end",
    },
    "random": {
        **DEFAULT_ATTRS,
        "name": "random",
    },
    "grid": {
        **DEFAULT_ATTRS,
        "name": "grid",
    },
    "circle": {
        **DEFAULT_ATTRS,
        "name": "circle",
        "nodeDimensionsIncludeLabels": False,
    },
    "concentric": {
        **DEFAULT_ATTRS,
        "name": "concentric",
        "minNodeSpacing": 40,
        "nodeDimensionsIncludeLabels": False,
    },
    "breadthfirst": {
        **DEFAULT_ATTRS,
        "name": "breadthfirst",
        "directed": True,
    },
    "fcose": {
        **DEFAULT_ATTRS,
        "name": "fcose",
    },
    "cola": {
        **DEFAULT_ATTRS,
        "name": "cola",
    },
}
