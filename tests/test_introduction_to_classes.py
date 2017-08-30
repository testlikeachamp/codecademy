import pytest

from codecademy.introduction_to_classes import Animal
from codecademy.introduction_to_classes import Customer
from codecademy.introduction_to_classes import Fruit
from codecademy.introduction_to_classes import ReturningCustomer
from codecademy.introduction_to_classes import Triangle


test_name = 'Apple'
test_color = 'Green'
test_flavor = 'Sweet'
test_poisonous = False
test_weight = 200


def test_Fruit_description():
    apple = Fruit(test_name, test_color, test_flavor, test_poisonous, test_weight)

    assert apple.name == test_name
    assert apple.color == test_color
    assert apple.flavor == test_flavor
    assert apple.poisonous == test_poisonous
    assert apple.weight == test_weight

    assert apple.description() == "I'm a %s %s and I taste %s." % (test_color, test_name, test_flavor)


@pytest.mark.parametrize("bite_size, expected", [(1, 199), (100, 100), (200, 0), (300, 0)])
def test_Fruit_bite_it(bite_size, expected):
    apple = Fruit(test_name, test_color, test_flavor, test_poisonous, test_weight)
    apple.bite_it(bite_size)
    assert apple.weight == expected


@pytest.mark.parametrize("input_neg", [
    0,
    -0.1,
    -1,
    -100,
    None,
    True,
    False,
    "",
    "A"
])
def test_Fruit_bite_it_negative(input_neg):
    try:
        apple = Fruit(test_name, test_color, test_flavor, test_poisonous, test_weight)
        apple.bite_it(input_neg)
        raise Exception("Expected an exception from test_Fruit_bite_it_negative")
    except AssertionError as e:
        assert str(e) == "{} error type, please enter integer".format(input_neg)


@pytest.mark.parametrize("input_val, expected", [
    (True, False),
    (False, True),
])
def test_is_edible(input_val, expected):

    orange = Fruit(test_name, test_color, test_flavor, poisonous=input_val, weight=test_weight)
    assert orange.is_edible() == expected

@pytest.mark.parametrize("color_val,expected", [
    ("yellow", "yellow"),
    ("green", "green"),
    ("red", "red")
    ])
def test_get_color(color_val, expected):
    #test_color = yellow
    Lemon = Fruit(test_name, color_val, test_flavor, test_poisonous, test_weight)
    assert Lemon.get_color() == expected

def test_description():
    test_animal_name = "Cat"
    test_animal_age = 100
    hippo = Animal(test_animal_name, test_animal_age)
    assert hippo.description() == test_animal_name + " " + str(test_animal_age)


@pytest.mark.parametrize("test_animal_age_neg", [
    None,
    True,
    False,
    0,
    -1,
    ""
])
@pytest.mark.parametrize("test_animal_name_neg", [
    None,
    True,
    False,
    0
])
def test_description_negative(test_animal_name_neg, test_animal_age_neg):
    try:
        hippo = Animal(test_animal_name_neg, test_animal_age_neg)
        hippo.description()
        raise Exception("Expected an exception from test_description_negative")
    except AssertionError as e:
        assert str(e) == "Error type, please enter a valid value age or name"


@pytest.mark.parametrize("input_val", [
    1,
    12,
    123,
])
def test_display_cart(input_val):
    customer_test = Customer(input_val)
    assert customer_test.display_cart() == input_val


@pytest.mark.parametrize("input_neg", [
    None,
    True,
    False,
    0,
    -1,
    "",
    "A"
])
def test_display_cart_negative(input_neg):
    try:
        customer_test = Customer(input_neg)
        customer_test.display_cart()
        raise Exception("Expected an exception from test_display_cart_negative")
    except AssertionError as e:
        assert str(e) == "Error type, please enter a valid value"


@pytest.mark.parametrize("input_val", [
    1,
    12,
    123
])
def test_display_order_history(input_val):
    order_test = ReturningCustomer(input_val)
    assert order_test.display_order_history() == "I'm a string that stands in for your order history!"


@pytest.mark.parametrize("input_neg", [
    None,
    True,
    False,
    0,
    -1,
    "",
    "A"
])
def test_display_cart_negative(input_neg):
    try:
        order_test = ReturningCustomer(input_neg)
        order_test.display_order_history()
        raise Exception("Expected an exception from display_order_history")
    except AssertionError as e:
        assert str(e) == "Error type, please enter a valid value"


@pytest.mark.parametrize("test_angle1, test_angle2, test_angle3, expected", [
    (1, 1, 178, True),
    (59, 62, 59, True),
    (0.1, 1, 178.9, True),
])
def test_check_angles(test_angle1, test_angle2, test_angle3, expected):
    check_angles = Triangle(test_angle1, test_angle2, test_angle3)
    assert check_angles.check_angles() == expected


@pytest.mark.parametrize("test_angle1", [
    True,
    None,
    False,
    "",
    "A",
])
@pytest.mark.parametrize("test_angle2", [
    True,
    None,
    False,
    "",
    "A",
])
@pytest.mark.parametrize("test_angle3", [
    True,
    None,
    False,
    "",
    "A",
])
def test_check_angles_neg(test_angle1, test_angle2, test_angle3):
    try:
        Triangle(test_angle1, test_angle2, test_angle3)
        raise Exception("Expected an exception from test_check_angles_neg")
    except AssertionError as e:
        assert str(e) == "Error type, please enter a valid value"


@pytest.mark.parametrize("test_angle1", [
    180,
    100000,
    0,
    -1,
    -0.1
])
@pytest.mark.parametrize("test_angle2", [
    180,
    100000,
    0,
    -1,
    -0.1
])
@pytest.mark.parametrize("test_angle3", [
    180,
    100000,
    0,
    -1,
    -0.1
])
def test_check_angles_int_neg(test_angle1, test_angle2, test_angle3):
    try:
        Triangle(test_angle1, test_angle2, test_angle3)
        raise Exception("Expected an exception from test_check_angles_neg")
    except AssertionError as e:
        assert str(e) == "Angles is not in the range (0, 180)"


@pytest.mark.parametrize("test_angle1", [
    1,
    60,
    179,
    1,
    20,
    55,
])
@pytest.mark.parametrize("test_angle2", [
    1,
    61,
    179,
    1,
    20,
    55,
])
@pytest.mark.parametrize("test_angle3", [
    179,
    61,
    179,
    1,
    20,
    55,
])
def test_check_angles_sum_neg(test_angle1, test_angle2, test_angle3):
    try:
        Triangle(test_angle1, test_angle2, test_angle3)
        raise Exception("Expected an exception from test_check_angles_neg")
    except AssertionError as e:
        assert str(e) == "Sum of given angles not equal to 180"
