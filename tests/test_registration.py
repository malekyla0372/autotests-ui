from playwright.sync_api import sync_playwright, Page, expect
import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize(
    "email, username, password",
    [
        ("user@gmail.com", "username", "password")
    ]
)
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage, email: str,
                                 username: str, password: str):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(email=email, username=username, password=password)
    registration_page.click_registration_button()
    dashboard_page.check_visible_dashboard_title()
