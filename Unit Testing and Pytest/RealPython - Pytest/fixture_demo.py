

import pytest

@pytest.fixture
def example_fixture():
    return 1


def test_with_fixture(example_fixture):
    assert example_fixture == 1


def test_string_parse():
    s = 'M-1234567'
    assert '123' == s[2:5]
