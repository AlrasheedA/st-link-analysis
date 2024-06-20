import cytoscape from "cytoscape";
import State from "../utils/state";
import { debounce, getCyInstance } from "../utils/helpers";
import STYLES from "../utils/styles";

// Constants / Configurations
const CY_ID = "cy";
const SELECT_DEBOUNCE = 100;

function _handleSelection(e) {
    const selection = { selected: null, lastSelected: null };
    const type = e.type;
    if (type == "select") {
        selection.lastSelected = e.target;
    }
    selection.selected = e.cy.$(":selected");
    State.updateState("selection", selection);
}

function initCyto() {
    const cy = cytoscape({ container: document.getElementById(CY_ID) });
    cy.on("select unselect", debounce(_handleSelection, SELECT_DEBOUNCE));
    return cy;
}

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
