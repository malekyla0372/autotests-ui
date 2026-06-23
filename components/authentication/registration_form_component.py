from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id("authentication-ui-course-title-text")
        self.email_input = page.get_by_test_id("registration-form-email-input").locator('input')
        self.username_input = page.get_by_test_id("registration-form-username-input").locator('input')
        self.password_input = page.get_by_test_id("registration-form-password-input").locator('input')

    def fill_registration_form(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)

    def check_visible(self, email: str, username: str, password: str):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text("UI Course")

        expect(self.email_input).to_be_visible()
        expect(self.email_input).to_have_value(email)

        expect(self.username_input).to_be_visible()
        expect(self.username_input).to_have_value(username)

        expect(self.password_input).to_be_visible()
        expect(self.password_input).to_have_value(password)