from abc import ABC, abstractmethod


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Team name cannot be empty!")

        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")

        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")

        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        average_protection = int(sum([x.protection for x in self.equipment]) / max(len(self.equipment), 1))
        output = (f'Name: {self.name}\nCountry: {self.country}\nAdvantage: {self.advantage} points\nBudget: {self.budget:.2f}EUR\n'
                  f'Wins: {self.wins}\nTotal Equipment Price: {sum([x.price for x in self.equipment]):.2f}\n'
                  f'Average Protection: {average_protection}')

        return output

    @property
    def total_protection(self):
        return sum([x.protection for x in self.equipment])
