import sys

import pytest

from codecademy.day_at_the_supermarket import compute_bill


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
        # assert False, "Expected an exception from compute_bill()"  # not recommended, since AssertionError will be thrown
        # raise Exception("Expected an exception from compute_bill()")  # OK to use
        pytest.fail("Expected an exception from compute_bill()")  # best way
    except AssertionError as e:
        assert str(e) == str(input) + " error enter type"
