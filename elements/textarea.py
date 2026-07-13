from elements.base_element import BaseElement
from playwright.sync_api import expect


class Textarea(BaseElement):
    def get_locator(self, **kwargs):
        locator = self.get_locator(**kwargs)
        return super().get_locator(**kwargs).locator("textarea").first

    def fill(self, value: str, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_value(value)
