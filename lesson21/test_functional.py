import pytest

from lesson21.code_for_testing import Human


@pytest.mark.regression
def test_hair_colour_change():
    human = Human('Joshua', 18, 'Black')
    human.change_hair_color('Blonde')
    assert human.color == 'Blonde'


@pytest.mark.xfail(reason='Failed due to known bug', condition=True)
def test_growing(human, monkeypatch):
    monkeypatch.setattr(human, 'age', 60)
    human.grow()
    assert human.age == 62


@pytest.mark.skip('fucntionality not implemented yet')
def test_growing2(human, monkeypatch):
    monkeypatch.setattr(human, 'age', 60)
    human.grow()
    assert human.age == 61


@pytest.mark.smoke
def test_hair_colour_change_01():
    human = Human('Joshua', 18, 'Black')
    human.change_hair_color('Blonde')
    assert human.color == 'Blonde'


@pytest.mark.smoke
@pytest.mark.regression
def test_hair_colour_change_02():
    human = Human('Joshua', 18, 'Black')
    human.change_hair_color('Blonde')
    assert human.color == 'Blonde'


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize(
    "new_color,expected_color", [("Red", "Red"), ("Green", "Green")], ids=["Red color", "Green color"]
)
def test_multiple_color_variations(human, new_color, expected_color):
    human.change_hair_color(new_color)
    assert human.color == expected_color

def test_change_color_w_exception(human):
    with pytest.raises(Exception):
        human.change_hair_color('Red')


