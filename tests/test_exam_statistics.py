import sys

import pytest

from codecademy.exam_statistics import grades_average, grades_sum, grades_variance


@pytest.mark.parametrize("input_val,expected", [
    ([0, 1], 1),
    ([0, 1, 2], 3),
    ([0, 1, 10, 1], 12),
    ([0, 10, 20, 30], 60),
    ([1000, 1, 9, 100], 1110),
])
def test_grades_sum(input_val, expected):
    assert grades_sum(input_val) == expected


@pytest.mark.parametrize("input_val", [-1, "blah", None, False, [0, 1, "test", -1, "blah", None, False]])
def test_grades_sum_negative(input_val):
    try:
        grades_sum(input_val)
        raise Exception("Expected an exception from grades_sum")
    except AssertionError as e:
        assert str(e) == "Passed the wrong data type"


@pytest.mark.parametrize("input_val,expected", [
    ([0, 1], 0.5),
    ([0, 1, 2], 1),
    ([0, 1, 1, 2, 1], 1),
    ([10, 10, 10], 10),
])
def test_grades_average(input_val, expected):
    assert grades_average(input_val) == expected


@pytest.mark.parametrize("input_val", [-1, "blah", None, False, [0, 1, "test", -1, "blah", None, False]])
def test_grades_average_negative(input_val):
    try:
        grades_average(input_val)
        raise Exception("Expected an exception from grades_sum")
    except AssertionError as e:
        assert str(e) == "Passed the wrong data type"


@pytest.mark.parametrize("input_val,expected", [
    ([0], 0),
    ([0, 1], 0.25),
    ([0, 1, 2], 0.67),
    ([0, 1, 1, 2, 1], 0.4),
    ([10, 10, 10], 0),
    ([10, 50, 80, 100], 1150.0),
])
def test_grades_variance(input_val, expected):
    assert grades_variance(input_val) == expected


@pytest.mark.parametrize("input_val", [-1, "blah", None, False, [0, 1, "test", -1, "blah", None, False]])
def test_grades_variance_negative(input_val):
    try:
        grades_variance(input_val)
        raise Exception("Expected an exception from grades_sum")
    except AssertionError as e:
        assert str(e) == "Passed the wrong data type"
