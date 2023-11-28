from project.band_members.drummer import Drummer
from project.band_members.singer import Singer
from project.band_members.guitarist import Guitarist
from project.band import Band
from project.concert import Concert


class ConcertTrackerApp:
    MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.MUSICIAN_TYPES.keys():
            raise ValueError("Invalid musician type!")

        if self._check_if_musician_name_in_collection(name):
            raise Exception(f"{name} is already a musician!")

        new_musician = self.MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if self._check_for_name_in_bands(name):
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self._check_if_concert_place_already_registered(place)

        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._find_musician_by_name(musician_name)
        band_obj = self._find_band_by_name(band_name)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band_obj:
            raise Exception(f"{band_name} isn't a band!")

        band_obj.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        musician = self._find_musician_by_name(musician_name)
        band = self._find_band_by_name(band_name)

        if not musician or musician not in band.members: # May be error
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self._find_band_by_name(band_name)
        concert = self._check_if_concert_place_already_registered(concert_place)

        if not ConcertTrackerApp._check_band_members_if_fullstack(band):
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        self._check_members_skills(concert.genre, band)

        money = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {money:.2f}$ from the {concert.genre} concert in {concert_place}."

    # Helper methods
    def _check_members_skills(self, concert_genre, band):
        for member in band.members:
            result = member.get_skill_for_member(concert_genre)
            if not result:
                raise Exception(f"The {band.name} band is not ready to play at the concert!")
    @staticmethod
    def _check_band_members_if_fullstack(band):
        MEMBERS = {'Guitarist': 0, 'Drummer': 0, 'Singer': 0}
        for m_obj in band.members:
            if m_obj.get_type in MEMBERS:
                MEMBERS[m_obj.get_type] += 1
        result = [x[0] for x in MEMBERS.items() if x[1] > 0]

        if len(result) < 3:
            return False

        return True

    def _find_band_by_name(self, band_name):
        for band in self.bands:
            if band.name == band_name:
                return band
        raise Exception(f"{band_name} isn't a band!")

    def _find_musician_by_name(self, musician_name):
        for musician in self.musicians:
            if musician.name == musician_name:
                return musician
        return False

    def _check_if_musician_name_in_collection(self, musician_name):
        for musician in self.musicians:
            if musician.name == musician_name:
                return True
        return False

    def _check_for_name_in_bands(self, name):
        for band in self.bands:
            if band.name == name:
                return True
        return False

    def _check_if_concert_place_already_registered(self, place):
        for conc in self.concerts:
            if conc.place == place:
                return conc

        return False
