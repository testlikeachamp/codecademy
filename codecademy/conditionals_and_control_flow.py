def greater_less_equal_5(answer):
    """
    This function compares argument answer with number 5.
    :param answer: a number to be compared with 5
    :return: int, 1 if answer > 5, -1 if answer < 5, 0 otherwise
    """

    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0