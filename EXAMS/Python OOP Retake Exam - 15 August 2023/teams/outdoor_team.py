from .base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    INCREASE_TEAM_ADVANTAGE = 115
    INITIAL_BUDGET = 1000

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self.INITIAL_BUDGET)

    def win(self):
        self.advantage += self.INCREASE_TEAM_ADVANTAGE
        self.wins += 1

