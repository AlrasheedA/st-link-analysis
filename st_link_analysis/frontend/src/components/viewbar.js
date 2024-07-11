import { debounce, getCyInstance } from "../utils/helpers";

// Constants / Configurations
const IDS = {
    plus: "viewbarPlus",
    minus: "viewbarMinus",
    fit: "viewbarFit",
    center: "viewbarCenter",
};
const DELAYS = {
    default: 200,
    plus: 50,
    minus: 50,
};
const ZOOM_FACTOR = 0.8;

// Event Handlers
const clickHandlers = {
    plus: debounce(() => {
        const cy = getCyInstance();
        const ex = cy.extent();
        cy.animate({
            zoom: {
                level: cy.zoom() * (1 / ZOOM_FACTOR),
                position: { x: ex.x1 + 0.5 * ex.w, y: ex.y1 + 0.5 * ex.h },
            },
            duration: DELAYS.plus,
        });
    }, DELAYS.plus),

    minus: debounce(() => {
        const cy = getCyInstance();
        const ex = cy.extent();
        cy.animate({
            zoom: {
                level: cy.zoom() * ZOOM_FACTOR,
                position: { x: ex.x1 + 0.5 * ex.w, y: ex.y1 + 0.5 * ex.h },
            },
            duration: DELAYS.minus,
        });
    }, DELAYS.minus),

    fit: debounce(() => {
        const cy = getCyInstance();
        cy.animate({ fit: { padding: 20 }, duration: DELAYS.default });
    }, DELAYS.default),

    center: debounce(() => {
        const cy = getCyInstance();
        cy.animate({ center: {}, duration: DELAYS.default });
    }, DELAYS.default),
};

// View initialization
function initViewbar() {
    document
        .getElementById(IDS.plus)
        .addEventListener("click", clickHandlers.plus);
    document
        .getElementById(IDS.minus)
        .addEventListener("click", clickHandlers.minus);
    document
        .getElementById(IDS.fit)
        .addEventListener("click", clickHandlers.fit);
    document
        .getElementById(IDS.center)
        .addEventListener("click", clickHandlers.center);
}

export default initViewbar;
