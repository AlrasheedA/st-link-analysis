from playwright.sync_api import Page
import json


PAGE_NAME = "Events Listeners"
NODE_ID = "n4"
EDGE_ID = "e2"
ASSIGN_CY = "const cy = document.getElementById('cy')._cyreg.cy;"
FRAME_LOCATOR = "iframe[title*='st_link_analysis']"


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
    data = page.get_by_test_id("stJson").text_content().replace('""', '","')
    return json.loads(data)


def test_single_click_node_event(page: Page):
    page.get_by_role("link", name=PAGE_NAME).click()
    frame = page.frame_locator(FRAME_LOCATOR).first.locator(":root")
    frame.click(position={"x": 0, "y": 0})  # await and scroll to view

    pos = get_node_pos(NODE_ID, frame)
    frame.click(position=pos)
    page.wait_for_timeout(300)
    data = get_return_json(page)
    assert data["event"]["target_id"] == NODE_ID
    assert data["event"]["target_group"] == "nodes"
    assert data["event"]["name"] == "clicked_node"


def test_double_click_edge_event(page: Page):
    page.get_by_role("link", name=PAGE_NAME).click()
    frame = page.frame_locator(FRAME_LOCATOR).first.locator(":root")
    frame.click(position={"x": 0, "y": 0})  # await and scroll to view

    pos = get_edge_pos(EDGE_ID, frame)
    frame.dblclick(position=pos)
    page.wait_for_timeout(300)
    data = get_return_json(page)
    assert data["event"]["target_id"] == EDGE_ID
    assert data["event"]["target_group"] == "edges"
    assert data["event"]["name"] == "another_name"


def test_single_click_edge_no_event(page: Page):
    page.get_by_role("link", name=PAGE_NAME).click()
    frame = page.frame_locator(FRAME_LOCATOR).first.locator(":root")
    frame.click(position={"x": 0, "y": 0})  # await and scroll to view

    pos = get_edge_pos(EDGE_ID, frame)
    frame.click(position=pos)
    page.wait_for_timeout(250)
    data = get_return_json(page)
    assert data == {}
