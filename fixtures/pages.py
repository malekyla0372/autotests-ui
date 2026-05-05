from lib2to3.pgen2 import driver

import pytest
from playwright.sync_api import Page

from fixtures.browsers import chromium_page
from pages.login_page import LoginPage

def login_page(chromium_page: Page) -> LoginPage: # зачем рисовать эти стрелочки и что значат двоеточие и параметр такой
    return LoginPage(page=chromium_page()) # я так понимаю что тут задаю параметры странице типо какую страницу жду
