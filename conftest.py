import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Use headless=False for headed mode
        page = browser.new_page()
        yield page
        page.close()
        browser.close()
