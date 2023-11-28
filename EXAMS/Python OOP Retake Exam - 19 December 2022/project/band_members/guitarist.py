from project.band_members.musician import Musician


class Guitarist(Musician):
    CONCERT_SKILLS = {'Rock': 'play rock', 'Metal': 'play metal',
                      'Jazz': 'play jazz'}

    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def get_skills(self):
        return ["play metal", "play rock", "play jazz"]

    @property
    def get_type(self):
        return "Guitarist"

