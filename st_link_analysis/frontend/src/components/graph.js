import cytoscape from "cytoscape";
import fcose from "cytoscape-fcose";
import cola from "cytoscape-cola";
import State from "../utils/state";
import { debounce, getCyInstance, debouncedSetValue } from "../utils/helpers";
import STYLES from "../utils/styles";

// Register cytoscape extensions
cytoscape.use(fcose);
cytoscape.use(cola);

// Constants & configurations
const CY_ID = "cy";
const SELECT_DEBOUNCE = 100;

// Event hanlders
function _handleSelection(e) {
    const selection = { selected: null, lastSelected: null };
    const type = e.type;
    if (type == "select") {
        selection.lastSelected = e.target;
    }
    selection.selected = e.cy.$(":selected");
    State.updateState("selection", selection);
    document.body.focus();
}

// Initailize cytoscape (only runs once)
function initCyto(listeners) {
    const cy = cytoscape({ container: document.getElementById(CY_ID) });
    cy.on("select unselect", debounce(_handleSelection, SELECT_DEBOUNCE));
    listeners.forEach((L) => {
        cy.on(
            L.event_type,
            L.selector,
            (e) => {
                debouncedSetValue({
                    action: L.name,
                    data: {
                        type: e.type,
                        target_id: e.target.id(),
                        target_group: e.target.group(),
                    },
                    timestamp: Date.now(),
                });
            },
            Math.max(L.debounce, 100)
        );
    });
    return cy;
}

// Callbacks for state changes
const graph = {
    updateHighlight: function () {
        const cy = getCyInstance();
        const el = State.getState("selection").lastSelected;
        cy.$(".highlight").removeClass("highlight");
        const g = el?.group();
        if (g == "nodes") {
            el.connectedEdges().addClass("highlight");
        } else if (g == "edges") {
            el.connectedNodes().addClass("highlight");
        }
    },
    updateLayout: function () {
        const cy = getCyInstance();
        cy.layout(State.getState("layout")).run();
    },
    updateStyle: function () {
        const cy = getCyInstance();
        const { theme, custom_style } = State.getState("style");
        const style = [
            ...STYLES[theme]["default"],
            ...custom_style,
            ...STYLES[theme]["highlight"],
        ];
        document.body.setAttribute("data-theme", theme);
        cy.style(style);
    },
};

export default initCyto;
export { graph };
