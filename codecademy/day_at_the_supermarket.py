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
