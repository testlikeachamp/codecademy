import pytest

from codecademy.day_at_the_supermarket import compute_bill
from codecademy.day_at_the_supermarket import fizz_count
from codecademy.day_at_the_supermarket import compute_bill_11
from codecademy.day_at_the_supermarket import compute_bill_13


@pytest.mark.parametrize("test_input,expected", [
    ([], 0),
    ([0, 1, 3, False, None], 0),
    (["banana"], 4),
    (["banana", "orange", "pear"], 8.5),
    (["banana", "orange", "pear", "apple"], 8.5),
    (["banana", "orange", "orange", "pear", "apple"], 10),
    (["banana", "banana", "orange", "pear", "apple"], 12.5),
    (["orange", "pear"], 4.5),
    (["orange", "pear", "potato"], 4.5),
    (["banana", "banana", "orange", "pear", "apple"], 12.5)
])
def test_compute_bill(test_input, expected):
    assert compute_bill(test_input) == expected


@pytest.mark.parametrize("test_input", [0, False, True, None])
def test_compute_bill_negative(test_input):
    try:
        compute_bill(test_input)
        pytest.fail("Expected an exception from compute_bill()")  # best way
        assert False, "Expected an exception from compute_bill()"
    except AssertionError as e:
        assert str(e) == str(test_input) + " error enter type"


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
        raise Exception("Expected an exception from fizz_count()")
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


@pytest.mark.parametrize("input_11", [0, False, True, None, 'potato'])
def test_compute_bill_11_negative(input_11):
    try:
        compute_bill(input_11)
        raise Exception("Expected an exception from compute_bill_11()")
    except AssertionError as e:
        assert str(e) == str(input_11) + " error enter type"


@pytest.mark.parametrize("input_13,expected", [
    ([], 0),
    ([0, 1, 3, False, None], 0),
    (["banana"], 4),
    (["banana", "orange", "pear"], 8.5),
    (["banana", "orange", "pear", "apple"], 8.5),
    (["banana", "orange", "orange", "pear", "apple"], 10.0),
    (["banana", "banana", "orange", "pear", "apple"], 12.5),
    (["orange", "pear"], 4.5),
    (["orange", "pear", "potato"], 4.5),
    (["banana", "banana", "orange", "pear", "apple"], 12.5)
])
def test_compute_bill_13(input_13, expected):
    assert compute_bill_13(input_13) == expected


@pytest.mark.parametrize("input_13", [0, False, True, None, 'potato'])
def test_compute_bill_13_negative(input_13):
    try:
        compute_bill(input_13)
        raise Exception("Expected an exception from compute_bill_13()")
    except AssertionError as e:
        assert str(e) == str(input_13) + " error enter type"
