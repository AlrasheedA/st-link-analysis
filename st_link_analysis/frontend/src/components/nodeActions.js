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
    }
}

const nodeActionsHandlers = {
    remove: debounce(_handleRemove, DELAYS.default),
    expand: debounce(_handleExpand, DELAYS.default),
};

function initNodeActions(enableNodeActions) {
    if (enableNodeActions === false) {
        return;
    }

    // 'REMOVE' triggers
    document.addEventListener("keydown", (e) => {
        if (["Delete", "Backspace"].includes(e.key)) {
            nodeActionsHandlers.remove();
        }
    });
    document
        .getElementById(IDS.remove)
        .addEventListener("click", nodeActionsHandlers.remove);

    // 'EXPAND' triggers
    getCyInstance().on("dblclick dbltap", "node", nodeActionsHandlers.expand);
    document
        .getElementById(IDS.expand)
        .addEventListener("click", nodeActionsHandlers.expand);

    // focus for keydown events
    document.body.setAttribute("tabindex", "0");
    document.body.focus();
}

export default initNodeActions;
