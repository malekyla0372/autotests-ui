from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    button_registration = page.get_by_test_id('registration-page-registration-button')
    expect(button_registration).to_be_disabled()

    email_input = page.get_by_test_id("registration-form-email-input")
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id("registration-form-username-input")
    username_input.fill("username")

    password_input = page.get_by_test_id("registration-form-password-input")
    password_input.fill("password")

    button_registration = page.get_by_test_id('registration-page-registration-button')
    expect(button_registration).to_be_enabled()

    page.wait_for_timeout(5000)
