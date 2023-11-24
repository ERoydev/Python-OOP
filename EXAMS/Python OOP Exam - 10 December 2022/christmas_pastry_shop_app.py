from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:
    DELICACY_TYPES = {'Gingerbread': Gingerbread, "Stolen": Stolen}
    BOOTH_TYPES = {'Open Booth': OpenBooth, 'Private Booth': PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float): # It could be problem that i raise in helper methods
        delicacy = self._create_obj_by_type(type_delicacy, name, price, self.DELICACY_TYPES)

        if not delicacy:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if self._check_if_delicacy_name_exists(delicacy):
            raise Exception(f"{delicacy.name} already exists!")

        self.delicacies.append(delicacy)
        return f"Added delicacy {delicacy.name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth = self._create_obj_by_type(type_booth, booth_number, capacity, self.BOOTH_TYPES)

        if not booth:
            raise Exception(f"{type_booth} is not a valid booth!")

        if self._check_if_booth_number_exists(booth):
            raise Exception(f"Booth number {booth.booth_number} already exists!")

        self.booths.append(booth)
        return f"Added booth number {booth.booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number, delicacy_name):
        booth = self._find_booth_by_number(booth_number)
        delicacy = self._find_delicacy_by_name(delicacy_name)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self._find_booth_by_number(booth_number)
        bill = booth.price_for_reservation + sum([x.price for x in booth.delicacy_orders])
        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False

        self.income += bill

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    # HELPER METHODS
    def _check_if_delicacy_name_exists(self, delicacy):
        result = [el for el in self.delicacies if el.name == delicacy.name]

        if len(result) > 0:
            return True

    def _check_if_booth_number_exists(self, booth):
        result = [el for el in self.booths if booth.booth_number == el.booth_number]

        if len(result) > 0:
            return True

    @staticmethod
    def _create_obj_by_type(type_obj, parameter1, parameter2, TYPES):
        if type_obj in TYPES:
            return TYPES[type_obj](parameter1, parameter2)

    def _find_booth_by_number(self, number):
        for booth in self.booths:
            if booth.booth_number == number:
                return booth

    def _find_delicacy_by_name(self, name):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                return delicacy
