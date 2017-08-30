import sys

if sys.version_info > (3,):
    long = int


def greater_less_equal_5(answer):
    """
    This function compares argument answer with number 5.
    :param answer: a number to be compared with 5
    :return: int, 1 if answer > 5, -1 if answer < 5, 0 otherwise
    """
    # assert not isinstance(answer, (str, bool)) and answer is not None, "{} was not int or float".format(answer)
    assert type(answer) in (int, float, long), "{} was not int or float".format(answer)
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0
