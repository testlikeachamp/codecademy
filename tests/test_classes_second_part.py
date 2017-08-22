import pytest

from codecademy.classes_second_part import Car


@pytest.mark.parametrize("input_model, input_color, input_mpg, expected", [
    ("bmw", "red", 100, "This is a bmw red with 100 MPG."),
    ("ford", "blue", 200, "This is a ford blue with 200 MPG."),
])
def test_is_edible(input_model, input_color, input_mpg, expected):
    some_car = Car(input_model, input_color, input_mpg)
    assert some_car.display_car(input_model, input_color, input_mpg) == expected
