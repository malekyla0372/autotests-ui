import pytest

@pytest.mark.smoke
def test_smoke_case():
    ...

@pytest.mark.regression
def test_regression_case():
    ...

@pytest.mark.smoke
@pytest.mark.regression
def test_smoke_and_regression():
    ...

@pytest.mark.smoke
class TestSuit:
    @pytest.mark.smoke
    def test_1(self):
        ...
    def test_2(self):
        ...

@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        ...
    @pytest.mark.slow
    def test_password_reset(self):
        ...
    def test_logout(self):
        ...

def test_critical_login():
    ...