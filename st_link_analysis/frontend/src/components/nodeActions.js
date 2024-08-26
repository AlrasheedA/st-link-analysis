import State from "../utils/state";
import { getCyInstance, debouncedSetValue, debounce } from "../utils/helpers";

// Configs
const IDS = {
    remove: "nodeActionsRemove",
    expand: "nodeActionsExpand",
};
const DELAYS = {
    default: 150,
};
const expandLayout = {
    name: "fcose",
    animationDuration: 500,
    randomize: false,
    fit: false,
    nodeDimensionsIncludeLabels: true,
    uniformNodeDimensions: true,
    numIter: 50,
    tile: false,
};

function animateNeighbors(parent, neighbors) {
    const pos = parent.position();
    const layout = {
        ...expandLayout,
        fixedNodeConstraint: [
            {
                nodeId: parent.id(),
                position: pos,
            },
        ],
    };
    neighbors.position(pos);
    neighbors.addClass("highlight");
    parent.connectedEdges().addClass("highlight");
    getCyInstance().layout(layout).run();
}

function _handleRemove() {
    const nodes = State.getState("selection").selected?.filter("node");
    if (nodes?.length > 0) {
        nodes.remove();
        debouncedSetValue({
            action: "remove",
            data: {
                node_ids: nodes.map((n) => {
                    return n.id();
                }),
            },
            timestamp: Date.now(),
        });
        nodes.unselect();
        State.updateState("lastExpanded", false);
    }
}

function _handleExpand() {
    const node = State.getState("selection").lastSelected?.filter("node");
    if (node?.group() == "nodes") {
        debouncedSetValue({
            action: "expand",
            data: { node_ids: [node.id()] },
            timestamp: Date.now(),
        });
        State.updateState("lastExpanded", node);
    }
}

const nodeActionsHandlers = {
    remove: debounce(_handleRemove, DELAYS.default),
    expand: debounce(_handleExpand, DELAYS.default),
};

function initNodeActions(nodeActions) {
    if (nodeActions.length === 0) {
        const nodeActions = document.getElementById("nodeActions");
        nodeActions.style.display = "none";
        return;
    }

    if (nodeActions.includes("remove")) {
        const remove = document.getElementById(IDS.remove);
        remove.addEventListener("click", nodeActionsHandlers.remove);
        remove.style.display = "flex";
        // keydown event
        document.addEventListener("keydown", (e) => {
            if (["Delete", "Backspace"].includes(e.key)) {
                nodeActionsHandlers.remove();
            }
        });
        // focus for keydown events
        document.body.setAttribute("tabindex", "0");
    }

    if (nodeActions.includes("expand")) {
        const expand = document.getElementById(IDS.expand);
        expand.addEventListener("click", nodeActionsHandlers.expand);
        expand.style.display = "flex";
        // dobule click event
        getCyInstance().on(
            "dblclick dbltap",
            "node",
            nodeActionsHandlers.expand
        );
    }
}

export { animateNeighbors };
export default initNodeActions;
