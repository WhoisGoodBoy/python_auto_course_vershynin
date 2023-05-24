import pytest

from lesson27.infrastructure.people_service import PeopleService
from lesson27.entities.people_entity import People


@pytest.fixture
def people_service():

    yield PeopleService()


@pytest.fixture
def fifth_person():
    yield People(
        name='Leia Organa',
        height='150',
        mass='49',
        hair_color='brown',
        skin_color='light'
    )