import pytest
from playwright.sync_api import Page, sync_playwright

from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()



@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture
def logged_in_page(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()

    # page.goto("https://tiki.vn/")

    login_page.login_with_password("0375956110", "Vuhue162005")
    # login_page.verifi_login_success()

    yield page