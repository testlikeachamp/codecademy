import sys

import pytest

from codecademy.day_at_the_supermarket import compute_bill
from codecademy.day_at_the_supermarket import fizz_count
from codecademy.day_at_the_supermarket import compute_bill_11


@pytest.mark.parametrize("input,expected", [
    ([], 0),
    ([0, 1, 3, False, None], 0),
    (["banana"], 4),
    (["banana", "orange", "pear"], 8.5),
    (["banana", "orange", "pear", "apple"], 8.5),
    (["banana", "orange", "orange", "pear", "apple"], 10),
    (["banana", "banana", "orange", "pear", "apple"], 12.5),
    (["orange", "pear"], 4.5),
    (["orange", "pear", "potato"], 4.5),
    (["banana", "banana", "orange", "pear", "apple"], 4.5)
])
def test_compute_bill(input, expected):
    assert compute_bill(input) == expected


@pytest.mark.parametrize("input", [0, False, True, None])
def test_compute_bill_negative(input):
    try:
        compute_bill(input)
        assert False, "Expected an exception from compute_bill()"
    except AssertionError as e:
        assert str(e) == str(input) + " error enter type"


@pytest.mark.parametrize("input_fizz,expected", [
    ([], 0),
    ([0, 1, 3, False, None, 'fizz'], 1),
    (['fizz'], 1),
    (['fizz', 2222, 'fizz'], 2),
    (['fizz', ['fizz', 2222, 'fizz'], ('fizz', 2222)], 1),
])
def test_fizz_count(input_fizz, expected):
    assert fizz_count(input_fizz) == expected


@pytest.mark.parametrize("input_fizz_negative", [
    (),
    {},
    ('fizz', 0),
    tuple('fizz'),
    ('fizz', 2222),
    {1: 'fizz', 2: 'blah'},
    {'fizz', 'blah', 'fizz', 2222}
])
def test_fizz_count_negative(input_fizz_negative):
    try:
        fizz_count(input_fizz_negative)
        assert False, "Expected an exception from fizz_count()"
    except AssertionError as e:
        assert str(e) == str(input_fizz_negative) + " error enter type"


@pytest.mark.parametrize("input_11,expected", [
    ([], 0),
    ([0, 1, 3, False, None], 0),
    (["banana"], 4),
    (["banana", "orange", "pear"], 8.5),
    (["banana", "orange", "pear", "apple"], 10.5),
    (["banana", "orange", "orange", "pear", "apple"], 12),
    (["banana", "banana", "orange", "pear", "apple"], 14.5),
    (["orange", "pear"], 4.5),
    (["orange", "pear", "potato"], 4.5),
    (["banana", "banana", "orange", "pear", "apple"], 14.5)
])
def test_compute_bill_11(input_11, expected):
    assert compute_bill_11(input_11) == expected
