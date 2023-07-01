import pytest


def test_add_naumbers():
    assert 2 + 2 ==4


def test_multiply_numbers():
    assert 2 * 2 == 4


@pytest.mark.skip()
def test_skip():
    pass
