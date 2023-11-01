from Animal.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender="Female")

    @staticmethod
    def make_sound():
        return "Meow"
