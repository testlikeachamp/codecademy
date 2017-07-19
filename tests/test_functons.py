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
