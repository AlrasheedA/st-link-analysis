from playwright.sync_api import Page, expect
import json
import re


PAGE_NAME = "Node Actions"
NODE_ID = "c"
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

def get_return_json(page: Page):
    AWAIT_RETURN_ACTION(page)
    data = (
        page.get_by_test_id("stJson")
        .text_content()
        .replace('""', '","')
        .replace('}"', '},"')
    )
    data = re.sub("([0-9]+):", "", data)
    return json.loads(data)


def test_iframe_exists_events(page: Page):
    page.get_by_role("link", name=PAGE_NAME).click()
    page.wait_for_load_state("networkidle")
    frames = page.query_selector_all(FRAME_LOCATOR)
    assert len(frames) == 1


def test_expand_dblclick(page: Page):
    page.get_by_role("link", name=PAGE_NAME).click()
    frame = page.frame_locator(FRAME_LOCATOR).first.locator(":root")
    frame.click(position={"x": 0, "y": 0})  # await and scroll to view

    pos = get_node_pos(NODE_ID, frame)
    frame.dblclick(position=pos)
    AWAIT_SELECT(frame)
    page.get_by_text('"action":"').click() # awaits for action
    data = get_return_json(page)

    assert data["action"] == "expand"
    assert data["data"]["node_ids"][0] == NODE_ID


def test_expand_button(page: Page):
    page.get_by_role("link", name=PAGE_NAME).click()
    frame = page.frame_locator(FRAME_LOCATOR).first.locator(":root")
    frame.click(position={"x": 0, "y": 0})  # await and scroll to view

    pos = get_node_pos(NODE_ID, frame)
    frame.click(position=pos)
    AWAIT_SELECT(frame)
    frame.get_by_title("Expand Node").click()
    data = get_return_json(page)

    assert data["action"] == "expand"
    assert data["data"]["node_ids"][0] == NODE_ID


def test_remove_keydown(page: Page):
    page.get_by_role("link", name=PAGE_NAME).click()
    frame = page.frame_locator(FRAME_LOCATOR).first.locator(":root")
    frame.click(position={"x": 0, "y": 0})  # await and scroll to view

    pos = get_node_pos(NODE_ID, frame)
    frame.click(position=pos)
    AWAIT_SELECT(frame)
    page.keyboard.down("Delete")
    data = get_return_json(page)

    assert data["action"] == "remove"
    assert data["data"]["node_ids"][0] == NODE_ID


def test_remove_button(page: Page):
    page.get_by_role("link", name=PAGE_NAME).click()
    frame = page.frame_locator(FRAME_LOCATOR).first.locator(":root")
    frame.click(position={"x": 0, "y": 0})  # await and scroll to view

    pos = get_node_pos(NODE_ID, frame)
    frame.click(position=pos)
    AWAIT_SELECT(frame)
    frame.get_by_title("Remove Nodes").click()
    data = get_return_json(page)

    assert data["action"] == "remove"
    assert data["data"]["node_ids"][0] == NODE_ID
