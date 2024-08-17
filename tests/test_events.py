from playwright.sync_api import Page, expect
import json


PAGE_NAME = "Events Listeners"
NODE_ID = "n4"
EDGE_ID = "e2"
ASSIGN_CY = "const cy = document.getElementById('cy')._cyreg.cy;"
FRAME_LOCATOR = "iframe[title*='st_link_analysis']"

def AWAIT_RETURN_ACTION(page):
    page.get_by_text('"action":"').click()

def AWAIT_SELECT(frame):
    infopanel_label = frame.locator('#infopanelLabel')
    expect(infopanel_label).to_be_visible()

def get_node_pos(_id, iframe):
    pos = iframe.evaluate(f"""() => {{
        {ASSIGN_CY}
        return cy.getElementById("{_id}").renderedPosition();
    }}""")
    return pos


def get_edge_pos(_id, iframe):
    pos = iframe.evaluate(f"""() => {{
        {ASSIGN_CY}
        return cy.getElementById("{_id}").renderedMidpoint();
    }}""")
    return pos


def get_return_json(page: Page):
    data = (
        page.get_by_test_id("stJson")
        .text_content()
        .replace('""', '","')
        .replace('}"', '},"')
    )
    return json.loads(data)


def test_iframe_exists_events(page: Page):
    page.get_by_role("link", name=PAGE_NAME).click()
    page.wait_for_load_state("networkidle")
    frames = page.query_selector_all(FRAME_LOCATOR)
    assert len(frames) == 1


def test_single_click_node_event(page: Page):
    page.get_by_role("link", name=PAGE_NAME).click()
    frame = page.frame_locator(FRAME_LOCATOR).first.locator(":root")
    frame.click(position={"x": 0, "y": 0})  # await and scroll to view

    pos = get_node_pos(NODE_ID, frame)
    frame.click(position=pos)
    AWAIT_RETURN_ACTION(page)
    data = get_return_json(page)

    assert data["data"]["target_id"] == NODE_ID
    assert data["data"]["target_group"] == "nodes"
    assert data["action"] == "clicked_node"


def test_double_click_edge_event(page: Page):
    page.get_by_role("link", name=PAGE_NAME).click()
    frame = page.frame_locator(FRAME_LOCATOR).first.locator(":root")
    frame.click(position={"x": 0, "y": 0})  # await and scroll to view

    pos = get_edge_pos(EDGE_ID, frame)
    frame.dblclick(position=pos)
    AWAIT_RETURN_ACTION(page)
    data = get_return_json(page)

    assert data["data"]["target_id"] == EDGE_ID
    assert data["data"]["target_group"] == "edges"
    assert data["action"] == "another_name"


def test_single_click_edge_no_event(page: Page):
    page.get_by_role("link", name=PAGE_NAME).click()
    frame = page.frame_locator(FRAME_LOCATOR).first.locator(":root")
    frame.click(position={"x": 0, "y": 0})  # await and scroll to view

    pos = get_edge_pos(EDGE_ID, frame)
    frame.click(position=pos)
    AWAIT_SELECT(frame)
    data = get_return_json(page)

    assert data == {}
