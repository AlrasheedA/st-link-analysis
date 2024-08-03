import { Streamlit } from "streamlit-component-lib";

function debounce(func, wait) {
    let timeout;
    return function (...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
}

function getCyInstance() {
    const cy = document.getElementById("cy")?._cyreg?.cy;
    if (!cy) {
        console.error("Cytoscape instance not found.");
        return null;
    }
    return cy;
}

function setStreamlitValue({ action, data, timestamp } = {}) {
    Streamlit.setComponentValue({
        action: action,
        data: data,
        timestamp: timestamp,
    });
}

const debouncedSetValue = debounce(setStreamlitValue, 100);

export { debounce, getCyInstance, debouncedSetValue };
