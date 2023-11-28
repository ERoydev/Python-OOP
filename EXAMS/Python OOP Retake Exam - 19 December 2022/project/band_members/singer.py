from project.band_members.musician import Musician


class Singer(Musician):
    CONCERT_SKILLS = {'Rock': 'sing high pitch notes', 'Metal': 'sing low pitch notes', 'Jazz': 'sing high pitch notes'}

    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def get_skills(self):
        return ["sing high pitch notes", "sing low pitch notes"]

    @property
    def get_type(self):
        return "Singer"

