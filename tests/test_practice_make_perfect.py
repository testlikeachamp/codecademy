import sys

import pytest

from codecademy.practice_make_perfect import is_int
from codecademy.practice_make_perfect import factorial


@pytest.mark.parametrize("input_val,expected", [
    (-sys.maxsize-2, True),
    (-sys.maxsize-1,  True),
    (-sys.maxsize,  True),
    (-3037000499, True),
    (-1, True),
    (0, True),
    (1, True),
    (3037000499, True),
    (sys.maxsize-1, True),
    (sys.maxsize, True),
    (sys.maxsize+1, True),
    (1.1, False),
    (1.2, False),
    (1.4, False),
    (1.5, True),
    (1.6, True),
    (1.7, True),
    (1.9, True),
])
def test_is_int(input_val, expected):
    assert is_int(input_val) == expected


@pytest.mark.parametrize("input_neg", [
    None,
    True,
    False,
    "",
    "some text"
])
def test_is_int_negative(input_neg):
    try:
        is_int(input_neg)
        raise Exception("Expected an exception from is_int")
    except AssertionError as e:
        assert str(e) == "{} passed the wrong data type".format(input_neg)

# END is_int


@pytest.mark.parametrize("input_val,expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
])
def test_factorial(input_val, expected):
    assert factorial(input_val) == expected


@pytest.mark.parametrize("input_neg", [
    None,
    True,
    False,
    "",
    "some text"
])
def test_factorial_negative(input_neg):
    try:
        factorial(input_neg)
        raise Exception("Expected an exception from factorial")
    except AssertionError as e:
        assert str(e) == "{} passed the wrong data type".format(input_neg)

# END factorial
