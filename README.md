# st-link-analysis

A custom Streamlit component for link analysis, built with Cytoscape.js and Streamlit.

## Overview

This project provides a Streamlit custom component for visualizing and interacting with graph data using Cytoscape.js. It supports customizable edge and node styles, labels, colors, captions, and icons.

## Demo
WIP

## Features

- **Customizable Node and Edge Styles**: Easily define the appearance of nodes and edges using a variety of style options.
- **Material Icons Support**: Supports a subset of Material icons for styling nodes which can be passed by name (e.g., `icon='person'`). Arbitrary icons can still be used by passing a url (`icon='url(...)'`).
- **Customizable Layouts**: Choose from different layout algorithms to arrange the graph elements. Currently only Cytoscape JS base layouts are supported.
- **Interactive Features:**
  - Fullscreen button.
  - JSON export button.
  - Layout refresh button.
  - Highlights neighboring nodes or edges when an element is selected.
  - View all properties of the selected elements in a sidebar.


## Installation

To install the package, use pip:

```bash
pip install st-link-analysis
```

## Usage

Here is a basic example of how to use the component in your Streamlit app:

```python
import streamlit as st
from st_link_analysis import st_link_analysis

# Sample data
elements = [
    {'data': {'id': 'A', 'label': 'Node A'}},
    {'data': {'id': 'B', 'label': 'Node B'}},
    {'data': {'source': 'A', 'target': 'B', 'label': 'Edge from A to B'}}
]

# Create the component
MyStreamlitComponent(elements=elements, height=500)
```

## API Reference

| Element                 | Description                                           |
|-------------------------|-------------------------------------------------------|
| `NodeStyle`             | Defines styles for nodes, including labels, colors, captions, and icons. Refer to docstring. |
| `EdgeStyle`             | Defines styles for edges, including curve styles, labels, colors, and directionality. Refer to docstring. |
| `st_link_analysis`      | Main component for creating and displaying the graph, including layout and height settings. Refer to docstring. |


## Development

WIP

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Cytoscape.js](https://js.cytoscape.org/)
- [Streamlit](https://www.streamlit.io/)
- [Material Icons](https://fonts.google.com/icons)



