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
        assert item in stock, "{} error enter type".format(food)
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
        else:
            print(item + " out off stock")
    return total
