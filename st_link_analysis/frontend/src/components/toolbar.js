import State from "../utils/state";
import { debounce, getCyInstance } from "../utils/helpers";

// Constants / Configurations
const IDS = {
    fullscreen: "toolbarFullscreen",
    refresh: "toolbarRefresh",
    export: "toolbarExport",
};
const DELAYS = {
    default: 150,
    fullscreen: 100,
    refresh: 200,
    export: 250,
};

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
};

// Toolbar initialization
function initToolbar() {
    document
        .getElementById(IDS.fullscreen)
        .addEventListener("click", clickHandlers.fullscreen);
    document
        .getElementById(IDS.refresh)
        .addEventListener("click", clickHandlers.refresh);
    document
        .getElementById(IDS.export)
        .addEventListener("click", clickHandlers.export);
}

export default initToolbar;
