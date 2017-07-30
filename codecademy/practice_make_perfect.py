import sys

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


def reverse(text):
    a = ""
    j = 0
    for i in range(len(text)):
        j = j - 1
        a += (text[len(text) + j])
    return a


