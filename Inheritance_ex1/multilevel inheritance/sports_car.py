from multilevel.car import Car


class SportsCar(Car):
    def __init__(self, name, model):
        super().__init__(name, model)

    def race(self):
        return "racing..."

