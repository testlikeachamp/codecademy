import pytest

from codecademy.conditionals_and_control_flow import greater_less_equal_5

#
# def test_greater_less_equal_5_minus_1():
#     assert greater_less_equal_5(-1) == -1
#
#
# def test_greater_less_equal_5_6():
#     assert greater_less_equal_5(6) == 1
#
#
# def test_greater_less_equal_5_5():
#     assert greater_less_equal_5(5) == 0

# -&     -10000000 ..... -1  0  +1 ...  2  ..4 5 6...... 100000 ..... +&


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
