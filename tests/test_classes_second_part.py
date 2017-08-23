import pytest

from codecademy.classes_second_part import Car

test_model = 'bmw'
test_color = 'Green'
test_mpg = 100
test_condition = "used"


def test_display_car():
    my_car = Car(test_model, test_color, test_mpg)

    assert my_car.model == test_model
    assert my_car.color == test_color
    assert my_car.mpg == test_mpg

    assert my_car.display_car() == "This is a %s %s with %s MPG." % (test_model, test_color, test_mpg)


def test_drive_car():
    my_car = Car(test_model, test_color, test_mpg)
    assert my_car.drive_car() == test_condition


@pytest.mark.parametrize("input_val", [-1, 0, None, False, True])
def test_drive_car_neg(input_val):

    try:
        my_car = Car(test_model, test_color, test_mpg)
        raise Exception("Expected an exception test_drive_car_neg")
    except AssertionError as e:
        assert str(e) == "Invalid entering data type"
