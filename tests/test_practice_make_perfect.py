import sys

import pytest


from codecademy.practice_make_perfect import count, factorial, is_int, median, product, reverse, scrabble_score
from codecademy.practice_make_perfect import is_even, digit_sum, is_prime, anti_vowel, censor, purify, remove_duplicates


@pytest.mark.parametrize("input_val,expected", [
    (-sys.maxsize-2, True),
    (-sys.maxsize-1,  True),
    (-sys.maxsize,  True),
    (-3037000499, True),
    (-1, True),
    (0, True),
    (1, True),
    (3037000499, True),
    (sys.maxsize-1, True),
    (sys.maxsize, True),
    (sys.maxsize+1, True),
    (1.1, False),
    (1.2, False),
    (1.4, False),
    (1.5, True),
    (1.6, True),
    (1.7, True),
    (1.9, True),
    (-1.1, False),
])
def test_is_int(input_val, expected):
    assert is_int(input_val) == expected


@pytest.mark.parametrize("input_neg", [
    None,
    True,
    False,
    "",
    "some text"
])
def test_is_int_negative(input_neg):
    try:
        is_int(input_neg)
        raise Exception("Expected an exception from is_int")
    except AssertionError as e:
        assert str(e) == "{} passed the wrong data type".format(input_neg)

# END is_int


@pytest.mark.parametrize("input_val,expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
])
def test_factorial(input_val, expected):
    assert factorial(input_val) == expected


@pytest.mark.parametrize("input_neg", [
    None,
    True,
    False,
    "",
    "some text"
])
def test_factorial_negative(input_neg):
    try:
        factorial(input_neg)
        raise Exception("Expected an exception from factorial")
    except AssertionError as e:
        assert str(e) == "{} passed the wrong data type".format(input_neg)

# END factorial


@pytest.mark.parametrize("input_val,expected", [
    ("", ""),
    ("a", "a"),
    ("ab", "ba"),
    ("abc", "cba"),
    ("az", "za"),
    ("za", "az"),
    ("z", "z"),
    (u"aaz", u"zaa")
])
def test_reverse(input_val, expected):
    assert reverse(input_val) == expected


@pytest.mark.parametrize("input_neg", [
    None,
    True,
    False,
    0,
    1
])
def test_reverse_negative(input_neg):
    try:
        reverse(input_neg)
        raise Exception("Expected an exception from reverse")
    except AssertionError as e:
        assert str(e) == "{} passed the wrong data type".format(input_neg)

# END reverse


@pytest.mark.parametrize("input_val,expected", [
    ("a", 1),
    ("aa", 2),
    ("ab", 4),
    ("abc", 7),
    ("z", 10),
    ("za", 11),
    ("zy", 14),
    ("zyx", 22),
])
def test_scrabble_score(input_val, expected):
    assert scrabble_score(input_val) == expected


@pytest.mark.parametrize("input_neg", [
    None,
    True,
    False,
    0,
    1,
    [],
    "1",
])
def test_scrabble_score_negative(input_neg):
    try:
        scrabble_score(input_neg)
        raise Exception("Expected an exception from scrabble_score")
    except AssertionError as e:
        assert str(e) == "Passed the wrong data type or key"


@pytest.mark.parametrize("input_val2, expected", [
    ("a", 1),
    (False, 2),
    (-1, 1),
    (0, 1),
    (1, 1),
    ([1, 2, 3], 1),
    (("test", 123), 1),
    ({"some_key": 123}, 1),
])
def test_count(input_val2, expected):
    assert count(["a", False, True, False, -1, 0, 1, [1, 2, 3],
                  ("test", 123), {"some_key": 123}], input_val2) == expected

# END count


@pytest.mark.parametrize("input_val,expected", [
    ([0], 0),
    ([0, 1], 0),
    ([1], 1),
    ([1, 1], 1),
    ([1, 2], 2),
    ([1, 2, 3], 6),
    ([-1, 1], -1),
    ([-1, -1], 1),

])
def test_product(input_val, expected):
    assert product(input_val) == expected


@pytest.mark.parametrize("input_neg", [
    None,
    True,
    False,
    0,
    1,
    "some text",
    ["a"],
    [False, True, 1, 2, "some text"]
])
def test_product_negative(input_neg):
    try:
        product(input_neg)
        raise Exception("Expected an exception from product")
    except AssertionError as e:
        assert str(e) == "Passed the wrong data type"


@pytest.mark.parametrize("input_val,expected", [
    ([0], 0),
    ([0, 1, 0], 0),
    ([5, 2, 4, 2], 3),
    ([10, 0, 22], 10),
    ([-1, 0, -2, -3], -1.5),
])
def test_median(input_val, expected):
    assert median(input_val) == expected


@pytest.mark.parametrize("input_neg", [
    None,
    True,
    False,
    0,
    1,
    "some text",
    ["a"],
    [False, True, 1, 2, "some text"]
])
def test_median_negative(input_neg):
    try:
        product(input_neg)
        raise Exception("Expected an exception from product")
    except AssertionError as e:
        assert str(e) == "Passed the wrong data type"


@pytest.mark.parametrize("test_input,expected", [
    (-sys.maxsize-2, False),
    (-sys.maxsize-1,  True),
    (-sys.maxsize,  False),
    (-3037000499, False),
    (-3037000498, True),
    (-10, True),
    (-9, False),
    (-8, True),
    (-1, False),
    (0, True),
    (1, False),
    (8, True),
    (9, False),
    (10, True),
    (3037000498, True),
    (3037000499, False),
    (sys.maxsize-1, True),
    (sys.maxsize, False),
    (sys.maxsize+1, True),
])
def test_is_even(test_input, expected):
    assert is_even(test_input) == expected


@pytest.mark.parametrize("input_negative", [
    None,
    True,
    False,
    0.1,
    -1.1,
    "some text",
    ["a"],
    [False, True, 1, 2, "some text"]
])
def test_is_even_negative(input_negative):
    try:
        is_even(input_negative)
        raise Exception("Expected an exception from is_even()")
    except AssertionError as e:
        assert str(e) == "{} is not integer".format(input_negative)


@pytest.mark.parametrize("test_input,expected", [
    (1, 1),
    (12, 3),
    (123, 6),
    (1234, 10),
    (12345, 15),
    (123456, 21),
    (sys.maxsize-1, 87),
    (sys.maxsize, 88),
    (sys.maxsize+1, 89),
])
def test_digit_sum(test_input, expected):
    assert digit_sum(test_input) == expected


@pytest.mark.parametrize("input_negative", [
    None,
    True,
    False,
    -sys.maxsize,
    -1.1,
    0,
    0.1,
    1.1,
    "some text",
    ["a"],
    [False, True, 1, 2, "some text"]
])
def test_digit_sum_negative(input_negative):
    try:
        digit_sum(input_negative)
        raise Exception("Expected an exception from digit_num()")
    except AssertionError as e:
        assert str(e) == "{} is not integer or not a positive integer".format(input_negative)


@pytest.mark.parametrize("test_input,expected", [
    (-sys.maxsize - 2, False),
    (-sys.maxsize - 1, False),
    (-sys.maxsize, False),
    (-3037000499, False),
    (-10, False),
    (-3, False),
    (-2, False),
    (-1, False),
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (13, True),
    (15, False),
    (227, True),
    (sys.maxsize - 1, False),
    (sys.maxsize, False),
    (sys.maxsize + 1, False),
])
def test_is_prime(test_input, expected):
    assert is_prime(test_input) == expected


@pytest.mark.parametrize("input_negative", [
    None,
    True,
    False,
    -1.1,
    0.1,
    1.1,
    "some text",
    ["a"],
    [False, True, 1, 2, "some text"]
])
def test_is_prime_negative(input_negative):
    try:
        is_prime(input_negative)
        raise Exception("Expected an exception from is_prime()")
    except AssertionError as e:
        assert str(e) == "{} is not integer".format(input_negative)


@pytest.mark.parametrize("test_input,expected", [
    ('This is test and tasty', 'Ths s tst nd tsty'),
    ('AaOoEeIiQqUu', ''),
    ('AaOoEeIiQqUuYy', 'Yy'),
    (3037000499, '3037000499'),
    (False, 'Fls'),
    (True, 'Tr'),
    (None, 'Nn'),
    ([1, 2, 'O'], '[1, 2, \'\']'),
    ({'Yes': 'The right answer'}, '{\'Ys\': \'Th rght nswr\'}'),
    (sys.maxsize, '9223372036854775807'),
])
def test_anti_vowel(test_input, expected):
    assert anti_vowel(test_input) == expected


@pytest.mark.parametrize("test_input_text,test_input_word,expected", [
    ('This is test and that is tasty', 'is', 'This ** test and that ** tasty'),
    ('Aa Oo Ee Ii Qq Uu', 'Aa Oo', 'Aa Oo Ee Ii Qq Uu'),
    ('the THE the THe', 'the', '*** THE *** THe'),
    ('We are made of steel', 'They', 'We are made of steel')
])
def test_censor(test_input_text, test_input_word, expected):
    assert censor(test_input_text, test_input_word) == expected


@pytest.mark.parametrize("text_input_negative, word_input_negative", [
    (3037000499, '3037000499'),
    (False, 'Fls'),
    (True, 'Tr'),
    (None, 'Nn'),
    ([1, 2, 'O'], '[1, 2, \'\']'),
    ({'Yes': 'The right answer'}, '{\'Ys\': \'Th rght nswr\'}'),
    (sys.maxsize, '9223372036854775807'),
])
def test_censor_negative(text_input_negative, word_input_negative):
    try:
        censor(text_input_negative, word_input_negative)
        raise Exception("Expected an exception from is_prime()")
    except AssertionError as e:
        assert str(e) == "Passed the wrong data type"


@pytest.mark.parametrize("test_input,expected", [
    ([0, 1, 2, 3, 4], [0, 2, 4]),
    ([-4, -3, -2, -1, 0], [-4, -2, 0]),
    ([1, 3, 5], []),
])
def test_purify(test_input, expected):
    assert purify(test_input) == expected


@pytest.mark.parametrize("input_negative", [
    None,
    True,
    False,
    -1.1,
    0.1,
    1.1,
    "some text",
    ["a"],
    [False, True, 1, 2, "some text"],
    [1, 3, 4, 5, "a"]
])
def test_purify_negative(input_negative):
    try:
        purify(input_negative)
        raise Exception("Expected an exception from is_prime()")
    except AssertionError as e:
        assert str(e) == "Passed the wrong data type" or\
               "Passed the wrong data type - wrong element inside list"


@pytest.mark.parametrize("test_input,expected", [
    ([0, 1, 2, 3, 4, 3, 2, 1], [0, 4, 3, 2, 1]),
    ([-4, -3, -2, -1, 0, -1, -1], [-4, -3, -2, 0, -1]),
    ([1, 1, 1, 1], [1]),
])
def test_remove_duplicates(test_input, expected):
    assert remove_duplicates(test_input) == expected


@pytest.mark.parametrize("input_negative", [
    None,
    True,
    False,
    -1.1,
    0.1,
    1.1,
    "some text",
    ["a"],
    [False, True, 1, 2, "some text"],
    [1, 3, 4, 5, "a"]
])
def test_remove_duplicates_negative(input_negative):
    try:
        remove_duplicates(input_negative)
        raise Exception("Expected an exception from is_prime()")
    except AssertionError as e:
        assert str(e) == "Passed the wrong data type" or\
               "Passed the wrong data type - wrong element inside list"
