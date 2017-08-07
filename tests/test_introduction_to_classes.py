import sys

import pytest

from codecademy.introduction_to_classes import param


@pytest.mark.parametrize("input_val", [
    ("Jeffrey", 2)
])
def test_param(input_val):
    assert param(input_val) == "Jeffrey 2 True"
