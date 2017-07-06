from codecademy.conditionals_and_control_flow import greater_less_equal_5


import sys

def test_max_greater_5():
    assert greater_less_equal_5(sys.maxsize-1) == 1

def test_100_greater_5():
    assert greater_less_equal_5(100-1) == 1

def test_100_minus_1_greater_5():
    assert greater_less_equal_5(100) == 1

def test_greater_5():
    assert greater_less_equal_5(6) == 1

def test_equal_5():
    assert greater_less_equal_5(5) == 0

def test_less_5():
    assert greater_less_equal_5(4) == -1

def test_2_less_5():
    assert greater_less_equal_5(2) == -1

def test_0_less_5():
    assert greater_less_equal_5(0) == -1

def test_minus_1_less_5():
    assert greater_less_equal_5(-1) == -1

def test_minus_100_plus_1_less_5():
    assert greater_less_equal_5(-100+1) == -1

def test_min_plus_1_less_5():
    assert greater_less_equal_5(-sys.maxsize+1) == -1




