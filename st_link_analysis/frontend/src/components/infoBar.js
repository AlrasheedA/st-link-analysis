import State from "../utils/state";

// Constants / Configurations
const INFOBAR_ID = "infobar";
const LABEL_ID = "infobarLabel";
const PROPS_ID = "infobarProps";

// InfoBar children updates
function _updateLabel(color, label, icon) {
    const label_div = document.getElementById(LABEL_ID);
    label_div.firstChild.innerText = label;
    label_div.firstChild.style.borderColor = color;
    label_div.lastChild.style.backgroundColor = color;
    if (icon) {
        label_div.lastChild.style.backgroundImage = `url(${icon})`;
    } else {
        label_div.lastChild.style.backgroundImage = null;
    }
}

function _updateProps(data) {
    const props = document.getElementById(PROPS_ID);
    props.innerHTML = Object.entries(data)
        .map(([key, value]) => {
            return `
        <div class='infobar__prop'>
            <p class='infobar__key'>${key}</p>
            <p class='infobar__val'>${value}</p>
        </div>`;
        })
        .join("");
}

// InfoBar update
function updateInfoBar() {
    const infoBar = document.getElementById(INFOBAR_ID);
    const el = State.getState("selection").lastSelected;
    let color, data, label, selected, icon;
    if (el) {
        color = el.style().backgroundColor;
        data = el.data();
        label = data["label"] || el.group().slice(0, -1).toUpperCase();
        selected = "element";
        icon = el.style()["background-image"];
    } else {
        color = "hsla(0, 0%, 0%, 0)";
        data = {};
        label = "";
        selected = null;
        icon = null;
    }
    infoBar.setAttribute("data-selected", selected);
    _updateLabel(color, label, icon);
    _updateProps(data);
}

export default updateInfoBar;
