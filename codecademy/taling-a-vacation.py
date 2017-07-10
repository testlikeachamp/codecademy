# Taking a vacation
def hotel_cost(nights):
    """this function calculates the rate for the number of days
"""
    return 140 * nights

def plane_ride_cost(city):
    """compares the names of cities and returns the price for 1 day
"""
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    """"car price with a discount for more days
"""
    cost = 40 * days
    if days >= 7:
        cost = cost - 50
    elif days >= 3:
        cost = cost - 20
    return cost

def trip_cost(city, days, spending_money):
    """calculate total sum"""
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print trip_cost("Los Angeles", 5, 600)