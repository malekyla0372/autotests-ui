import pytest
import random

PLATFORM = 'Linux'
@pytest.mark.flaky(reruns=3, reruns_delay=2)

@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_reruns():
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_rerun_1(self):
        assert random.choice([True, False])

    def test_rerun_2(self):
        assert random.choice([True, False])

@pytest.mark.flaky(reruns=3, reruns_delay=2, condition= PLATFORM == 'Windows')
def test_rerun_condition():
    assert random.choice([True, False])