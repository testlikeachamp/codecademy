import sys

import pytest

from codecademy.functions import biggest_number
from codecademy.functions import deserves_another
from codecademy.functions import distance_from_zero
from codecademy.functions import distance_from_zero_type
from codecademy.functions import one_good_turn
from codecademy.functions import smallest_number
from codecademy.functions import square


@pytest.mark.parametrize("test_square_input,test_square_expected", [
    (-10, 100),
    (-1, 1),
    (0, 0),
    (1, 1),
    (2, 4),
    (10, 100),
])
def test_square(test_square_input, test_square_expected):
    assert square(test_square_input) == test_square_expected


@pytest.mark.parametrize("test_input,expected", [
    (-100, -99),
    (-1, 0),
    (0, 1),
    (1, 2),
    (100, 101),
])
def test_one_good_turn(test_input, expected):
    assert one_good_turn(test_input) == expected


@pytest.mark.parametrize("test_square_expected,test_deserves_another_expected", [
    (-100, -97),
    (-1, 2),
    (0, 3),
    (1, 4),
    (100, 103),
])
def test_deserves_another(test_square_expected, test_deserves_another_expected):
    assert deserves_another(test_square_expected) == test_deserves_another_expected


def test_biggest_number():
    assert biggest_number(1,2,3,4,5) == 5


def test_smallest_number():
    assert smallest_number(-1,0,1,2,3) == -1


def test_distance_from_zeror():
    assert distance_from_zero(-2) == 2


@pytest.mark.parametrize("distance_from_zero_type_input,distance_from_zero_type_expected", [
    (-10, 10),
    (-1, 1),
    (0, 0),
    ("a", "Nope"),
])
def test_square(distance_from_zero_type_input, distance_from_zero_type_expected):
    assert distance_from_zero_type(distance_from_zero_type_input) == distance_from_zero_type_expected
