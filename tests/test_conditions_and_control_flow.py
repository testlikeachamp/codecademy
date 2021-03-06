from codecademy.conditionals_and_control_flow import greater_less_equal_5

import sys

import pytest


@pytest.mark.parametrize("test_input,expected", [
    (-sys.maxsize - 2, -1),
    (-sys.maxsize - 1, -1),
    (-sys.maxsize, -1),
    (-sys.maxsize**0.5, -1),
    (-1, -1),
    (0, -1),
    (1, -1),
    (3, -1),
    (4, -1),
    (5, 0),
    (6, 1),
    (sys.maxsize**0.5, 1),
    (sys.maxsize - 1, 1),
    (sys.maxsize, 1),
    (sys.maxsize + 1, 1)
])
def test_greater_less_equal_5l(test_input, expected):
    assert greater_less_equal_5(test_input) == expected

