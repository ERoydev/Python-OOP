from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    EQUIPMENT_TYPES = {'ElbowPad': ElbowPad, 'KneePad': KneePad}
    TEAM_TYPES = {'OutdoorTeam': OutdoorTeam, 'IndoorTeam': IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type):
        if equipment_type not in Tournament.EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")

        new_equipment = Tournament.EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type, team_name, country, advantage):
        if team_type not in Tournament.TEAM_TYPES:
            raise Exception("Invalid team type!")

        if self.capacity <= len(self.teams):
            return "Not enough tournament capacity."

        new_team = self.TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type, team_name):
        equipment = self._find_equipment_by_type(equipment_type)
        team = self._find_team_by_name(team_name)

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self._find_team_by_name(team_name)

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipment = [x for x in self.equipment if x.__class__.__name__ == equipment_type]
        [equip.increase_price() for equip in equipment]
        return f"Successfully changed {len(equipment)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self._find_team_by_name(team_name1)
        team2 = self._find_team_by_name(team_name2)

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_points = team1.advantage + team1.total_protection
        team2_points = team2.advantage + team2.total_protection

        if team1_points > team2_points:
            team1.win()
            return f"The winner is {team1.name}."

        elif team1_points < team2_points:
            team2.win()
            return f"The winner is {team2.name}."

        else:
            return "No winner in this game."

    def get_statistics(self):
        output = f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:"
        for team in sorted(self.teams, key=lambda x: -x.wins):
            output += f"\n{team.get_statistics()}"

        return output




    # Helper function
    def _find_team_by_name(self, team_name):
        for team in self.teams:
            if team.name == team_name:
                return team

        else:
            raise Exception("No such team!")

    def _find_equipment_by_type(self, equipment_type):
        return [x for x in self.equipment if x.__class__.__name__ == equipment_type][-1]


