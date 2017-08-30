class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous, weight):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous
        self.weight = weight

    def description(self):
        return "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self, type_poisonous):
        assert type(type_poisonous) == bool, "Error type, please enter boolean"
        if not self.poisonous:
            return True
        else:
            return False

    def bite_it(self, bite_size):
        assert type(bite_size) in (int, float) and bite_size > 0,\
            "{} error type, please enter integer".format(bite_size)
        if bite_size > self.weight:
            self.weight = 0
            return
        self.weight = self.weight - bite_size


class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"

    def __init__(self, name, age):
        assert type(name) == str and type(age) in (int, float) and age > 0,"Error type, please enter a valid value age or name"
        self.name = name
        self.age = age

    def description(self):
        return self.name + " " + str(self.age)


class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        assert type(customer_id) == int and customer_id > 0, "Error type, please enter a valid value"
        self.customer_id = customer_id

    def display_cart(self):
        return self.customer_id


class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        return "I'm a string that stands in for your order history!"


class Triangle(object):
    def __init__(self, angle1, angle2, angle3):

        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

        for a in (angle1, angle2, angle3):
            assert type(a) in (int, float), "Error type, please enter a valid value"
            assert 0 < a < 180, "Angles is not in the range (0, 180)"
        assert self.check_angles(), "Sum of given angles not equal to 180"

    number_of_sides = 3

    def check_angles(self):
        return self.angle1 + self.angle2 + self.angle3 == 180


# nicolas13sochi part

# 2-4-6-8

# Class definition
class Animal6(object):
    """Makes cute animals."""
    is_alive = True

    def __init__(self, name, age, is_hungry):
        assert type(name) == str and type(age) in (int, float) and age > 0, "Error type, please enter a valid value age or name"
        assert type(is_hungry) == bool, "Error type, please enter boolean"
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

    def description(self):
        return "{} + " " + {}".format(self.name, self.age)


# 10

class ShoppingCart10(object):
    """Creates shopping cart objects for users of our fine website."""
    items_in_cart = {}

    def __init__(self, customer_name):
        assert type(customer_name) == str, "Error type, please enter a valid value"
        self.customer_name = customer_name

    def add_item10(self, product, price):
        """Add product to the cart."""
        assert type(product) == str and type(price) in (int, float) and price > 0,\
            "Error type, please enter a valid value"
        if product not in self.items_in_cart:
            self.items_in_cart[product] = price
            return product + " added."
        else:
            return product + " is already in the cart."

    def remove_item10(self, product):
        """Remove product from the cart."""
        assert type(product) == str, "Error type, please enter a valid value"
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            return product + " removed."
        else:
            return product + " is not in the cart."


# 12-16-18

class Shape12(object):
    """Makes shapes!"""

    def __init__(self, number_of_sides):
        assert isinstance(number_of_sides, int) and number_of_sides >= 3, "Error type, please enter a valid value"
        self.number_of_sides = number_of_sides


class Triangle12(Shape12):

    def __init__(self, angle1, angle2, angle3):

        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

        for a in (angle1, angle2, angle3):
            assert type(a) in (int, float), "Error type, please enter a valid value"
            assert 0 < a < 180, "Angles is not in the range (0, 180)"
        assert self.check_angles12(), "Sum of given angles not equal to 180"

    def check_angles12(self):
        return self.angle1 + self.angle2 + self.angle3 == 180


class Equilateral12(Triangle12):
    angle = 60

    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle


# 14

class Employee14(object):
    """Models real-life employees!"""

    def __init__(self, employee_name):
        assert type(employee_name) == str, "Error type, please enter a valid value"
        self.employee_name = employee_name

    def calculate_wage14(self, hours):
        assert type(hours) in (int, float) and hours > 0, "Error type, please enter a valid value"
        self.hours = hours
        return hours * 20.00


class PartTimeEmployee14(Employee14):

    def calculate_wage14(self, hours):
        assert type(hours) in (int, float) and hours > 0, "Error type, please enter a valid value"
        self.hours = hours
        return hours * 12.00

    def full_time_wage14(self, hours):
        return super(PartTimeEmployee14, self).calculate_wage14(hours)
