import pytest

from lesson21.code_for_testing import Human


@pytest.fixture
def human() -> Human:
    human = Human('Alex',30, 'Black')
    human.grow()
    yield human
