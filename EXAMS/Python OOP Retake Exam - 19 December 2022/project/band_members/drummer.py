from project.band_members.musician import Musician


class Drummer(Musician):
    CONCERT_SKILLS = {'Rock': 'play the drums with drumsticks', 'Metal': 'play the drums with drumsticks',
                      'Jazz': 'play the drums with drum brushes'}

    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def get_skills(self):
        return ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]

    @property
    def get_type(self):
        return "Drummer"

