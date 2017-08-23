class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

        assert type(model) in (str, int) and type(color) == str and type(mpg) == int, \
            "Invalid enter data type"
        # assert self.display_car()
        assert self.drive_car()

    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.model, self.color, self.mpg)

    def drive_car(self):
        self.condition = "used"
        assert type(self.condition) == str, "Invalid entering data type"
        return self.condition


class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        super(ElectricCar, self).__init__(model, color, mpg)
        self.battery_type = battery_type

    def drive_car(self):
        self.condition = "like new"
        return self.condition


class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

