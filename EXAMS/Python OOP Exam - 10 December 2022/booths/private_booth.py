from project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON = 3.50

    def __init__(self, booth_number, capacity):
        super().__init__(booth_number, capacity)

    @property
    def price_per_person(self):
        return PrivateBooth.PRICE_PER_PERSON

    def reserve(self, number_of_people):
        price_reservation = self.price_per_person * number_of_people
        self.price_for_reservation = price_reservation
        self.is_reserved = True
