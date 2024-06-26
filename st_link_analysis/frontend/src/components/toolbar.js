import State from "../utils/state";
import { debounce, getCyInstance } from "../utils/helpers";

// Constants / Configurations
const FS_ID = "toolbarFullscreen";
const REFRESH_ID = "toolbarRefresh";
const EXPORT_ID = "toolbarExport";
const FS_DEBOUNCE = 100;
const REFRESH_DEBOUNCE = 200;
const EXPORT_DEBOUNCE = 250;

// Event Handlers
function __handleFsClick() {
    if (document.fullscreenElement) {
        document.exitFullscreen();
    } else {
        document.getElementById("container").requestFullscreen();
    }
}

function _handleRefreshClick() {
    const cy = getCyInstance();
    cy.layout(State.getState("layout")).run();
}

function _handleExportClick() {
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
}

// Toolbar initialization
function initToolbar() {
    const fs = document.getElementById(FS_ID);
    const refresh = document.getElementById(REFRESH_ID);
    const json_export = document.getElementById(EXPORT_ID);

    fs.addEventListener("click", debounce(__handleFsClick, FS_DEBOUNCE));
    refresh.addEventListener(
        "click",
        debounce(_handleRefreshClick, REFRESH_DEBOUNCE)
    );
    json_export.addEventListener(
        "click",
        debounce(_handleExportClick, EXPORT_DEBOUNCE)
    );
}

export default initToolbar;
