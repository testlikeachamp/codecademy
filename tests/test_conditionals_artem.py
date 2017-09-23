import pytest

from codecademy.conditionals_and_control_flow import greater_less_equal_5

@pytest.mark.parametrize("test_input,expected", [
    (-10000000, -1),
    (-1, -1),
    (0, -1),
    (1, -1),
    (2, -1),
    (4, -1),
    (5, 0)
])
def test_greater_less_equal_5(test_input, expected):
    assert greater_less_equal_5(test_input) == expected
