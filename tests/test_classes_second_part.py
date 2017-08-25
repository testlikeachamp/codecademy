import pytest

from codecademy.classes_second_part import Car
from codecademy.classes_second_part import ElectricCar
from codecademy.classes_second_part import Point3D

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


def test_drive_electric_car():
    test_condition = "like new"
    my_car = ElectricCar(test_model, test_color, test_mpg, test_battery_type)
    assert my_car.drive_car() == test_condition

x = 1
y = 2
z = 3


def test_point():
    points = Point3D(x, y, z)
    assert eval(points.__repr__()) == (1, 2, 3)


