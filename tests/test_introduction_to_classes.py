import pytest

from codecademy.introduction_to_classes import Animal
from codecademy.introduction_to_classes import Customer
from codecademy.introduction_to_classes import Fruit
from codecademy.introduction_to_classes import ReturningCustomer
from codecademy.introduction_to_classes import Triangle
from codecademy.introduction_to_classes import Animal6
from codecademy.introduction_to_classes import ShoppingCart10
from codecademy.introduction_to_classes import Shape12, Triangle12, Equilateral12
from codecademy.introduction_to_classes import Employee14, PartTimeEmployee14


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

    orange = Fruit(test_name, test_color, test_flavor, input_val, test_weight)
    assert orange.is_edible(input_val) == expected


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


# nicolas13sochi part
def test_Animal6_description():
    test_name6 = "Joffrey"
    test_age6 = 5
    test_is_hungry = True
    animal = Animal6(test_name6, test_age6, test_is_hungry)
    assert animal.description() == "{} + " " + {}".format(test_name6, test_age6)


@pytest.mark.parametrize("test_animal_name_negative", [
    None,
    True,
    False,
    0,
    "Joffrey"
])
@pytest.mark.parametrize("test_animal_age_negative", [
    None,
    True,
    False,
    0,
    -1,
    "",
    6
])
@pytest.mark.parametrize("test_animal_is_hungry", [
    None,
    "Yes",
    "No",
    0,
    -1,
    ""
])
def test_Animal6_description_negative(test_animal_name_negative, test_animal_age_negative, test_animal_is_hungry):
    try:
        animal = Animal6(test_animal_name_negative, test_animal_age_negative, test_animal_is_hungry)
        animal.description()
        raise Exception("Expected an exception from test_description_negative")
    except AssertionError as e:
        assert str(e) == "Error type, please enter a valid value age or name" \
               or "Error type, please enter boolean"


def test_shopping_cart10():
    test_customer_name = "Nick"
    nick = ShoppingCart10("Nick")
    assert nick.customer_name == test_customer_name


@pytest.mark.parametrize("test_input_product,test_input_price,expected", [
    ('Apple', 100 , "Apple added."),
    ('Orange', 50.25, 'Orange added.'),
    ('Apple', 100, "Apple is already in the cart."),
    ('Orange', 50.25, 'Orange is already in the cart.')
])
def test_add_item10(test_input_product, test_input_price, expected):
    nick = ShoppingCart10('Nick')
    assert nick.add_item10(test_input_product, test_input_price) == expected


@pytest.mark.parametrize("test_product_negative", [
    None,
    True,
    False,
    0,
    -1,
    ""
])
@pytest.mark.parametrize("test_price_negative", [
    None,
    True,
    False,
    0,
    "A"
])
def test_add_item10_negative(test_product_negative, test_price_negative):
    try:
        nick = ShoppingCart10('Nick')
        nick.add_item10(test_product_negative, test_price_negative)
        raise Exception("Expected an exception from test_description_negative")
    except AssertionError as e:
        assert str(e) == "Error type, please enter a valid value"


@pytest.mark.parametrize("test_input_product,expected", [
    ('Apple', "Apple removed."),
    ('Orange', 'Orange removed.')
])
def test_remove_item10_1(test_input_product, expected):
    nick = ShoppingCart10('Nick')
    nick.add_item10(test_input_product, 100)
    assert nick.remove_item10(test_input_product) == expected


@pytest.mark.parametrize("test_input_product,expected", [
    ('Apple', "Apple is not in the cart."),
    ('Orange', 'Orange is not in the cart.')
])
def test_remove_item10_2(test_input_product, expected):
    nick = ShoppingCart10('Nick')
    assert nick.remove_item10(test_input_product) == expected


@pytest.mark.parametrize("test_product_negative", [
    None,
    True,
    False,
    0,
    -1
])
def test_remove_item10_negative(test_product_negative):
    try:
        nick = ShoppingCart10('Nick')
        nick.remove_item10(test_product_negative)
        raise Exception("Expected an exception from test_description_negative")
    except AssertionError as e:
        assert str(e) == "Error type, please enter a valid value"


def test_Shape12():
    test_number_of_sides = 3
    my_figure = Shape12(3)
    assert my_figure.number_of_sides == test_number_of_sides


@pytest.mark.parametrize("test_angle1, test_angle2, test_angle3", [
    (1, 1, 178),
    (59, 62, 59),
    (0.1, 1, 178.9),
])
def test_Triangle12(test_angle1, test_angle2, test_angle3):
    my_figure = Triangle12(test_angle1, test_angle2, test_angle3)
    assert my_figure.angle1 == test_angle1
    assert my_figure.angle2 == test_angle2
    assert my_figure.angle3 == test_angle3


@pytest.mark.parametrize("test_angle1", [
    False,
    -1,
    180,
    0,
    True,
    None,
])
@pytest.mark.parametrize("test_angle2", [
    False,
    -1,
    180,
    0,
    True,
    None,
])
@pytest.mark.parametrize("test_angle3", [
    False,
    -1,
    180,
    0,
    True,
    None,
])
def test_Triangle12_negative(test_angle1, test_angle2, test_angle3):
    try:
        Triangle12(test_angle1, test_angle2, test_angle3)
        raise Exception("Expected an exception from Triangle12")
    except AssertionError as e:
        assert str(e) == "Error type, please enter a valid value" \
               or "Angles is not in the range (0, 180)"


@pytest.mark.parametrize("test_angle1, test_angle2, test_angle3, expected", [
    (1, 1, 178, True),
    (59, 62, 60, False),
    (0.1, 1, 178.9, True),
])
def test_check_angles12(test_angle1, test_angle2, test_angle3, expected):
    try:
        check_angles = Triangle12(test_angle1, test_angle2, test_angle3)
        assert check_angles.check_angles12() == expected
    except AssertionError as e:
        assert str(e) == "Sum of given angles not equal to 180"



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
def test_check_angles12_sum_neg(test_angle1, test_angle2, test_angle3):
    try:
        Triangle12(test_angle1, test_angle2, test_angle3)
        raise Exception("Expected an exception from test_check_angles_neg")
    except AssertionError as e:
        assert str(e) == "Sum of given angles not equal to 180"


def test_Equilateral12():
    test_angle = 60
    my_figure = Equilateral12()
    assert my_figure.angle1 == test_angle
    assert my_figure.angle2 == test_angle
    assert my_figure.angle3 == test_angle


@pytest.mark.parametrize("test_name", [
    "David",
    -1,
    180,
    0,
    True,
    None,
])
def test_Employee14(test_name):
    try:
        david = Employee14(test_name)
        assert david.employee_name == test_name
    except AssertionError as e:
        assert str(e) == "Error type, please enter a valid value"


@pytest.mark.parametrize("test_hours,expected", [
    (1, 20),
    (40, 800),
    (0.5, 10),
])
def test_calculate_wage14(test_hours, expected):
    david = Employee14("David")
    assert david.calculate_wage14(test_hours) == expected


@pytest.mark.parametrize("test_hours_negative", [
    "David",
    -1,
    0,
    True,
    None,
])
def test_calculate_wage14_negative(test_hours_negative):
    try:
        david = Employee14('David')
        david.calculate_wage14(test_hours_negative)
        raise Exception("Expected an exception from calculate_wage14")
    except AssertionError as e:
        assert str(e) == "Error type, please enter a valid value"


@pytest.mark.parametrize("test_hours,expected", [
    (1, 12),
    (40, 480),
    (0.5, 6),
])
def test_calculate_wage14_pt(test_hours, expected):
    david = PartTimeEmployee14("David")
    assert david.calculate_wage14(test_hours) == expected


@pytest.mark.parametrize("test_hours_negative", [
    "David",
    -1,
    0,
    True,
    None,
])
def test_calculate_wage14_pt_negative(test_hours_negative):
    try:
        david = PartTimeEmployee14('David')
        david.calculate_wage14(test_hours_negative)
        raise Exception("Expected an exception from calculate_wage14")
    except AssertionError as e:
        assert str(e) == "Error type, please enter a valid value"


@pytest.mark.parametrize("test_hours,expected", [
    (1, 20),
    (40, 800),
    (0.5, 10),
])
def test_full_time_wage14(test_hours, expected):
    david = PartTimeEmployee14("David")
    assert david.full_time_wage14(test_hours) == expected


@pytest.mark.parametrize("test_hours_negative", [
    "David",
    -1,
    0,
    True,
    None,
])
def test_full_time_wage14_negative(test_hours_negative):
    try:
        david = PartTimeEmployee14('David')
        david.full_time_wage14(test_hours_negative)
        raise Exception("Expected an exception from calculate_wage14")
    except AssertionError as e:
        assert str(e) == "Error type, please enter a valid value"
