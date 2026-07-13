from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email input')
        self.password_input = Input(page, 'login-form-password-input', 'Password input')

        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')

    def fill(self, email: str, password: str, index: int):
        self.email_input.fill(email, index=index)
        self.email_input.check_have_value(email, index=index)

        self.password_input.fill(password, index=index)
        self.password_input.check_have_value(password, index=index)

    def check_visible(self, email: str, password: str, index: int):
        self.email_input.check_visible(index=index)
        self.email_input.check_have_value(email, index=index)

        self.password_input.check_visible(index=index)
        self.password_input.check_have_value(password, index=index)
