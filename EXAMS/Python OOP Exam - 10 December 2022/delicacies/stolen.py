from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    PORTION_GRAMS = 250

    def __init__(self, name, price):
        super().__init__(name, Stolen.PORTION_GRAMS, price)

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."
