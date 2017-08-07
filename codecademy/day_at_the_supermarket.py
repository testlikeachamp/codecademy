# from collections import Counter

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


# Write your code below!
def compute_bill(food):
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
"""The function counts str 'fizz' in the input list"""


def fizz_count(x):
    count = 0
    for item in x:
        if item == 'fizz':
            count += 1
    return count


print(fizz_count(['fizz', 'blits', 'fizz']))

#  11 Making a Purchase
"""Calculate the sum of prices for fruit's list"""


def compute_bill_11(food):
    total = 0
    for item in food:
        total += prices[item]
    return total

print(compute_bill_11(['banana', 'apple', 'pear']))

#  13 Let's check out
"""Finalize A day at the supermarket"""


def compute_bill_13(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total

print(compute_bill_13(['banana', 'apple', 'pear']))