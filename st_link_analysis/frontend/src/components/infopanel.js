import State from "../utils/state";

// Constants / Configurations
const INFOPANEL_ID = "infopanel";
const LABEL_ID = "infopanelLabel";
const PROPS_ID = "infopanelProps";
const NODEACTIONS_ID = "nodeActions";

// Infopanel children updates
function _updateLabel(color, label, icon) {
    const label_div = document.getElementById(LABEL_ID);
    label_div.firstChild.innerText = label;
    label_div.firstChild.style.borderColor = color;
    label_div.lastChild.style.backgroundColor = color;
    if (icon && icon != "none") {
        label_div.lastChild.style.backgroundImage = `url(${icon})`;
    } else {
        label_div.lastChild.style.backgroundImage = "";
    }
}

function _updateProps(data) {
    const props = document.getElementById(PROPS_ID);
    props.innerHTML = Object.entries(data)
        .filter((item) => {
            return item[0] != "label";
        })
        .map(([key, value]) => {
            return `
        <div class='infopanel__prop'>
            <p class='infopanel__key'>${key}</p>
            <p class='infopanel__val'>${value}</p>
        </div>`;
        })
        .join("");
}

// infopanel update
function updateInfopanel() {
    const infopanel = document.getElementById(INFOPANEL_ID);
    const nodeActions = document.getElementById(NODEACTIONS_ID);
    const el = State.getState("selection").lastSelected;
    let color, data, label, expanded, icon;
    if (el) {
        color = el.style().backgroundColor;
        data = el.data();
        label = data["label"] || el.group().slice(0, -1).toUpperCase();
        expanded = true;
        icon = el.style()["background-image"];
    } else {
        color = "hsla(0, 0%, 0%, 0)";
        data = {};
        label = "";
        expanded = false;
        icon = null;
    }
    infopanel.setAttribute("data-expanded", expanded);
    nodeActions.setAttribute("data-expanded", expanded);
    _updateLabel(color, label, icon);
    _updateProps(data);
}

export default updateInfopanel;
