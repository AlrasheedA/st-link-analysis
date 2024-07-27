"""
For more details refer to https://js.cytoscape.org/#events
"""

RESERVED_NAMES = ["remove", "expand"]

class Event:
    def __init__(
        self,
        name: str,
        event_type: str,
        selector: str,
    ) -> None:
        """
        Define an event to pass to component constructor and listen to.

        Parameters
        ----------
        name: str
            User defined name which will be included in the return value to help
            identify the event
        event_type: str
            A space separated list of cytoscape.js events names to listen to
            (e.g."click tap"). For a full list of event types refer to
            https://js.cytoscape.org/#events
        selector: str
            A selector to specify elements for which the event handler runs
            (e.g. "node"). For specification details refer to https://js.cytoscape.org/#selectors

        Example
        ----------
        >>> e1 = Event("clicked_node", "click tap", "node")
        """
        self.name = name
        self.event_type = event_type
        self.selector = selector
        if name in RESERVED_NAMES:
            raise ValueError(f"{RESERVED_NAMES} are reserved action names")

    def dump(self) -> dict:
        return {
            "name": self.name,
            "event_type": self.event_type,
            "selector": self.selector,
        }
