from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):

        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_visible = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_visible).to_be_visible()

        folder_visible = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(folder_visible).to_be_visible()

        no_results_visible = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(no_results_visible).to_be_visible()

        description_visible = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(description_visible).to_be_visible()