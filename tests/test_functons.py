import sys

import pytest

from codecademy.functions import biggest_number
from codecademy.functions import deserves_another
from codecademy.functions import distance_from_zero
from codecademy.functions import distance_from_zero_type
from codecademy.functions import one_good_turn
from codecademy.functions import smallest_number
from codecademy.functions import square
from codecademy.functions import tax
from codecademy.functions import tip
from codecademy.functions import power


@pytest.mark.parametrize("test_square_input,test_square_expected", [
    (-sys.maxsize-2, (sys.maxsize+2) ** 2),
    (-sys.maxsize-1, (sys.maxsize+1)**2),
    (-sys.maxsize, sys.maxsize**2),
    (-3037000499, 3037000499**2),
    (-10, 100),
    (-1, 1),
    (0, 0),
    (1, 1),
    (10, 100),
    (3037000499, 3037000499**2),
    (sys.maxsize-1, (sys.maxsize-1) ** 2),
    (sys.maxsize, sys.maxsize ** 2),
    (sys.maxsize + 1, (sys.maxsize + 1)**2)
])
def test_square(test_square_input, test_square_expected):
    assert square(test_square_input) == test_square_expected


@pytest.mark.parametrize("test_input,expected", [
    (-sys.maxsize-2, -sys.maxsize-1),
    (-sys.maxsize-1,  -sys.maxsize),
    (-sys.maxsize,  -sys.maxsize+1),
    (-3037000499, -3037000498),
    (-1, 0),
    (0, 1),
    (1, 2),
    (3037000499, 3037000500),
    (sys.maxsize-1, sys.maxsize),
    (sys.maxsize, sys.maxsize+1),
    (sys.maxsize+1, sys.maxsize+2)
])
def test_one_good_turn(test_input, expected):
    assert one_good_turn(test_input) == expected


@pytest.mark.parametrize("test_square_expected,test_deserves_another_expected", [
    (-sys.maxsize-2,  -sys.maxsize+1),
    (-sys.maxsize-1,  -sys.maxsize+2),
    (-sys.maxsize,  -sys.maxsize+3),
    (-3037000499, -3037000496),
    (-1, 2),
    (0, 3),
    (1, 4),
    (3037000499, 3037000502),
    (sys.maxsize-1, sys.maxsize+2),
    (sys.maxsize, sys.maxsize+3),
    (sys.maxsize+1, sys.maxsize+4)
])
def test_deserves_another(test_square_expected, test_deserves_another_expected):
    assert deserves_another(test_square_expected) == test_deserves_another_expected


def test_biggest_number():
    assert biggest_number(-sys.maxsize, -sys.maxsize-1, -3037000499, -1, 0, 1, 3037000499,
                          sys.maxsize-1, sys.maxsize) == sys.maxsize


def test_smallest_number():
    assert smallest_number(-sys.maxsize, -sys.maxsize-1, -3037000499, -1, 0, 1, 3037000499,
                          sys.maxsize-1, sys.maxsize) == -sys.maxsize-1


@pytest.mark.parametrize("test_distance_from_zero_input,test_distance_from_zero_expected", [
    (-sys.maxsize-2,  sys.maxsize+2),
    (-sys.maxsize-1,  sys.maxsize+1),
    (-sys.maxsize,  sys.maxsize),
    (-3037000499, 3037000499),
    (-1, 1),
    (0, 0),
    (1, 1),
    (3037000499, 3037000499),
    (sys.maxsize-1, sys.maxsize-1),
    (sys.maxsize, sys.maxsize),
    (sys.maxsize+1, sys.maxsize+1)

])
def test_distance_from_zero(test_distance_from_zero_input, test_distance_from_zero_expected):
    assert distance_from_zero(test_distance_from_zero_input) == test_distance_from_zero_expected


@pytest.mark.parametrize("distance_from_zero_type_input,distance_from_zero_type_expected", [
    (-sys.maxsize-2,  sys.maxsize+2),
    (-sys.maxsize-1,  sys.maxsize+1),
    (-sys.maxsize,  sys.maxsize),
    (-3037000499, 3037000499),
    (-1, 1),
    (0, 0),
    (1, 1),
    (3037000499, 3037000499),
    (sys.maxsize-1, sys.maxsize-1),
    (sys.maxsize, sys.maxsize),
    (sys.maxsize+1, sys.maxsize+1),
    ("a", "Nope"),
    ("", "Nope"),
    (False, "Nope"),
    (True, "Nope"),
    (None, "Nope")
])
def test_square(distance_from_zero_type_input, distance_from_zero_type_expected):
    assert distance_from_zero_type(distance_from_zero_type_input) == distance_from_zero_type_expected


@pytest.mark.parametrize("test_input_tax,expected_tax", [
    (-1, None),
    (0, 0),
    (1, 1.08),
    (5.0, 5.4),
    (36641, 39572.28)
])
def test_tax(test_input_tax, expected_tax):
    assert tax(test_input_tax) == expected_tax


@pytest.mark.parametrize("test_input_tip, expected_tip", [
    (-1, None),
    (0, 0),
    (1, 1.15),
    (5.0, 5.75),
    (36641, 42137.15)
])
def test_tip(test_input_tip, expected_tip):
    assert tip(test_input_tip) == expected_tip


@pytest.mark.parametrize("test_input_base", [-100, -3, -1, 0, 1, 3, 100])
@pytest.mark.parametrize("test_input_exponent", [-100, -3, -1, 0, 1, 3, 100])
def test_power(test_input_base, test_input_exponent):
    power(test_input_base, test_input_exponent)
