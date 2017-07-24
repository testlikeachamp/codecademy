import sys

import pytest

from codecademy.day_at_the_supermarket import compute_bill


@pytest.mark.parametrize("input,expected", [
    (["banana"], 4),
    (["banana", "orange", "pear"], 8.5),
    (["banana", "orange", "pear", "apple"], 8.5),
    (["banana", "orange", "orange", "pear", "apple"], 10),
    (["banana", "banana", "orange", "pear", "apple"], 12.5)
])
def test_compute_bill(input, expected):
    assert compute_bill(input) == expected


@pytest.mark.parametrize("input", [[], [0, 1, 3, False, None], ["orange", "pear"], ["orange", "pear", "potato"],
                                                             ["banana", "banana", "orange", "pear", "apple"],
                                                             0, False, True, None])
def test_compute_bill_negative(input):
    try:
        compute_bill(input)
        assert str(False) + " error enter type"
    except AssertionError as e:
        assert str(e) == str(input) + " error enter type"
