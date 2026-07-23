import pytest

@pytest.mark.xfail(reason="Bag not fixed yet")
def test_with_bag():
    ...
@pytest.mark.xfail(reason="Bag already fixed")
def test_without_bag():
    ...


