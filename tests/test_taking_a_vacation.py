import sys

import pytest

from codecademy.taking_a_vacation import hotel_cost
from codecademy.taking_a_vacation import plane_ride_cost
from codecademy.taking_a_vacation import rental_car_cost
from codecademy.taking_a_vacation import trip_cost


@pytest.mark.parametrize("input,expected", [
    (1, 140),
    (2, 2*140),
    (7, 7*140),
    (31, 31*140),
    (365, 365*140)
])
def test_hotel_cost(input, expected):
    assert hotel_cost(input) == expected


@pytest.mark.parametrize("input", [-1, "blah", False, None])
def test_hotel_cost_negative(input):
    try:
        hotel_cost(input)
        assert False, "Expected an exception from hotel_cost"
    except AssertionError as e:
        assert str(e) == str(input) + " was not int or positive integer > 0"


@pytest.mark.parametrize("input,expected", [
    ("Charlotte", 183),
    ("Tampa", 220),
    ("Pittsburgh", 222),
    ("Los Angeles", 475)
])
def test_plane_ride_cost(input, expected):
    assert plane_ride_cost(input) == expected


def test_plane_ride_cost_negative():
    try:
        plane_ride_cost('sochi')
        assert False, "Expected an exception from plane_ride_cost"
    except ValueError as e:
        assert str(e) == "We Don't fly to the city sochi"


@pytest.mark.parametrize("input,expected", [
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
def test_rental_car_cost(input, expected):
    assert rental_car_cost(input) == expected


@pytest.mark.parametrize("input", [-1, 0, "blah", False, None])
def test_rental_car_cost_negative(input):
    try:
        hotel_cost(input)
        assert False, "Expected an exception from rental_car_cost"
    except AssertionError as e:
        assert str(e) == str(input) + " was not int or positive integer > 0"




