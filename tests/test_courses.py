from playwright.sync_api import sync_playwright, expect, Page
import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


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


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    create_course_page.check_visible_create_course_title()

    create_course_page.check_disabled_create_course_button()

    create_course_page.check_visible_image_preview_empty_view()

    create_course_page.check_visible_image_upload_view()

    create_course_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )

    create_course_page.check_visible_exercises_title()

    create_course_page.check_visible_create_exercise_button()

    create_course_page.check_visible_exercises_empty_view()

    create_course_page.upload_preview_image("./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)

    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_course_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )