import pytest

from codecademy.functions_artem import weather_report

@pytest.mark.parametrize("temperature,expected", [
    (-10000000, "freezing"),
    (-1, "freezing"),
    (0, "cold"),
    (1, "cold"),
    (9, "cold"),
    (10, "warm"),
    (11, "warm"),
    (100000, "warm")
])
def test_weather_report(temperature, expected):
    assert weather_report(temperature) == expected