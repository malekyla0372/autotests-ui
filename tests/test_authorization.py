from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.autorization
@pytest.mark.regression
def test_wrong_email_or_password_autorization():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill("user.name@gmail.com")

        password_input = page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill("password")

        login_button = page.get_by_test_id('login-page-login-button')
        login_button.click()

        worng_email_or_password = page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(worng_email_or_password).to_be_visible()
        expect(worng_email_or_password).to_have_text('Wrong email or password')