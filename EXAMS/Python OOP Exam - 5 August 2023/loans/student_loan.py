from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    TYPE = "StudentLoan"
    INTEREST_RATE = 1.5
    AMOUNT = 2000

    def __init__(self):
        super().__init__(StudentLoan.INTEREST_RATE, StudentLoan.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.2

