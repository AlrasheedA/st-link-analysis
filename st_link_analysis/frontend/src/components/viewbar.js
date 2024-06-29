import { debounce, getCyInstance } from "../utils/helpers";

// Constants / Configurations
const PLUS_ID = "viewbarPlus";
const MINUS_ID = "viewbarMinus";
const FIT_ID = "viewbarFit";
const CENTER_ID = "viewbarCenter";
const ZOOM_DEBOUNCE = 50;
const FIT_DEBOUNCE = 200;
const ZOOM_FACTOR = 0.8;

// Event Handlers
function _handlePlusClick() {
    const cy = getCyInstance();
    const ex = cy.extent();
    cy.animate({
        zoom: {
            level: cy.zoom() * (1 / ZOOM_FACTOR),
            position: { x: ex.x1 + 0.5 * ex.w, y: ex.y1 + 0.5 * ex.h },
        },
        duration: ZOOM_DEBOUNCE,
    });
}

function _handleMinusClick() {
    const cy = getCyInstance();
    const ex = cy.extent();
    cy.animate({
        zoom: {
            level: cy.zoom() * ZOOM_FACTOR,
            position: { x: ex.x1 + 0.5 * ex.w, y: ex.y1 + 0.5 * ex.h },
        },
        duration: ZOOM_DEBOUNCE,
    });
}

function _handleFitClick() {
    const cy = getCyInstance();
    cy.animate({ fit: { padding: 20 }, duration: FIT_DEBOUNCE });
}

function _handleCenterClick() {
    const cy = getCyInstance();
    cy.animate({ center: {}, duration: FIT_DEBOUNCE });
}

// View initialization
function initViewbar() {
    const plus = document.getElementById(PLUS_ID);
    const minus = document.getElementById(MINUS_ID);
    const fit = document.getElementById(FIT_ID);
    const cent = document.getElementById(CENTER_ID);

    plus.addEventListener("click", debounce(_handlePlusClick, ZOOM_DEBOUNCE));
    minus.addEventListener("click", debounce(_handleMinusClick, ZOOM_DEBOUNCE));
    fit.addEventListener("click", debounce(_handleFitClick, FIT_DEBOUNCE));
    cent.addEventListener("click", debounce(_handleCenterClick, FIT_DEBOUNCE));
}

export default initViewbar;
