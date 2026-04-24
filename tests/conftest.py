import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


@pytest.fixture
def chromium_page(playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()

@pytest.fixture(scope="session")
def initialize_browser_state(playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id("registration-form-email-input").locator('input')
    email_input.fill("user@gmail.com")

    username_input = page.get_by_test_id("registration-form-username-input").locator('input')
    username_input.fill("username")

    password_input = page.get_by_test_id("registration-form-password-input").locator('input')
    password_input.fill("password")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    page.wait_for_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    context.storage_state(path='browser-state.json')

    yield

    browser.close()


@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    yield page

    context.close()
    browser.close()