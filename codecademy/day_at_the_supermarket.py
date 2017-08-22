# from collections import Counter

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!


def compute_bill(food):
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }

    assert isinstance(food, (list, tuple, set)), "{} error enter type".format(food)
    total = 0
    for item in food:
        if item not in stock:
            print(str(item) + " not in price")
        elif stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
        else:
            print(str(item) + " out of stock")
    print("total: " + str(total))
    return total


#  4 Lists + Functions


def fizz_count(x):
    """The function counts str 'fizz' in the input list"""
    assert isinstance(x, list), "{} error enter type".format(x)
    count = 0
    for item in x:
        if item == 'fizz':
            count += 1
    return count


#  11 Making a Purchase


def compute_bill_11(food):
    """Calculate the sum of prices for fruit's list"""
    assert isinstance(food, (list, tuple, set)), "{} error enter type".format(food)
    total = 0
    for item in food:
        try:
            total += prices[item]
        except KeyError as e:
            print("The item {} is not in price-list".format(e))
    return total


#  13 Let's check out


def compute_bill_13(food):
    """Finalize A day at the supermarket"""
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    assert isinstance(food, (list, tuple, set)), "{} error enter type".format(food)
    total = 0
    for item in food:
        try:
            if stock[item] > 0:
                total += prices[item]
                stock[item] -= 1
        except KeyError as e:
            print("The item {} is not in price-list".format(e))
    return total
