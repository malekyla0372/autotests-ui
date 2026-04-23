import pytest

@pytest.mark.skip(reason='Feature under development')
def test_future_development():
    ...

@pytest.mark.skip(reason='Feature under development')
class TestFutureDevelopment:
    def test_future_development_1(self):
        ...
    def test_future_development_2(self):
        ...

