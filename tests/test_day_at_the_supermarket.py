import sys

import pytest

from codecademy.day_at_the_supermarket import compute_bill


@pytest.mark.parametrize("test_compute_bill_input,test_compute_bill_expected", [
    (["banana"], 4),
    (["banana", "orange", "pear"], 8.5),
    (["banana", "orange", "pear", "apple"], 8.5),
    (["banana", "orange", "orange", "pear", "apple"], 10),
    (["banana", "banana", "orange", "pear", "apple"], 12.5)
])
def test_compute_bill(test_compute_bill_input, test_compute_bill_expected):
    assert compute_bill(test_compute_bill_input) == test_compute_bill_expected


@pytest.mark.parametrize("test_compute_bil_negative_input", [[], [0, 1, 3, False, None], ["orange", "pear"],
                                                             ["orange", "pear", "potato"],
                                                             ["banana", "banana", "orange", "pear", "apple"],
                                                             0, False, True, None])
def test_compute_bill_negative(test_compute_bil_negative_input):
    try:
        compute_bill(test_compute_bil_negative_input)
    except AssertionError as e:
        assert str(e) == str(test_compute_bil_negative_input) + " error enter type"
