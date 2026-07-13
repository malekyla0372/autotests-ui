from components.base_component import BaseComponent

from playwright.sync_api import Page, expect
from elements.text import Text


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = Text(page, "navigation-navbar-app-title-text", "App title")
        self.welcome_title = Text(page, "navigation-navbar-welcome-title-text", "Welcome title")

    def check_visible(self, username: str, index: int):
        self.app_title.check_visible(index=index)
        self.app_title.check_have_text("UI Course", index=index)

        self.welcome_title.check_visible(index=index)
        self.welcome_title.check_have_text(f"Welcome, {username}!", index=index)
