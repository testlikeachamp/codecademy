import pytest

from codecademy.introduction_to_classes import Fruit


def test_Fruit_description():
    test_name = 'Apple'
    test_color = 'Green'
    test_flavor = 'Sweet'
    test_poisonous = False
    test_weight = 200

    apple = Fruit(test_name, test_color, test_flavor, test_poisonous, test_weight)

    assert apple.name == test_name
    assert apple.color == test_color
    assert apple.flavor == test_flavor
    assert apple.poisonous == test_poisonous
    assert apple.weight == test_weight

    assert apple.description() == "I'm a %s %s and I taste %s." % (test_color, test_name, test_flavor)


@pytest.mark.parametrize("bite_size, expected", [(1, 199), (100, 100), (200, 0), (300, 0)])
def test_Fruit_bite_it(bite_size, expected):
    test_name = 'Apple'
    test_color = 'Green'
    test_flavor = 'Sweet'
    test_poisonous = False
    test_weight = 200

    apple = Fruit(test_name, test_color, test_flavor, test_poisonous, test_weight)

    apple.bite_it(bite_size)
    assert apple.weight == expected
