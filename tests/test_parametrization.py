import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [ 1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0

@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
@pytest.mark.parametrize('os', ['macos', 'linux', 'windows', 'debian'])
def test_multiple_of_numbers(browser: str, os: str):
    assert len(os + browser) > 0

@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f"Running test on browser: {browser}")

class TestOperations:
    def test_user_with_operations(self):
        ...
    def test_user_without_operations(self):
        ...

users = {
    '+7000000011': 'User with money on bank account',
    '+7000000022': 'User without money on bank account',
    '+7000000033': 'User with operations on bank account',
}

@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identifiers(phone_number: str):
    ...
