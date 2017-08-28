import pytest

from codecademy.classes_second_part import Car, ElectricCar, Point3D

test_model = 'bmw'
test_color = 'Green'
test_mpg = 100
test_battery_type = "li"


def test_display_car():
    my_car = Car(test_model, test_color, test_mpg)

    assert my_car.model == test_model
    assert my_car.color == test_color
    assert my_car.mpg == test_mpg

    assert my_car.display_car() == "This is a %s %s with %s MPG." % (test_model, test_color, test_mpg)


def test_drive_car():
    test_condition = "used"
    my_car = Car(test_model, test_color, test_mpg)
    assert my_car.drive_car() == test_condition
    assert my_car.condition == test_condition


def test_drive_electric_car():
    test_condition = "like new"
    my_car = ElectricCar(test_model, test_color, test_mpg, test_battery_type)
    assert my_car.drive_car() == test_condition
    assert my_car.condition == test_condition


@pytest.mark.parametrize("x, y, z", [
    (0, 0, 0),
    (0, 1, 1),
    (1, 1, 1),
    (-1, -1, 0),
    (123, 222, 999),
])
def test_get_class_average(x, y, z):
    points = Point3D(x, y, z)
    assert eval(str(points)) == (x, y, z)


@pytest.mark.parametrize("x", [
    None,
    True,
    False,
    "",
    "a"
])
@pytest.mark.parametrize("y", [
    None,
    True,
    False,
    "",
    "a"
])
@pytest.mark.parametrize("z", [
    None,
    True,
    False,
    "",
    "a"
])
def test_get_class_average_neg(x, y, z):
    try:
        Point3D(x, y, z)
        raise Exception("Expected an exception from test_get_class_average_neg")
    except AssertionError as e:
        assert str(e) == "Invalid enter data type"
