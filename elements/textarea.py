from elements.base_element import BaseElement
from playwright.sync_api import expect
import allure
from tools.logger import get_logger

logger = get_logger("TEXTAREA")

class Textarea(BaseElement):
    @property
    def type_of(self):
        return "textarea"

    def get_locator(self, nth: int = 0, **kwargs):
        return super().get_locator(nth, **kwargs).locator("textarea").first

    def fill(self, value: str, nth: int = 0, **kwargs):
        step = f"Fill {self.type_of} '{self.name}' with '{value}'"

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        step = f"Check that {self.type_of} '{self.name}' has value '{value}'"

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)
