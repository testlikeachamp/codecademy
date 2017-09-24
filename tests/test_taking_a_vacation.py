import pytest

from codecademy.taking_a_vacation import hotel_cost, plane_ride_cost, rental_car_cost, trip_cost, trip_cost_only


@pytest.mark.parametrize("input_nights,expected", [
    (1, 140),
    (2, 2*140),
    (7, 7*140),
    (31, 31*140),
    (365, 365*140)
])
def test_hotel_cost(input_nights, expected):
    assert hotel_cost(input_nights) == expected


@pytest.mark.parametrize("input_nights", [-1, "blah", False, None])
def test_hotel_cost_negative(input_nights):
    try:
        hotel_cost(input_nights)
        assert False, "Expected an exception from hotel_cost"
    except AssertionError as e:
        assert str(e) == str(input_nights) + " was not int or positive integer > 0"


@pytest.mark.parametrize("input_city,expected", [
    ("Charlotte", 183),
    ("Tampa", 220),
    ("Pittsburgh", 222),
    ("Los Angeles", 475)
])
def test_plane_ride_cost(input_city, expected):
    assert plane_ride_cost(input_city) == expected


def test_plane_ride_cost_negative():
    try:
        plane_ride_cost('sochi')
        assert False, "Expected an exception from plane_ride_cost"
    except ValueError as e:
        assert str(e) == "We Don't fly to the city sochi"


@pytest.mark.parametrize("input_days,expected", [
    (1, 40),
    (2, 80),
    (3, 40*3-20),
    (4, 40*4-20),
    (5, 40*5-20),
    (6, 40*6-20),
    (7, 40*7-50),
    (8, 40*8-50),
    (365, 40*365-50)
])
def test_rental_car_cost(input_days, expected):
    assert rental_car_cost(input_days) == expected


@pytest.mark.parametrize("input_nights", [-1, 0, "blah", False, None])
def test_rental_car_cost_negative(input_nights):
    try:
        hotel_cost(input_nights)
        assert False, "Expected an exception from rental_car_cost"
    except AssertionError as e:
        assert str(e) == str(input_nights) + " was not int or positive integer > 0"


@pytest.mark.parametrize("input_city, input_days, input_spending_money, expected", [
    ("Charlotte", 1, 100, 463),
    ("Tampa", 7, 100, 1530),
    ("Pittsburgh", 31, 100, 5852),
    ("Los Angeles", 365, 100, 66225)
])
def test_trip_cost(input_city, input_days, input_spending_money, expected):
    assert trip_cost(input_city, input_days, input_spending_money) == expected


@pytest.mark.parametrize("input_spending_money", [-1, "blah", None, False])
@pytest.mark.parametrize("input_days", [-1, "blah", False, None])
def test_trip_cost_negative(input_days, input_spending_money):
    try:
        trip_cost('Sochi', input_days, input_spending_money)
        raise Exception("Expected an exception from trip_cost()")
    except AssertionError as e:
        assert (str(e) == str(input_days) + " was not int or positive integer > 0")\
               or str(e) == str(input_spending_money) + " was not int or float or positive number >= 0"
    except ValueError as e:
        assert str(e) == "We Don't fly to the city Sochi"


@pytest.mark.parametrize("input_city, input_days, expected", [
    ("Charlotte", 1, 363),
    ("Tampa", 7, 1430),
    ("Pittsburgh", 31, 5752),
    ("Los Angeles", 365, 66125)
])
def test_trip_cost_only(input_city, input_days, expected):
    assert trip_cost_only(input_city, input_days) == expected


@pytest.mark.parametrize("input_days", [-1, "blah", False, None])
def test_trip_cost_only_negative(input_days):
    try:
        trip_cost_only('Sochi', input_days)
        raise Exception("Expected an exception from trip_cost()")
    except AssertionError as e:
        assert (str(e) == str(input_days) + " was not int or positive integer > 0")
    except ValueError as e:
        assert str(e) == "We Don't fly to the city Sochi"
