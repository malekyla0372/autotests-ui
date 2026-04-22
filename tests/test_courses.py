from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    from playwright.sync_api import sync_playwright, expect

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('name@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('name')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('pass')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        page.wait_for_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        page.wait_for_timeout(3000)

        context.storage_state(path='test-browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='test-browser-state.json')
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_visible = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_visible).to_be_visible()

        folder_visible = page.get_by_test_id('courses-list-empty-view-icon')
        expect(folder_visible).to_be_visible()

        no_results_visible = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(no_results_visible).to_be_visible()

        description_visible = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(description_visible).to_be_visible()