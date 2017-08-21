from codecademy.conditionals_and_control_flow import greater_less_equal_5


def test_greater_less_equal_5_minus_1():
    assert greater_less_equal_5(-1) == -1


def test_greater_less_equal_5_6():
    assert greater_less_equal_5(6) == 1


def test_greater_less_equal_5_5():
    assert greater_less_equal_5(5) == 0
