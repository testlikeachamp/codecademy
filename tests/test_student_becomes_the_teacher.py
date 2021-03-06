import sys

import pytest

from codecademy.student_becomes_the_teacher import average, get_average, get_letter_grade, get_class_average, average_5


@pytest.mark.parametrize("test_input,expected", [
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
def test_average(test_input, expected):
    assert average(test_input) == expected


keny = {
    "name": "Lloyd",
    "homework": [20, 20, 20],
    "quizzes": [10, 10, 10],
    "tests": [5, 5, 5]
}


@pytest.mark.parametrize("test_input,expected", [
    (keny, 6.5)
])
def test_get_average(test_input, expected):
    assert get_average(test_input) == expected


keny_neg = {
    "name": "Lloyd",
    "homework": [20, 20, 20],
    "quizzes": [10, 10, 10],
    "tests-key": [5, 5, 5]
}


@pytest.mark.parametrize("input_neg", [
    None,
    True,
    False,
    0,
    1,
    keny_neg
])
def test_get_average_negative(input_neg):
    try:
        get_average(input_neg)
        raise Exception("Expected an exception from get_average")
    except TypeError as e:
            assert str(e) == "{} Passed the wrong data type".format(input_neg)
    except AssertionError as e:
        assert str(e) == "Please check student key name"


@pytest.mark.parametrize("test_input,expected", [
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
def test_get_letter_grade(test_input, expected):
    assert get_letter_grade(test_input) == expected


@pytest.mark.parametrize("test_input", [-1, "blah", None, False])
def test_get_letter_grade_negative(test_input):
    try:
        get_letter_grade(test_input)
        raise Exception("Expected an exception from get_letter_grade")
    except AssertionError as e:
        assert str(e) == str(test_input) + " was not int or float"


Lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
Alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
Tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


@pytest.mark.parametrize("test_input,expected", [
    ([Lloyd, Alice, Tyler], 67.67),
])
def test_get_class_average(test_input, expected):
    assert get_class_average(test_input) == expected


@pytest.mark.parametrize("input_neg", [
    None,
    True,
    False,
    0,
    1,
    "",
    "Test row",
])
def test_get_class_average_negative(input_neg):
    try:
        get_class_average(input_neg)
        raise Exception("Expected an exception from get_average")
    except TypeError as e:
            assert str(e) == "{} Passed the wrong data type".format(input_neg)


@pytest.mark.parametrize("test_input, expected", [
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
    ([33, 33, 34], 33.33)
])
def test_average_5(test_input, expected):
    assert average_5(test_input) == expected


@pytest.mark.parametrize("input_negative", [
    None,
    True,
    False,
    0,
    1,
    "",
    "Test row",
    {},
    (),
    ["B", 0]
])
def test_average_5_negative(input_negative):
    try:
        average_5(input_negative)
        raise Exception("Expected an exception from average_5()")
    except AssertionError as e:
        assert str(e) == "{} error type, please enter list of numbers".format(input_negative)
    except TypeError as e:
        assert str(e) == "{} some of element inside numbers is wrong (not int or float)".format(input_negative)
