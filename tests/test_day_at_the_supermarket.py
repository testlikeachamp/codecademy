import sys

import pytest

from codecademy.day_at_the_supermarket import compute_bill


@pytest.mark.parametrize("test_compute_bill_input,test_compute_bill_expected", [
    (["banana"], 4),
    (["apple"], 0),
    (["orange"], 1.5),
    (["pear"], 3),
    (["banana", "apple"], 4),
    (["banana", "apple", "orange"], 5.5),
    (["banana", "apple", "orange", "pear", "apple"], 8.5)
])
def test_compute_bill(test_compute_bill_input, test_compute_bill_expected):
    assert compute_bill(test_compute_bill_input) == test_compute_bill_expected


@pytest.mark.parametrize("test_compute_bil_negative_input", [-1, 0, "blah", False, None])
def test_compute_bill_negative(test_compute_bil_negative_input):
    try:
        compute_bill(test_compute_bil_negative_input)
    except AssertionError as e:
        assert str(e) == str(test_compute_bil_negative_input) + " was not list type"
