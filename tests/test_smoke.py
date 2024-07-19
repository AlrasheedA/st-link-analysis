from playwright.sync_api import Page, expect


def test_run(page: Page):
    expect(page).to_have_title("Readme")


def test_iframe_exists(page: Page):
    page.click("a[href*='node_style']")
    page.wait_for_load_state("networkidle")
    frames = page.query_selector_all("iframe[title*='st_link_analysis']")
    assert len(frames) == 1
