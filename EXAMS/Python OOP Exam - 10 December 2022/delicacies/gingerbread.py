from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    PORTION_GRAMS = 200

    def __init__(self, name, price):
        super().__init__(name, Gingerbread.PORTION_GRAMS, price)

    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."
