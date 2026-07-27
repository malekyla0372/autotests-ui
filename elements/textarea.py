from elements.base_element import BaseElement
from playwright.sync_api import expect
import allure

class Textarea(BaseElement):
    @property
    def type_of(self):
        return "textarea"

    def get_locator(self, nth: int = 0, **kwargs):
        return super().get_locator(nth, **kwargs).locator("textarea").first

    def fill(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f"Fill {self.type_of} '{self.name}' with '{value}'"):
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f"Check that {self.type_of} '{self.name}' has value '{value}'"):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_value(value)
