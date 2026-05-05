import pytest
from playwright.sync_api import Page

from fixtures.browsers import chromium_page
from pages.login_page import LoginPage

def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)
