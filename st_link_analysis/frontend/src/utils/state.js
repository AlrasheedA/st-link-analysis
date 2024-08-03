class StateManager {
    constructor() {
        if (StateManager.instance) {
            return StateManager.instance;
        }
        this.state = {
            selection: {
                selected: null,
                lastSelected: null,
            },
            style: {
                theme: "light",
                custom_style: [],
            },
            layout: null,
            lastExpanded: false,
        };
        this.observers = {
            selection: [],
            style: [],
            layout: [],
            lastExpanded: [],
        };
        StateManager.instance = this;
        return this;
    }
    getState(name) {
        return this.state[name];
    }
    updateState(name, value) {
        this.state[name] = value;
        this.notify(name);
    }
    subscribe(name, observer) {
        this.observers[name].push(observer);
    }
    notify(name) {
        this.observers[name].forEach((ob) => {
            ob(this.state[name]);
        });
    }
}

const State = new StateManager();
Object.freeze(State);

export default State;
