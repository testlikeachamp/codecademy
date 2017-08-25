import pytest

from codecademy.list_and_functions import join_strings
from codecademy.list_and_functions import flatten


@pytest.mark.parametrize("test_input,expected", [
    (["banana", "orange", "pear"], "bananaorangepear"),
    (["ba", "na", "na", "66"], "banana66"),
    (["water", "melon"], "watermelon")
])
def test_join_strings(test_input, expected):
    assert join_strings(test_input) == expected


@pytest.mark.parametrize("input_negative", [
    None,
    True,
    False,
    0,
    "",
    "Test row",
    {},
    ('a', 'b'),
    ['a', 1, 'b']
])
def test_join_strings_negative(input_negative):
    try:
        join_strings(input_negative)
        raise Exception("Expected an exception from join_strings()")
    except AssertionError as e:
        assert str(e) == "{} is not a list".format(input_negative)
    except TypeError as e:
        assert str(e) == "The element in words is not a string"


@pytest.mark.parametrize("test_input,expected", [
    ([["banana", "orange"], [1, 2, 3]], ["banana", "orange", 1, 2, 3]),
    ([["ba", "na", "na"], ["66", 33, False]], ["ba", "na", "na", "66", 33, False]),
    ([["water", "melon"], ["watermelon", 21, None]], ["water", "melon", "watermelon", 21, None])
])
def test_flatten(test_input, expected):
    assert flatten(test_input) == expected


@pytest.mark.parametrize("input_negative", [
    None,
    True,
    False,
    0,
    "",
    "Test row",
    [[5, 6, 3, 4], None]
])
def test_flatten_negative(input_negative):
    try:
        flatten(input_negative)
        raise Exception("Expected an exception flatten()")
    except AssertionError as e:
        assert str(e) == "{} is not a list".format(input_negative) or \
               "The element inside {} is not a list".format(input_negative)
