from abc import ABC, abstractmethod


class BaseLoan(ABC):
    def __init__(self, interest_rate: float, amount: float):
        self.interest_rate = interest_rate
        self.amount = amount
        self.granted = False

    @abstractmethod
    def increase_interest_rate(self):
        pass

    def loan_change_granted_status(self):
        self.granted = not self.granted
