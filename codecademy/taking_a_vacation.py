#  Taking a vacation


def hotel_cost(nights):
    """this function calculates the rate for the number of days"""
    assert type(nights) == int and nights > 0, "{} was not int or positive integer > 0".format(nights)
    return 140 * nights


def plane_ride_cost(city):
    """compares the names of cities and returns the price for 1 day"""
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        raise ValueError("We Don't fly to the city {}".format(city))


def rental_car_cost(days):
    """car price with a discount for more days"""
    assert type(days) == int and days > 0, "{} was not int or positive integer > 0".format(days)
    cost = 40 * days
    if days >= 7:
        cost = cost - 50
    elif days >= 3:
        cost = cost - 20
    return cost


def trip_cost(city, days, spending_money):
    """calculate total sum"""
    assert type(spending_money) in (int, float) and spending_money >= 0,\
        "{} was not int or float or positive number >= 0".format(spending_money)
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money


def trip_cost_only(city, days):
    """calculate sum of hotel cost, plane ride cost and rental car only"""
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days)
