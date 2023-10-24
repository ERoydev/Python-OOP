from abc import ABC, abstractmethod


class Shapes(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius * self.radius


class Rectangle(Shapes):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 1 / 2 * self.base * self.height


class AreaCalculator:
    def __init__(self, collection):
        assert isinstance(collection, list), "`shapes` should be of type `list`."
        self.collection = collection

    @property
    def total_area(self):
        total = 0

        for shape in self.collection:
            total += shape.get_area()

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)