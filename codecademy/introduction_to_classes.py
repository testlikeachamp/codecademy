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

    def is_edible(self):
        if not self.poisonous:
            return True
        else:
            return False

    def get_color(self):
        return self.color

    def bite_it(self, bite_size):
        assert type(bite_size) in (int, float) and bite_size > 0
        if bite_size > self.weight:
            self.weight = 0
            return
        self.weight = self.weight - bite_size

