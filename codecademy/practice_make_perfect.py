import sys
import math

if sys.version_info > (3,):
    long = int


def is_int(x):
    # function compute an integer number or not, and return false or true
    assert isinstance(x, (int, float, long)) and type(x) is not bool, "{} passed the wrong data type".format(x)
    if x - round(x) > 0:
        return False
    else:
        if x < 0 and x - round(x) < 0:
            return False
        else:
            return True
# END is_int


def factorial(x):
    assert isinstance(x, (int, float, long)) and type(x) is not bool, "{} passed the wrong data type".format(x)
    x = abs(x)
    if x == 1 or x == 0:
        print(1)
        return 1
    else:
        i = 1
        for n in range(1, (x + 1)):
            i = n * i
            print(i)
    return i
# END factorial


def reverse(text):
    assert isinstance(text, str), "{} passed the wrong data type".format(text)
    a = ""
    j = 0
    for i in range(len(text)):
        j = j - 1
        a += (text[len(text) + j])
    return a
# END reverse


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def scrabble_score(word):
    assert isinstance(word, str) and len(word) > 0, "Passed the wrong data type or key"
    for key in word:
        if key not in set(score):
            raise AssertionError("Passed the wrong data type or key")
    word = word.lower()
    total = 0
    for i in word:  # iterate over the string
        total += score[i]
    return total
# END scrabble_score


def count(sequence, item):
    item = str(item)
    j = 0
    for i in sequence:
        i = str(i)
        if i == item:
            j += 1

    return j
# END count


def product(item_list):
    assert isinstance(item_list, list), "Passed the wrong data type"
    for item in item_list:
        if type(item) != int:
            raise AssertionError("Passed the wrong data type")
    j = 1
    for i in item_list:
        j *= i
    return j
# END product


def median(a):
    assert isinstance(a, list), "Passed the wrong data type"
    for item in a:
        if type(item) != int:
            raise AssertionError("Passed the wrong data type")
    a = sorted(a)
    b = len(a)
    if b % 2 == 0:
        return (a[len(a)//2] + a[(len(a)//2) - 1]) / 2.0
    else:
        return a[(len(a)-1)//2]
# END median



