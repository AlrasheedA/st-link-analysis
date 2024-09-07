# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

## [0.3.0] - 2024-09-07

### Added

-   Added `node_actions` parameter to allow users to list which node actions to
    enable (e.g. `remove`, `expand`, or both).
    ([#28](https://github.com/AlrasheedA/st-link-analysis/pull/28))
-   Added `caption` parameter for `EdgeStyle` to allow users to specify which edge
    attribute to use as caption/label.
    ([#30](https://github.com/AlrasheedA/st-link-analysis/pull/30))

### Changed

-   Reduce use of `wait_for_timeout` in tests by replacing it with selectors where
    appropriate, allowing Playwright to handle waiting automatically.
    ([#25](https://github.com/AlrasheedA/st-link-analysis/pull/25))
-   Add pytest reruns to to avoid manual retrying of CI flaky tests.
    ([#25](https://github.com/AlrasheedA/st-link-analysis/pull/25))

### Deprecated

-   Depreceated the use of `enable_node_actions` parameter. `node_actions` should be
    used instead to enable node actions. If `enable_node_actions` is set to True
    and `node_actions` is not provided, default actions ('remove', 'expand')
    will be enabled.
    ([#28](https://github.com/AlrasheedA/st-link-analysis/pull/28))
-   Depreceated the use of `labeled` parameter for `EdgeStyle`. `caption` should be
    used instead to specify edge caption/label. If `labeled` is set to True and `caption`
    is not provided, default caption 'label' will be used.
    ([#30](https://github.com/AlrasheedA/st-link-analysis/pull/30)) 

## [0.2.0] - 2024-08-03

### Added

-   Enable passing a list of events to listen to. When any of these events are triggered,
    the event information is sent back to the Streamlit app as the component's return
    value. The list of events can be defined using instances of the `Event` class and
    then passed to the component's `events` parameter.
    ([#14](https://github.com/AlrasheedA/st-link-analysis/pull/14))
-   Preview of the list of supported icons in the demo.
    ([#15](https://github.com/AlrasheedA/st-link-analysis/pull/15)).
-   Enable node removal and expansion by passing `True` to the `enable_node_actions`
    parameter. Removal is triggered by delete keydown or remove button click. Expansion
    is triggered by node double click or expand button click. When any of these events
    are triggered the event is sent back along with selected node IDs to the Streamlit
    app as the component's return value
    ([#21](https://github.com/AlrasheedA/st-link-analysis/pull/21)).

### Changed

-   Remove redundant "label" from infopanel props. The label is already displayed at
    the top of the infopanel.
-   Rename `infobar` to `infopanel`
-   Refactor reusable css styles.
-   `height` now can only be initialized once. Changing values requires remounting
    the component.

### Fixed

-   Prevent last selected node's icon from showing when selecting an edge.
-   Pass default layout parameters to cola and fcose layouts
-   Disable infopanel from expanding when selecting multiple elements

## [0.1.0] - 2024-07-11

### Added

-   Changelog
-   fcose and cola layout support ([#10](https://github.com/AlrasheedA/st-link-analysis/pull/10))
-   Viewbar frontend component for zooming, fitting, and centering the view ([#8](https://github.com/AlrasheedA/st-link-analysis/pull/8))
-   Github workflow for PRs
-   README development instructions
-   Python linting and testing (Ruff & playwright-pytest)
-   Node formatting and linting (Prettier & ESLint)

### Changed

-   Updated CSS styling ([#7](https://github.com/AlrasheedA/st-link-analysis/pull/7))
-   Extended examples to include more functionality + documentation ()

### Removed

-   Examples in the module's directory

## [0.0.1] - 2024-06-22

Initial release
