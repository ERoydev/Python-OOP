

class Equipment:
    ID = 0

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.get_next_id()

    @staticmethod
    def get_next_id():
        Equipment.ID += 1
        return Equipment.ID

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

