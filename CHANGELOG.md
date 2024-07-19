# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

### Added

-   Enable passing a list of events to listen to. When any of these events are triggered,
    the event information is sent back to the Streamlit app as the component's return
    value. The list of events can be defined using instances of the `Event` class and
    then passed to the component's `events` parameter.
-   Preview of the list of supported icons in the demo.

### Changed

-   Remove redundant "label" from infobar props. The label is already displayed at the top of the infobar.

### Fixed

-   Prevent last selected node's icon from showing when selecting an edge.
-   Pass default layout paramters to cola and fcose layouts

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
