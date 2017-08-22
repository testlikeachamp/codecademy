import pytest

from codecademy.functions_artem import weather_report

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

"""def weather_report(temperature):
    if temperature < 0:
        return "freezing"
    elif 0 <= temperature < 10:
        return 'cold'
    else:
        return 'warm'"""
# -&     -10000000 ..... -1  0  +1 ...  9  ..10..12.... 100000 ..... +&


@pytest.mark.parametrize("temperature,expected", [
    (-10000000, "freezing"),
    (-1, "freezing"),
    (0, "cold"),
    (1, "cold"),
    (9, "cold"),
    (10, "warm"),
    (12, "warm"),
    (100000, "warm")
])
def test_weather_report(temperature, expected):
    assert weather_report(temperature) == expected