import sys

if sys.version_info > (3,):
    long = int
    unicode = str


def is_int(x):
    # function compute an integer number or not, and return false or true
    assert type(x) in (int, float, long), "{} passed the wrong data type".format(x)
    if x - round(x) > 0:
        return False
    else:
        if x < 0 and x - round(x) < 0:
            return False
        else:
            return True
# END is_int


def factorial(x):
    assert type(x) in (int, float, long), "{} passed the wrong data type".format(x)
    x = abs(x)
    if x == 1 or x == 0:
        print(1)
        return 1
    else:
        i = 1
        for n in range(1, x + 1):
            i = n * i
            print(i)
    return i
# END factorial


def reverse(text):
    assert isinstance(text, (str, unicode)), "{} passed the wrong data type".format(text)
    a = ""
    j = 0
    for i in range(len(text)):
        j = j - 1
        a += text[len(text) + j]
    return a
# END reverse


def scrabble_score(word):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
    assert type(word) == str and set(word) <= set(score), "Passed the wrong data type or key"
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
        assert type(item) == int, "Passed the wrong data type"
    j = 1
    for i in item_list:
        j *= i
    return j
# END product


def median(a):
    assert isinstance(a, list), "Passed the wrong data type"
    for item in a:
        assert isinstance(item, int), "Passed the wrong data type"
    a = sorted(a)
    b = len(a)
    if b % 2 == 0:
        return (a[len(a)//2] + a[(len(a)//2) - 1]) / 2.0
    else:
        return a[(len(a)-1)//2]
# END median

#  nicolas13sochi part


# 2 is_even
def is_even(x):
    """a function is_even that will take a number x as input.
If x is even, then return True.
Otherwise, return False."""
    assert type(x) == int, "{} is not integer".format(x)
    if x % 2 == 0:
        return True
    else:
        return False


# 4 digit_sum
def digit_sum(n):
    """a function called digit_sum that takes a positive integer n as input
and returns the sum of all that number's digits. """
    assert type(n) == int and n > 0, "{} is not integer or not a positive integer".format(n)
    result = 0
    for number in str(n):
        result += int(number)
    return result


# 6 is_prime
def is_prime(x):
    """For each number n from 2 to x - 1, test if x is evenly divisible by n.
If it is, return False.
If none of them are, then return True."""
    assert type(x) == int, "{} is not integer".format(x)
    n = 2
    while True:
        if x > 3 and n < x:
            if x % n == 0:
                return False
            else:
                n += 1
        elif x < 2:
            return False
        elif x == 2 or x == 3:
            return True
        else:
            return True


# 8 anti_vowel
def anti_vowel(text):
    """Define a function called anti_vowel that takes one string, text,
as input and returns the text with all of the vowels removed. We don't count Y as a vowel."""
    text = str(text)
    vow_list = []
    vow_check_list = ["a", "A", "o", "O", "u", "U", "e", "E", "i", "I", "q", "Q"]
    i = 0
    the_word_to_print = ""
    for vow in text:
        vow_list.append(vow)
    while i <= len(text):
        for v in vow_check_list:
            while v in vow_list:
                vow_list.remove(v)
            i += 1
    for char in vow_list:
        the_word_to_print += str(char)
    return the_word_to_print


# 10 def censor:
def censor(text, word):
    """a function called censor that takes two strings, text and word, as input.
It should return the text with the word you chose replaced with asterisks (***)."""
    assert isinstance(text, str) and isinstance(word, str), "Passed the wrong data type"
    text_list = text.split()
    print(text_list)
    result = " "
    for i, w in enumerate(text_list):
        if w == word:
            text_list[i] = "*" * len(word)
    result = result.join(text_list)
    return result


# 12 purify

def purify(numbers):
    """a function called purify that takes in a list of numbers,
removes all odd numbers in the list, and returns the result. """
    assert isinstance(numbers, list), "Passed the wrong data type"
    even_list = []
    for number in numbers:
        assert isinstance(number, int), "Passed the wrong data type - wrong element inside list"
        if (number % 2) == 0:
            even_list.append(number)
    return even_list


# 14 remove_duplicates

def remove_duplicates(numbers):
    """a function remove_duplicates that takes in a list and
removes elements of the list that are the same."""
    assert isinstance(numbers, list), "Passed the wrong data type"
    newest_list = []
    duplicates = []
    i = 0
    for number in numbers:
        assert isinstance(number, int), "Passed the wrong data type - wrong element inside list"
        if numbers[i] not in numbers[(i+1):len(numbers)]:
            duplicates.append(number)
            i += 1
        else:
            newest_list.append(number)
            print(number)
            i += 1
    if len(newest_list) == 0:
        return numbers
    else:
        return duplicates
