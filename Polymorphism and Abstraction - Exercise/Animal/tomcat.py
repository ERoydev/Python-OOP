from Animal.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender="Male")

    @staticmethod
    def make_sound():
        return "Hiss"
