#  16. Passing a range into a function


def join_strings(words):
    """Create a function that concatenates strings."""
    assert type(words) == list, "{} is not a list".format(words)
    result = ""
    for word in words:
        if type(word) == str:
            result += word
        else:
            raise TypeError("The element in words is not a string")
    return result


#  18. Using a list of lists in a function


def flatten(lists):
    """Create a function called flatten that takes a single list
    and concatenates all the sublists that are part of it into a single list."""
    assert type(lists) == list, "{} is not a list".format(lists)
    results = []
    for numbers in lists:
        assert type(numbers) == list, "The element inside {} is not a list".format(lists)
        for number in numbers:
            results.append(number)
    return results
