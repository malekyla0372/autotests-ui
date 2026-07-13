from playwright.sync_api import Page

from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from elements.button import Button
from elements.link import Link


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(page, 'registration-page-login-link', 'Registration button')
        self.login_link = Link(page, 'registration-page-login-link', 'Login link')

    def click_registration_button(self, index: int):
        self.registration_button.click(index=index)

    def click_login_link(self, index: int):
        self.login_link.click(index=index)
