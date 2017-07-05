# 4. Function ex-3
def square(n):
    """This function returns the square of a number."""
    squared = n ** 2
    print "%d squared is %d." % (n, squared)
    return squared

square(10)
# END 4. Function ex-3

# 4. Function ex-5
def one_good_turn(n):
    """"simply add 1 to parameter of this function."""
    return n + 1

def deserves_another(n):
    """"Adds 2 to the output of function 'one_good_turn'."""
    return one_good_turn(n) + 2
# END 4. Function ex-5

# 4. Function ex-12
def biggest_number(*args):
    """"Returns the biggest of arguments."""
    print max(args)
    return max(args)

def smallest_number(*args):
    """"Returns the smaller of arguments."""
    print min(args)
    return min(args)

def distance_from_zero(arg):
    """"Return the absolute value of a arguments."""
    print abs(arg)
    return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)
# END 4. Function ex-12

# 4. Function ex-19
def distance_from_zero(arg):
    """Depending on the type of argument returned absolute value or 'Nope'"""
    if type(arg) == int or type(arg) == float:
        return abs(arg)
    else:
        return "Nope"
# END 4. Function ex-19
