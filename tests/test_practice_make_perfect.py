import sys

import pytest

from codecademy.practice_make_perfect import is_int
from codecademy.practice_make_perfect import factorial
from codecademy.practice_make_perfect import reverse
from codecademy.practice_make_perfect import scrabble_score
from codecademy.practice_make_perfect import count
from codecademy.practice_make_perfect import product
from codecademy.practice_make_perfect import median


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
    (-1.1, False),
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


@pytest.mark.parametrize("input_val,expected", [
    ("", ""),
    ("a", "a"),
    ("ab", "ba"),
    ("abc", "cba"),
    ("az", "za"),
    ("za", "az"),
    ("z", "z"),
    (u"aaz", u"zaa")
])
def test_reverse(input_val, expected):
    assert reverse(input_val) == expected


@pytest.mark.parametrize("input_neg", [
    None,
    True,
    False,
    0,
    1
])
def test_reverse_negative(input_neg):
    try:
        reverse(input_neg)
        raise Exception("Expected an exception from reverse")
    except AssertionError as e:
        assert str(e) == "{} passed the wrong data type".format(input_neg)

# END reverse


@pytest.mark.parametrize("input_val,expected", [
    ("a", 1),
    ("aa", 2),
    ("ab", 4),
    ("abc", 7),
    ("z", 10),
    ("za", 11),
    ("zy", 14),
    ("zyx", 22),
])
def test_scrabble_score(input_val, expected):
    assert scrabble_score(input_val) == expected


@pytest.mark.parametrize("input_neg", [
    None,
    True,
    False,
    0,
    1,
    [],
    "1",
])
def test_scrabble_score_negative(input_neg):
    try:
        scrabble_score(input_neg)
        raise Exception("Expected an exception from scrabble_score")
    except AssertionError as e:
        assert str(e) == "Passed the wrong data type or key"


@pytest.mark.parametrize("input_val2, expected", [
    ("a", 1),
    (False, 2),
    (-1, 1),
    (0, 1),
    (1, 1),
    ([1, 2, 3], 1),
    (("test", 123), 1),
    ({"some_key": 123}, 1),
])
def test_count(input_val2, expected):
    assert count(["a", False, True, False, -1, 0, 1, [1, 2, 3], ("test", 123), {"some_key": 123}], input_val2) == expected
# END count


@pytest.mark.parametrize("input_val,expected", [
    ([0], 0),
    ([0, 1], 0),
    ([1], 1),
    ([1, 1], 1),
    ([1, 2], 2),
    ([1, 2, 3], 6),
    ([-1, 1], -1),
    ([-1, -1], 1),

])
def test_product(input_val, expected):
    assert product(input_val) == expected


@pytest.mark.parametrize("input_neg", [
    None,
    True,
    False,
    0,
    1,
    "some text",
    ["a"],
    [False, True, 1, 2, "some text"]
])
def test_product_negative(input_neg):
    try:
        product(input_neg)
        raise Exception("Expected an exception from product")
    except AssertionError as e:
        assert str(e) == "Passed the wrong data type"


@pytest.mark.parametrize("input_val,expected", [
    ([0], 0),
    ([0, 1, 0], 0),
    ([5, 2, 4, 2], 3),
    ([10, 0, 22], 10),
    ([-1, 0, -2, -3], -1.5),
])
def test_median(input_val, expected):
    assert median(input_val) == expected


@pytest.mark.parametrize("input_neg", [
    None,
    True,
    False,
    0,
    1,
    "some text",
    ["a"],
    [False, True, 1, 2, "some text"]
])
def test_median_negative(input_neg):
    try:
        product(input_neg)
        raise Exception("Expected an exception from product")
    except AssertionError as e:
        assert str(e) == "Passed the wrong data type"

