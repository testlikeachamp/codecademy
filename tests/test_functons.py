from codecademy.functions import one_good_turn
from codecademy.functions import square
from codecademy.functions import deserves_another
from codecademy.functions import biggest_number

import pytest, sys


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



