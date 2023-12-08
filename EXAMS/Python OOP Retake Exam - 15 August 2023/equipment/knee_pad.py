from .base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PROTECTION = 120
    PRICE = 15
    INCREASE_PRICE = 1.20

    def __init__(self):
        super().__init__(protection=self.PROTECTION, price=self.PRICE)

    def increase_price(self):
        self.price *= self.INCREASE_PRICE
