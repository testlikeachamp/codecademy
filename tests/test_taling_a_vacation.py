import sys

import pytest

from codecademy.taling_a_vacation import hotel_cost
from codecademy.taling_a_vacation import plane_ride_cost
from codecademy.taling_a_vacation import rental_car_cost
from codecademy.taling_a_vacation import trip_cost

@pytest.mark.parametrize("test_hotel_cost_input,test_hotel_cost_expected", [
    (1, 140),
    (2, 2*140),
    (7, 7*140),
    (31, 31*140),
    (365, 365*140)
])
def test_hotel_cost(test_hotel_cost_input, test_hotel_cost_expected):
    assert hotel_cost(test_hotel_cost_input) == test_hotel_cost_expected


def test_hotel_cost_negative():
    try:
        hotel_cost('abcd')
    except AssertionError as e:
        assert e.message == "abcd was not int or positive integer > 0"


@pytest.mark.parametrize("test_plane_ride_cost_input,test_plane_ride_cost_expected", [
    ("Charlotte", 183),
    ("Tampa", 220),
    ("Pittsburgh", 222),
    ("Los Angeles", 475)
])
def test_plane_ride_cost(test_plane_ride_cost_input, test_plane_ride_cost_expected):
    assert plane_ride_cost(test_plane_ride_cost_input) == test_plane_ride_cost_expected


def test_plane_ride_cost_negative():
    try:
        plane_ride_cost('sochi')
    except ValueError as kaka:
        assert kaka.message == "We Don't fly to the city sochi"


@pytest.mark.parametrize("test_rental_car_cost_input,test_rental_car_cost_expected", [
    (0, 0),
    (1, 40),
    (2, 80),
    (3, 40*3-20),
    (4, 40*4-20),
    (5, 40*5-20),
    (6, 40*6-20),
    (7, 40*7-50),
    (8, 40*8-50),
    (365, 40*365-50)
])
def test_rental_car_cost(test_rental_car_cost_input, test_rental_car_cost_expected):
    assert rental_car_cost(test_rental_car_cost_input) == test_rental_car_cost_expected




