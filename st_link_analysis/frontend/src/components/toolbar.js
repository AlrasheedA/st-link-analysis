import State from "../utils/state";
import { debounce, getCyInstance, setStreamlitValue } from "../utils/helpers";

// Constants / Configurations
const IDS = {
    fullscreen: "toolbarFullscreen",
    refresh: "toolbarRefresh",
    export: "toolbarExport",
    expand: "toolbarExpand",
    remove: "toolbarRemove",
};
const DELAYS = {
    default: 150,
    fullscreen: 100,
    refresh: 200,
    export: 250,
};

// Helper
function prepareSelectionData(selection) {
    const nodes = selection.filter("node").map((e) => {
        return e.id();
    });
    const edges = selection.filter("edge").map((e) => {
        return e.id();
    });
    return {
        nodes: nodes,
        edges: edges,
    };
}

// Event Handlers
const clickHandlers = {
    fullscreen: debounce(() => {
        if (document.fullscreenElement) {
            document.exitFullscreen();
        } else {
            document.getElementById("container").requestFullscreen();
        }
    }, DELAYS.fullscreen),

    refresh: debounce(() => {
        const cy = getCyInstance();
        cy.layout(State.getState("layout")).run();
    }, DELAYS.refresh),

    export: debounce(() => {
        const cy = getCyInstance();
        let json = cy.elements().not(":hidden").jsons();
        json = new Blob([JSON.stringify(json, null, 2)], {
            type: "application/json",
        });
        json = URL.createObjectURL(json);
        const link = document.createElement("a");
        link.href = json;
        link.download = "graph.json";
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(json);
    }, DELAYS.export),

    expand: debounce(() => {
        const selection = State.getState("selection").selected;
        setStreamlitValue({
            action: "toolbar_expand",
            data: prepareSelectionData(selection),
            timestamp: Date.now(),
        });
        console.log(State.getState("selection").selected);
    }, DELAYS.default),

    remove: debounce(() => {
        const selection = State.getState("selection").selected;
        setStreamlitValue({
            action: "toolbar_remove",
            data: prepareSelectionData(selection),
            timestamp: Date.now(),
        });
    }, DELAYS.default),
};

// Toolbar initialization
function initToolbar(extendedToolbar) {
    document
        .getElementById(IDS.fullscreen)
        .addEventListener("click", clickHandlers.fullscreen);
    document
        .getElementById(IDS.refresh)
        .addEventListener("click", clickHandlers.refresh);
    document
        .getElementById(IDS.export)
        .addEventListener("click", clickHandlers.export);

    if (extendedToolbar) {
        document.getElementById(IDS.export).nextSibling.remove();
        document
            .getElementById(IDS.expand)
            .addEventListener("click", clickHandlers.expand);
        document
            .getElementById(IDS.remove)
            .addEventListener("click", clickHandlers.remove);
    } else {
        let el = document.getElementById(IDS.expand);
        for (let i = 0; i < 3; i++) {
            let sib = el.nextSibling;
            el.remove();
            el = sib;
        }
    }
}

export default initToolbar;
