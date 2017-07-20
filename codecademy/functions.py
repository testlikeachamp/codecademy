import sys

if sys.version_info > (3,):
    long = int

# 4. Function ex-3
def square(n):
    """This function returns the square of a number."""
    assert isinstance(n, (int, long)), "{} was not int or long".format()
    squared = n ** 2
    print("%d squared is %d." % (n, squared))
    return squared
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
    print(max(args))
    return (max(args))

def smallest_number(*args):
    """"Returns the smaller of arguments."""
    print(min(args))
    return (min(args))

def distance_from_zero(arg):
    """"Return the absolute value of a arguments."""
    print(abs(arg))
    return (abs(arg))
# END 4. Function ex-12

# 4. Function ex-19
def distance_from_zero_type(arg):
    """Depending on the type of argument returned absolute value or 'Nope'"""
    if type(arg) == bool or type(arg) == str or arg is None:
        return "Nope"
    else:
        return abs(arg)
# END 4. Function ex-19

# 4. Function ex-1
def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print("With tax: %f" % bill)
    return bill


def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print("With tip: %f" % bill)
    return bill

# END 4. Function ex-1

# 4. Function ex-4
def power(base, exponent):  # Add your parameters here!
    """It should take two arguments, a base and an exponent,
     and raise the first to the power of the second."""
    result = base ** exponent
    print("%d to the power of %d is %d." % (base, exponent, result))

# END 4. Function ex-4

# 4. Function ex-6
def cube(number):
    """Return the cube of the argument"""
    return number**3


def by_three(number):
    """Return the argument is divisible by 3, by_three should call cube(number)
     and return its result. Otherwise, by_three should return False"""
    if number % 3 == 0:
        return cube(number)
    else:
        return False
# END 4. Function ex-6

# 4. Function ex-17
def shut_down(s):
    """Return the message depends of shut_down() argument"""
    if s == 'yes':
        return "Shutting down"
    elif s == 'no':
        return "Shutdown aborted"
    else:
        return "Sorry"

# END 4. Function ex-17
