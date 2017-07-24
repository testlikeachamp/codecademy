import sys

import pytest

from codecademy.student_becomes_the_teacher import average
from codecademy.student_becomes_the_teacher import get_average


@pytest.mark.parametrize("test_average_input,test_average_expected", [
    ([0], 0),
    ([1], 1),
    ([49], 49),
    ([50], 50),
    ([51], 51),
    ([99], 99),
    ([100], 100),
    ([0, 0], 0),
    ([0, 1], 0.5),
    ([0, 49], 24.5),
    ([25, 25], 25),
    ([0, 51], 25.5),
    ([99], 99),
    ([100], 100),
    ([0, 0, 0], 0.0),
    ([0, 0, 1], 0.33),
    ([0, 24, 25], 16.33),
    ([0, 25, 25], 16.67),
    ([0, 25, 26], 17.0),
    ([33, 33, 33], 33.0),
    ([33, 33, 34], 33.33),
])
def test_average(test_average_input, test_average_expected):
    assert average(test_average_input) == test_average_expected


keny = {
    "name": "Lloyd",
    "homework": [20, 20, 20],
    "quizzes": [10, 10, 10],
    "tests": [5, 5, 5]
}


@pytest.mark.parametrize("test_get_average_input,test_get_average_expected", [
    (keny, 6.5)
])
def test_get_average(test_get_average_input, test_get_average_expected):
    assert get_average(test_get_average_input) == test_get_average_expected


keny_neg = {
    "name": "Lloyd",
    "homework": [20, 20, 20],
    "quizzes": [10, 10, 10],
    "tests11": [5, 5, 5]
}


@pytest.mark.parametrize("test_get_average_negative_input", [
    None,
    True,
    False,
    0,
    1,
    keny_neg
])
def test_get_average_negative(test_get_average_negative_input):
    try:
        get_average(test_get_average_negative_input)
        assert False + "Expected an exception from get_average"
    except AssertionError as e:
        print("Passed the wrong data type")
        assert str(e) == str(test_get_average_negative_input) + " Passed the wrong data type"
    except KeyError as e:
        print("Please check student key name")
        assert str(False) + " Please check student key name"
