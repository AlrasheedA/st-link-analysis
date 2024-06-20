import State from "../utils/state";

// Constants / Configurations
const INFOBAR_ID = "infoBar";
const LABEL_ID = "infoBar_label";
const PROPS_ID = "infoBar_props";

// InfoBar children updates
function _updateLabel(color, label) {
    const label_div = document.getElementById(LABEL_ID);
    label_div.style.backgroundColor = color;
    label_div.innerText = label;
}

function _updateProps(data) {
    const props = document.getElementById(PROPS_ID);
    props.innerHTML = Object.entries(data)
        .map(([key, value]) => {
            return `
        <div class='prop'>
            <p class='propKey'>${key}</p>
            <p class='propVal'>${value}</p>
        </div>`;
        })
        .join("");
}

// InfoBar update
function updateInfoBar() {
    const infoBar = document.getElementById(INFOBAR_ID);
    const el = State.getState("selection").lastSelected;
    let color, data, label, selected;
    if (el) {
        color = el.style().backgroundColor;
        data = el.data();
        label = data["label"] || el.group().slice(0, -1).toUpperCase();
        selected = "element";
    } else {
        color = "white";
        data = {};
        label = "";
        selected = null;
    }
    infoBar.setAttribute("data-selected", selected);
    _updateLabel(color, label);
    _updateProps(data);
}

export default updateInfoBar;
