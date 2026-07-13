from typing import Pattern

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text
from elements.button import Button


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', 'Icon')
        self.title = Text(page, f'{identifier}-drawer-list-item-title-text', 'Text')
        self.button = Button(page, f'{identifier}-drawer-list-item-button', 'Button')

    def check_visible(self, title: str, index: int):
        self.icon.check_visible(index=index)

        self.title.check_visible(index=index)
        self.title.check_have_text(title, index=index)

        self.button.check_visible(index=index)

    def navigate(self, expected_url: Pattern[str], index: int):
        self.button.click(index=index)
        self.check_current_url(expected_url)
