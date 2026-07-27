from playwright.sync_api import Page
import allure
from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.title = Text(page, f'{identifier}-widget-title-text', 'Title')
        self.chart = Image(page, f'{identifier}-{chart_type}-chart', 'Chart')

    @allure.step('Check visible chart on dashboard')
    def check_visible(self, title: str):
        self.title.check_visible()
        self.title.check_have_text(title)

        self.chart.check_visible()