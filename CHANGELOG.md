# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

### Changed

-   Reduce use of `wait_for_timeout` in tests by replacing it with selectors where
    appropriate, allowing Playwright to handle waiting automatically.

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
-   Pass default layout paramters to cola and fcose layouts
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
