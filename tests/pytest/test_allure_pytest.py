import allure

@allure.step("Opening browser")
def open_browser():
    with allure.step("Open browser"):
        ...
    with allure.step("start browser"):
        ...

@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    pass

@allure.step("Closing browser")
def close_browser():
    ...

def test_feature():
    create_course(title="Locust")
    create_course(title="Pytest")
    create_course(title="Python")
    create_course(title="Playwright")