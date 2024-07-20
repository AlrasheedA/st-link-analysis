import "./style.css";
import { Streamlit } from "streamlit-component-lib";
import State from "./utils/state.js";
import { debounce } from "./utils/helpers.js";
import initCyto, { graph } from "./components/graph.js";
import initToolbar from "./components/toolbar.js";
import initViewbar from "./components/viewbar.js";
import updateInfobar from "./components/infobar.js";

// Constants / Configurations
const CONTAINER_ID = "container";
const RENDER_DEBOUNCE = 100;
const SETFRAME_DELAY = 150;

// Subscribe to state changes
State.subscribe("selection", updateInfobar);
State.subscribe("selection", graph.updateHighlight);
State.subscribe("layout", graph.updateLayout);
State.subscribe("style", graph.updateStyle);

// Initialize variables for onRender
let cy;
let elements, newElements;
let style, newStyle;
let layout, newLayout;
let height, newHeight;

// Streamlit render event handler
function onRender(event) {
    const { args, theme } = event.detail;
    newElements = JSON.stringify(args["elements"]);
    newStyle = JSON.stringify(args["style"]) + theme.base;
    newLayout = JSON.stringify(args["layout"]);
    newHeight = args["height"];
    // Set height first
    if (newHeight != height) {
        height = newHeight;
        document.getElementById("container").style.height = height;
    }
    // Initialize cytoscape instance once
    if (!cy) {
        cy = initCyto(args["events"]);
        initToolbar(args["extended_toolbar"]);
        initViewbar();
    }
    // Only update if changes detected
    if (newElements != elements) {
        elements = newElements;
        cy.json({ elements: args["elements"] });
    }
    if (newStyle != style) {
        style = newStyle;
        State.updateState("style", {
            custom_style: args["style"],
            theme: theme.base,
        });
    }
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
