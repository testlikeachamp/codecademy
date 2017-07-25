import sys

import pytest

from codecademy.student_becomes_the_teacher import average
from codecademy.student_becomes_the_teacher import get_average
from codecademy.student_becomes_the_teacher import get_letter_grade


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
    "tests-key": [5, 5, 5]
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
        assert False, "Expected an exception from get_average"
    except AssertionError as e:
        print("Passed the wrong data type")
        assert str(e) == str(test_get_average_negative_input) + " Passed the wrong data type"
    except KeyError as e:
        print("Please check student key name")
        assert str(e) == str(test_get_average_negative_input) + " Please check student key name"


@pytest.mark.parametrize("input,expected", [
    (0, "F"),
    (1, "F"),
    (29, "F"),
    (30, "F"),
    (31, "F"),
    (59, "F"),
    (60, "D"),
    (61, "D"),
    (64, "D"),
    (65, "D"),
    (66, "D"),
    (69, "D"),
    (70, "C"),
    (71, "C"),
    (74, "C"),
    (75, "C"),
    (76, "C"),
    (79, "C"),
    (80, "B"),
    (81, "B"),
    (84, "B"),
    (85, "B"),
    (86, "B"),
    (89, "B"),
    (90, "A"),
    (91, "A"),
    (94, "A"),
    (95, "A"),
    (96, "A"),
    (99, "A"),
    (100, "A"),
])
def test_get_letter_grade(input, expected):
    assert get_letter_grade(input) == expected


@pytest.mark.parametrize("input", [-1, "blah", None, False])
def test_get_letter_grade_negative(input):
    try:
        get_letter_grade(input)
        assert False, "Expected an exception from get_letter_grade"
    except AssertionError as e:
        assert str(e) == str(input) + " was not int or float"
