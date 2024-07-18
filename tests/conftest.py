import time
import pytest
from playwright.sync_api import Page


@pytest.fixture(autouse=True, scope="session")
def run_streamlit():
    import subprocess

    p = subprocess.Popen(
        [
            "streamlit",
            "run",
            "app.py",
            "--server.port",
            "8512",
            "--server.headless",
            "true",
            "--browser.gatherUsageStats",
            "false",
        ],
        cwd="./examples",
    )
    time.sleep(5)
    try:
        yield 1
    finally:
        print("killing process")
        p.kill()


@pytest.fixture(autouse=True, scope="function")
def goto_streamlit(page: Page):
    page.goto("localhost:8512")
