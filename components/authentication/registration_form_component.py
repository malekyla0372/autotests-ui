from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, 'registration-form-email-input', 'Email input')
        self.username_input = Input(page, 'registration-form-username-input', 'Username input')
        self.password_input = Input(page, 'registration-form-password-input', 'Password input')

    def fill(self, email: str, username: str, password: str, index: int):
        self.email_input.fill(email, index=index)
        self.email_input.check_have_value(email, index=index)

        self.username_input.fill(username, index=index)
        self.username_input.check_have_value(username, index=index)

        self.password_input.fill(password, index=index)
        self.password_input.check_have_value(password, index=index)

    def check_visible(self, email: str, username: str, password: str, index: int):
        self.email_input.check_visible(index=index)
        self.email_input.check_have_value(email, index=index)

        self.username_input.check_visible(index=index)
        self.username_input.check_have_value(username, index=index)

        self.password_input.check_visible(index=index)
        self.password_input.check_have_value(password, index=index)
