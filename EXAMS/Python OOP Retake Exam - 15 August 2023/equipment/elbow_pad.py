from .base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    PROTECTION = 90
    PRICE = 25
    INCREASE_PRICE = 1.10

    def __init__(self):
        super().__init__(protection=self.PROTECTION, price=self.PRICE)

    def increase_price(self):
        self.price *= self.INCREASE_PRICE
