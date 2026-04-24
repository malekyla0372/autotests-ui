import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("AUTO_USE: Send analytics data")

@pytest.fixture(scope='session')
def settings():
    print("SESSION: Initializing test automation settings")

@pytest.fixture(scope='class')
def user():
    print("CLASS: Creating user data")

@pytest.fixture(scope='function')
def user():
    print("FUNCTION: Open browser on each test")

class TestUserFlow:
    def test_user_can_login(self):
        ...
    def test_user_can_create_course(self):
        ...