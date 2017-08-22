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

    def is_edible(self, type_posinous):
        assert type(type_posinous) == bool, "Error type, please enter boolean"
        if not self.poisonous:
            return True
        else:
            return False

    def bite_it(self, bite_size):
        assert type(bite_size) in (int, float) and bite_size > 0, "{} error type, please enter integer".format(bite_size)
        if bite_size > self.weight:
            self.weight = 0
            return
        self.weight = self.weight - bite_size


class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"

    def __init__(self, name, age):
        assert type(name) == str and type(age) in (int, float) and age > 0, "Error type, please enter a valid value age or name"
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
        for a in (angle1, angle2, angle3):
            assert type(a) in (int, float), "Error type, please enter a valid value"

        assert 0 < angle1 < 180 and 0 < angle2 < 180 and 0 < angle3 < 180, \
            "Sum of given angles not equal to 180"

        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3

    def check_angles(self):
        if (self.angle1+self.angle2+self.angle3) == 180:
            return True
        else:
            return False
