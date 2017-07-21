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
    # max_stock = Counter(food)

    assert type(food) == list, "{} was not list type".format(food)
    for item in food:
        if item not in stock:
            assert False, "{} product was not in the list of stock".format(food[item])
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
        # elif stock[item] < max_stock[item]:
    return total
