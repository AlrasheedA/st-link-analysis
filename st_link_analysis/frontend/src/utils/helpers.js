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

export { debounce, getCyInstance };
