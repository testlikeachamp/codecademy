import sys

import pytest

from codecademy.taling_a_vacation import hotel_cost
from codecademy.taling_a_vacation import plane_ride_cost
from codecademy.taling_a_vacation import rental_car_cost
from codecademy.taling_a_vacation import trip_cost

@pytest.mark.parametrize("test_hotel_cost_input,test_hotel_cost_expected", [
    (-sys.maxsize - 1, (-sys.maxsize - 1)*140),
    (-sys.maxsize, -sys.maxsize*140),
    (-1, -140),
    (0, 0),
    (1, 140),
    (3037000499, 425180069860),
    (sys.maxsize - 1, (sys.maxsize-1)*140),
    (sys.maxsize, sys.maxsize*140)
])
def test_hotel_cost(test_hotel_cost_input, test_hotel_cost_expected):
    assert hotel_cost(test_hotel_cost_input) == test_hotel_cost_expected


@pytest.mark.parametrize("test_plane_ride_cost_input,test_plane_ride_cost_expected", [
    ("Charlotte", 183),
    ("Tampa", 220),
    ("Pittsburgh", 222),
    ("Los Angeles", 475)
])
def test_plane_ride_cost(test_plane_ride_cost_input, test_plane_ride_cost_expected):
    assert plane_ride_cost(test_plane_ride_cost_input) == test_plane_ride_cost_expected


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
    (3037000499, 3037000499*40-50),
    (sys.maxsize-1, (sys.maxsize-1)*40-50),
    (sys.maxsize, sys.maxsize*40-50)
])
def test_rental_car_cost(test_rental_car_cost_input, test_rental_car_cost_expected):
    assert rental_car_cost(test_rental_car_cost_input) == test_rental_car_cost_expected


