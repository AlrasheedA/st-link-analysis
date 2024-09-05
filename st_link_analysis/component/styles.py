import warnings

from typing import Optional


# TODO: remove if no depreciation warnings
class LinkAnalysisDeprecationWarning(DeprecationWarning):
    pass


warnings.simplefilter("once", LinkAnalysisDeprecationWarning)


class NodeStyle:
    def __init__(
        self,
        label: str,
        color: Optional[str] = None,
        caption: Optional[str] = None,
        icon: Optional[str] = None,
    ) -> None:
        """
        Define a custom style of a node in the graph based on label.

        Parameters
        ----------
        label : str
            The label of the node. This label is used to identify the group or
            category of the node.
        color : Optional[str]
            Specifies the background color of the node. If not provided, the
            default node color "#0a0a0a" will be used.
        caption : Optional[str]
            Name of the node's attribute to use as caption/label. If not provided,
            no caption will be shown.
        icon: Optional[str]
            Node icon to be passed by the name of Material Icons (e.g. 'person')
            or by url (e.g. url('...')). A list of supported icons is available
            in `st_link_analysis.component.icons`

        Example
        -------
        >>> node_style = NodeStyle(label="Person", color="#345eeb", caption="name")
        """
        self.label = label
        self.color = color
        self.caption = caption
        self.icon = icon

    def dump(self) -> dict:
        selector = f"node[label='{self.label}']"
        style = {}

        if self.color:
            style["background-color"] = self.color
        if self.caption:
            style["label"] = f"data({self.caption})"
        if self.icon:
            if not self.icon.startswith("url"):
                self.icon = f"./icons/{self.icon.lower()}.svg"
            style["background-image"] = self.icon

        return {
            "selector": selector,
            "style": style,
        }


class EdgeStyle:
    def __init__(
        self,
        label: str,
        color: Optional[str] = None,
        caption: Optional[str] = None,
        labeled: bool = False,  # deprecated
        directed: bool = False,
        curve_style: Optional[str] = None,
    ) -> None:
        """
        Define a custom style of an edge in the graph based on label.

        Parameters
        ----------
        label : str
            The label of the edge. This label is used to identify the group or
            category of the edge.
        color : Optional[str]
            Specifies the color of the edge line.
        caption : Optional[str], default None
            Name of the edge's attribute to use as caption/label. If not provided,
            no caption will be shown.
        labeled : bool, default False (deprecated)
            This parameter is deprecated and will be removed in a future release. Use
            `caption` instead to specify edge caption/label. If `labeled` is set to True
            and `caption` is not provided, default caption 'label' will be used.
        directed : bool, default False
            Indicates whether the edge is directed. If True, the edge will be
            rendered with an arrow pointing from the source to target. Default
            is False. Note: Arrows will not be displayed if `curve_style`
            is set to "haystack".
        curve_style: Optional[str]
            Specifies the edge curving method to use. By default, it is set to
            "bezier", which is suitable for multigraphs. For large, simple graphs,
            consider using "haystack" for better performance. For more options
            and detailed information,visit: https://js.cytoscape.org/#style/edge-line

        Example
        -------
        >>> edge_style = EdgeStyle(label="FOLLOWS", color="#345eeb")
        """
        self.label = label
        self.color = color
        self.caption = caption
        self.directed = directed
        self.curve_style = curve_style

        # TODO: remove in next version along with imports, docs, and signature
        if labeled is not None:
            warnings.warn(
                "Paramter `labeled` is deprecated and will be removed in a future release. "
                "Please use the `caption` parameter instead.",
                LinkAnalysisDeprecationWarning,
            )
        if labeled and not caption:
            self.caption = "label"

    def dump(self) -> dict:
        selector = f"edge[label='{self.label}']"
        style = {}

        if self.color:
            style["line-color"] = self.color
            style["background-color"] = self.color
            style["text-background-color"] = self.color
            style["target-arrow-color"] = self.color
        if self.caption:
            style["label"] = f"data({self.caption})"
        if self.directed:
            style["target-arrow-shape"] = "triangle"
        if self.curve_style:
            style["curve-style"] = self.curve_style

        return {
            "selector": selector,
            "style": style,
        }
