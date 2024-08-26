import "./style.css";
import { Streamlit } from "streamlit-component-lib";
import State from "./utils/state.js";
import { debounce } from "./utils/helpers.js";
import initCyto, { graph } from "./components/graph.js";
import initToolbar from "./components/toolbar.js";
import initViewbar from "./components/viewbar.js";
import initNodeActions, { animateNeighbors } from "./components/nodeActions.js";
import updateInfopanel from "./components/infopanel.js";

// Constants / Configurations
const CONTAINER_ID = "container";
const RENDER_DEBOUNCE = 100;
const SETFRAME_DELAY = 150;

// Subscribe to state changes
State.subscribe("selection", updateInfopanel);
State.subscribe("selection", graph.updateHighlight);
State.subscribe("layout", graph.updateLayout);
State.subscribe("style", graph.updateStyle);

// Initialize variables for onRender
let cy;
let elements, newElements;
let style, newStyle;
let layout, newLayout;

// Streamlit render event handler
function onRender(event) {
    const { args, theme } = event.detail;
    newElements = JSON.stringify(args["elements"]);
    newStyle = JSON.stringify(args["style"]) + theme.base;
    newLayout = JSON.stringify(args["layout"]);
    document.getElementById("container").style.height = args["height"];

    // Initialize once
    if (!cy) {
        document.getElementById("container").style.height = args["height"];
        cy = initCyto(args["events"]);
        cy.json({ elements: args["elements"] });
        elements = newElements;
        initNodeActions(args["nodeActions"]);
        initToolbar();
        initViewbar();
    }
    // Elements dynamic update
    if (newElements != elements) {
        elements = newElements;
        const lastExpanded = State.getState("lastExpanded");
        if (lastExpanded === false) {
            // default behavior
            cy.json({ elements: args["elements"] });
        } else {
            // if last action === expand
            const newNodes = cy
                .add([
                    ...args["elements"]["nodes"],
                    ...args["elements"]["edges"],
                ])
                .filter("node");
            animateNeighbors(lastExpanded, newNodes);
        }
    }
    State.updateState("lastExpanded", false);

    // Style dynamic update
    if (newStyle != style) {
        style = newStyle;
        State.updateState("style", {
            custom_style: args["style"],
            theme: theme.base,
        });
    }

    // Layout dynamic update
    if (newLayout != layout) {
        layout = newLayout;
        State.updateState("layout", args["layout"]);
    }

    setTimeout(() => {
        Streamlit.setFrameHeight();
    }, SETFRAME_DELAY);
}

// Reset streamlit frame height on fullscreen changes
document.addEventListener("fullscreenchange", function () {
    setTimeout(() => {
        Streamlit.setFrameHeight();
        document.getElementById(CONTAINER_ID).scrollIntoView();
    }, SETFRAME_DELAY);
});

setTimeout(() => {
    Streamlit.setFrameHeight();
}, SETFRAME_DELAY);
Streamlit.events.addEventListener(
    Streamlit.RENDER_EVENT,
    debounce(onRender, RENDER_DEBOUNCE)
);
Streamlit.setComponentReady();
